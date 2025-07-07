from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import time
import json


def create_news_analyst(llm, toolkit):
    def news_analyst_node(state):
        current_date = state["trade_date"]
        ticker = state["company_of_interest"]

        if toolkit.config["online_tools"]:
            tools = [toolkit.get_global_news_openai, toolkit.get_google_news]
        else:
            tools = [
                toolkit.get_finnhub_news,
                toolkit.get_reddit_news,
                toolkit.get_google_news,
            ]

        system_message = (
            "IMPORTANTE: Responde SIEMPRE en español. Todos los análisis, reportes y decisiones deben estar en español.\n\nEres un investigador de noticias encargado de analizar noticias recientes y tendencias durante la semana pasada. Por favor escribe un reporte comprensivo del estado actual del mundo que sea relevante para trading y macroeconomía. Mira noticias de EODHD y finnhub para ser comprensivo. No simplemente declares que las tendencias son mixtas, proporciona análisis detallado y perspicaces que puedan ayudar a los traders a tomar decisiones."
            + """ Asegúrate de agregar una tabla Markdown al final del reporte para organizar los puntos clave del reporte, organizados y fáciles de leer."""
        )

        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "IMPORTANTE: Responde SIEMPRE en español. Eres un asistente de IA útil, colaborando con otros asistentes."
                    " Usa las herramientas proporcionadas para avanzar hacia responder la pregunta."
                    " Si no puedes responder completamente, está bien; otro asistente con diferentes herramientas"
                    " ayudará donde lo dejaste. Ejecuta lo que puedas para hacer progreso."
                    " Si tú o cualquier otro asistente tiene la PROPUESTA DE TRANSACCIÓN FINAL: **COMPRAR/MANTENER/VENDER** o entregable,"
                    " prefija tu respuesta con PROPUESTA DE TRANSACCIÓN FINAL: **COMPRAR/MANTENER/VENDER** para que el equipo sepa que debe parar."
                    " Tienes acceso a las siguientes herramientas: {tool_names}.\n{system_message}"
                    "Para tu referencia, la fecha actual es {current_date}. Estamos examinando la empresa {ticker}",
                ),
                MessagesPlaceholder(variable_name="messages"),
            ]
        )

        prompt = prompt.partial(system_message=system_message)
        prompt = prompt.partial(tool_names=", ".join([tool.name for tool in tools]))
        prompt = prompt.partial(current_date=current_date)
        prompt = prompt.partial(ticker=ticker)

        chain = prompt | llm.bind_tools(tools)
        result = chain.invoke(state["messages"])

        report = ""

        if len(result.tool_calls) == 0:
            report = result.content

        return {
            "messages": [result],
            "news_report": report,
        }

    return news_analyst_node
