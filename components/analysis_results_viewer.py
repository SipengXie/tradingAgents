"""
分析结果查看器组件
显示历史和实时的分析结果
"""

import streamlit as st


def render_historical_results(loaded_data: dict, state_mgr):
    """
    渲染历史分析结果

    Args:
        loaded_data: 加载的历史数据
        state_mgr: 状态管理器实例
    """
    st.header("📊 历史分析结果")

    # 遍历所有日期的结果
    for date, state in loaded_data.items():
        with st.expander(f"📅 {date} - {state.get('company_of_interest', 'N/A')}", expanded=True):
            # 添加按钮以开始与这个报告的交易员对话
            if st.button(f"💬 与交易员讨论此报告", key=f"chat_{date}"):
                # 设置聊天上下文
                state_mgr.set_chat_context_from_analysis(
                    state.get('company_of_interest', 'N/A'),
                    state,
                    state.get('final_decision', {})
                )
                state_mgr.clear_chat_messages()
                st.rerun()

            # 显示最终决策
            _render_final_decision(state)

            # 显示各种报告
            _render_reports(state)


def render_realtime_results(analysis_data: dict, state_mgr):
    """
    渲染实时分析结果

    Args:
        analysis_data: 分析数据
        state_mgr: 状态管理器实例
    """
    st.header("🔄 实时分析结果")

    state = analysis_data['state']
    decision = analysis_data['decision']
    ticker = analysis_data['ticker']

    # 添加与交易员讨论按钮
    if st.button("💬 与交易员讨论实时分析", key="chat_realtime"):
        state_mgr.set_chat_context_from_analysis(ticker, state, decision)
        state_mgr.clear_chat_messages()
        st.rerun()

    # 显示决策
    st.subheader(f"📈 {ticker} 的最终决策：")
    if decision:
        if isinstance(decision, str):
            decision_color = {
                "LONG": "green",
                "SHORT": "red",
                "NEUTRAL": "orange"
            }.get(decision.upper(), "blue")
            st.markdown(f"### :{decision_color}[{decision.upper()}]")
        else:
            st.json(decision)

    # 显示详细报告
    st.subheader("📄 智能体详细报告：")
    _render_reports(state)

    # 清除实时分析按钮
    if st.button("🗑️ 清除实时分析", disabled=state_mgr.analysis_in_progress):
        state_mgr.clear_realtime_analysis()

    st.divider()


def _render_final_decision(state: dict):
    """
    渲染最终决策

    Args:
        state: 状态字典
    """
    final_decision = state.get('final_decision', {})
    if final_decision and isinstance(final_decision, dict):
        col1, col2, col3 = st.columns(3)
        with col1:
            action = final_decision.get('action', 'N/A')
            if action == 'LONG':
                st.success(f"### 💰 {action}")
            elif action == 'SHORT':
                st.error(f"### 📉 {action}")
            else:
                st.warning(f"### ⏸️ {action}")
        with col2:
            st.metric("置信度", final_decision.get('confidence', 'N/A'))
        with col3:
            st.info(f"资产: {state.get('company_of_interest', 'N/A')}")

        if final_decision.get('reasoning'):
            st.markdown("**决策理由:**")
            st.write(final_decision['reasoning'])


def _render_reports(state: dict):
    """
    渲染各种分析报告

    Args:
        state: 状态字典
    """
    # 市场技术分析
    if state.get('market_report'):
        with st.expander("🔍 市场技术分析"):
            st.write(state['market_report'])

    # 社交情绪分析
    if state.get('sentiment_report'):
        with st.expander("📱 社交情绪分析"):
            st.write(state['sentiment_report'])

    # 新闻分析
    if state.get('news_report'):
        with st.expander("📰 新闻分析"):
            st.write(state['news_report'])

    # 基本面分析
    if state.get('fundamentals_report'):
        with st.expander("📊 基本面分析"):
            st.write(state['fundamentals_report'])

    # 投资辩论结果
    if state.get('investment_debate_state', {}).get('judge_decision'):
        with st.expander("⚖️ 研究员辩论（看涨 vs 看跌）"):
            st.write(state['investment_debate_state']['judge_decision'])

    # 交易员提案
    if state.get('trader_investment_plan'):
        with st.expander("💼 交易员提案"):
            st.write(state['trader_investment_plan'])

    # 风险评估
    if state.get('risk_debate_state', {}).get('judge_decision'):
        with st.expander("🛡️ 风险管理评估"):
            st.write(state['risk_debate_state']['judge_decision'])
