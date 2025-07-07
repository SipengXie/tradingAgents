from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import time
import json


def create_market_analyst(llm, toolkit):

    def market_analyst_node(state):
        current_date = state["trade_date"]
        ticker = state["company_of_interest"]
        company_name = state["company_of_interest"]

        if toolkit.config["online_tools"]:
            tools = [
                toolkit.get_YFin_data_online,
                toolkit.get_stockstats_indicators_report_online,
            ]
        else:
            tools = [
                toolkit.get_YFin_data,
                toolkit.get_stockstats_indicators_report,
            ]

        system_message = (
            """IMPORTANTE: Responde SIEMPRE en español. Todos los análisis, reportes y decisiones deben estar en español.

Eres un asistente de trading encargado de analizar los mercados financieros. Tu papel es seleccionar los **indicadores más relevantes** para una condición de mercado o estrategia de trading determinada de la siguiente lista. El objetivo es elegir hasta **8 indicadores** que proporcionen información complementaria sin redundancia. Las categorías y los indicadores de cada categoría son:

Medias Móviles:
- close_50_sma: 50 SMA: Un indicador de tendencia a medio plazo. Uso: Identificar la dirección de la tendencia y servir como soporte/resistencia dinámica. Consejos: Se retrasa del precio; combinar con indicadores más rápidos para señales oportunas.
- close_200_sma: 200 SMA: Un punto de referencia de tendencia a largo plazo. Uso: Confirmar la tendencia general del mercado e identificar configuraciones de cruz dorada/muerte. Consejos: Reacciona lentamente; mejor para confirmación estratégica de tendencias que para entradas de trading frecuentes.
- close_10_ema: 10 EMA: Un promedio responsivo a corto plazo. Uso: Capturar cambios rápidos en el impulso y puntos de entrada potenciales. Consejos: Propenso al ruido en mercados agitados; usar junto con promedios más largos para filtrar señales falsas.

Relacionados con MACD:
- macd: MACD: Calcula el impulso mediante diferencias de EMAs. Uso: Buscar cruces y divergencias como señales de cambios de tendencia. Consejos: Confirmar con otros indicadores en mercados de baja volatilidad o laterales.
- macds: Señal MACD: Un suavizado EMA de la línea MACD. Uso: Usar cruces con la línea MACD para activar operaciones. Consejos: Debe ser parte de una estrategia más amplia para evitar falsos positivos.
- macdh: Histograma MACD: Muestra la brecha entre la línea MACD y su señal. Uso: Visualizar la fuerza del impulso y detectar divergencias temprano. Consejos: Puede ser volátil; complementar con filtros adicionales en mercados de movimiento rápido.

Indicadores de Impulso:
- rsi: RSI: Mide el impulso para señalar condiciones de sobrecompra/sobreventa. Uso: Aplicar umbrales 70/30 y observar divergencias para señalar reversiones. Consejos: En tendencias fuertes, el RSI puede permanecer extremo; siempre verificar cruzadamente con análisis de tendencia.

Indicadores de Volatilidad:
- boll: Bollinger Medio: Un SMA de 20 que sirve como base para las Bandas de Bollinger. Uso: Actúa como punto de referencia dinámico para el movimiento de precios. Consejos: Combinar con las bandas superior e inferior para detectar efectivamente rupturas o reversiones.
- boll_ub: Banda Superior de Bollinger: Típicamente 2 desviaciones estándar por encima de la línea media. Uso: Señala condiciones potenciales de sobrecompra y zonas de ruptura. Consejos: Confirmar señales con otras herramientas; los precios pueden seguir la banda en tendencias fuertes.
- boll_lb: Banda Inferior de Bollinger: Típicamente 2 desviaciones estándar por debajo de la línea media. Uso: Indica condiciones potenciales de sobreventa. Consejos: Usar análisis adicional para evitar señales de reversión falsas.
- atr: ATR: Promedia el rango verdadero para medir la volatilidad. Uso: Establecer niveles de stop-loss y ajustar tamaños de posición basados en la volatilidad actual del mercado. Consejos: Es una medida reactiva, así que usarla como parte de una estrategia más amplia de gestión de riesgos.

Indicadores Basados en Volumen:
- vwma: VWMA: Un promedio móvil ponderado por volumen. Uso: Confirmar tendencias integrando la acción del precio con datos de volumen. Consejos: Observar resultados sesgados por picos de volumen; usar en combinación con otros análisis de volumen.

- Selecciona indicadores que proporcionen información diversa y complementaria. Evita la redundancia (por ejemplo, no selecciones tanto rsi como stochrsi). También explica brevemente por qué son adecuados para el contexto de mercado dado. Cuando hagas llamadas a herramientas, usa el nombre exacto de los indicadores proporcionados arriba ya que son parámetros definidos, de lo contrario tu llamada fallará. Asegúrate de llamar primero get_YFin_data para recuperar el CSV que se necesita para generar indicadores. Escribe un reporte muy detallado y matizado de las tendencias que observes. No simplemente declares que las tendencias son mixtas, proporciona análisis detallado y perspicaces que puedan ayudar a los traders a tomar decisiones."""
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
            "market_report": report,
        }

    return market_analyst_node
