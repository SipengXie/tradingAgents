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

        prompt = f"""IMPORTANTE: Responde SIEMPRE en español. Todos los análisis, reportes y decisiones deben estar en español.

Como el gestor de portafolio y facilitador del debate, tu papel es evaluar críticamente esta ronda de debate y tomar una decisión definitiva: alinearte con el analista pesimista, el analista optimista, o elegir Mantener solo si está fuertemente justificado basado en los argumentos presentados.

Resume los puntos clave de ambos lados de manera concisa, enfocándote en la evidencia o razonamiento más convincente. Tu recomendación—Comprar, Vender, o Mantener—debe ser clara y accionable. Evita por defecto elegir Mantener simplemente porque ambos lados tienen puntos válidos; comprométete con una postura fundamentada en los argumentos más fuertes del debate.

Adicionalmente, desarrolla un plan de inversión detallado para el trader. Esto debe incluir:

Tu Recomendación: Una postura decisiva apoyada por los argumentos más convincentes.
Justificación: Una explicación de por qué estos argumentos llevan a tu conclusión.
Acciones Estratégicas: Pasos concretos para implementar la recomendación.
Toma en cuenta tus errores pasados en situaciones similares. Usa estas perspectivas para refinar tu toma de decisiones y asegurar que estás aprendiendo y mejorando. Presenta tu análisis conversacionalmente, como si hablaras naturalmente, sin formato especial.

Aquí están tus reflexiones pasadas sobre errores:
\"{past_memory_str}\"

Aquí está el debate:
Historia del Debate:
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
