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

        trader_decision = state["trader_investment_plan"]

        prompt = f"""IMPORTANTE: Responde SIEMPRE en español. Todos los análisis, reportes y decisiones deben estar en español.

Como el Analista de Riesgo Seguro/Conservador, tu objetivo principal es proteger activos, minimizar la volatilidad, y asegurar crecimiento constante y confiable. Priorizas la estabilidad, seguridad, y mitigación de riesgos, evaluando cuidadosamente pérdidas potenciales, recesiones económicas, y volatilidad del mercado. Al evaluar la decisión o plan del trader, examina críticamente elementos de alto riesgo, señalando dónde la decisión puede exponer a la firma a riesgo indebido y dónde alternativas más cautelosas podrían asegurar ganancias a largo plazo. Aquí está la decisión del trader:

{trader_decision}

Tu tarea es contrarrestar activamente los argumentos de los Analistas Agresivo y Neutral, destacando dónde sus puntos de vista pueden pasar por alto amenazas potenciales o fallar en priorizar la sostenibilidad. Responde directamente a sus puntos, aprovechando las siguientes fuentes de datos para construir un caso convincente para un ajuste de enfoque de bajo riesgo a la decisión del trader:

Reporte de Investigación de Mercado: {market_research_report}
Reporte de Sentimiento de Redes Sociales: {sentiment_report}
Reporte de Últimos Asuntos Mundiales: {news_report}
Reporte de Fundamentos de la Empresa: {fundamentals_report}
Aquí está el historial actual de conversación: {history} Aquí está la última respuesta del analista agresivo: {current_risky_response} Aquí está la última respuesta del analista neutral: {current_neutral_response}. Si no hay respuestas de los otros puntos de vista, no alucines y solo presenta tu punto.

Comprómetete cuestionando su optimismo y enfatizando las posibles desventajas que pueden haber pasado por alto. Aborda cada uno de sus contrapuntos para mostrar por qué una postura conservadora es en última instancia el camino más seguro para los activos de la firma. Enfócate en debatir y criticar sus argumentos para demostrar la fortaleza de una estrategia de bajo riesgo sobre sus enfoques. Responde conversacionalmente como si estuvieras hablando sin ningún formato especial."""

        response = llm.invoke(prompt)

        argument = f"Analista Conservador: {response.content}"

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
