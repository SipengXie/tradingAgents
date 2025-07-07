import functools
import time
import json


def create_trader(llm, memory):
    def trader_node(state, name):
        company_name = state["company_of_interest"]
        investment_plan = state["investment_plan"]
        market_research_report = state["market_report"]
        sentiment_report = state["sentiment_report"]
        news_report = state["news_report"]
        fundamentals_report = state["fundamentals_report"]

        curr_situation = f"{market_research_report}\n\n{sentiment_report}\n\n{news_report}\n\n{fundamentals_report}"
        past_memories = memory.get_memories(curr_situation, n_matches=2)

        past_memory_str = ""
        if past_memories:
            for i, rec in enumerate(past_memories, 1):
                past_memory_str += rec["recommendation"] + "\n\n"
        else:
            past_memory_str = "No past memories found."

        context = {
            "role": "user",
            "content": f"IMPORTANTE: Responde SIEMPRE en español. Basado en un análisis comprensivo por un equipo de analistas, aquí hay un plan de inversión personalizado para {company_name}. Este plan incorpora perspectivas de tendencias técnicas actuales del mercado, indicadores macroeconómicos, y sentimiento de redes sociales. Usa este plan como fundamento para evaluar tu próxima decisión de trading.\n\nPlan de Inversión Propuesto: {investment_plan}\n\nUtiliza estas perspectivas para tomar una decisión informada y estratégica.",
        }

        messages = [
            {
                "role": "system",
                "content": f"""IMPORTANTE: Responde SIEMPRE en español. Eres un agente de trading analizando datos de mercado para tomar decisiones de inversión. Basado en tu análisis, proporciona una recomendación específica para comprar, vender, o mantener. Termina con una decisión firme y siempre concluye tu respuesta con 'PROPUESTA DE TRANSACCIÓN FINAL: **COMPRAR/MANTENER/VENDER**' para confirmar tu recomendación. No olvides utilizar lecciones de decisiones pasadas para aprender de tus errores. Aquí hay algunas reflexiones de situaciones similares en las que negociaste y las lecciones aprendidas: {past_memory_str}""",
            },
            context,
        ]

        result = llm.invoke(messages)

        return {
            "messages": [result],
            "trader_investment_plan": result.content,
            "sender": name,
        }

    return functools.partial(trader_node, name="Trader")
