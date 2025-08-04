"""
加密货币专用工具集
提供Binance和备用数据源的访问接口
"""
from typing import Annotated, Optional
from langchain_core.tools import tool
from tradingagents.dataflows import crypto_interface
import logging

logger = logging.getLogger(__name__)


class CryptoToolkit:
    """加密货币交易工具集"""
    
    def __init__(self, config: dict):
        self.config = config
        
    @staticmethod
    @tool
    def get_crypto_market_data(
        symbol: Annotated[str, "加密货币交易对，如 BTCUSDT, ETHUSDT"],
        start_date: Annotated[str, "开始日期，格式：yyyy-mm-dd"],
        end_date: Annotated[str, "结束日期，格式：yyyy-mm-dd"],
        interval: Annotated[str, "K线间隔：1m,5m,15m,30m,1h,4h,1d,1w"] = "1h",
        data_source: Annotated[str, "数据源：binance（优先）或 finnhub"] = "binance"
    ) -> str:
        """
        获取加密货币市场数据（OHLCV）
        
        优先从Binance获取实时数据，如果失败则使用Finnhub备用数据源。
        返回包含开盘价、最高价、最低价、收盘价、成交量的数据。
        """
        try:
            if data_source == "binance":
                result = crypto_interface.get_binance_market_data(
                    symbol, start_date, end_date, interval
                )
                # 检查是否是错误报告
                if "执行失败" in result:
                    logger.info("Binance失败，尝试使用Finnhub备用数据源")
                    return crypto_interface.get_finnhub_crypto_data(
                        symbol, start_date, end_date
                    )
                return result
            else:
                return crypto_interface.get_finnhub_crypto_data(
                    symbol, start_date, end_date
                )
        except Exception as e:
            logger.error(f"获取市场数据失败: {e}")
            return f"获取 {symbol} 市场数据失败\n错误: {str(e)}\n\n请检查:\n1. 交易对符号是否正确\n2. 日期范围是否有效\n3. 网络连接是否正常"
    
    @staticmethod
    @tool
    def get_crypto_funding_rate(
        symbol: Annotated[str, "永续合约交易对，如 BTCUSDT"],
        limit: Annotated[int, "返回记录数量"] = 100
    ) -> str:
        """
        获取加密货币永续合约资金费率历史
        
        资金费率是永续合约特有的机制，正值表示多头向空头支付费用，
        负值表示空头向多头支付费用。高资金费率可能预示市场过热。
        """
        return crypto_interface.get_binance_funding_rate(symbol, limit)
    
    @staticmethod
    @tool
    def get_crypto_liquidations(
        symbol: Annotated[str, "交易对，如 BTCUSDT"],
        start_time: Annotated[Optional[str], "开始时间，格式：yyyy-mm-dd HH:MM:SS"] = None,
        end_time: Annotated[Optional[str], "结束时间，格式：yyyy-mm-dd HH:MM:SS"] = None,
        limit: Annotated[int, "返回记录数量"] = 100
    ) -> str:
        """
        获取加密货币清算数据
        
        清算数据反映了市场的杠杆水平和风险状况。
        大量清算可能导致价格剧烈波动。
        """
        return crypto_interface.get_binance_liquidations(
            symbol, start_time, end_time, limit
        )
    
    @staticmethod
    @tool
    def get_crypto_orderbook_depth(
        symbol: Annotated[str, "交易对，如 BTCUSDT"],
        limit: Annotated[int, "深度档位：5,10,20,50,100,500,1000,5000"] = 20
    ) -> str:
        """
        获取加密货币订单簿深度数据
        
        显示买卖盘的深度信息，帮助分析：
        - 支撑和阻力位
        - 市场流动性
        - 大单分布（鲸鱼活动）
        """
        return crypto_interface.get_binance_orderbook(symbol, limit)
    
    @staticmethod
    @tool
    def get_crypto_open_interest(
        symbol: Annotated[str, "期货交易对，如 BTCUSDT"],
        period: Annotated[str, "时间周期：5m,15m,30m,1h,2h,4h,6h,12h,1d"] = "1h",
        limit: Annotated[int, "返回记录数量"] = 30
    ) -> str:
        """
        获取加密货币期货持仓量数据
        
        持仓量（Open Interest）反映市场参与度和趋势强度：
        - 上升趋势+持仓量增加 = 趋势延续
        - 上升趋势+持仓量减少 = 趋势可能反转
        """
        return crypto_interface.get_binance_open_interest(symbol, period, limit)
    
    @staticmethod
    @tool
    def get_crypto_long_short_ratio(
        symbol: Annotated[str, "交易对，如 BTCUSDT"],
        period: Annotated[str, "时间周期：5m,15m,30m,1h,2h,4h,6h,12h,1d"] = "1h",
        limit: Annotated[int, "返回记录数量"] = 30
    ) -> str:
        """
        获取加密货币多空比数据
        
        显示市场参与者的多空持仓比例：
        - 比值 > 1：多头占优
        - 比值 < 1：空头占优
        - 极端值可能预示反转
        """
        return crypto_interface.get_binance_long_short_ratio(symbol, period, limit)
    
    @staticmethod
    @tool
    def get_crypto_technical_indicators(
        symbol: Annotated[str, "交易对，如 BTCUSDT"],
        interval: Annotated[str, "K线间隔：15m,30m,1h,4h,1d"] = "1h",
        indicators: Annotated[list[str], "指标列表：rsi,macd,boll,ema,volume_profile"] = None,
        start_date: Annotated[str, "开始日期（格式：YYYY-MM-DD），可选"] = None,
        end_date: Annotated[str, "结束日期（格式：YYYY-MM-DD），可选"] = None
    ) -> str:
        """
        获取加密货币技术指标分析
        
        专为加密货币优化的技术指标：
        - RSI：相对强弱指数（加密货币版本使用14周期）
        - MACD：异同移动平均线（适配24/7交易）
        - Bollinger Bands：布林带（使用20周期，2倍标准差）
        - EMA：指数移动平均线（9/21/55/200）
        - Volume Profile：成交量分布
        
        注意：如果不提供日期参数，将使用最近60天的数据来计算指标
        """
        if indicators is None:
            indicators = ["rsi", "macd", "boll", "volume_profile"]
        
        return crypto_interface.get_crypto_technical_analysis(
            symbol, interval, indicators, start_date, end_date
        )
    
    @staticmethod
    @tool
    def get_crypto_whale_trades(
        symbol: Annotated[str, "交易对，如 BTCUSDT"],
        min_amount: Annotated[float, "最小交易金额（USDT）"] = 100000,
        limit: Annotated[int, "返回记录数量"] = 50
    ) -> str:
        """
        获取加密货币大额交易（鲸鱼交易）
        
        追踪大额交易活动：
        - 大额买入：可能推动价格上涨
        - 大额卖出：可能造成价格压力
        - 异常大单：可能是市场操纵或机构活动
        """
        return crypto_interface.get_binance_whale_trades(symbol, min_amount, limit)
    
    @staticmethod 
    @tool
    def get_crypto_market_sentiment(
        symbol: Annotated[str, "交易对，如 BTCUSDT"],
        source: Annotated[str, "数据源：fear_greed, social, funding"] = "fear_greed"
    ) -> str:
        """
        获取加密货币市场情绪指标
        
        多维度情绪分析：
        - fear_greed：恐惧贪婪指数（0-100）
        - social：社交媒体情绪
        - funding：资金费率情绪
        """
        return crypto_interface.get_crypto_sentiment(symbol, source)