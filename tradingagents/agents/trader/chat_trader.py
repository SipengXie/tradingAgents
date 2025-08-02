import functools
from typing import List, Dict, Any

def create_chat_trader(llm):
    """创建一个可以进行对话的交易员智能体"""
    
    def chat_trader_node(messages: List[Dict[str, str]], context: Dict[str, Any] = None):
        """
        处理与用户的对话
        
        Args:
            messages: 对话历史
            context: 上下文信息（包含分析报告等）
        
        Returns:
            str: 交易员的回复
        """
        system_prompt = """重要提示：务必用中文回复！
        
您是一名专业的金融交易员，正在与用户讨论投资决策。您可以：
1. 解释您的交易决策和理由
2. 回答关于市场分析的问题
3. 讨论风险管理策略
4. 根据用户的风险偏好提供个性化建议
5. 解释技术指标和基本面因素

请保持专业、友好的语气，用简洁清晰的语言解释复杂的金融概念。
"""
        
        # 如果有上下文信息（如分析报告），添加到系统提示中
        if context:
            context_info = "\n\n=== 当前分析报告完整内容 ===\n"
            
            # 添加资产信息
            if context.get("company_of_interest"):
                context_info += f"\n【分析资产】{context['company_of_interest']}\n"
            
            # 添加最终决策
            if context.get("final_decision"):
                decision = context['final_decision']
                if isinstance(decision, dict):
                    context_info += f"\n【最终决策】\n"
                    context_info += f"- 操作: {decision.get('action', 'N/A')}\n"
                    context_info += f"- 置信度: {decision.get('confidence', 'N/A')}\n"
                    if decision.get('reasoning'):
                        context_info += f"- 理由: {decision['reasoning']}\n"
                else:
                    context_info += f"\n【最终决策】{decision}\n"
            
            # 添加各项分析报告（完整内容，不截断）
            if context.get("market_report"):
                context_info += f"\n【市场技术分析】\n{context['market_report']}\n"
            
            if context.get("sentiment_report"):
                context_info += f"\n【社交情绪分析】\n{context['sentiment_report']}\n"
            
            if context.get("news_report"):
                context_info += f"\n【新闻分析】\n{context['news_report']}\n"
            
            if context.get("fundamentals_report"):
                context_info += f"\n【基本面分析】\n{context['fundamentals_report']}\n"
            
            if context.get("trader_investment_plan"):
                context_info += f"\n【交易计划】\n{context['trader_investment_plan']}\n"
            
            system_prompt += context_info
            system_prompt += "\n基于以上完整的报告内容，请回答用户的问题。你可以引用报告中的任何部分来支持你的回答。"
        
        # 构建完整的消息列表
        full_messages = [{"role": "system", "content": system_prompt}]
        full_messages.extend(messages)
        
        # 调用LLM获取回复
        result = llm.invoke(full_messages)
        
        return result.content
    
    return chat_trader_node