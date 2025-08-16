import time
import json


def create_research_manager(llm, memory):
    def research_manager_node(state) -> dict:
        history = state["investment_debate_state"].get("history", "")
        market_research_report = state["market_report"]
        sentiment_report = state["sentiment_report"]
        news_report = state["news_report"]
        fundamentals_report = state["fundamentals_report"]

        investment_debate_state = state["investment_debate_state"]

        curr_situation = f"{market_research_report}\n\n{sentiment_report}\n\n{news_report}\n\n{fundamentals_report}"
        past_memories = memory.get_memories(curr_situation, n_matches=2)

        past_memory_str = ""
        for i, rec in enumerate(past_memories, 1):
            past_memory_str += rec["recommendation"] + "\n\n"

        prompt = f"""**重要提示**：务必使用中文回答，所有分析、报告和决策均应使用中文。

作为投资组合经理和辩论协调者，您的任务是批判性地评估本轮辩论，并根据最有力的论据做出明确决策：与看跌分析师一致、与看涨分析师一致，或在有充分理由时保持中立。

请简洁总结双方的关键观点，重点突出最具说服力的证据或推理。您的建议——做多、做空或保持中性——应明确且可操作。避免仅因双方都有合理观点而默认中性。应基于最强论据做出明确的立场。

此外，为交易者制定详细的交易计划，内容包括：

1. **建议**：基于最有力论据的明确决策。
2. **理由说明**：阐述支持这一决策的论据。
3. **战略行动**：实施建议的具体步骤。
4. **过往反思**：考虑以往类似决策中的错误，并利用这些见解完善当前决策过程。

以下是您对过往错误的反思：
"{past_memory_str}"

以下是辩论内容：
辩论历史：
{history}"""
        response = llm.invoke(prompt)

        new_investment_debate_state = {
            "judge_decision": response.content,
            "history": investment_debate_state.get("history", ""),
            "bear_history": investment_debate_state.get("bear_history", ""),
            "bull_history": investment_debate_state.get("bull_history", ""),
            "current_response": response.content,
            "count": investment_debate_state["count"],
        }

        return {
            "investment_debate_state": new_investment_debate_state,
            "investment_plan": response.content,
        }

    return research_manager_node
