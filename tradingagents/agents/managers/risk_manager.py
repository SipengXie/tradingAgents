import time
import json


def create_risk_manager(llm, memory):
    def risk_manager_node(state) -> dict:

        company_name = state["company_of_interest"]

        history = state["risk_debate_state"]["history"]
        risk_debate_state = state["risk_debate_state"]
        market_research_report = state["market_report"]
        news_report = state["news_report"]
        fundamentals_report = state["news_report"]
        sentiment_report = state["sentiment_report"]
        trader_plan = state["investment_plan"]

        curr_situation = f"{market_research_report}\n\n{sentiment_report}\n\n{news_report}\n\n{fundamentals_report}"
        past_memories = memory.get_memories(curr_situation, n_matches=2)

        past_memory_str = ""
        for i, rec in enumerate(past_memories, 1):
            past_memory_str += rec["recommendation"] + "\n\n"

        prompt = f"""重要提示：务必始终使用中文回答。所有分析、报告和决策都应使用中文。

作为风险管理裁判和辩论协调者，您的任务是评估三位风险分析师——激进型、中性型和保守型——的辩论，并为交易者制定最佳行动方案。您的决定必须清晰、果断，并基于充分的论据。仅在有明确支持的情况下选择保持中性。

## 决策指南：

1. **总结关键论点**：提炼每位分析师的最有力观点，聚焦与市场背景的相关性。
2. **提供理由说明**：通过直接引用辩论中的论据和反驳，阐明您为何做出此决策。
3. **完善交易计划**：从交易者原始计划 **{trader_plan}** 出发，结合分析师的见解进行调整。
4. **过往经验反思**：利用 **{past_memory_str}** 中的经验教训，避免重复过往错误，确保决策优化。

## 交付成果：

- 明确、可操作的建议：做多、做空或保持中性。
- 基于辩论和过往经验的详细推理。

---

**分析师辩论历史：**  
{history}

---

专注于可操作的见解和持续改进。基于过往经验教训，批判性地评估所有观点，确保每个决定都能带来更好的结果。"""

        response = llm.invoke(prompt)

        new_risk_debate_state = {
            "judge_decision": response.content,
            "history": risk_debate_state["history"],
            "risky_history": risk_debate_state["risky_history"],
            "safe_history": risk_debate_state["safe_history"],
            "neutral_history": risk_debate_state["neutral_history"],
            "latest_speaker": "Judge",
            "current_risky_response": risk_debate_state["current_risky_response"],
            "current_safe_response": risk_debate_state["current_safe_response"],
            "current_neutral_response": risk_debate_state["current_neutral_response"],
            "count": risk_debate_state["count"],
        }

        return {
            "risk_debate_state": new_risk_debate_state,
            "final_trade_decision": response.content,
        }

    return risk_manager_node
