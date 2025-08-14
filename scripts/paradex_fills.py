#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Paradex 成交历史查询脚本
查询用户在 Paradex 上的成交历史记录
"""

import os
import sys
import asyncio
from datetime import datetime
from typing import List, Dict, Any
from dotenv import load_dotenv
from paradex_py import Paradex
from paradex_py.environment import Environment

# 设置输出编码为 UTF-8
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

# 加载环境变量
load_dotenv()

def format_fill_data(fill: Dict[str, Any]) -> str:
    """格式化成交数据为可读字符串"""
    # 解析时间戳
    timestamp = datetime.fromtimestamp(int(fill.get('created_at', 0)) / 1000)
    
    # 格式化基本信息
    symbol = fill.get('market', 'Unknown')
    side = fill.get('side', 'Unknown')
    size = fill.get('size', '0')
    price = fill.get('price', '0')
    
    # 计算交易金额
    try:
        trade_value = float(size) * float(price)
    except (ValueError, TypeError):
        trade_value = 0.0
    
    # 获取手续费信息
    fee = fill.get('fee', '0')
    
    # 获取 PnL 信息（如果存在）
    realized_pnl = fill.get('realized_pnl', 'N/A')
    
    return f"""
交易时间: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}
交易对:   {symbol}
方向:     {side.upper()}
数量:     {size}
价格:     {price}
交易金额: {trade_value:.2f}
手续费:   {fee}
实现PnL:  {realized_pnl}
订单ID:   {fill.get('order_id', 'N/A')}
成交ID:   {fill.get('id', 'N/A')}
{'-' * 50}
"""

async def get_fills_history(paradex_client: Paradex, limit: int = 50) -> List[Dict[str, Any]]:
    """获取成交历史记录"""
    try:
        print(f"正在获取最近 {limit} 条成交记录...")
        
        # 使用正确的 API 方法名和参数
        params = {"page_size": limit}
        fills_response = paradex_client.api_client.fetch_fills(params=params)
        
        if isinstance(fills_response, dict) and 'results' in fills_response:
            return fills_response['results']
        elif isinstance(fills_response, list):
            return fills_response
        else:
            print(f"获取成交数据格式: {type(fills_response)}")
            print(f"成交数据内容: {fills_response}")
            return []
            
    except Exception as e:
        print(f"获取成交历史失败: {str(e)}")
        return []

async def get_positions(paradex_client: Paradex) -> List[Dict[str, Any]]:
    """获取当前持仓信息"""
    try:
        print("正在获取当前持仓...")
        
        # 使用正确的 API 方法名
        positions_response = paradex_client.api_client.fetch_positions()
        
        if isinstance(positions_response, dict) and 'results' in positions_response:
            return positions_response['results']
        elif isinstance(positions_response, list):
            return positions_response
        else:
            print(f"获取持仓数据格式: {type(positions_response)}")
            print(f"持仓数据内容: {positions_response}")
            return []
            
    except Exception as e:
        print(f"获取持仓信息失败: {str(e)}")
        return []

def format_position_data(position: Dict[str, Any]) -> str:
    """格式化持仓数据为可读字符串"""
    symbol = position.get('market', 'Unknown')
    side = position.get('side', 'Unknown')
    size = position.get('size', '0')
    entry_price = position.get('entry_price', '0')
    mark_price = position.get('mark_price', '0')
    unrealized_pnl = position.get('unrealized_pnl', '0')
    
    return f"""
持仓品种: {symbol}
方向:     {side.upper()}
数量:     {size}
开仓价:   {entry_price}
标记价:   {mark_price}
未实现PnL: {unrealized_pnl}
{'-' * 30}
"""

async def main():
    """主函数"""
    print("=" * 60)
    print("Paradex 成交历史查询工具")
    print("=" * 60)
    
    # 获取环境变量
    l1_address = os.getenv('PARADEX_ADDR')
    l1_private_key = os.getenv('PARADEX_KEY')
    
    if not l1_address or not l1_private_key:
        print("[错误] 请在 .env 文件中配置 PARADEX_ADDR 和 PARADEX_KEY")
        print("示例:")
        print('PARADEX_ADDR="0x你的以太坊地址"')
        print('PARADEX_KEY="0x你的私钥"')
        return
    
    try:
        # 初始化 Paradex 客户端
        print(f"[信息] L1 地址: {l1_address}")
        print("[信息] 正在连接 Paradex 主网...")
        
        # 使用主网（正确的字符串值）
        try:
            print("[尝试] 连接 Paradex 主网...")
            paradex = Paradex(
                env="prod",  # 使用字符串值
                l1_address=l1_address,
                l1_private_key=l1_private_key
            )
            print("[成功] 主网连接成功")
        except Exception as prod_error:
            print(f"[失败] 主网连接失败: {str(prod_error)}")
            print("[信息] 尝试连接测试网...")
            try:
                paradex = Paradex(
                    env="testnet",  # 使用字符串值
                    l1_address=l1_address,
                    l1_private_key=l1_private_key
                )
                print("[成功] 测试网连接成功")
            except Exception as test_error:
                print(f"[失败] 测试网也连接失败: {str(test_error)}")
                raise test_error
        
        print(f"[成功] L2 地址: {hex(paradex.account.l2_address)}")
        print(f"[成功] L2 公钥: {hex(paradex.account.l2_public_key)}")
        
        # 1. 获取当前持仓
        print("\n" + "=" * 60)
        print("[持仓] 当前持仓信息")
        print("=" * 60)
        
        positions = await get_positions(paradex)
        
        if positions:
            for position in positions:
                print(format_position_data(position))
        else:
            print("[持仓] 暂无持仓记录")
        
        # 2. 获取成交历史
        print("\n" + "=" * 60)
        print("[成交] 成交历史记录")
        print("=" * 60)
        
        fills = await get_fills_history(paradex, limit=20)
        
        if fills:
            print(f"[成交] 共找到 {len(fills)} 条成交记录:")
            for fill in fills:
                print(format_fill_data(fill))
        else:
            print("[成交] 暂无成交记录")
            
        # 3. 生成总结
        if fills:
            total_trades = len(fills)
            buy_trades = sum(1 for fill in fills if fill.get('side', '').lower() == 'buy')
            sell_trades = total_trades - buy_trades
            
            print("\n" + "=" * 60)
            print("[统计] 交易统计")
            print("=" * 60)
            print(f"总交易数: {total_trades}")
            print(f"买入交易: {buy_trades}")
            print(f"卖出交易: {sell_trades}")
            
            # 按交易对分组统计
            symbols = {}
            for fill in fills:
                symbol = fill.get('market', 'Unknown')
                if symbol not in symbols:
                    symbols[symbol] = {'count': 0, 'volume': 0.0}
                symbols[symbol]['count'] += 1
                try:
                    size = float(fill.get('size', 0))
                    symbols[symbol]['volume'] += size
                except (ValueError, TypeError):
                    pass
            
            print(f"\n交易对统计:")
            for symbol, stats in symbols.items():
                print(f"  {symbol}: {stats['count']} 笔交易, 总量 {stats['volume']:.4f}")
        
    except Exception as e:
        print(f"[错误] {str(e)}")
        print("\n可能的解决方案:")
        print("1. 检查网络连接")
        print("2. 确认地址和私钥正确")
        print("3. 确认账户已在 Paradex 主网上激活")

if __name__ == "__main__":
    asyncio.run(main())