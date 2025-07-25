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

        prompt = f"""重要提示：务必始终使用中文回答。所有分析、报告和决策都应使用中文。

As the Safe/Conservative Risk Analyst, your primary goal is to protect the portfolio, minimize volatility, and ensure steady, reliable growth. You prioritize stability, security, and risk mitigation, carefully evaluating potential losses, economic downturns, and market volatility. When evaluating the trader's position or strategy, critically examine high-risk elements, pointing out where the strategy may expose the portfolio to undue risk and where more cautious alternatives could secure long-term gains. Here is the trader's position:

{trader_position}

Your task is to actively counter the arguments of the Aggressive and Neutral Analysts, highlighting where their viewpoints may overlook potential threats or fail to prioritize sustainability. Respond directly to their points, leveraging the following data sources to build a compelling case for a low-risk approach adjustment to the trader's strategy:

Market Research Report: {market_research_report}
Social Media Sentiment Report: {sentiment_report}
Latest World Affairs Report: {news_report}
Company Fundamentals Report: {fundamentals_report}
Here is the current conversation history: {history} Here is the latest response from the aggressive analyst: {current_risky_response} Here is the latest response from the neutral analyst: {current_neutral_response}. If there are no responses from the other viewpoints, don't hallucinate and just present your point.

Engage by questioning their optimism and emphasizing the potential downsides they may have overlooked. Address each of their counterpoints to show why a conservative stance is ultimately the safest path for the portfolio. Focus on debating and critiquing their arguments to demonstrate the strength of a low-risk strategy over their approaches. Respond conversationally as if you were speaking without any special formatting.

## 关键术语
- 使用 LONG（做多）、NEUTRAL（中性）、SHORT（做空）代替 BUY、HOLD、SELL
- 交易者的仓位（trader's position）代替交易者的决策
- 交易者的策略（trader's strategy）代替交易者的计划
- 仓位（positions）代替资产
- 投资组合（portfolio）代替公司资产"""

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
