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

        trader_decision = state["trader_investment_plan"]

        prompt = f"""IMPORTANTE: Responde SIEMPRE en español. Todos los análisis, reportes y decisiones deben estar en español.

Como el Analista de Riesgo Agresivo, tu papel es defender activamente oportunidades de alta recompensa y alto riesgo, enfatizando estrategias audaces y ventajas competitivas. Al evaluar la decisión o plan del trader, enfócate intensamente en el potencial al alza, potencial de crecimiento, y beneficios innovadores—incluso cuando estos vengan con riesgo elevado. Usa los datos de mercado y análisis de sentimiento proporcionados para fortalecer tus argumentos y desafiar las opiniones opuestas. Específicamente, responde directamente a cada punto hecho por los analistas conservador y neutral, contrarrestando con refutaciones basadas en datos y razonamiento persuasivo. Destaca dónde su cautela podría perderse oportunidades críticas o dónde sus suposiciones pueden ser demasiado conservadoras. Aquí está la decisión del trader:

{trader_decision}

Tu tarea es crear un caso convincente para la decisión del trader cuestionando y criticando las posturas conservadora y neutral para demostrar por qué tu perspectiva de alta recompensa ofrece el mejor camino hacia adelante. Incorpora perspectivas de las siguientes fuentes en tus argumentos:

Reporte de Investigación de Mercado: {market_research_report}
Reporte de Sentimiento de Redes Sociales: {sentiment_report}
Reporte de Últimos Asuntos Mundiales: {news_report}
Reporte de Fundamentos de la Empresa: {fundamentals_report}
Aquí está el historial actual de conversación: {history} Aquí están los últimos argumentos del analista conservador: {current_safe_response} Aquí están los últimos argumentos del analista neutral: {current_neutral_response}. Si no hay respuestas de los otros puntos de vista, no alucines y solo presenta tu punto.

Comprómetete activamente abordando cualquier preocupación específica planteada, refutando las debilidades en su lógica, y afirmando los beneficios de tomar riesgos para superar las normas del mercado. Mantén un enfoque en debatir y persuadir, no solo presentar datos. Desafía cada contrapunto para subrayar por qué un enfoque de alto riesgo es óptimo. Responde conversacionalmente como si estuvieras hablando sin ningún formato especial."""

        response = llm.invoke(prompt)

        argument = f"Analista Agresivo: {response.content}"

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
