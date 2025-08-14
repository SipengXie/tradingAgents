#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试集成 Paradex 数据的交易员智能体
"""

import os
import sys
import asyncio
from datetime import datetime

# 添加项目根目录到 Python 路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from tradingagents.agents.trader.chat_trader import create_chat_trader
from tradingagents.agents.utils.paradex_tools import get_paradex_manager

# 设置输出编码
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

# 加载环境变量
load_dotenv()

def test_paradex_data_manager():
    """测试 Paradex 数据管理器"""
    print("=" * 60)
    print("测试 Paradex 数据管理器")
    print("=" * 60)
    
    manager = get_paradex_manager()
    
    # 测试持仓数据
    print("\n[测试] 获取持仓数据...")
    positions = manager.get_positions_summary()
    if positions.get("success"):
        print(f"✅ 持仓数据获取成功")
        print(f"   - 持仓品种: {positions.get('total_positions', 0)}")
        print(f"   - 总盈亏: {positions.get('total_unrealized_pnl', 0):.2f} USDC")
    else:
        print(f"❌ 持仓数据获取失败: {positions.get('error', 'Unknown')}")
    
    # 测试交易历史
    print("\n[测试] 获取交易历史...")
    history = manager.get_trading_history(limit=10)
    if history.get("success"):
        print(f"✅ 交易历史获取成功")
        analysis = history.get("analysis", {})
        print(f"   - 交易笔数: {analysis.get('total_trades', 0)}")
        print(f"   - 已实现盈亏: {analysis.get('total_realized_pnl', 0):.2f} USDC")
        print(f"   - 最活跃品种: {analysis.get('most_active_symbol', 'N/A')}")
    else:
        print(f"❌ 交易历史获取失败: {history.get('error', 'Unknown')}")
    
    # 测试投资组合概览
    print("\n[测试] 获取投资组合概览...")
    overview = manager.get_portfolio_overview()
    if overview.get("success"):
        print(f"✅ 投资组合概览获取成功")
        insights = overview.get("insights", [])
        if insights:
            print("   投资组合洞察:")
            for i, insight in enumerate(insights[:3], 1):
                print(f"   {i}. {insight}")
    else:
        print(f"❌ 投资组合概览获取失败: {overview.get('error', 'Unknown')}")

def test_chat_trader():
    """测试集成 Paradex 的聊天交易员"""
    print("\n" + "=" * 60)
    print("测试集成 Paradex 的聊天交易员")
    print("=" * 60)
    
    # 初始化 LLM
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ 请设置 OPENAI_API_KEY 环境变量")
        return
    
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.0,
        api_key=api_key,
        base_url=os.getenv('TRADINGAGENTS_BACKEND_URL', 'https://api.openai.com/v1')
    )
    
    # 创建聊天交易员
    chat_trader = create_chat_trader(llm)
    
    # 测试对话
    test_messages = [
        {
            "role": "user", 
            "content": "你好，请基于我的实际持仓情况，告诉我当前的投资组合状况如何？"
        }
    ]
    
    print("\n[测试] 发送消息到交易员...")
    print(f"用户消息: {test_messages[0]['content']}")
    
    try:
        response = chat_trader(test_messages)
        print(f"\n✅ 交易员回复:")
        print("-" * 40)
        print(response)
        print("-" * 40)
    except Exception as e:
        print(f"❌ 交易员回复失败: {str(e)}")

def test_trader_with_market_context():
    """测试带市场上下文的交易员"""
    print("\n" + "=" * 60)
    print("测试带市场分析上下文的交易员")
    print("=" * 60)
    
    # 初始化 LLM
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ 请设置 OPENAI_API_KEY 环境变量")
        return
    
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.0,
        api_key=api_key,
        base_url=os.getenv('TRADINGAGENTS_BACKEND_URL', 'https://api.openai.com/v1')
    )
    
    # 创建聊天交易员
    chat_trader = create_chat_trader(llm)
    
    # 模拟市场分析上下文
    context = {
        "company_of_interest": "BTC-USD-PERP",
        "market_report": """
技术分析报告：
- BTC 当前价格 $98,500，位于重要支撑位附近
- RSI 指标显示 35，处于超卖区域
- MACD 呈现看涨背离信号
- 成交量相比前期有所放大
        """,
        "sentiment_report": """
社交情绪分析：
- Twitter 情绪指数：偏悲观 (-0.3)
- Reddit 讨论热度：中等
- 机构持仓报告显示增持趋势
        """,
        "final_decision": {
            "action": "LONG",
            "confidence": "75%",
            "reasoning": "技术面显示超卖反弹机会，机构资金流入支撑"
        }
    }
    
    # 测试对话
    test_messages = [
        {
            "role": "user", 
            "content": "基于当前的市场分析，我应该如何调整我的 BTC 持仓？考虑到我的实际交易情况，你有什么具体建议？"
        }
    ]
    
    print("\n[测试] 发送带上下文的消息...")
    print(f"用户消息: {test_messages[0]['content']}")
    print(f"市场上下文: {context['company_of_interest']} - {context['final_decision']['action']}")
    
    try:
        response = chat_trader(test_messages, context)
        print(f"\n✅ 交易员回复:")
        print("-" * 40)
        print(response)
        print("-" * 40)
    except Exception as e:
        print(f"❌ 交易员回复失败: {str(e)}")

def main():
    """主测试函数"""
    print("🚀 Paradex 集成交易员测试开始")
    print(f"🕒 测试时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # 测试数据管理器
    test_paradex_data_manager()
    
    # 测试聊天交易员
    test_chat_trader()
    
    # 测试带市场上下文的交易员
    test_trader_with_market_context()
    
    print("\n" + "=" * 60)
    print("🎉 所有测试完成！")
    print("=" * 60)

if __name__ == "__main__":
    main()