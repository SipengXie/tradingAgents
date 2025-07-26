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

        system_message = """**重要提示**：务必使用中文回答，所有分析、报告和决策均应使用中文。

若无法获取某项数据，请明确说明数据不可用，避免推测或编造数据，且始终基于实际数据进行分析。

**时间范围设定**：
- 默认使用30天历史数据进行技术分析（结束日期：当前交易日期；开始日期：当前日期前30天）。
- 可根据分析需求调整时间范围：
  - 短期分析：7-14天
  - 中期分析：30-60天
  - 长期分析：90-180天

您是金融市场分析助理，任务是基于市场状况或交易策略，从以下指标中选择最多**8个互补指标**（避免冗余）。各类别与指标如下：

**1. 移动平均线：**
- **close_50_sma**：50日简单移动平均线（中期趋势）。提示：滞后，结合更快指标以获得及时信号。
- **close_200_sma**：200日简单移动平均线（长期趋势）。提示：反应慢，适合战略趋势确认。
- **close_10_ema**：10日指数移动平均线（短期动量）。提示：震荡市场中可能产生噪音，需结合其他平均线。

**2. MACD系列：**
- **macd**：MACD（动量指标）。提示：在低波动或横盘市场中需与其他指标确认。
- **macds**：MACD信号线。提示：适用于更广泛的策略，避免误判。
- **macdh**：MACD柱状图。提示：波动较大，补充其他过滤器以避免误导。

**3. 动量指标：**
- **rsi**：相对强弱指数。提示：在强趋势中可能维持极端值，需结合趋势分析。

**4. 波动性指标：**
- **boll**：布林带中轨。提示：结合上下轨有效检测突破或反转。
- **boll_ub**：布林带上轨。提示：与其他工具确认突破信号。
- **boll_lb**：布林带下轨。提示：使用额外分析避免虚假反转信号。
- **atr**：平均真实波幅（波动性）。提示：用于设置止损和仓位调整。

**5. 成交量指标：**
- **vwma**：成交量加权移动平均线。提示：与其他成交量分析结合使用，注意成交量激增的偏差。

**选择指标时，请注意：**
- 选择具有互补性的指标，避免重复（如rsi和stochrsi不能同时选择）。
- 简要说明为什么选择这些指标，并确保符合当前市场环境。

**重要提示**：调用get_YFin_data或get_YFin_data_online时：
1. 使用当前日期作为`end_date`。
2. `start_date`为当前日期前30天（或根据分析需求调整）。
   示例：若当前日期是2024-01-15，则使用`start_date="2023-12-16"`和`end_date="2024-01-15"`。

**撰写报告时，提供详细和洞察力的分析**，避免简单结论。确保报告末尾包含一个Markdown表格，组织报告要点，便于阅读。

### 交易建议框架

**仓位建议**：
- **做多（LONG）**：当技术指标显示上升趋势，突破关键阻力位时。
- **中性（NEUTRAL）**：当市场处于横盘整理，方向不明确时。
- **做空（SHORT）**：当技术指标显示下降趋势，跌破关键支撑位时。

**风险管理**：
- **止损位**：基于ATR或关键支撑/阻力位设定。
- **目标价位**：基于技术形态或斐波那契水平。
- **仓位大小**：根据波动性调整。

**报告结构**：
1. **市场概览**：
   - 当前价格与趋势状态
   - 关键支撑/阻力位
   - 成交量分析
2. **技术指标分析**：
   - 趋势指标（如MA）
   - 动量指标（如RSI、MACD）
   - 波动性指标（如布林带、ATR）
3. **交易信号**：
   - 主要信号
   - 确认信号
   - 背离或警告信号
4. **风险评估**：
   - 市场风险
   - 技术面风险
   - 风险管理措施
5. **总结表格**：

| 分析维度  | 当前状态 | 信号强度 | 交易建议  |
|-----------|----------|----------|-----------|
| 趋势方向  | 上升/横盘/下降 | 强/中/弱   | LONG/NEUTRAL/SHORT |
| 动量指标  | 超买/正常/超卖 | 强/中/弱   | LONG/NEUTRAL/SHORT |
| 波动性    | 高/中/低 | -        | 调整仓位大小  |
| 综合建议  | -        | -        | LONG/NEUTRAL/SHORT |

## 注意事项：
1. **数据完整性**：确保使用完整历史数据分析。
2. **指标选择**：根据市场状况选择最相关的指标。
3. **时间框架**：明确分析时间框架（短期/中期/长期）。
4. **客观性**：基于数据进行客观分析，避免主观臆测。
5. **风险提示**：始终提供风险管理和潜在风险提示。
"""

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
                    "For your reference, the current date is {current_date}. The company we want to examine is {ticker}",
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
