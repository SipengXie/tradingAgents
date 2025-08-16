from langchain_core.messages import AIMessage
import time
import json


def create_bull_researcher(llm, memory):
    def bull_node(state) -> dict:
        investment_debate_state = state["investment_debate_state"]
        history = investment_debate_state.get("history", "")
        bull_history = investment_debate_state.get("bull_history", "")

        current_response = investment_debate_state.get("current_response", "")
        market_research_report = state["market_report"]
        sentiment_report = state["sentiment_report"]
        news_report = state["news_report"]
        fundamentals_report = state["fundamentals_report"]

        curr_situation = f"{market_research_report}\n\n{sentiment_report}\n\n{news_report}\n\n{fundamentals_report}"
        past_memories = memory.get_memories(curr_situation, n_matches=2)

        past_memory_str = ""
        for i, rec in enumerate(past_memories, 1):
            past_memory_str += rec["recommendation"] + "\n\n"

        prompt = f"""

**重要提示**：务必使用中文回答，所有分析、报告和决策均应使用中文。

您是一个看涨分析师，主张建立该资产的多头仓位。您的任务是基于增长潜力、竞争优势和积极的市场指标，构建强有力的论据来支持做多，并有效地反驳看跌分析师的观点。

## 重点分析内容：

- **增长潜力**：突出公司市场机会、收入预测和可扩展性。
- **竞争优势**：强调独特产品、强大品牌或市场主导地位等优势。
- **积极指标**：利用财务健康状况、行业趋势和近期积极新闻作为证据支持。
- **反驳看跌观点**：批判性地分析看跌分析师的论点，结合具体数据和有力推理，逐一回应其关切，展示看涨观点更有力的依据。
- **互动辩论**：通过与看跌分析师的观点进行互动辩论，强化看涨立场，而不仅仅是列举数据。

## 可用资源：

- 市场研究报告：{market_research_report}
- 社交媒体情绪报告：{sentiment_report}
- 最新新闻与全球时事：{news_report}
- 公司基本面报告：{fundamentals_report}
- 辩论历史：{history}
- 最新看跌观点：{current_response}
- 以往经验教训：{past_memory_str}

## 交易建议格式：

基于您的分析，得出明确的交易建议，选择以下之一：

- **做多（LONG）**：建议做多该资产。
- **中性（NEUTRAL）**：建议保持中性，不建立仓位。
- **做空（SHORT）**：建议做空该资产（尽管作为看涨分析师，极少给出此建议）。


"""

        response = llm.invoke(prompt)

        argument = f"Bullish Analyst: {response.content}"

        new_investment_debate_state = {
            "history": history + "\n" + argument,
            "bull_history": bull_history + "\n" + argument,
            "bear_history": investment_debate_state.get("bear_history", ""),
            "current_response": argument,
            "count": investment_debate_state["count"] + 1,
        }

        return {"investment_debate_state": new_investment_debate_state}

    return bull_node
