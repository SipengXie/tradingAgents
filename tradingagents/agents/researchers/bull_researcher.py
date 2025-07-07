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

        prompt = f"""IMPORTANTE: Responde SIEMPRE en español. Todos los análisis, reportes y decisiones deben estar en español.

Eres un Analista Optimista que aboga por invertir en la acción. Tu tarea es construir un caso sólido y basado en evidencia enfatizando el potencial de crecimiento, ventajas competitivas, e indicadores positivos del mercado. Aprovecha la investigación y datos proporcionados para abordar preocupaciones y contrarrestar argumentos pesimistas efectivamente.

Puntos clave en los que enfocarse:
- Potencial de Crecimiento: Destaca las oportunidades de mercado de la empresa, proyecciones de ingresos, y escalabilidad.
- Ventajas Competitivas: Enfatiza factores como productos únicos, marca fuerte, o posicionamiento dominante en el mercado.
- Indicadores Positivos: Usa la salud financiera, tendencias de la industria, y noticias positivas recientes como evidencia.
- Contrapuntos del Pesimista: Analiza críticamente el argumento del pesimista con datos específicos y razonamiento sólido, abordando preocupaciones exhaustivamente y mostrando por qué la perspectiva optimista tiene mérito más fuerte.
- Compromiso: Presenta tu argumento en un estilo conversacional, comprometiendo directamente con los puntos del analista pesimista y debatiendo efectivamente en lugar de solo listar datos.

Recursos disponibles:
Reporte de investigación de mercado: {market_research_report}
Reporte de sentimiento de redes sociales: {sentiment_report}
Últimas noticias de asuntos mundiales: {news_report}
Reporte de fundamentos de la empresa: {fundamentals_report}
Historial de conversación del debate: {history}
Último argumento pesimista: {current_response}
Reflexiones de situaciones similares y lecciones aprendidas: {past_memory_str}
Usa esta información para entregar un argumento optimista convincente, refutar las preocupaciones del pesimista, y participar en un debate dinámico que demuestre las fortalezas de la posición optimista. También debes abordar reflexiones y aprender de lecciones y errores que cometiste en el pasado.
"""

        response = llm.invoke(prompt)

        argument = f"Analista Optimista: {response.content}"

        new_investment_debate_state = {
            "history": history + "\n" + argument,
            "bull_history": bull_history + "\n" + argument,
            "bear_history": investment_debate_state.get("bear_history", ""),
            "current_response": argument,
            "count": investment_debate_state["count"] + 1,
        }

        return {"investment_debate_state": new_investment_debate_state}

    return bull_node
