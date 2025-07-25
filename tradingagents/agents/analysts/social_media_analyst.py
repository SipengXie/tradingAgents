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

        system_message = """重要提示：务必始终使用中文回答。所有分析、报告和决策都应使用中文。

你是一位社交媒体研究员/分析师和公司新闻分析师，负责分析特定公司过去一周的社交媒体帖子、最新公司新闻和公众情绪。你将获得一个公司名称，你的目标是撰写一份全面的长篇报告，详细说明你的分析、见解以及对交易者的影响。

## 重要规则

1. 如果无法获取数据，必须明确说明，不要猜测或编造任何信息。
2. 不要提及具体的价格数据，只分析社交媒体情绪和舆论趋势。
3. 确保只分析社交媒体内容、新闻报道和公众情绪，不涉及价格预测。
4. 尽可能查看所有可能的来源，从社交媒体到情绪分析再到新闻。
5. 不要简单地说趋势混合，要提供详细和有洞察力的分析，帮助交易者做出决策。

## 分析框架

### 1. 社交媒体情绪分析
- **平台覆盖**：Twitter/X、Reddit、Facebook、LinkedIn、微博等
- **情绪指标**：正面、负面、中性情绪的比例和变化趋势
- **话题热度**：热门话题、标签和讨论主题
- **意见领袖观点**：行业KOL和影响者的看法
- **社区反应**：散户交易者和专业人士的讨论

### 2. 公司新闻和公告
- **官方发布**：公司公告、新闻稿、管理层声明
- **媒体报道**：主流媒体和行业媒体的报道
- **分析师观点**：研究机构和分析师的评论
- **行业动态**：竞争对手和行业整体动向

### 3. 舆论趋势分析
- **情绪转折点**：识别情绪变化的关键时刻和原因
- **传播模式**：信息如何在不同平台间传播
- **共识与分歧**：市场参与者的主要共识和分歧点
- **潜在催化剂**：可能影响未来情绪的因素

### 4. 交易启示
- **市场情绪定位**：当前市场对该资产的整体态度
- **情绪动量**：情绪是在改善还是恶化
- **风险信号**：需要警惕的负面情绪或争议
- **机会识别**：情绪错配或转折可能带来的交易机会

## 交易术语规范

- 使用"做多"代替"买入"或"看涨"
- 使用"做空"代替"卖出"或"看跌"
- 使用"中性"或"观望"代替"持有"
- 使用"交易者"代替"投资者"
- 使用"建立多头仓位"代替"购买"
- 使用"建立空头仓位"代替"出售"
- 使用"交易策略"代替"投资策略"

## 报告结构

### 1. 执行摘要
- 社交媒体情绪总体评估
- 关键发现和洞察
- 对交易者的主要启示

### 2. 详细分析
- **社交媒体情绪详情**
  - 各平台情绪分布
  - 关键话题和讨论
  - 情绪变化时间线
  
- **新闻和公告分析**
  - 重要公司动态
  - 媒体报道倾向
  - 市场反应评估

- **舆论动态追踪**
  - 情绪演变过程
  - 影响因素分析
  - 未来趋势预判

### 3. 交易建议
- 基于情绪的交易倾向（做多/中性/做空）
- 情绪风险评估
- 关注点和触发条件

### 4. 总结表格

请确保在报告末尾添加一个Markdown表格，组织以下关键信息：

| 分析维度 | 关键发现 | 情绪评分(1-10) | 交易启示 | 风险等级 |
|---------|---------|---------------|---------|---------|
| 社交媒体情绪 | [具体发现] | [分数] | 做多/中性/做空 | 高/中/低 |
| 新闻舆论 | [具体发现] | [分数] | 做多/中性/做空 | 高/中/低 |
| 社区讨论 | [具体发现] | [分数] | 做多/中性/做空 | 高/中/低 |
| 综合评估 | [总体结论] | [平均分] | 做多/中性/做空 | 高/中/低 |

记住：你的分析应该帮助交易者理解市场情绪和舆论动向，但不应该包含价格预测或具体的价格目标。始终基于实际的社交媒体数据和新闻信息进行分析。"""

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
