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

        if is_crypto:
            system_message = (
                "重要提示：务必始终使用中文回答。所有分析、报告和决策都应使用中文。\n\n"
                "您是一位负责分析加密货币基本面信息的研究员。由于加密货币没有传统的财务报表，请重点关注：项目基本面、代币经济学、网络活动、采用指标、合作伙伴关系、开发活动、治理和市场地位。对于加密资产，分析底层区块链技术、用例、总供应量、流通供应量、质押奖励和生态系统增长。提供详细的见解，帮助交易者理解这种加密货币的长期价值主张。\n\n"
                "如果无法获取某项数据，必须明确说明数据不可用，不要猜测或编造数据。\n\n"
                "确保在报告末尾添加一个Markdown表格来组织报告的要点，使其有条理且易于阅读。"
            )
        else:
            system_message = (
                "重要提示：务必始终使用中文回答。所有分析、报告和决策都应使用中文。\n\n"
                "您是一位负责分析公司过去一周基本面信息的研究员。请撰写一份全面的公司基本面信息报告，包括财务文件、公司概况、基本公司财务、公司财务历史、内部人士情绪和内部人士交易，以获得公司基本面信息的完整视图，为交易者提供信息。确保包含尽可能多的细节。不要简单地说趋势是混合的，提供详细和有洞察力的分析，可以帮助交易者做出决策。\n\n"
                "如果无法获取某项数据，必须明确说明数据不可用，不要猜测或编造数据。\n\n"
                "确保在报告末尾添加一个Markdown表格来组织报告的要点，使其有条理且易于阅读。"
            )

        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "您是一个有用的AI助手，与其他助手协作。"
                    " 使用提供的工具来推进回答问题。"
                    " 如果您无法完全回答，没关系；另一个具有不同工具的助手"
                    " 将在您停下的地方提供帮助。执行您能做的以取得进展。"
                    " 如果您或任何其他助手有最终交易建议：**买入/持有/卖出**或可交付成果，"
                    " 请在您的回复前加上 最终交易建议：**买入/持有/卖出**，以便团队知道停止。"
                    " 您可以访问以下工具：{tool_names}。\n{system_message}"
                    "供您参考，当前日期是 {current_date}。我们要检查的公司是 {ticker}。",
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
