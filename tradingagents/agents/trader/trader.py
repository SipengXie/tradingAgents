import functools
import time
import json


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

        context = {
            "role": "user",
            "content": f"重要提示：务必用中文回复！ 基于团队分析师的综合评估，以下是针对{company_name}的个性化交易策略。此计划结合了当前市场技术趋势、宏观经济指标和社交媒体情绪。请将该策略作为基础，评估您接下来的交易决策。\n\n建议交易策略：{investment_plan}\n\n请使用这些洞察力做出明智且具战略性的决策。",
        }

        messages = [
            {
                "role": "system",
                "content": f"""重要提示：务必用中文回复！ 您是一名交易员，负责分析市场数据并做出交易决策。基于您的分析，提供具体的交易建议——做多、做空或中性。做出明确的决策，并在最后使用“FINAL TRADING PROPOSAL: LONG/NEUTRAL/SHORT”确认您的建议。同时，回顾过往决策中的经验和教训，从中学习。以下是类似情形的反思和教训：{past_memory_str}""",
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
