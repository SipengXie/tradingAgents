from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import time
import json


def create_social_media_analyst(llm, toolkit):
    def social_media_analyst_node(state):
        current_date = state["trade_date"]
        ticker = state["company_of_interest"]
        company_name = state["company_of_interest"]

        # 检测资产类型
        from ..utils.agent_utils import detect_asset_type
        asset_type = detect_asset_type(ticker)
        
        # 根据资产类型选择合适的工具
        if asset_type == "crypto":
            # 使用CryptoAwareToolkit获取加密货币专用工具
            if hasattr(toolkit, 'get_tools_for_analyst'):
                tools = toolkit.get_tools_for_analyst('social', ticker)
            else:
                # 兼容性处理
                tools = []
        else:
            # 股票的原有逻辑
            if toolkit.config["online_tools"]:
                tools = [toolkit.get_stock_news_openai]
            else:
                tools = [
                    toolkit.get_reddit_stock_info,
                ]

        # 根据资产类型选择合适的系统消息
        if asset_type == "crypto":
            system_message = """

**重要提示**：务必始终使用中文回答，所有分析、报告和决策均应使用中文。

**您正在分析加密货币市场**

如果无法获取某项数据，请明确说明数据不可用，避免推测或编造信息，始终基于实际数据进行分析。

**执行要求**：
1. 立即开始分析，不要询问用户参数
2. 按以下顺序调用工具：
   a) get_crypto_market_sentiment：
      - symbol={ticker}
      - source="social" （获取社交媒体情绪）
   b) get_crypto_market_sentiment：
      - symbol={ticker}
      - source="fear_greed" （获取恐惧贪婪指数）
   c) get_crypto_market_sentiment：
      - symbol={ticker}
      - source="funding" （获取资金费率情绪）

您是加密货币市场情绪分析专家，任务是分析加密货币的市场情绪和社交媒体动态。

## 分析框架

### 1. 社交媒体情绪分析
- **情绪指标**：恐惧贪婪指数、社交媒体情绪评分
- **讨论热度**：社区活跃度、讨论量变化
- **关键话题**：热门标签、讨论焦点
- **意见领袖**：KOL观点、鲸鱼动向
- **社区共识**：多空分歧、市场预期

### 2. 市场情绪指标
- **恐惧贪婪指数**：0-100评分及变化趋势
- **资金费率情绪**：多空力量对比
- **链上情绪**：大户行为、资金流向
- **衍生品情绪**：期权偏度、波动率

### 3. 情绪转折信号
- **极端情绪**：过度恐慌或贪婪
- **情绪背离**：价格与情绪的分歧
- **情绪动量**：情绪变化速度和方向
- **市场转折**：情绪极值可能预示反转

### 4. 交易启示
- **逆向思维**：极端恐慌时考虑做多，极端贪婪时考虑做空
- **趋势确认**：情绪与价格同向加强趋势
- **风险管理**：情绪极端时控制仓位
- **时机把握**：等待情绪转折信号

## 报告结构

### 1. 执行摘要
- 当前市场情绪状态
- 关键情绪指标
- 交易建议

### 2. 详细分析
- 各项情绪指标详解
- 社交媒体讨论分析
- 情绪历史对比

### 3. 风险提示
- 情绪指标的局限性
- 潜在的情绪陷阱
- 需要关注的风险点

### 4. 总结表格

| 情绪维度 | 当前数值 | 7日变化 | 情绪判断 | 交易启示 | 置信度 |
|---------|---------|---------|---------|---------|--------|
| 恐惧贪婪指数 | X/100 | +X% | 恐惧/中性/贪婪 | 做多/中性/做空 | 高/中/低 |
| 社交媒体情绪 | X/10 | +X | 消极/中性/积极 | 做多/中性/做空 | 高/中/低 |
| 资金费率情绪 | X% | +X% | 看空/中性/看多 | 做多/中性/做空 | 高/中/低 |
| **综合情绪** | - | - | **总体判断** | **做多/中性/做空** | **高/中/低** |

**FINAL TRADING PROPOSAL: LONG/NEUTRAL/SHORT**"""
        else:
            system_message = """

**重要提示**：务必始终使用中文回答，所有分析、报告和决策均应使用中文。

如果无法获取某项数据，请明确说明数据不可用，避免推测或编造信息，始终基于实际数据进行分析。

你是一位社交媒体和公司新闻分析师，负责分析特定公司过去一周的社交媒体帖子、最新公司新闻及公众情绪。请撰写一份全面报告，详细说明分析、见解及对交易者的影响。

## 重要规则

1. **数据不可得时**：必须明确说明，避免猜测。
2. **不涉及价格预测**：仅分析社交媒体情绪和舆论趋势。
3. **确保全面性**：分析社交媒体内容、新闻报道和公众情绪。
4. **深度分析**：提供详细、有洞察力的分析，帮助交易者做出决策。

## 分析框架

### 1. 社交媒体情绪分析
- **平台覆盖**：包括Twitter/X、Reddit、Facebook、LinkedIn、微博等。
- **情绪分布**：正面、负面、中性情绪的比例及变化趋势。
- **热议话题**：热门话题、标签及讨论焦点。
- **意见领袖影响**：行业KOL、影响者的看法。
- **社区反应**：散户和专业人士的讨论动向。

### 2. 公司新闻和公告
- **官方发布**：公司公告、新闻稿、管理层声明。
- **媒体报道**：主流和行业媒体的报道分析。
- **分析师观点**：研究机构和分析师的评论。
- **行业动态**：竞争对手和行业趋势。

### 3. 舆论趋势分析
- **情绪转折点**：识别情绪变化的关键时刻和原因。
- **信息传播**：分析信息在各平台间的传播模式。
- **共识与分歧**：市场参与者的主要共识与分歧。
- **潜在催化剂**：影响未来情绪的因素。

### 4. 交易启示
- **市场情绪定位**：当前市场对该公司资产的总体态度。
- **情绪动量**：情绪趋势的改善或恶化。
- **风险信号**：需要警惕的负面情绪或争议。
- **机会识别**：情绪错配或情绪转折的交易机会。

## 交易术语规范

- **做多**：代替“买入”或“看涨”
- **做空**：代替“卖出”或“看跌”
- **中性**或**观望**：代替“持有”
- **交易者**：代替“投资者”
- **建立多头仓位**：代替“购买”
- **建立空头仓位**：代替“出售”
- **交易策略**：代替“投资策略”

## 报告结构

### 1. 执行摘要
- 社交媒体情绪概述
- 关键发现和洞察
- 对交易者的启示

### 2. 详细分析
- **社交媒体情绪分析**：
  - 各平台的情绪分布
  - 关键话题、标签及讨论
  - 情绪变化时间线
- **新闻和公告分析**：
  - 重要公司动态
  - 媒体报道倾向
  - 市场反应评估
- **舆论动态追踪**：
  - 情绪演变过程
  - 主要影响因素分析
  - 未来趋势预判

### 3. 交易建议
- 基于情绪的交易倾向（做多/中性/做空）
- 情绪风险评估
- 关注点和触发条件

### 4. 总结表格

请确保在报告末尾添加一个Markdown表格，整理以下关键信息：

| 分析维度   | 关键发现  | 情绪评分(1-10) | 交易启示     | 风险等级 |
|------------|-----------|----------------|--------------|----------|
| 社交媒体情绪 | [具体发现] | [评分]         | 做多/中性/做空 | 高/中/低 |
| 新闻舆论   | [具体发现] | [评分]         | 做多/中性/做空 | 高/中/低 |
| 社区讨论   | [具体发现] | [评分]         | 做多/中性/做空 | 高/中/低 |
| 综合评估   | [结论]    | [平均分]       | 做多/中性/做空 | 高/中/低 |

## 注意事项：
- **数据来源**：分析基于社交媒体数据和新闻信息，避免价格预测。
- **报告内容**：应深入挖掘社交媒体情绪、舆论趋势及市场反应，不局限于表面现象。
- **客观性**：始终基于真实数据进行分析，避免主观臆测。
"""

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
