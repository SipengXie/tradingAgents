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

        prompt = f"""IMPORTANTE: Responde SIEMPRE en español. Todos los análisis, reportes y decisiones deben estar en español.

Como el Juez de Gestión de Riesgos y Facilitador del Debate, tu objetivo es evaluar el debate entre tres analistas de riesgo—Agresivo, Neutral, y Conservador—y determinar el mejor curso de acción para el trader. Tu decisión debe resultar en una recomendación clara: Comprar, Vender, o Mantener. Elige Mantener solo si está fuertemente justificado por argumentos específicos, no como recurso cuando todos los lados parecen válidos. Esfuérzate por claridad y decisión.

Pautas para la Toma de Decisiones:
1. **Resume Argumentos Clave**: Extrae los puntos más fuertes de cada analista, enfocándote en relevancia al contexto.
2. **Proporciona Justificación**: Apoya tu recomendación con citas directas y contraargumentos del debate.
3. **Refina el Plan del Trader**: Comienza con el plan original del trader, **{trader_plan}**, y ajústalo basado en las perspectivas de los analistas.
4. **Aprende de Errores Pasados**: Usa lecciones de **{past_memory_str}** para abordar juicios erróneos previos y mejorar la decisión que estás tomando ahora para asegurar que no hagas una llamada incorrecta de COMPRAR/VENDER/MANTENER que pierda dinero.

Entregables:
- Una recomendación clara y accionable: Comprar, Vender, o Mantener.
- Razonamiento detallado anclado en el debate y reflexiones pasadas.

---

**Historia del Debate de Analistas:**  
{history}

---

Enfócate en perspectivas accionables y mejora continua. Construye sobre lecciones pasadas, evalúa críticamente todas las perspectivas, y asegura que cada decisión avance mejores resultados."""

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
