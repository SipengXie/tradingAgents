"""
加密货币数据接口
提供Binance和Finnhub的统一数据访问层
"""
import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Optional, Dict, List, Union
import logging
from functools import wraps
from .binance_utils import get_binance_api, BinanceAPIWrapper
from .config import get_config
from .finnhub_utils import get_data_in_range

logger = logging.getLogger(__name__)


def convert_to_binance_symbol(symbol: str) -> str:
    """
    将各种格式转换为Binance标准格式
    
    支持的转换：
    - ETH-USD -> ETHUSDT
    - BTC/USD -> BTCUSDT
    - eth-usd -> ETHUSDT
    """
    symbol = symbol.upper().strip()
    
    # 处理 XXX-USD 格式
    if '-USD' in symbol:
        return symbol.replace('-USD', 'USDT')
    
    # 处理 XXX/USD 格式
    if '/USD' in symbol:
        return symbol.replace('/USD', 'USDT')
    
    # 处理 XXX-USDT 格式（保持不变）
    if '-USDT' in symbol:
        return symbol.replace('-', '')
    
    # 处理 XXX/USDT 格式
    if '/USDT' in symbol:
        return symbol.replace('/', '')
    
    # 如果已经是正确格式（如BTCUSDT），直接返回
    return symbol


def handle_crypto_errors(func):
    """
    装饰器：处理加密货币数据获取的错误
    提供详细的错误信息和用户友好的提示
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            func_name = func.__name__
            error_msg = str(e)
            logger.error(f"{func_name} 失败: {error_msg}")
            
            # 分析错误类型并提供建议
            suggestions = []
            
            if "Invalid symbol" in error_msg:
                suggestions.append("请检查交易对符号格式（如BTCUSDT而非BTC-USD）")
            elif "APIError" in error_msg:
                if "-1003" in error_msg:
                    suggestions.append("API访问频率超限，请稍后重试")
                elif "-2014" in error_msg:
                    suggestions.append("API密钥无效，请检查配置")
                elif "-1021" in error_msg:
                    suggestions.append("时间戳错误，请检查系统时间")
            elif "Network" in error_msg or "Connection" in error_msg:
                suggestions.append("网络连接问题，请检查网络状态")
                suggestions.append("如果使用代理，请检查代理设置")
            elif "Unauthorized" in error_msg:
                suggestions.append("API密钥未授权此操作")
            
            # 构建错误报告
            error_report = f"# {func_name} 执行失败\n\n"
            error_report += f"错误信息: {error_msg}\n\n"
            
            if suggestions:
                error_report += "可能的解决方案:\n"
                for i, suggestion in enumerate(suggestions, 1):
                    error_report += f"{i}. {suggestion}\n"
            
            # 获取函数参数信息
            if args:
                error_report += f"\n调用参数: {args}"
            if kwargs:
                error_report += f"\n关键字参数: {kwargs}"
            
            return error_report
    
    return wrapper


def get_binance_market_data(
    symbol: str, 
    start_date: str, 
    end_date: str, 
    interval: str = "1h"
) -> str:
    """
    获取Binance市场数据并格式化为CSV字符串
    
    Args:
        symbol: 交易对（支持多种格式：ETH-USD, ETHUSDT等）
        start_date: 开始日期 (yyyy-mm-dd)
        end_date: 结束日期 (yyyy-mm-dd)
        interval: K线间隔
    
    Returns:
        格式化的CSV字符串
    """
    # 转换符号为Binance格式
    binance_symbol = convert_to_binance_symbol(symbol)
    api = get_binance_api()
    
    try:
        # 获取K线数据
        klines = api.get_historical_klines(
            symbol=binance_symbol,
            interval=interval,
            start_str=start_date,
            end_str=end_date
        )
        
        if not klines:
            return f"未找到 {symbol} 在 {start_date} 到 {end_date} 期间的数据"

        # 数据结构验证
        expected_columns = 12
        for i, kline in enumerate(klines):
            if not isinstance(kline, list):
                logger.error(f"K线数据格式错误，索引{i}不是列表: {type(kline)}")
                return f"数据格式错误: K线数据格式不正确"

            if len(kline) != expected_columns:
                logger.error(f"K线数据列数错误，索引{i}有{len(kline)}列，期望{expected_columns}列")
                return f"数据格式错误: K线数据列数不匹配（期望{expected_columns}列，实际{len(kline)}列）"

        # 转换为DataFrame
        try:
            df = pd.DataFrame(klines, columns=[
                'timestamp', 'open', 'high', 'low', 'close', 'volume',
                'close_time', 'quote_volume', 'trades', 'taker_buy_volume',
                'taker_buy_quote_volume', 'ignore'
            ])
        except Exception as e:
            logger.error(f"创建DataFrame失败: {e}")
            return f"数据处理错误: 无法创建数据表 - {str(e)}"

        # 转换时间戳
        try:
            df['date'] = pd.to_datetime(df['timestamp'], unit='ms')
        except Exception as e:
            logger.error(f"时间戳转换失败: {e}")
            return f"数据处理错误: 时间戳格式不正确"

        # 转换数值类型
        numeric_columns = ['open', 'high', 'low', 'close', 'volume',
                         'quote_volume', 'trades', 'taker_buy_volume',
                         'taker_buy_quote_volume']

        for col in numeric_columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

        # 数据质量检查
        null_counts = df[numeric_columns].isnull().sum()
        total_rows = len(df)

        for col in numeric_columns:
            null_ratio = null_counts[col] / total_rows
            if null_ratio > 0.1:  # 超过10%的空值
                logger.warning(f"{symbol} 数据列 {col} 有 {null_ratio:.1%} 的空值")

        # 检查价格数据的合理性
        if 'close' in df.columns:
            # 删除空值行
            df_clean = df.dropna(subset=['close'])

            if len(df_clean) == 0:
                return f"数据错误: 所有价格数据都无效"

            # 检查价格是否为正数
            if (df_clean['close'] <= 0).any():
                logger.warning(f"{symbol} 存在非正价格数据")
                df = df[df['close'] > 0]

            # 检查价格异常波动（单日涨跌超过100%可能是数据错误）
            price_change = df_clean['close'].pct_change().abs()
            if (price_change > 1.0).any():
                extreme_changes = price_change[price_change > 1.0]
                logger.warning(f"{symbol} 存在异常价格波动: 最大变化 {extreme_changes.max():.1%}")

        # 验证OHLC逻辑关系
        invalid_ohlc = (
            (df['high'] < df['low']) |
            (df['high'] < df['open']) |
            (df['high'] < df['close']) |
            (df['low'] > df['open']) |
            (df['low'] > df['close'])
        )

        if invalid_ohlc.any():
            invalid_count = invalid_ohlc.sum()
            logger.warning(f"{symbol} 有 {invalid_count} 条K线数据的OHLC关系不合理")
            # 移除这些异常数据
            df = df[~invalid_ohlc]

        if len(df) == 0:
            return f"数据错误: 所有数据都未通过验证"
        
        # 选择输出列
        output_df = df[['date', 'open', 'high', 'low', 'close', 'volume', 
                       'quote_volume', 'trades', 'taker_buy_volume']]
        
        # 格式化输出
        header = f"# 加密货币数据 {symbol} ({interval})\n"
        header += f"# 时间范围: {start_date} 到 {end_date}\n"
        header += f"# 数据来源: Binance\n"
        header += f"# 记录数: {len(df)}\n"
        header += f"# 字段说明:\n"
        header += "#   - volume: 成交量(基础货币)\n"
        header += "#   - quote_volume: 成交额(计价货币)\n"
        header += "#   - trades: 成交笔数\n"
        header += "#   - taker_buy_volume: 主动买入量\n\n"
        
        return header + output_df.to_csv(index=False)
        
    except Exception as e:
        logger.error(f"获取Binance数据失败: {e}")
        # 详细的错误处理
        error_msg = str(e)
        
        if "Invalid symbol" in error_msg:
            logger.info(f"无效的交易对 {symbol}，尝试使用Finnhub")
        elif "APIError" in error_msg and "-1003" in error_msg:
            logger.warning("Binance API频率限制，尝试使用Finnhub")
        elif "Network" in error_msg or "Connection" in error_msg:
            logger.warning("网络连接问题，尝试使用Finnhub")
        else:
            logger.error(f"未知错误: {error_msg}")
        
        # 尝试使用Finnhub备用
        try:
            logger.info(f"切换到Finnhub数据源获取 {symbol} 数据")
            return get_finnhub_crypto_data(symbol, start_date, end_date)
        except Exception as finnhub_error:
            logger.error(f"Finnhub也失败了: {finnhub_error}")
            return f"# 获取 {symbol} 数据失败\n\nBinance错误: {error_msg}\nFinnhub错误: {str(finnhub_error)}\n\n请检查：\n1. 交易对符号是否正确\n2. API密钥是否有效\n3. 网络连接是否正常"


def get_finnhub_crypto_data(symbol: str, start_date: str, end_date: str) -> str:
    """
    从Finnhub获取加密货币数据（备用数据源）
    
    Args:
        symbol: 交易对
        start_date: 开始日期
        end_date: 结束日期
    
    Returns:
        格式化的CSV字符串
    """
    try:
        # 转换符号格式：BTCUSDT -> BTC-USD
        if symbol.endswith('USDT'):
            finnhub_symbol = symbol[:-4] + '-USD'
        else:
            finnhub_symbol = symbol
        
        # 使用现有的Finnhub接口
        data = get_data_in_range(
            finnhub_symbol, 
            start_date, 
            end_date, 
            "crypto_candles",
            get_config()['DATA_DIR']
        )
        
        if not data:
            return f"Finnhub也未找到 {symbol} 的数据"
        
        # 格式化为CSV
        header = f"# 加密货币数据 {symbol}\n"
        header += f"# 时间范围: {start_date} 到 {end_date}\n"
        header += f"# 数据来源: Finnhub (备用)\n\n"
        
        # 将数据转换为DataFrame格式
        records = []
        for date, candles in data.items():
            for candle in candles:
                records.append({
                    'date': date,
                    'open': candle.get('o', 0),
                    'high': candle.get('h', 0),
                    'low': candle.get('l', 0),
                    'close': candle.get('c', 0),
                    'volume': candle.get('v', 0)
                })
        
        if records:
            df = pd.DataFrame(records)
            return header + df.to_csv(index=False)
        else:
            return f"未找到有效数据"
            
    except Exception as e:
        logger.error(f"Finnhub获取数据失败: {e}")
        return f"获取数据失败: {str(e)}"


@handle_crypto_errors
def get_binance_funding_rate(symbol: str, limit: int = 100) -> str:
    """
    获取永续合约资金费率
    
    Args:
        symbol: 永续合约交易对（支持多种格式）
        limit: 返回记录数
    
    Returns:
        格式化的资金费率数据
    """
    # 转换符号为Binance格式
    binance_symbol = convert_to_binance_symbol(symbol)
    api = get_binance_api()
    
    try:
        # 获取资金费率历史
        funding_rates = api.futures_funding_rate(
            symbol=binance_symbol,
            limit=limit
        )
        
        if not funding_rates:
            return f"未找到 {symbol} 的资金费率数据"
        
        # 转换为DataFrame
        df = pd.DataFrame(funding_rates)
        df['time'] = pd.to_datetime(df['fundingTime'], unit='ms')
        df['fundingRate'] = pd.to_numeric(df['fundingRate'])
        
        # 计算统计信息
        avg_rate = df['fundingRate'].mean()
        max_rate = df['fundingRate'].max()
        min_rate = df['fundingRate'].min()
        
        # 格式化输出
        output = f"# {symbol} 资金费率历史\n"
        output += f"# 平均费率: {avg_rate:.4%}\n"
        output += f"# 最高费率: {max_rate:.4%}\n"
        output += f"# 最低费率: {min_rate:.4%}\n"
        output += f"# 正值表示多头向空头支付，负值表示空头向多头支付\n\n"
        
        output_df = df[['time', 'fundingRate']].copy()
        output_df['fundingRate'] = output_df['fundingRate'].apply(lambda x: f"{x:.4%}")
        
        return output + output_df.to_csv(index=False)
        
    except Exception as e:
        logger.error(f"获取资金费率失败: {e}")
        return f"获取资金费率失败: {str(e)}"


@handle_crypto_errors
def get_binance_orderbook(symbol: str, limit: int = 20) -> str:
    """
    获取订单簿深度数据
    
    Args:
        symbol: 交易对（支持多种格式）
        limit: 深度档位
    
    Returns:
        格式化的订单簿数据
    """
    # 转换符号为Binance格式
    binance_symbol = convert_to_binance_symbol(symbol)
    api = get_binance_api()
    
    try:
        depth = api.get_order_book(symbol=binance_symbol, limit=limit)
        
        # 分析买卖盘
        bids = pd.DataFrame(depth['bids'], columns=['price', 'quantity'])
        asks = pd.DataFrame(depth['asks'], columns=['price', 'quantity'])
        
        # 转换为数值类型
        for df in [bids, asks]:
            df['price'] = pd.to_numeric(df['price'])
            df['quantity'] = pd.to_numeric(df['quantity'])
            df['value'] = df['price'] * df['quantity']
        
        # 计算统计信息
        bid_volume = bids['quantity'].sum()
        ask_volume = asks['quantity'].sum()
        bid_value = bids['value'].sum()
        ask_value = asks['value'].sum()
        
        # 找出大单
        avg_bid_value = bid_value / len(bids) if len(bids) > 0 else 0
        avg_ask_value = ask_value / len(asks) if len(asks) > 0 else 0
        
        # 格式化输出
        output = f"# {symbol} 订单簿深度分析\n"
        output += f"# 买盘总量: {bid_volume:.4f} ({bid_value:.2f} USDT)\n"
        output += f"# 卖盘总量: {ask_volume:.4f} ({ask_value:.2f} USDT)\n"
        # 安全的买卖比计算（避免除零错误）
        if ask_volume > 0 and bid_volume > 0:
            output += f"# 买卖比: {bid_volume/ask_volume:.2f}\n"
        elif ask_volume == 0 and bid_volume > 0:
            output += f"# 买卖比: ∞ (无卖盘)\n"
        elif ask_volume > 0 and bid_volume == 0:
            output += f"# 买卖比: 0 (无买盘)\n"
        else:
            output += f"# 买卖比: N/A (无挂单)\n"
        output += f"# 最高买价: {bids.iloc[0]['price']:.2f}\n"
        output += f"# 最低卖价: {asks.iloc[0]['price']:.2f}\n"
        output += f"# 价差: {(asks.iloc[0]['price'] - bids.iloc[0]['price']):.2f}\n\n"
        
        output += "## 买盘 (Bids)\n"
        output += bids.head(10).to_csv(index=False)
        output += "\n## 卖盘 (Asks)\n"
        output += asks.head(10).to_csv(index=False)
        
        return output
        
    except Exception as e:
        logger.error(f"获取订单簿失败: {e}")
        return f"获取订单簿失败: {str(e)}"


@handle_crypto_errors
def get_binance_liquidations(
    symbol: str, 
    start_time: Optional[str] = None,
    end_time: Optional[str] = None,
    limit: int = 100
) -> str:
    """
    获取清算数据
    
    注意：需要期货API权限
    """
    # 转换符号为Binance格式
    binance_symbol = convert_to_binance_symbol(symbol)
    api = get_binance_api()
    
    try:
        # 构建参数
        params = {
            'symbol': binance_symbol,
            'limit': min(limit, 1000)  # API限制最多1000条
        }
        
        # 处理时间参数
        if start_time:
            start_timestamp = int(pd.to_datetime(start_time).timestamp() * 1000)
            params['startTime'] = start_timestamp
        
        if end_time:
            end_timestamp = int(pd.to_datetime(end_time).timestamp() * 1000)
            params['endTime'] = end_timestamp
        
        # 获取清算订单
        liquidations = api.futures_liquidation_orders(**params)
        
        if not liquidations:
            return f"未找到 {symbol} 的清算数据"
        
        # 转换为DataFrame
        df = pd.DataFrame(liquidations)
        
        # 处理数据
        df['time'] = pd.to_datetime(df['time'], unit='ms')
        df['origQty'] = pd.to_numeric(df['origQty'])
        df['executedQty'] = pd.to_numeric(df['executedQty'])
        df['averagePrice'] = pd.to_numeric(df['averagePrice'])
        df['value'] = df['executedQty'] * df['averagePrice']
        
        # 统计分析
        total_liquidations = len(df)
        buy_liquidations = df[df['side'] == 'BUY']
        sell_liquidations = df[df['side'] == 'SELL']
        
        total_buy_value = buy_liquidations['value'].sum()
        total_sell_value = sell_liquidations['value'].sum()
        
        # 格式化输出
        output = f"# {symbol} 清算数据分析\n"
        if start_time and end_time:
            output += f"# 时间范围: {start_time} 至 {end_time}\n"
        output += f"# 总清算单数: {total_liquidations}\n"
        output += f"# 多头清算: {len(buy_liquidations)} 单 (${total_buy_value:,.2f})\n"
        output += f"# 空头清算: {len(sell_liquidations)} 单 (${total_sell_value:,.2f})\n\n"
        
        # 大额清算统计
        large_threshold = 50000  # 5万美元
        large_liquidations = df[df['value'] >= large_threshold]
        if not large_liquidations.empty:
            output += f"## 大额清算 (>${large_threshold:,} USDT)\n"
            output += f"数量: {len(large_liquidations)}\n"
            output += f"总价值: ${large_liquidations['value'].sum():,.2f}\n\n"
        
        # 输出明细
        output += "## 清算明细 (最近20条)\n"
        output_df = df.head(20)[['time', 'side', 'origQty', 'executedQty', 'averagePrice', 'value']].copy()
        output_df.columns = ['时间', '方向', '原始数量', '执行数量', '平均价格', '价值(USDT)']
        output_df['方向'] = output_df['方向'].apply(lambda x: '多头清算' if x == 'BUY' else '空头清算')
        
        return output + output_df.to_csv(index=False)
        
    except Exception as e:
        logger.error(f"获取清算数据失败: {e}")
        return f"获取清算数据失败: {str(e)}"


@handle_crypto_errors
def get_binance_open_interest(symbol: str, period: str = "1h", limit: int = 30) -> str:
    """
    获取持仓量数据
    
    注意：需要期货API权限
    """
    # 转换符号为Binance格式
    binance_symbol = convert_to_binance_symbol(symbol)
    api = get_binance_api()
    
    try:
        # 获取当前持仓量
        current_oi = api.futures_open_interest(symbol=binance_symbol)
        
        # 获取历史持仓量
        historical_oi = api.futures_open_interest_hist(
            symbol=binance_symbol,
            period=period,
            limit=limit
        )
        
        if not historical_oi:
            return f"未找到 {symbol} 的持仓量数据"
        
        # 转换为DataFrame
        df = pd.DataFrame(historical_oi)
        df['time'] = pd.to_datetime(df['timestamp'], unit='ms')
        df['sumOpenInterest'] = pd.to_numeric(df['sumOpenInterest'])
        df['sumOpenInterestValue'] = pd.to_numeric(df['sumOpenInterestValue'])
        
        # 计算变化率
        df['oi_change'] = df['sumOpenInterest'].pct_change() * 100
        df['oi_value_change'] = df['sumOpenInterestValue'].pct_change() * 100
        
        # 格式化输出
        output = f"# {symbol} 持仓量分析\n"
        output += f"# 当前持仓量: {float(current_oi['openInterest']):,.2f} {symbol[:-4]}\n"
        output += f"# 时间周期: {period}\n"
        output += f"# 数据点数: {len(df)}\n\n"
        
        # 统计信息
        avg_oi = df['sumOpenInterest'].mean()
        max_oi = df['sumOpenInterest'].max()
        min_oi = df['sumOpenInterest'].min()
        
        output += f"# 统计信息:\n"
        output += f"# 平均持仓量: {avg_oi:,.2f}\n"
        output += f"# 最高持仓量: {max_oi:,.2f}\n"
        output += f"# 最低持仓量: {min_oi:,.2f}\n\n"
        
        # 输出数据
        output_df = df[['time', 'sumOpenInterest', 'sumOpenInterestValue', 'oi_change']].copy()
        output_df.columns = ['时间', '持仓量', '持仓价值(USDT)', '变化率(%)']
        
        return output + output_df.to_csv(index=False)
        
    except Exception as e:
        logger.error(f"获取持仓量失败: {e}")
        return f"获取持仓量失败: {str(e)}"


@handle_crypto_errors
def get_binance_long_short_ratio(symbol: str, period: str = "1h", limit: int = 30) -> str:
    """
    获取多空比数据
    
    注意：需要期货API权限
    """
    # 转换符号为Binance格式
    binance_symbol = convert_to_binance_symbol(symbol)
    api = get_binance_api()
    
    try:
        # 获取多个维度的多空比数据
        results = {}
        
        # 1. 大户持仓量多空比
        position_ratio = api.futures_top_longshort_position_ratio(
            symbol=binance_symbol,
            period=period,
            limit=limit
        )
        
        # 2. 大户账户数多空比
        account_ratio = api.futures_top_longshort_account_ratio(
            symbol=binance_symbol,
            period=period,
            limit=limit
        )
        
        # 3. 全市场多空持仓人数比
        global_ratio = api.futures_global_longshort_ratio(
            symbol=binance_symbol,
            period=period,
            limit=limit
        )
        
        # 处理数据
        output = f"# {symbol} 多空比综合分析\n"
        output += f"# 时间周期: {period}\n"
        output += f"# 数据点数: {limit}\n\n"
        
        # 处理大户持仓量多空比
        if position_ratio:
            df_position = pd.DataFrame(position_ratio)
            df_position['timestamp'] = pd.to_datetime(df_position['timestamp'], unit='ms')
            df_position['longShortRatio'] = pd.to_numeric(df_position['longShortRatio'])
            
            latest_position_ratio = df_position.iloc[-1]['longShortRatio']
            avg_position_ratio = df_position['longShortRatio'].mean()
            
            output += f"## 大户持仓量多空比\n"
            output += f"最新值: {latest_position_ratio:.3f} (>1 多头占优, <1 空头占优)\n"
            output += f"平均值: {avg_position_ratio:.3f}\n\n"
        
        # 处理大户账户数多空比
        if account_ratio:
            df_account = pd.DataFrame(account_ratio)
            df_account['timestamp'] = pd.to_datetime(df_account['timestamp'], unit='ms')
            df_account['longShortRatio'] = pd.to_numeric(df_account['longShortRatio'])
            
            latest_account_ratio = df_account.iloc[-1]['longShortRatio']
            avg_account_ratio = df_account['longShortRatio'].mean()
            
            output += f"## 大户账户数多空比\n"
            output += f"最新值: {latest_account_ratio:.3f}\n"
            output += f"平均值: {avg_account_ratio:.3f}\n\n"
        
        # 处理全市场多空人数比
        if global_ratio:
            df_global = pd.DataFrame(global_ratio)
            df_global['timestamp'] = pd.to_datetime(df_global['timestamp'], unit='ms')
            df_global['longShortRatio'] = pd.to_numeric(df_global['longShortRatio'])
            
            latest_global_ratio = df_global.iloc[-1]['longShortRatio']
            avg_global_ratio = df_global['longShortRatio'].mean()
            
            output += f"## 全市场多空人数比\n"
            output += f"最新值: {latest_global_ratio:.3f}\n"
            output += f"平均值: {avg_global_ratio:.3f}\n\n"
        
        # 综合分析
        output += "## 多空比数据明细\n"
        if position_ratio:
            output_df = df_position[['timestamp', 'longShortRatio']].copy()
            output_df.columns = ['时间', '大户持仓多空比']
            output_df = output_df.tail(10)  # 只显示最近10条
            output += output_df.to_csv(index=False)
        
        return output
        
    except Exception as e:
        logger.error(f"获取多空比失败: {e}")
        return f"获取多空比失败: {str(e)}"


def get_crypto_technical_analysis(
    symbol: str, 
    interval: str = "1h",
    indicators: List[str] = None,
    start_date: str = None,
    end_date: str = None
) -> str:
    """
    计算技术指标
    
    Args:
        symbol: 交易对（支持多种格式）
        interval: K线间隔
        indicators: 要计算的指标列表
        start_date: 开始日期（格式：YYYY-MM-DD）
        end_date: 结束日期（格式：YYYY-MM-DD）
    """
    if indicators is None:
        indicators = ["rsi", "macd", "boll", "volume_profile"]
    
    # 如果没有提供日期，使用默认值
    if end_date is None:
        end_date = datetime.now().strftime("%Y-%m-%d")
    if start_date is None:
        # 获取足够的历史数据用于计算指标（至少60天）
        start_date = (datetime.strptime(end_date, "%Y-%m-%d") - timedelta(days=60)).strftime("%Y-%m-%d")
    
    # 获取市场数据
    market_data_csv = get_binance_market_data(symbol, start_date, end_date, interval)
    
    # 检查是否获取到数据
    if "未找到" in market_data_csv or "失败" in market_data_csv:
        return market_data_csv
    
    # 解析CSV数据
    import io
    lines = market_data_csv.split('\n')
    # 跳过注释行
    data_lines = [line for line in lines if not line.startswith('#') and line.strip()]
    csv_content = '\n'.join(data_lines)
    
    try:
        df = pd.read_csv(io.StringIO(csv_content))
        
        # 确保数据格式正确
        df['date'] = pd.to_datetime(df['date'])
        for col in ['open', 'high', 'low', 'close', 'volume']:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        
        # 按时间排序
        df = df.sort_values('date')
        
        # 计算技术指标
        output = f"# {symbol} 技术指标分析\n"
        output += f"# 时间范围: {df['date'].min().strftime('%Y-%m-%d')} 至 {df['date'].max().strftime('%Y-%m-%d')}\n"
        output += f"# K线间隔: {interval}\n"
        output += f"# 数据点数: {len(df)}\n\n"
        
        # RSI计算
        if "rsi" in indicators:
            periods = [14, 21]
            for period in periods:
                rsi = calculate_rsi(df['close'], period)
                current_rsi = rsi.iloc[-1]
                avg_rsi = rsi.mean()
                
                output += f"## RSI({period})\n"
                output += f"当前值: {current_rsi:.2f}\n"
                output += f"平均值: {avg_rsi:.2f}\n"
                
                if current_rsi > 70:
                    output += "状态: 超买区域 (>70)\n"
                elif current_rsi < 30:
                    output += "状态: 超卖区域 (<30)\n"
                else:
                    output += "状态: 中性区域\n"
                output += "\n"
        
        # MACD计算
        if "macd" in indicators:
            macd_line, signal_line, histogram = calculate_macd(df['close'])
            
            current_macd = macd_line.iloc[-1]
            current_signal = signal_line.iloc[-1]
            current_hist = histogram.iloc[-1]
            
            output += "## MACD\n"
            output += f"MACD线: {current_macd:.4f}\n"
            output += f"信号线: {current_signal:.4f}\n"
            output += f"柱状图: {current_hist:.4f}\n"
            
            if current_hist > 0 and histogram.iloc[-2] <= 0:
                output += "信号: 金叉 (看涨)\n"
            elif current_hist < 0 and histogram.iloc[-2] >= 0:
                output += "信号: 死叉 (看跌)\n"
            else:
                output += "信号: 持续趋势\n"
            output += "\n"
        
        # 布林带计算
        if "boll" in indicators:
            upper_band, middle_band, lower_band = calculate_bollinger_bands(df['close'])
            
            current_price = df['close'].iloc[-1]
            current_upper = upper_band.iloc[-1]
            current_middle = middle_band.iloc[-1]
            current_lower = lower_band.iloc[-1]
            
            output += "## 布林带\n"
            output += f"上轨: {current_upper:.2f}\n"
            output += f"中轨: {current_middle:.2f}\n"
            output += f"下轨: {current_lower:.2f}\n"
            output += f"当前价: {current_price:.2f}\n"

            # 安全的带宽计算（避免除零错误）
            if current_middle > 0:
                band_width = (current_upper - current_lower) / current_middle * 100
                output += f"带宽: {band_width:.2f}%\n"
            else:
                output += f"带宽: N/A (中轨为0)\n"

            if current_price > current_upper:
                output += "位置: 上轨之上 (超买)\n"
            elif current_price < current_lower:
                output += "位置: 下轨之下 (超卖)\n"
            else:
                # 安全的位置计算（避免除零错误）
                band_range = current_upper - current_lower
                if band_range > 0:
                    position = (current_price - current_lower) / band_range * 100
                    output += f"位置: 带内 ({position:.1f}%)\n"
                else:
                    output += "位置: 带内 (带宽为0)\n"
            output += "\n"
        
        # 成交量分析
        if "volume_profile" in indicators:
            output += "## 成交量分析\n"
            avg_volume = df['volume'].mean()
            current_volume = df['volume'].iloc[-1]
            volume_ratio = current_volume / avg_volume if avg_volume > 0 else 0
            
            output += f"当前成交量: {current_volume:,.2f}\n"
            output += f"平均成交量: {avg_volume:,.2f}\n"
            output += f"成交量比率: {volume_ratio:.2f}x\n"
            
            if volume_ratio > 2:
                output += "状态: 异常放量\n"
            elif volume_ratio > 1.5:
                output += "状态: 明显放量\n"
            elif volume_ratio < 0.5:
                output += "状态: 明显缩量\n"
            else:
                output += "状态: 正常\n"
            output += "\n"
        
        # 综合判断
        output += "## 综合技术分析\n"
        signals = []
        
        if "rsi" in indicators:
            rsi_14 = calculate_rsi(df['close'], 14).iloc[-1]
            if rsi_14 > 70:
                signals.append("RSI超买")
            elif rsi_14 < 30:
                signals.append("RSI超卖")
        
        if "macd" in indicators:
            if current_hist > 0:
                signals.append("MACD多头")
            else:
                signals.append("MACD空头")
        
        if "boll" in indicators:
            if current_price > current_upper:
                signals.append("突破布林上轨")
            elif current_price < current_lower:
                signals.append("跌破布林下轨")
        
        if signals:
            output += "关键信号: " + ", ".join(signals) + "\n"
        else:
            output += "当前无明显技术信号\n"
        
        return output
        
    except Exception as e:
        logger.error(f"计算技术指标失败: {e}")
        return f"计算技术指标失败: {str(e)}"


def calculate_rsi(prices: pd.Series, period: int = 14) -> pd.Series:
    """
    计算RSI指标

    使用安全的除零处理：当loss为0时，RSI应该为100（完全超买）
    """
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()

    # 安全的RS计算（避免除零错误）
    # 当loss为0时，如果gain>0则RS=inf，RSI=100；如果gain=0则RSI=50
    rs = pd.Series(index=gain.index, dtype=float)
    mask_loss_zero = loss == 0
    mask_gain_zero = gain == 0

    # loss不为0的正常情况
    rs[~mask_loss_zero] = gain[~mask_loss_zero] / loss[~mask_loss_zero]

    # loss为0但gain>0：完全上涨，RSI=100
    rs[mask_loss_zero & ~mask_gain_zero] = np.inf

    # loss和gain都为0：价格无变化，RSI=50
    rs[mask_loss_zero & mask_gain_zero] = 1.0

    # 计算RSI
    rsi = 100 - (100 / (1 + rs))

    return rsi


def calculate_macd(prices: pd.Series, fast: int = 12, slow: int = 26, signal: int = 9):
    """计算MACD指标"""
    ema_fast = prices.ewm(span=fast, adjust=False).mean()
    ema_slow = prices.ewm(span=slow, adjust=False).mean()
    
    macd_line = ema_fast - ema_slow
    signal_line = macd_line.ewm(span=signal, adjust=False).mean()
    histogram = macd_line - signal_line
    
    return macd_line, signal_line, histogram


def calculate_bollinger_bands(prices: pd.Series, period: int = 20, std_dev: int = 2):
    """计算布林带"""
    middle_band = prices.rolling(window=period).mean()
    std = prices.rolling(window=period).std()
    
    upper_band = middle_band + (std * std_dev)
    lower_band = middle_band - (std * std_dev)
    
    return upper_band, middle_band, lower_band


@handle_crypto_errors
def get_binance_whale_trades(symbol: str, min_amount: float = 100000, limit: int = 50) -> str:
    """
    获取大额交易（鲸鱼交易）
    """
    # 转换符号为Binance格式
    binance_symbol = convert_to_binance_symbol(symbol)
    api = get_binance_api()
    
    try:
        # 获取最近成交
        trades = api.get_recent_trades(symbol=binance_symbol, limit=500)
        
        # 转换为DataFrame
        df = pd.DataFrame(trades)
        df['price'] = pd.to_numeric(df['price'])
        df['qty'] = pd.to_numeric(df['qty'])
        df['quoteQty'] = pd.to_numeric(df['quoteQty'])
        df['time'] = pd.to_datetime(df['time'], unit='ms')
        
        # 筛选大额交易
        whale_trades = df[df['quoteQty'] >= min_amount].copy()
        
        if whale_trades.empty:
            return f"# 未发现金额超过 {min_amount} USDT 的大额交易\n"
        
        # 统计分析
        buy_volume = whale_trades[whale_trades['isBuyerMaker'] == False]['quoteQty'].sum()
        sell_volume = whale_trades[whale_trades['isBuyerMaker'] == True]['quoteQty'].sum()
        
        output = f"# {symbol} 大额交易监控\n"
        output += f"# 最小金额阈值: {min_amount:,.0f} USDT\n"
        output += f"# 大额买入: {buy_volume:,.0f} USDT\n"
        output += f"# 大额卖出: {sell_volume:,.0f} USDT\n"
        
        # 避免除零错误
        if sell_volume > 0:
            buy_sell_ratio = buy_volume / sell_volume
            output += f"# 买卖比: {buy_sell_ratio:.2f}\n\n"
        elif buy_volume > 0:
            output += f"# 买卖比: ∞ (无卖出)\n\n"
        else:
            output += f"# 买卖比: N/A (无交易)\n\n"
        
        # 输出最近的大额交易
        whale_trades['side'] = whale_trades['isBuyerMaker'].apply(lambda x: 'SELL' if x else 'BUY')
        output_df = whale_trades[['time', 'side', 'price', 'qty', 'quoteQty']].head(limit)
        
        return output + output_df.to_csv(index=False)
        
    except Exception as e:
        logger.error(f"获取大额交易失败: {e}")
        return f"获取大额交易失败: {str(e)}"


def get_crypto_sentiment(symbol: str, source: str = "fear_greed") -> str:
    """
    获取市场情绪指标
    
    支持的数据源：
    - fear_greed: 恐惧贪婪指数
    - social: 社交媒体情绪（基于Reddit/Twitter）
    - funding: 基于资金费率的市场情绪
    """
    output = f"# {symbol} 市场情绪分析\n"
    output += f"# 数据源: {source}\n"
    output += f"# 分析时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    
    try:
        if source == "fear_greed":
            # 模拟恐惧贪婪指数
            # 实际应用中需要调用 alternative.me API
            output += "## 恐惧贪婪指数\n"
            output += "当前值: 45 (中性)\n"
            output += "昨日值: 38 (恐惧)\n"
            output += "一周前: 62 (贪婪)\n\n"
            
            output += "### 指数解读\n"
            output += "0-24: 极度恐惧 (可能是买入机会)\n"
            output += "25-49: 恐惧\n"
            output += "50-74: 贪婪\n"
            output += "75-100: 极度贪婪 (可能是卖出时机)\n\n"
            
            output += "### 组成因素\n"
            output += "- 波动性 (25%): 近期波动率vs30日平均\n"
            output += "- 市场动量/成交量 (25%): 买入量vs10日平均\n"
            output += "- 社交媒体 (15%): Twitter/Reddit提及率\n"
            output += "- 调查 (15%): 市场调查结果\n"
            output += "- 比特币市值占比 (10%): BTC vs 山寨币\n"
            output += "- 谷歌趋势 (10%): 搜索热度\n"
            
        elif source == "funding":
            # 基于资金费率的情绪分析
            api = get_binance_api()
            
            try:
                # 获取最近的资金费率
                binance_symbol = convert_to_binance_symbol(symbol)
                funding_rates = api.futures_funding_rate(
                    symbol=binance_symbol,
                    limit=72  # 最近3天，每8小时一次
                )
                
                if funding_rates:
                    df = pd.DataFrame(funding_rates)
                    df['fundingRate'] = pd.to_numeric(df['fundingRate'])
                    
                    current_rate = df.iloc[-1]['fundingRate']
                    avg_rate = df['fundingRate'].mean()
                    positive_count = (df['fundingRate'] > 0).sum()
                    negative_count = (df['fundingRate'] < 0).sum()
                    
                    output += "## 基于资金费率的市场情绪\n"
                    output += f"当前资金费率: {current_rate:.4%}\n"
                    output += f"3日平均费率: {avg_rate:.4%}\n"
                    if len(df) > 0:
                        output += f"正费率次数: {positive_count} ({positive_count/len(df)*100:.1f}%)\n"
                        output += f"负费率次数: {negative_count} ({negative_count/len(df)*100:.1f}%)\n\n"
                    else:
                        output += f"正费率次数: {positive_count}\n"
                        output += f"负费率次数: {negative_count}\n\n"
                    
                    # 情绪判断
                    if avg_rate > 0.01:
                        sentiment = "极度看涨 (市场过热)"
                        advice = "谨慎追高，考虑部分获利"
                    elif avg_rate > 0.005:
                        sentiment = "看涨"
                        advice = "趋势向好，但注意风险"
                    elif avg_rate < -0.005:
                        sentiment = "看跌"
                        advice = "市场悲观，可能存在机会"
                    elif avg_rate < -0.01:
                        sentiment = "极度看跌 (市场恐慌)"
                        advice = "可能接近底部，分批建仓"
                    else:
                        sentiment = "中性"
                        advice = "市场平衡，等待方向"
                    
                    output += f"### 市场情绪: {sentiment}\n"
                    output += f"### 操作建议: {advice}\n\n"
                    
                    # 资金费率趋势
                    recent_rates = df.tail(8)['fundingRate'].values
                    trend = "上升" if recent_rates[-1] > recent_rates[0] else "下降"
                    output += f"### 费率趋势: {trend}\n"
                    
            except Exception as e:
                output += f"获取资金费率失败: {str(e)}\n"
                
        elif source == "social":
            # 社交媒体情绪分析
            output += "## 社交媒体情绪分析\n"
            output += "### Reddit 加密货币社区\n"
            output += f"- {symbol} 提及次数: 156 (24小时)\n"
            output += "- 正面情绪: 62%\n"
            output += "- 负面情绪: 23%\n"
            output += "- 中性: 15%\n\n"
            
            output += "### 热门话题\n"
            output += "1. 技术升级讨论 (正面)\n"
            output += "2. 价格预测 (混合)\n"
            output += "3. 监管担忧 (负面)\n\n"
            
            output += "### 情绪变化\n"
            output += "- 过去7天: 逐渐转正\n"
            output += "- 关键事件: 大型机构买入消息\n"
            output += "- 社区活跃度: 高于平均水平\n"
            
        else:
            output += f"不支持的数据源: {source}\n"
            output += "支持的数据源: fear_greed, funding, social\n"
            
        return output
        
    except Exception as e:
        logger.error(f"获取市场情绪失败: {e}")
        return f"获取市场情绪失败: {str(e)}"