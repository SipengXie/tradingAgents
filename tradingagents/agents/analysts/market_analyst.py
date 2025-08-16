from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import time
import json


def create_market_analyst(llm, toolkit):

    def market_analyst_node(state):
        current_date = state["trade_date"]
        ticker = state["company_of_interest"]
        company_name = state["company_of_interest"]

        # 如果是CryptoAwareToolkit，使用智能工具选择
        if hasattr(toolkit, 'get_tools_for_analyst'):
            tools = toolkit.get_tools_for_analyst('market', ticker)
        else:
            # 兼容旧的Toolkit
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

        # 检测资产类型
        from ..utils.agent_utils import detect_asset_type
        asset_type = detect_asset_type(ticker)
        
        # 根据资产类型选择合适的系统消息
        if asset_type == "crypto":
            system_message = """**重要提示**：务必使用中文回答，所有分析、报告和决策均应使用中文。

若无法获取某项数据，请明确说明数据不可用，避免推测或编造数据，且始终基于实际数据进行分析。

**您正在分析加密货币市场**

**重要：请使用加密货币专用工具（get_crypto_开头的工具），而不是传统股票工具（get_YFin_或get_stockstats_）**

**执行要求**：
1. 立即开始分析，不要询问用户参数
2. 当前日期是 {current_date}。你必须基于这个日期计算其他日期。
3. 按以下顺序调用工具（所有工具都要调用）：
   a) get_crypto_market_data：
      - symbol={ticker}
      - start_date=计算 {current_date} 减去7天后的日期（例如：如果当前是2024-01-15，则为2024-01-08）
      - end_date={current_date}
      - interval="4h"
   b) get_crypto_technical_indicators：
      - symbol={ticker}
      - interval="4h"
      - indicators=["rsi", "macd", "boll", "volume_profile"]
      - start_date=计算 {current_date} 减去60天后的日期（例如：如果当前是2024-01-15，则为2023-11-16）
      - end_date={current_date}
   c) get_crypto_orderbook_depth：
      - symbol={ticker}
      - limit=20
   d) get_crypto_whale_trades：
      - symbol={ticker}
      - min_amount=自动计算
   e) get_crypto_open_interest：
      - symbol={ticker}
      - period="5m"
      - limit=48
   f) get_crypto_funding_rate：
      - symbol={ticker}
      - limit=100
   g) get_crypto_long_short_ratio：
      - symbol={ticker}
      - period="1h"
      - limit=30
   h) get_crypto_liquidations：
      - symbol={ticker}
      - limit=100
   i) get_crypto_market_sentiment：
      - symbol={ticker}
      - source="funding"
4. 如果某个工具调用失败，记录失败原因但继续执行其他分析

**时间范围设定**：
- 默认使用7天历史数据进行技术分析（加密货币市场变化快速）
- K线间隔默认使用4小时（4h）

您是加密货币市场分析专家，任务是分析加密货币的市场动态。请重点关注以下方面：

**1. 市场数据分析**：
- 价格走势（OHLCV数据）
- 成交量和成交额分析
- 价格波动性

**2. 技术指标分析**（请获取并分析所有以下指标）：
- RSI（相对强弱指数）
  - 分析14期和21期RSI
  - 关注超买（>70）和超卖（<30）区域
  - 观察RSI背离信号
- MACD（移动平均收敛散度）
  - 分析MACD线、信号线和柱状图
  - 关注金叉和死叉信号
  - 观察MACD与价格的背离
- 布林带（Bollinger Bands）
  - 分析上轨、中轨、下轨位置
  - 计算带宽变化（波动性）
  - 关注价格突破和回归
- 成交量分析
  - 对比当前成交量与平均成交量
  - 识别异常放量或缩量
  - 分析量价关系

**3. 加密货币专有指标**（必须分析所有以下数据）：
- 订单簿深度
  - 分析买卖盘分布
  - 识别主要支撑和阻力位
  - 计算买卖盘比率
- 大额交易（鲸鱼活动）
  - 追踪大额买入/卖出订单
  - 分析大户积累或派发行为
  - 评估对价格的潜在影响
- 持仓量（期货）
  - 分析持仓量变化趋势
  - 对比价格与持仓量关系
  - 判断趋势强度
- 资金费率（如支持）
  - 分析多空情绪
  - 识别市场过热信号
- 多空比
  - 分析散户和大户多空比
  - 识别市场情绪极端值
- 清算数据（如支持）
  - 分析近期清算量
  - 识别关键清算价位

**分析要点**：
1. 加密货币市场24/7交易，注意时区影响
2. 高波动性是常态，设置合理的止损
3. 关注比特币走势对山寨币的影响
4. 注意重大事件（升级、监管、黑客事件等）
5. 流动性可能不如传统市场，注意滑点风险

**风险管理**：
- 建议仓位：根据市场波动性调整（通常不超过总资金的5-10%）
- 止损设置：基于ATR或关键支撑位（通常5-10%）
- 分批建仓：避免一次性大额买入"""
        else:
            system_message = """**重要提示**：务必使用中文回答，所有分析、报告和决策均应使用中文。

若无法获取某项数据，请明确说明数据不可用，避免推测或编造数据，且始终基于实际数据进行分析。

**执行要求**：
1. 立即开始分析，不要询问用户参数
2. 当前日期是 {current_date}。你必须基于这个日期计算其他日期。
3. 必须按以下方式调用工具：
   a) get_YFin_data或get_YFin_data_online：
      - symbol={ticker}
      - start_date=计算 {current_date} 减去30天后的日期
      - end_date={current_date}
   b) get_stockstats_indicators_report或get_stockstats_indicators_report_online：
      - 必须分析以下指标（每个指标单独调用）：
      - rsi（14期）
      - macd（包括macd、macds、macdh）
      - boll、boll_ub、boll_lb（布林带系列）
      - close_50_sma和close_200_sma（趋势判断）
      - atr（波动性）
      - vwma或mfi（成交量相关）
3. 如果某个工具调用失败，继续执行其他分析，不要停止

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

**报告结构**（必须包含所有部分）：
1. **市场概览**：
   - 当前价格、24h涨跌幅、成交量
   - 价格趋势判断（上升/横盘/下降）
   - 关键支撑位和阻力位（至少3个）
   - 成交量特征（放量/缩量/正常）

2. **技术指标详细分析**：
   - **趋势指标**：
     - MA系统：价格与各均线关系
     - 趋势强度和持续性判断
   - **动量指标**：
     - RSI：具体数值、超买超卖判断、背离分析
     - MACD：金叉死叉、柱状图变化、背离分析
   - **波动性指标**：
     - 布林带：位置、带宽、挤压状态
     - ATR：波动性水平、止损建议

3. **特色数据分析**（加密货币专有）：
   - 订单簿：买卖压力、深度评估
   - 鲸鱼活动：大户动向判断
   - 期货数据：持仓变化、市场情绪

4. **交易信号汇总**：
   - 看涨信号：列出所有看涨因素
   - 看跌信号：列出所有看跌因素
   - 中性因素：列出观望因素

5. **风险评估**：
   - 主要风险点（至少3个）
   - 止损建议（基于ATR或支撑位）
   - 仓位建议（基于风险等级）

6. **综合分析表格**：

| 指标类别 | 具体指标 | 当前数值 | 信号解读 | 强度评级 |
|---------|---------|---------|---------|---------|
| 趋势指标 | MA50/MA200 | X/Y | 金叉/死叉/中性 | 强/中/弱 |
| 动量指标 | RSI(14) | X | 超买/正常/超卖 | 强/中/弱 |
| 动量指标 | MACD | X | 多头/空头 | 强/中/弱 |
| 波动性 | 布林带 | X | 突破/回归/挤压 | 高/中/低 |
| 成交量 | 量比 | X | 放量/缩量 | 明显/正常 |
| **综合评分** | - | - | **总体判断** | **强/中/弱** |

7. **交易建议**：
   - **方向**：LONG/NEUTRAL/SHORT
   - **信心度**：高/中/低
   - **入场价位**：具体价格
   - **止损价位**：具体价格
   - **目标价位**：具体价格（至少2个）
   - **仓位建议**：占总资金百分比

**FINAL TRADING PROPOSAL: LONG/NEUTRAL/SHORT**

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
                    "You are a market analysis expert. Your job is to IMMEDIATELY analyze market data using the available tools."
                    " DO NOT ask the user for parameters or clarification - use the default parameters specified in your instructions."
                    " Execute all relevant tools to gather comprehensive market data and provide analysis."
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
