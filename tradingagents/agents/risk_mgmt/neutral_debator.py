import time
import json


def create_neutral_debator(llm):
    def neutral_node(state) -> dict:
        risk_debate_state = state["risk_debate_state"]
        history = risk_debate_state.get("history", "")
        neutral_history = risk_debate_state.get("neutral_history", "")

        current_risky_response = risk_debate_state.get("current_risky_response", "")
        current_safe_response = risk_debate_state.get("current_safe_response", "")

        market_research_report = state["market_report"]
        sentiment_report = state["sentiment_report"]
        news_report = state["news_report"]
        fundamentals_report = state["fundamentals_report"]

        trader_decision = state["trader_investment_plan"]

        prompt = f"""IMPORTANTE: Responde SIEMPRE en español. Todos los análisis, reportes y decisiones deben estar en español.

Como el Analista de Riesgo Neutral, tu papel es proporcionar una perspectiva equilibrada, sopesando tanto los beneficios potenciales como los riesgos de la decisión o plan del trader. Priorizas un enfoque integral, evaluando las ventajas y desventajas mientras consideras tendencias de mercado más amplias, cambios económicos potenciales, y estrategias de diversificación. Aquí está la decisión del trader:

{trader_decision}

Tu tarea es desafiar tanto a los Analistas Agresivo como Conservador, señalando dónde cada perspectiva puede ser demasiado optimista o demasiado cautelosa. Usa perspectivas de las siguientes fuentes de datos para apoyar una estrategia moderada y sostenible para ajustar la decisión del trader:

Reporte de Investigación de Mercado: {market_research_report}
Reporte de Sentimiento de Redes Sociales: {sentiment_report}
Reporte de Últimos Asuntos Mundiales: {news_report}
Reporte de Fundamentos de la Empresa: {fundamentals_report}
Aquí está el historial actual de conversación: {history} Aquí está la última respuesta del analista agresivo: {current_risky_response} Aquí está la última respuesta del analista conservador: {current_safe_response}. Si no hay respuestas de los otros puntos de vista, no alucines y solo presenta tu punto.

Comprómetete activamente analizando ambos lados críticamente, abordando debilidades en los argumentos agresivo y conservador para abogar por un enfoque más equilibrado. Desafía cada uno de sus puntos para ilustrar por qué una estrategia de riesgo moderado podría ofrecer lo mejor de ambos mundos, proporcionando potencial de crecimiento mientras protege contra volatilidad extrema. Enfócate en debatir en lugar de simplemente presentar datos, apuntando a mostrar que una vista equilibrada puede llevar a los resultados más confiables. Responde conversacionalmente como si estuvieras hablando sin ningún formato especial."""

        response = llm.invoke(prompt)

        argument = f"Analista Neutral: {response.content}"

        new_risk_debate_state = {
            "history": history + "\n" + argument,
            "risky_history": risk_debate_state.get("risky_history", ""),
            "safe_history": risk_debate_state.get("safe_history", ""),
            "neutral_history": neutral_history + "\n" + argument,
            "latest_speaker": "Neutral",
            "current_risky_response": risk_debate_state.get(
                "current_risky_response", ""
            ),
            "current_safe_response": risk_debate_state.get("current_safe_response", ""),
            "current_neutral_response": argument,
            "count": risk_debate_state["count"] + 1,
        }

        return {"risk_debate_state": new_risk_debate_state}

    return neutral_node
