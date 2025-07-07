from langchain_core.messages import AIMessage
import time
import json


def create_bear_researcher(llm, memory):
    def bear_node(state) -> dict:
        investment_debate_state = state["investment_debate_state"]
        history = investment_debate_state.get("history", "")
        bear_history = investment_debate_state.get("bear_history", "")

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

Eres un Analista Pesimista que hace el caso en contra de invertir en la acción. Tu objetivo es presentar un argumento bien razonado enfatizando riesgos, desafíos, e indicadores negativos. Aprovecha la investigación y datos proporcionados para destacar posibles desventajas y contrarrestar argumentos optimistas efectivamente.

Puntos clave en los que enfocarse:

- Riesgos y Desafíos: Destaca factores como saturación de mercado, inestabilidad financiera, o amenazas macroeconómicas que podrían obstaculizar el rendimiento de la acción.
- Debilidades Competitivas: Enfatiza vulnerabilidades como posicionamiento de mercado más débil, innovación en declive, o amenazas de competidores.
- Indicadores Negativos: Usa evidencia de datos financieros, tendencias de mercado, o noticias adversas recientes para apoyar tu posición.
- Contrapuntos del Optimista: Analiza críticamente el argumento optimista con datos específicos y razonamiento sólido, exponiendo debilidades o suposiciones demasiado optimistas.
- Compromiso: Presenta tu argumento en un estilo conversacional, comprometiendo directamente con los puntos del analista optimista y debatiendo efectivamente en lugar de simplemente listar hechos.

Recursos disponibles:

Reporte de investigación de mercado: {market_research_report}
Reporte de sentimiento de redes sociales: {sentiment_report}
Últimas noticias de asuntos mundiales: {news_report}
Reporte de fundamentos de la empresa: {fundamentals_report}
Historial de conversación del debate: {history}
Último argumento optimista: {current_response}
Reflexiones de situaciones similares y lecciones aprendidas: {past_memory_str}
Usa esta información para entregar un argumento pesimista convincente, refutar las afirmaciones del optimista, y participar en un debate dinámico que demuestre los riesgos y debilidades de invertir en la acción. También debes abordar reflexiones y aprender de lecciones y errores que cometiste en el pasado.
"""

        response = llm.invoke(prompt)

        argument = f"Analista Pesimista: {response.content}"

        new_investment_debate_state = {
            "history": history + "\n" + argument,
            "bear_history": bear_history + "\n" + argument,
            "bull_history": investment_debate_state.get("bull_history", ""),
            "current_response": argument,
            "count": investment_debate_state["count"] + 1,
        }

        return {"investment_debate_state": new_investment_debate_state}

    return bear_node
