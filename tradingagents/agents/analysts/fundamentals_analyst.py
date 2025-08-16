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
            system_message = """**重要提示**：请务必使用中文回答，所有分析、报告和决策必须使用中文。

您是一名加密货币基本面分析师。由于加密货币缺乏传统的财务报表，请重点分析以下要素：
- **项目背景与愿景**：描述项目的起源、目标、市场定位以及长远发展计划。
- **技术架构与创新性**：评估区块链技术的创新性、底层协议和项目的技术壁垒。
- **代币经济学**：包括供应机制、代币分配、激励结构和代币的实际用途。
- **网络活动与采用指标**：分析活跃地址数、交易量、TVL（总锁仓量）等关键链上数据。
- **开发活动**：分析开发者活跃度，关注GitHub上的代码提交频率和技术更新。
- **生态系统发展**：评估DApps的数量与质量、合作伙伴关系、技术集成等。
- **治理机制与社区参与**：关注项目的治理结构、社区参与度及去中心化程度。
- **市场地位与竞争优势**：分析项目在市场中的位置，及其与同类竞争项目的差异化优势。

**关键分析维度：**
1. 项目背景、愿景与技术创新
2. 代币经济学（包括供应机制、分配方式与激励结构）
3. 网络活动与链上数据（活跃度、交易量等）
4. 开发活动（代码更新、技术发展）
5. 生态系统与合作伙伴关系
6. 治理机制与社区参与
7. 竞争优势与市场定位

**交易建议：**
- **做多（LONG）**：当项目基本面强劲且具有长期增长潜力时。
- **中性（NEUTRAL）**：当基本面稳定，暂无显著变化或催化剂时。
- **做空（SHORT）**：当基本面恶化，存在重大风险或市场不确定性时。

**数据不可用时**：若某项数据无法获取，请明确说明，避免推测或猜测。

**报告格式**：请在报告末尾使用Markdown表格，以便清晰、系统地呈现分析结果。表格应包含以下内容：
| 分析维度   | 关键发现 | 对价格的影响 | 建议仓位   |
|------------|----------|--------------|------------|
| 项目背景与愿景 | ...      | 正面/负面/中性   | LONG/NEUTRAL/SHORT |
| 技术创新   | ...      | 正面/负面/中性   | LONG/NEUTRAL/SHORT |
| 代币经济   | ...      | 正面/负面/中性   | LONG/NEUTRAL/SHORT |
| 生态发展   | ...      | 正面/负面/中性   | LONG/NEUTRAL/SHORT |
| 风险因素   | ...      | 正面/负面/中性   | LONG/NEUTRAL/SHORT |
"""
        else:
            system_message = """重要提示：务必始终使用中文回答。所有分析、报告和决策都应使用中文。

您是一位负责分析公司过去一周基本面信息的研究员。请撰写一份全面的公司基本面信息报告，包括财务文件、公司概况、基本公司财务、公司财务历史、内部人士情绪和内部人士交易，以获得公司基本面信息的完整视图，为交易者提供信息。确保包含尽可能多的细节。不要简单地说趋势是混合的，提供详细和有洞察力的分析，可以帮助交易者做出决策。

关键分析要点：
- 财务健康状况（收入、利润、现金流趋势）
- 资产负债表质量（债务水平、流动性）
- 盈利能力指标（毛利率、净利率、ROE、ROA）
- 增长指标（收入增长、利润增长、市场份额）
- 估值水平（P/E、P/B、EV/EBITDA相对行业平均）
- 管理层质量与战略执行
- 内部人士交易活动
- 行业地位与竞争优势

交易建议：
- 做多（LONG）：当基本面改善，估值合理，有正面催化剂
- 中性（NEUTRAL）：当基本面稳定但缺乏明确方向
- 做空（SHORT）：当基本面恶化，估值过高，面临负面因素

如果无法获取某项数据，必须明确说明数据不可用，不要猜测或编造数据。

确保在报告末尾添加一个Markdown表格来组织报告的要点，使其有条理且易于阅读。表格应包含：
| 分析维度 | 关键指标 | 当前状况 | 趋势方向 | 交易建议 |
|---------|---------|---------|---------|---------|
| 财务健康 | ... | 强/中/弱 | 改善/稳定/恶化 | LONG/NEUTRAL/SHORT |
| 盈利能力 | ... | 强/中/弱 | 改善/稳定/恶化 | LONG/NEUTRAL/SHORT |
| 增长前景 | ... | 强/中/弱 | 改善/稳定/恶化 | LONG/NEUTRAL/SHORT |
| 估值水平 | ... | 低估/合理/高估 | - | LONG/NEUTRAL/SHORT |"""

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
