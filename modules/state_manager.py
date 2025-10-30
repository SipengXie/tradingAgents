"""
状态管理器
集中管理所有 Streamlit session_state 变量
"""

import streamlit as st
from tradingagents.default_config import DEFAULT_CONFIG


class StateManager:
    """统一管理 Streamlit session state"""

    def __init__(self):
        """初始化状态管理器"""
        pass

    def initialize(self):
        """初始化所有 session state 变量"""
        # API 测试相关
        if 'api_tested' not in st.session_state:
            st.session_state.api_tested = False
        if 'api_test_results' not in st.session_state:
            st.session_state.api_test_results = {}

        # 聊天相关
        if 'chat_messages' not in st.session_state:
            st.session_state.chat_messages = []
        if 'chat_context' not in st.session_state:
            st.session_state.chat_context = None
        if 'show_chat' not in st.session_state:
            st.session_state.show_chat = False

        # 分析相关
        if 'analysis_in_progress' not in st.session_state:
            st.session_state.analysis_in_progress = False
        if 'realtime_analysis' not in st.session_state:
            st.session_state.realtime_analysis = None
        if 'loaded_results' not in st.session_state:
            st.session_state.loaded_results = None

        # 手动学习相关
        if 'manual_selected_log' not in st.session_state:
            st.session_state.manual_selected_log = None
        if 'manual_learning_in_progress' not in st.session_state:
            st.session_state.manual_learning_in_progress = False
        if 'manual_learning_result' not in st.session_state:
            st.session_state.manual_learning_result = None
        if 'manual_decision_logs' not in st.session_state:
            st.session_state.manual_decision_logs = []
        if 'show_learned_logs' not in st.session_state:
            st.session_state.show_learned_logs = False
        if 'delete_confirm' not in st.session_state:
            st.session_state.delete_confirm = False

        # LLM 配置相关
        config = DEFAULT_CONFIG
        if 'llm_provider' not in st.session_state:
            st.session_state.llm_provider = config.get("llm_provider", "openai")
        if 'deep_think_llm' not in st.session_state:
            st.session_state.deep_think_llm = config.get("deep_think_llm", "openai/gpt-4.1")
        if 'quick_think_llm' not in st.session_state:
            st.session_state.quick_think_llm = config.get("quick_think_llm", "openai/gpt-4.1-mini")

    # API 测试相关属性
    @property
    def api_tested(self):
        return st.session_state.api_tested

    @api_tested.setter
    def api_tested(self, value):
        st.session_state.api_tested = value

    @property
    def api_test_results(self):
        return st.session_state.api_test_results

    @api_test_results.setter
    def api_test_results(self, value):
        st.session_state.api_test_results = value

    # 聊天相关属性
    @property
    def chat_messages(self):
        return st.session_state.chat_messages

    @chat_messages.setter
    def chat_messages(self, value):
        st.session_state.chat_messages = value

    @property
    def chat_context(self):
        return st.session_state.chat_context

    @chat_context.setter
    def chat_context(self, value):
        st.session_state.chat_context = value

    @property
    def show_chat(self):
        return st.session_state.show_chat

    @show_chat.setter
    def show_chat(self, value):
        st.session_state.show_chat = value

    # 分析相关属性
    @property
    def analysis_in_progress(self):
        return st.session_state.analysis_in_progress

    @analysis_in_progress.setter
    def analysis_in_progress(self, value):
        st.session_state.analysis_in_progress = value

    @property
    def realtime_analysis(self):
        return st.session_state.realtime_analysis

    @realtime_analysis.setter
    def realtime_analysis(self, value):
        st.session_state.realtime_analysis = value

    @property
    def has_realtime_analysis(self):
        return st.session_state.realtime_analysis is not None

    @property
    def loaded_results(self):
        return st.session_state.loaded_results

    @loaded_results.setter
    def loaded_results(self, value):
        st.session_state.loaded_results = value

    @property
    def has_loaded_results(self):
        return st.session_state.loaded_results is not None

    # 手动学习相关属性
    @property
    def manual_selected_log(self):
        return st.session_state.manual_selected_log

    @manual_selected_log.setter
    def manual_selected_log(self, value):
        st.session_state.manual_selected_log = value

    @property
    def manual_learning_in_progress(self):
        return st.session_state.manual_learning_in_progress

    @manual_learning_in_progress.setter
    def manual_learning_in_progress(self, value):
        st.session_state.manual_learning_in_progress = value

    @property
    def manual_learning_result(self):
        return st.session_state.manual_learning_result

    @manual_learning_result.setter
    def manual_learning_result(self, value):
        st.session_state.manual_learning_result = value

    @property
    def manual_decision_logs(self):
        return st.session_state.manual_decision_logs

    @manual_decision_logs.setter
    def manual_decision_logs(self, value):
        st.session_state.manual_decision_logs = value

    @property
    def show_learned_logs(self):
        return st.session_state.show_learned_logs

    @show_learned_logs.setter
    def show_learned_logs(self, value):
        st.session_state.show_learned_logs = value

    @property
    def delete_confirm(self):
        return st.session_state.delete_confirm

    @delete_confirm.setter
    def delete_confirm(self, value):
        st.session_state.delete_confirm = value

    # LLM 配置相关属性
    @property
    def llm_provider(self):
        return st.session_state.llm_provider

    @llm_provider.setter
    def llm_provider(self, value):
        st.session_state.llm_provider = value

    @property
    def deep_think_llm(self):
        return st.session_state.deep_think_llm

    @deep_think_llm.setter
    def deep_think_llm(self, value):
        st.session_state.deep_think_llm = value

    @property
    def quick_think_llm(self):
        return st.session_state.quick_think_llm

    @quick_think_llm.setter
    def quick_think_llm(self, value):
        st.session_state.quick_think_llm = value

    # 便捷方法
    def clear_realtime_analysis(self):
        """清除实时分析结果"""
        self.realtime_analysis = None

    def clear_loaded_results(self):
        """清除加载的历史结果"""
        self.loaded_results = None

    def clear_chat_messages(self):
        """清除聊天消息"""
        self.chat_messages = []

    def clear_manual_learning_result(self):
        """清除手动学习结果"""
        self.manual_learning_result = None

    def set_chat_context_from_analysis(self, ticker, state, decision):
        """从分析结果设置聊天上下文"""
        self.chat_context = {
            "company_of_interest": ticker,
            "final_decision": decision,
            "trader_investment_plan": state.get("trader_investment_plan", ""),
            "market_report": state.get("market_report", ""),
            "sentiment_report": state.get("sentiment_report", ""),
            "news_report": state.get("news_report", ""),
            "fundamentals_report": state.get("fundamentals_report", "")
        }
        self.show_chat = True
