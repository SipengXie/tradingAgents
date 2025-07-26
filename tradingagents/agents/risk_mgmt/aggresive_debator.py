import time
import json


def create_risky_debator(llm):
    def risky_node(state) -> dict:
        risk_debate_state = state["risk_debate_state"]
        history = risk_debate_state.get("history", "")
        risky_history = risk_debate_state.get("risky_history", "")

        current_safe_response = risk_debate_state.get("current_safe_response", "")
        current_neutral_response = risk_debate_state.get("current_neutral_response", "")

        market_research_report = state["market_report"]
        sentiment_report = state["sentiment_report"]
        news_report = state["news_report"]
        fundamentals_report = state["fundamentals_report"]

        trader_position = state["trader_investment_plan"]

        prompt = f"""

**重要提示**：务必使用中文回答，所有分析、报告和决策均应使用中文。

作为激进风险分析师，您的任务是积极倡导高回报、高风险的机会，强调大胆策略和竞争优势。在评估交易者的仓位（{trader_position}）或策略时，重点关注上行潜力、增长潜力和创新优势，即使这些带来较高的风险。利用市场数据和情绪分析来强化您的论点，并挑战保守型和中性型分析师的观点。具体来说，您需要直接回应保守型和中性型分析师的每个观点，通过数据驱动的反驳和有力推理来支持您的立场，强调他们的谨慎可能错失的重要机会，或他们的假设过于保守。

## 任务概述：
- **辩护交易者的策略**，通过强调其高回报潜力和市场机会，展示为什么高风险策略在此情境下是最佳选择。
- 直接回应保守型和中性型分析师的每个观点，逐一反驳并指出他们的逻辑和假设的局限性。
- 强调高回报策略如何通过承担一定的风险获得更大的市场机会。
  
## 可用资源：
- 市场研究报告：{market_research_report}
- 社交媒体情绪报告：{sentiment_report}
- 最新新闻和全球时事：{news_report}
- 公司基本面报告：{fundamentals_report}
- 当前辩论历史：{history}
- 保守型分析师的最新观点：{current_safe_response}
- 中性型分析师的最新观点：{current_neutral_response}

## 行动要求：
- 积极参与辩论，逐一回应保守型和中性型分析师提出的具体担忧，揭示他们的逻辑弱点，并重申高风险策略的优势。
- 通过反驳展示高风险策略如何在市场中创造更多机会，并加强交易者的仓位选择（{trader_position}）的合理性。
- 强调通过敢于承担风险来实现超越市场常规的回报。

## 关键术语：
- 使用 **LONG（做多）**、**NEUTRAL（中性）**、**SHORT（做空）** 代替 **BUY**、**HOLD**、**SELL**。
- **交易者的仓位（trader's position）** 代替 **交易者的决策**。
- **交易者的策略（trader's strategy）** 代替 **交易者的计划**。
- **仓位（positions）** 代替 **资产**。
- **投资组合（portfolio）** 代替 **公司资产**。

"""

        response = llm.invoke(prompt)

        argument = f"Aggressive Analyst: {response.content}"

        new_risk_debate_state = {
            "history": history + "\n" + argument,
            "risky_history": risky_history + "\n" + argument,
            "safe_history": risk_debate_state.get("safe_history", ""),
            "neutral_history": risk_debate_state.get("neutral_history", ""),
            "latest_speaker": "Risky",
            "current_risky_response": argument,
            "current_safe_response": risk_debate_state.get("current_safe_response", ""),
            "current_neutral_response": risk_debate_state.get(
                "current_neutral_response", ""
            ),
            "count": risk_debate_state["count"] + 1,
        }

        return {"risk_debate_state": new_risk_debate_state}

    return risky_node
