from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import time
import json


def create_social_media_analyst(llm, toolkit):
    def social_media_analyst_node(state):
        current_date = state["trade_date"]
        ticker = state["company_of_interest"]
        company_name = state["company_of_interest"]

        if toolkit.config["online_tools"]:
            tools = [toolkit.get_stock_news_openai]
        else:
            tools = [
                toolkit.get_reddit_stock_info,
            ]

        system_message = (
            "IMPORTANTE: Responde SIEMPRE en español. Todos los análisis, reportes y decisiones deben estar en español.\n\nEres un investigador/analista de redes sociales y noticias específicas de empresas encargado de analizar publicaciones en redes sociales, noticias recientes de la empresa, y el sentimiento público para una empresa específica durante la semana pasada. Se te dará el nombre de una empresa y tu objetivo es escribir un reporte comprensivo largo detallando tu análisis, perspectivas, e implicaciones para traders e inversores sobre el estado actual de esta empresa después de mirar redes sociales y lo que la gente dice sobre esa empresa, analizando datos de sentimiento de lo que la gente siente cada día sobre la empresa, y mirando noticias recientes de la empresa. Trata de mirar todas las fuentes posibles desde redes sociales hasta sentimiento hasta noticias. No simplemente declares que las tendencias son mixtas, proporciona análisis detallado y perspicaces que puedan ayudar a los traders a tomar decisiones."
            + """ Asegúrate de agregar una tabla Markdown al final del reporte para organizar los puntos clave del reporte, organizados y fáciles de leer.""",
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
                    "Para tu referencia, la fecha actual es {current_date}. La empresa actual que queremos analizar es {ticker}",
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
            "sentiment_report": report,
        }

    return social_media_analyst_node
