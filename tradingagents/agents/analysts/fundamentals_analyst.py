from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import time
import json


def create_fundamentals_analyst(llm, toolkit):
    def fundamentals_analyst_node(state):
        current_date = state["trade_date"]
        ticker = state["company_of_interest"]
        company_name = state["company_of_interest"]

        # Detectar si es criptomoneda
        is_crypto = ticker.endswith("-USD") or ticker.endswith("-EUR") or ticker.endswith("-USDT")
        
        if is_crypto:
            # Para criptomonedas, usar herramientas adaptadas
            if toolkit.config["online_tools"]:
                tools = [toolkit.get_fundamentals_openai]  # Puede buscar info de crypto online
            else:
                tools = []  # Sin herramientas offline específicas para crypto
        else:
            # Para acciones, usar herramientas tradicionales
            if toolkit.config["online_tools"]:
                tools = [toolkit.get_fundamentals_openai]
            else:
                tools = [
                    toolkit.get_finnhub_company_insider_sentiment,
                    toolkit.get_finnhub_company_insider_transactions,
                    toolkit.get_simfin_balance_sheet,
                    toolkit.get_simfin_cashflow,
                    toolkit.get_simfin_income_stmt,
                ]

        # Detectar si es criptomoneda
        is_crypto = ticker.endswith("-USD") or ticker.endswith("-EUR") or ticker.endswith("-USDT")
        
        if is_crypto:
            system_message = (
                "IMPORTANTE: Responde SIEMPRE en español. Todos los análisis, reportes y decisiones deben estar en español.\n\nEres un investigador encargado de analizar información fundamental sobre una criptomoneda. Dado que las criptomonedas no tienen estados financieros tradicionales, enfócate en: fundamentos del proyecto, tokenomics, actividad de la red, métricas de adopción, asociaciones, actividad de desarrollo, gobernanza, y posición en el mercado. Para activos cripto, analiza la tecnología blockchain subyacente, casos de uso, suministro total, suministro circulante, recompensas de staking, y crecimiento del ecosistema. Proporciona perspectivas detalladas que ayuden a los traders a entender la propuesta de valor a largo plazo de esta criptomoneda."
                + " Asegúrate de agregar una tabla Markdown al final del reporte para organizar los puntos clave del reporte, organizados y fáciles de leer."
            )
        else:
            system_message = (
                "IMPORTANTE: Responde SIEMPRE en español. Todos los análisis, reportes y decisiones deben estar en español.\n\nEres un investigador encargado de analizar información fundamental durante la semana pasada sobre una empresa. Por favor escribe un reporte comprensivo de la información fundamental de la empresa como documentos financieros, perfil de la empresa, finanzas básicas de la empresa, historial financiero de la empresa, sentimiento de insiders y transacciones de insiders para obtener una vista completa de la información fundamental de la empresa para informar a los traders. Asegúrate de incluir tanto detalle como sea posible. No simplemente declares que las tendencias son mixtas, proporciona análisis detallado y perspicaces que puedan ayudar a los traders a tomar decisiones."
                + " Asegúrate de agregar una tabla Markdown al final del reporte para organizar los puntos clave del reporte, organizados y fáciles de leer."
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
                    "Para tu referencia, la fecha actual es {current_date}. La empresa que queremos examinar es {ticker}",
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
            "fundamentals_report": report,
        }

    return fundamentals_analyst_node
