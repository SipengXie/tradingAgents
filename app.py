"""
AI 金融资产交易助手 - 主应用入口
使用 AI 智能体团队分析资产市场并提出交易决策
"""

import streamlit as st
import os

# 导入组件
from components.api_status_panel import render_api_status_panel
from components.learning_center import render_learning_center
from components.sidebar_config import render_sidebar
from components.analysis_results_viewer import (
    render_historical_results,
    render_realtime_results
)
from components.chat_interface import render_chat_interface

# 导入模块
from modules.state_manager import StateManager
from modules.analysis_executor import AnalysisExecutor

# --- 页面配置 ---
st.set_page_config(
    page_title="AI 交易助手",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 页面标题 ---
st.title("🤖 AI 金融资产交易助手")
st.markdown("该应用使用AI智能体团队分析资产市场并提出交易决策。请输入您的API密钥和分析参数以开始。")

# --- 初始化状态管理器 ---
state_mgr = StateManager()
state_mgr.initialize()

# --- API 状态面板 ---
if state_mgr.api_tested and state_mgr.api_test_results:
    render_api_status_panel(state_mgr.api_test_results)

# --- 学习中心 ---
render_learning_center(state_mgr)

st.divider()

# --- 侧边栏配置 ---
with st.sidebar:
    sidebar_config = render_sidebar(state_mgr)

# --- 主应用区域 ---
# 使用列布局来创建主内容区和右侧边栏
main_col, chat_col = st.columns([2, 1])

with main_col:
    # 显示加载的历史结果
    if state_mgr.has_loaded_results:
        render_historical_results(state_mgr.loaded_results, state_mgr)

        # 清除加载的结果按钮
        if st.button("🗑️ 清除历史结果", disabled=state_mgr.analysis_in_progress):
            state_mgr.clear_loaded_results()
            st.rerun()

        st.divider()

    # 如果分析正在进行，显示提示
    if state_mgr.analysis_in_progress:
        st.info("⏳ 分析正在进行中，请等待分析完成...")

    # 显示实时分析结果
    if state_mgr.has_realtime_analysis:
        render_realtime_results(state_mgr.realtime_analysis, state_mgr)

    # 执行分析
    if sidebar_config.get('run_analysis'):
        # 检查 API 密钥
        if not sidebar_config.get('openai_api_key') or not sidebar_config.get('finnhub_api_key'):
            st.error("请在侧边栏输入您的 OpenAI 和 Finnhub API 密钥。")
        else:
            # 设置环境变量
            os.environ["OPENAI_API_KEY"] = sidebar_config['openai_api_key']
            os.environ["FINNHUB_API_KEY"] = sidebar_config['finnhub_api_key']

            # 创建分析执行器
            executor = AnalysisExecutor(sidebar_config)

            selected_tickers = sidebar_config['selected_tickers']

            if len(selected_tickers) == 1:
                # 单一资产分析
                ticker = selected_tickers[0]

                # 设置分析进行中标志
                state_mgr.analysis_in_progress = True

                try:
                    result = executor.execute_single_analysis(
                        ticker,
                        sidebar_config['analysis_date'],
                        sidebar_config['llm_provider'],
                        sidebar_config['deep_think_llm'],
                        sidebar_config['quick_think_llm']
                    )

                    if result:
                        # 保存分析结果到实时分析 session state
                        state_mgr.realtime_analysis = result

                        # 保存分析结果到聊天上下文
                        state_mgr.set_chat_context_from_analysis(
                            ticker,
                            result['state'],
                            result['decision']
                        )
                except Exception as e:
                    st.error(f"分析失败: {str(e)}")
                finally:
                    # 分析完成，确保清除进行中标志
                    state_mgr.analysis_in_progress = False

                # 分析完成后重新运行以显示结果
                st.rerun()

            else:
                # 多资产分析
                state_mgr.analysis_in_progress = True

                try:
                    results = executor.execute_multi_analysis(
                        selected_tickers,
                        sidebar_config['analysis_date'],
                        sidebar_config['llm_provider'],
                        sidebar_config['deep_think_llm'],
                        sidebar_config['quick_think_llm']
                    )
                except Exception as e:
                    st.error(f"多资产分析失败: {str(e)}")
                finally:
                    state_mgr.analysis_in_progress = False

# 右侧聊天栏
with chat_col:
    render_chat_interface(state_mgr, sidebar_config.get('openai_api_key', ''))
