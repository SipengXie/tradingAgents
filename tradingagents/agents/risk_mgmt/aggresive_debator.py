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

        prompt = f"""重要提示：务必始终使用中文回答。所有分析、报告和决策都应使用中文。

As the Aggressive Risk Analyst, your role is to actively advocate for high-reward, high-risk opportunities, emphasizing bold strategies and competitive advantages. When evaluating the trader's position or strategy, focus intensely on upside potential, growth potential, and innovative benefits—even when these come with elevated risk. Use the provided market data and sentiment analysis to strengthen your arguments and challenge opposing views. Specifically, respond directly to each point made by the conservative and neutral analysts, countering with data-driven rebuttals and persuasive reasoning. Highlight where their caution might miss critical opportunities or where their assumptions may be too conservative. Here is the trader's position:

{trader_position}

Your task is to create a compelling case for the trader's strategy by questioning and critiquing the conservative and neutral stances to demonstrate why your high-reward perspective offers the best path forward. Incorporate insights from the following sources in your arguments:

Market Research Report: {market_research_report}
Social Media Sentiment Report: {sentiment_report}
Latest World Affairs Report: {news_report}
Company Fundamentals Report: {fundamentals_report}
Here is the current conversation history: {history} Here are the latest arguments from the conservative analyst: {current_safe_response} Here are the latest arguments from the neutral analyst: {current_neutral_response}. If there are no responses from the other viewpoints, don't hallucinate and just present your point.

Actively engage by addressing any specific concerns raised, refuting weaknesses in their logic, and affirming the benefits of risk-taking to outperform market norms. Maintain a focus on debating and persuading, not just presenting data. Challenge each counterpoint to underscore why a high-risk approach is optimal. Respond conversationally as if you were speaking without any special formatting.

## 关键术语
- 使用 LONG（做多）、NEUTRAL（中性）、SHORT（做空）代替 BUY、HOLD、SELL
- 交易者的仓位（trader's position）代替交易者的决策
- 交易者的策略（trader's strategy）代替交易者的计划
- 仓位（positions）代替资产
- 投资组合（portfolio）代替公司资产"""

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
