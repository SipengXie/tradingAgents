"""
决策日志查看器组件
显示决策日志的详细内容
"""

import streamlit as st
from utils.log_parsers import extract_risk, extract_proposal


class DecisionLogViewer:
    """决策日志查看器"""

    def __init__(self, log_data: dict, selected_log: dict):
        """
        初始化决策日志查看器

        Args:
            log_data: 日志数据
            selected_log: 选中的日志元信息
        """
        self.log_data = log_data
        self.selected_log = selected_log

        # 兼容两种结构：直接是对象 或 {date: state}
        if isinstance(log_data, dict) and 'decision_id' in log_data:
            self.decision_data = log_data
        elif isinstance(log_data, dict):
            # 取第一个键值
            self.decision_data = next(iter(log_data.values())) if log_data else {}
        else:
            self.decision_data = {}

    def render(self):
        """渲染完整的决策日志视图"""
        self.render_key_info()
        self.render_market_analysis()
        self.render_sentiment_analysis()
        self.render_news_analysis()
        self.render_debate()
        self.render_risk_assessment()
        self.render_trader_proposal()
        self.render_raw_json()

    def render_key_info(self):
        """渲染关键信息"""
        with st.expander("🔑 关键信息", expanded=True):
            colk1, colk2 = st.columns(2)
            with colk1:
                st.write(f"决策ID: {self.decision_data.get('decision_id', 'Unknown')}")
                st.write(f"时间戳: {self.decision_data.get('timestamp', 'Unknown')}")
            with colk2:
                st.write(f"市场: {self.selected_log.get('market', 'Unknown')}")
                st.write(f"日期: {self.selected_log.get('date', 'Unknown')}")

    def render_market_analysis(self):
        """渲染市场技术分析"""
        market_report_text = self.decision_data.get('market_report')
        technical_analysis = (
            self.decision_data.get('market_technical_analysis')
            or self.decision_data.get('technical_analysis')
            or self.decision_data.get('market_analysis')
            or market_report_text
        )
        with st.expander("📊 市场技术分析", expanded=False):
            st.write(technical_analysis or "无市场技术分析信息")

    def render_sentiment_analysis(self):
        """渲染社交情绪分析"""
        sentiment_analysis = (
            self.decision_data.get('social_sentiment_analysis')
            or self.decision_data.get('sentiment_analysis')
            or self.decision_data.get('social_analysis')
            or self.decision_data.get('sentiment_report')
        )
        with st.expander("📱 社交情绪分析", expanded=False):
            st.write(sentiment_analysis or "无社交情绪分析信息")

    def render_news_analysis(self):
        """渲染新闻分析"""
        news_analysis = (
            self.decision_data.get('news_analysis')
            or self.decision_data.get('market_news')
            or self.decision_data.get('news_report')
        )
        with st.expander("📰 新闻分析", expanded=False):
            st.write(news_analysis or "无新闻分析信息")

    def render_debate(self):
        """渲染研究员辩论"""
        debate_state = self.decision_data.get('investment_debate_state') or {}
        bull_researcher = (
            debate_state.get('bull_history')
            or self.decision_data.get('bull_researcher')
            or self.decision_data.get('bull_analysis')
            or self.decision_data.get('bullish_view')
        )
        bear_researcher = (
            debate_state.get('bear_history')
            or self.decision_data.get('bear_researcher')
            or self.decision_data.get('bear_analysis')
            or self.decision_data.get('bearish_view')
        )

        with st.expander("⚖️ 研究员辩论 (看涨 vs 看跌)", expanded=False):
            if bull_researcher or bear_researcher:
                col_bull, col_bear = st.columns(2)
                with col_bull:
                    st.markdown("**🐂 看涨观点:**")
                    st.write(bull_researcher or "无看涨分析")
                with col_bear:
                    st.markdown("**🐻 看跌观点:**")
                    st.write(bear_researcher or "无看跌分析")
                if debate_state.get('current_response'):
                    st.markdown("---")
                    st.markdown("**综合结论/当前回复**")
                    st.write(debate_state.get('current_response'))
            else:
                st.write("无研究员辩论信息")

    def render_risk_assessment(self):
        """渲染风险管理评估"""
        market_report_text = self.decision_data.get('market_report')
        risk_assessment = (
            self.decision_data.get('risk_management_assessment')
            or self.decision_data.get('risk_analysis')
            or self.decision_data.get('risk_management')
            or extract_risk(market_report_text)
        )
        with st.expander("🛡️ 风险管理评估", expanded=False):
            st.write(risk_assessment or "无风险管理评估信息")

    def render_trader_proposal(self):
        """渲染交易员提案"""
        market_report_text = self.decision_data.get('market_report')
        trader_proposal = (
            self.decision_data.get('trader_proposal')
            or self.decision_data.get('trading_proposal')
            or self.decision_data.get('trading_decision')
            or self.decision_data.get('final_decision')
            or self.decision_data.get('final_trade_decision')
            or extract_proposal(market_report_text)
        )
        with st.expander("💼 交易员提案", expanded=False):
            st.write(trader_proposal or "无交易员提案信息")

    def render_raw_json(self):
        """渲染原始 JSON"""
        with st.expander("📄 原始JSON", expanded=False):
            st.json(self.decision_data)
