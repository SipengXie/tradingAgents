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
            "重要提示：务必始终使用中文回答。所有分析、报告和决策都应使用中文。\n\n"
            "你是一位社交媒体研究员/分析师和公司新闻分析师，负责分析特定公司过去一周的社交媒体帖子、最新公司新闻和公众情绪。"
            "你将获得一个公司名称，你的目标是撰写一份全面的长篇报告，详细说明你的分析、见解以及对交易者和投资者的影响。\n\n"
            "重要规则：\n"
            "1. 如果无法获取数据，必须明确说明，不要猜测或编造任何信息。\n"
            "2. 不要提及具体的价格数据，只分析社交媒体情绪和舆论趋势。\n"
            "3. 确保只分析社交媒体内容、新闻报道和公众情绪，不涉及价格预测。\n"
            "4. 尽可能查看所有可能的来源，从社交媒体到情绪分析再到新闻。\n"
            "5. 不要简单地说趋势混合，要提供详细和有洞察力的分析，帮助交易者做出决策。\n\n"
            "请确保在报告末尾添加一个Markdown表格，以组织报告的关键点，使其有条理且易于阅读。"
        )

        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "你是一个有帮助的AI助手，与其他助手协作。"
                    " 使用提供的工具来推进回答问题。"
                    " 如果你无法完全回答，没关系；另一个拥有不同工具的助手会从你停下的地方继续帮助。"
                    " 执行你能做的，以取得进展。"
                    " 如果你或任何其他助手有最终交易建议：**买入/持有/卖出**或可交付成果，"
                    " 请在你的回复前加上 最终交易建议：**买入/持有/卖出**，以便团队知道可以停止。"
                    " 你可以访问以下工具：{tool_names}。\n{system_message}"
                    "供你参考，当前日期是 {current_date}。我们要分析的当前公司是 {ticker}",
                ),
                MessagesPlaceholder(variable_name="messages"),
            ]
        )

        prompt = prompt.partial(system_message=system_message)
        prompt = prompt.partial(tool_names=", ".join([tool.name for tool in tools]))
        prompt = prompt.partial(current_date=current_date)
        prompt = prompt.partial(ticker=ticker)

        chain = prompt | llm.bind_tools(tools)

        try:
            result = chain.invoke(state["messages"])
            report = ""
            
            # 处理工具调用结果
            if hasattr(result, 'tool_calls') and len(result.tool_calls) > 0:
                # 有工具调用，报告将在后续节点中生成
                report = ""
            elif hasattr(result, 'content'):
                # 直接返回内容作为报告
                report = result.content
            else:
                # 错误情况
                report = "错误：无法生成社交媒体分析报告。请检查数据源是否可用。"
                
            return {
                "messages": [result],
                "sentiment_report": report,
            }
        except Exception as e:
            # 错误处理
            error_message = f"社交媒体分析过程中发生错误：{str(e)}"
            from langchain_core.messages import AIMessage
            error_result = AIMessage(content=error_message)
            
            return {
                "messages": [error_result],
                "sentiment_report": error_message,
            }

    return social_media_analyst_node
