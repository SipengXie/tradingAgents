from langchain_core.messages import AIMessage
import time
import json


def create_safe_debator(llm):
    def safe_node(state) -> dict:
        risk_debate_state = state["risk_debate_state"]
        history = risk_debate_state.get("history", "")
        safe_history = risk_debate_state.get("safe_history", "")

        current_risky_response = risk_debate_state.get("current_risky_response", "")
        current_neutral_response = risk_debate_state.get("current_neutral_response", "")

        market_research_report = state["market_report"]
        sentiment_report = state["sentiment_report"]
        news_report = state["news_report"]
        fundamentals_report = state["fundamentals_report"]

        trader_position = state["trader_investment_plan"]

        prompt = f"""

**重要提示**：务必使用中文回答，所有分析、报告和决策均应使用中文。

作为保守型风险分析师，您的主要目标是保护投资组合，最小化波动性，确保稳定和可靠的增长。您优先考虑稳定性、安全性和风险缓解，仔细评估潜在的损失、经济衰退和市场波动。在评估交易者的仓位或策略时，您需要重点分析高风险元素，指出该策略可能使投资组合面临的不必要风险，以及更多保守的替代方案如何确保长期收益。

## 任务概述：
- **辩护交易者的仓位**：通过反驳激进型和中性型分析师的观点，强调其仓位的高风险和不稳定性，展示保守策略如何降低风险、确保稳定回报。
- **反击激进型分析师**：直接回应激进型分析师的每个反驳，分析其高风险仓位可能暴露的潜在威胁，以及市场波动可能对该仓位的负面影响。
- **针对中性型分析师的回应**：批判其对风险的过度低估，展示更为保守的策略如何确保长期稳定的回报，避免短期风险的干扰。

## 可用资源：
- 市场研究报告：{market_research_report}
- 社交媒体情绪报告：{sentiment_report}
- 最新新闻和全球时事：{news_report}
- 公司基本面报告：{fundamentals_report}
- 当前辩论历史：{history}
- 激进型分析师的最新观点：{current_risky_response}
- 中性型分析师的最新观点：{current_neutral_response}

## 行动要求：
- **辩护保守策略**：强调交易者的仓位中可能存在的高风险因素，针对激进型分析师的过度乐观进行反驳，解释为何保守策略能减少潜在的损失并确保稳定收益。
- **回应高风险观点**：通过反驳激进型分析师的高风险策略，展示为何降低风险暴露、控制波动性、优化回报是更为安全的选择。
- **优化交易者的策略**：结合保守策略调整交易者的仓位，建议更稳妥的投资方案，以保障长期回报。

## 关键术语：
- 使用 **LONG（做多）**、**NEUTRAL（中性）**、**SHORT（做空）** 代替 **BUY**、**HOLD**、**SELL**。
- **交易者的仓位（trader's position）** 代替 **交易者的决策**。
- **交易者的策略（trader's strategy）** 代替 **交易者的计划**。
- **仓位（positions）** 代替 **资产**。
- **投资组合（portfolio）** 代替 **公司资产**。
"""

        response = llm.invoke(prompt)

        argument = f"Conservative Analyst: {response.content}"

        new_risk_debate_state = {
            "history": history + "\n" + argument,
            "risky_history": risk_debate_state.get("risky_history", ""),
            "safe_history": safe_history + "\n" + argument,
            "neutral_history": risk_debate_state.get("neutral_history", ""),
            "latest_speaker": "Safe",
            "current_risky_response": risk_debate_state.get(
                "current_risky_response", ""
            ),
            "current_safe_response": argument,
            "current_neutral_response": risk_debate_state.get(
                "current_neutral_response", ""
            ),
            "count": risk_debate_state["count"] + 1,
        }

        return {"risk_debate_state": new_risk_debate_state}

    return safe_node
