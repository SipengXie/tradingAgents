import functools
import time
import json
from ..utils.paradex_tools import (
    get_paradex_manager, 
    format_positions_for_trader,
    format_trading_history_for_trader,
    format_portfolio_insights_for_trader
)


def create_trader(llm, memory):
    def trader_node(state, name):
        company_name = state["company_of_interest"]
        investment_plan = state["investment_plan"]
        market_research_report = state["market_report"]
        sentiment_report = state["sentiment_report"]
        news_report = state["news_report"]
        fundamentals_report = state["fundamentals_report"]

        curr_situation = f"{market_research_report}\n\n{sentiment_report}\n\n{news_report}\n\n{fundamentals_report}"
        past_memories = memory.get_memories(curr_situation, n_matches=2)

        past_memory_str = ""
        if past_memories:
            for i, rec in enumerate(past_memories, 1):
                past_memory_str += rec["recommendation"] + "\n\n"
        else:
            past_memory_str = "No past memories found."
        
        # 获取 Paradex 实时交易数据
        paradex_data_str = ""
        try:
            paradex_manager = get_paradex_manager()
            portfolio_overview = paradex_manager.get_portfolio_overview()
            
            positions_text = format_positions_for_trader(portfolio_overview.get("positions_summary", {}))
            history_text = format_trading_history_for_trader(portfolio_overview.get("trading_summary", {}))
            insights_text = format_portfolio_insights_for_trader(portfolio_overview)
            
            paradex_data_str = f"""
=== 🔴 PARADEX 实际交易数据 ===
{positions_text}

{history_text}

{insights_text}
"""
        except Exception as e:
            paradex_data_str = f"\n⚠️ Paradex 数据获取失败: {str(e)}\n"

        context = {
            "role": "user",
            "content": f"重要提示：务必用中文回复！ 基于团队分析师的综合评估，以下是针对{company_name}的个性化交易策略。此计划结合了当前市场技术趋势、宏观经济指标和社交媒体情绪。请将该策略作为基础，评估您接下来的交易决策。\n\n建议交易策略：{investment_plan}\n\n请使用这些洞察力做出明智且具战略性的决策。",
        }

        messages = [
            {
                "role": "system",
                "content": f"""重要提示：务必用中文回复！ 您是一名交易员，负责分析市场数据并做出交易决策。基于您的分析，提供具体的交易建议——做多、做空或中性。做出明确的决策，并在最后使用"FINAL TRADING PROPOSAL: LONG/NEUTRAL/SHORT"确认您的建议。

🔴 **重要：必须结合用户实际 Paradex 交易情况**
{paradex_data_str}

**决策指导原则：**
1. 首先考虑当前持仓情况和风险敞口
2. 结合历史交易模式和盈亏情况
3. 评估新建议与现有投资组合的协同效应
4. 考虑仓位管理和风险分散
5. 如果已有相关品种持仓，重点考虑加仓/减仓/平仓策略

同时，回顾过往决策中的经验和教训，从中学习。以下是类似情形的反思和教训：{past_memory_str}""",
            },
            context,
        ]

        result = llm.invoke(messages)

        return {
            "messages": [result],
            "trader_investment_plan": result.content,
            "sender": name,
        }

    return functools.partial(trader_node, name="Trader")
