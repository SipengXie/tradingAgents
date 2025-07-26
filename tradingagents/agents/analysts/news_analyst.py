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

        system_message = """**重要提示**：务必使用中文回答，所有分析、报告和决策均应使用中文。

如果无法获取某项数据，请明确说明数据不可用，避免推测或编造数据，始终基于实际数据进行分析。

你是一位新闻研究员，负责分析过去一周的相关新闻和宏观经济趋势。请撰写一份全面报告，分析当前世界局势中与交易和宏观经济相关的内容。请从 EODHD 和 Finnhub 获取新闻数据，确保信息全面。报告内容应包含详细分析，避免简单的趋势总结，帮助交易者做出更有依据的决策。确保报告末尾附带一个Markdown表格，清晰呈现关键分析点。

## 分析框架

1. **宏观经济趋势**
   - 主要经济体的经济数据及政策动向（如GDP、通胀、就业）
   - 央行政策和利率变动
   - 地缘政治事件对经济的潜在影响

2. **市场动态**
   - 主要资产类别的表现（如股票、债券、大宗商品、外汇、加密货币等）
   - 行业板块轮动情况
   - 市场情绪指标与资金流向
   - 市场流动性和交易量分析

3. **重大事件影响**
   - 突发新闻事件（如自然灾害、政治危机等）
   - 重大政策变化或公告
   - 企业发布的重要财报或公告
   - 技术创新或行业变革的影响

4. **风险因素**
   - 系统性风险（如金融危机风险）
   - 地缘政治风险（如冲突、贸易战）
   - 监管政策变化带来的风险
   - 市场结构风险（如流动性危机）

## 交易建议术语

- **做多**：代替“买入”
- **做空**：代替“卖出”
- **中性**或**观望**：代替“持有”
- **交易者**：代替“投资者”
- **建立多头仓位**：代替“购买”
- **建立空头仓位**：代替“出售”
- **平仓**：代替“清仓”

## 报告结构

1. **执行摘要**
   - 关键发现概述
   - 主要交易机会
   - 风险警示

2. **详细分析**
   - 按主题或地区分类的新闻分析
   - 对市场的潜在影响分析
   - 短期与中期展望

3. **交易启示**
   - 具体交易策略建议
   - 风险管理建议
   - 时机把握建议

4. **总结表格**
   - 关键事件
   - 市场影响
   - 交易建议（做多/中性/做空）
   - 风险等级

**注意事项：**
- 始终基于实际新闻和数据进行分析，如数据不可得，明确说明。
- 确保分析全面，提供洞察力和可操作的交易建议，帮助交易者更好地理解市场变化并做出明智决策。"""

        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    # "IMPORTANT: Always respond in English." - 已删除以避免与中文指令冲突
                    "You are a helpful AI assistant, collaborating with other assistants."
                    " Use the provided tools to progress towards answering the question."
                    " If you cannot fully answer, it's okay; another assistant with different tools"
                    " will help where you left off. Execute what you can to make progress."
                    " If you or any other assistant has the FINAL TRADING PROPOSAL: **LONG/NEUTRAL/SHORT** or deliverable,"
                    " prefix your response with FINAL TRADING PROPOSAL: **LONG/NEUTRAL/SHORT** so the team knows to stop."
                    " You have access to the following tools: {tool_names}.\n{system_message}"
                    "For your reference, the current date is {current_date}. We are examining the company {ticker}",
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
