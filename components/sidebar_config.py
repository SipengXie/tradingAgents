"""
侧边栏配置组件
包含 API 配置、测试、智能体参数和历史结果加载
"""

import os
import json
import streamlit as st
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
from tradingagents.default_config import DEFAULT_CONFIG
from utils.api_validators import APIValidator
from config.ui_constants import POPULAR_ASSETS


def render_sidebar(state_mgr) -> dict:
    """
    渲染侧边栏配置

    Args:
        state_mgr: 状态管理器实例

    Returns:
        侧边栏配置字典
    """
    # 加载环境变量
    if os.path.exists('.env'):
        load_dotenv()

    # API 配置
    api_keys = _render_api_config()

    # API 连接测试
    _render_api_test(api_keys, state_mgr)

    st.divider()

    # 智能体参数
    agent_params = _render_agent_params(state_mgr)

    st.divider()

    # 历史结果加载
    _render_history_loader(state_mgr)

    # 返回配置
    return {
        **api_keys,
        **agent_params
    }


def _render_api_config() -> dict:
    """
    渲染 API 配置区域

    Returns:
        API 密钥字典
    """
    st.header("🔑 API 配置")

    openai_api_key = st.text_input(
        "OpenAI API 密钥",
        type="password",
        value=os.getenv("OPENAI_API_KEY") or ""
    )
    finnhub_api_key = st.text_input(
        "Finnhub API 密钥",
        type="password",
        value=os.getenv("FINNHUB_API_KEY") or ""
    )
    binance_api_key = st.text_input(
        "Binance API 密钥",
        type="password",
        value=os.getenv("BINANCE_API_KEY") or ""
    )
    binance_api_secret = st.text_input(
        "Binance API Secret",
        type="password",
        value=os.getenv("BINANCE_API_SECRET") or ""
    )

    return {
        'openai_api_key': openai_api_key,
        'finnhub_api_key': finnhub_api_key,
        'binance_api_key': binance_api_key,
        'binance_api_secret': binance_api_secret
    }


def _render_api_test(api_keys: dict, state_mgr):
    """
    渲染 API 连接测试区域

    Args:
        api_keys: API 密钥字典
        state_mgr: 状态管理器实例
    """
    st.header("🔍 API 连接测试")

    # 获取配置
    config = DEFAULT_CONFIG.copy()
    backend_url = config.get("backend_url", "")
    embedding_url = config.get("embedding_url", "")
    embedding_model = config.get("embedding_model", "")
    embedding_api_key = config.get("embedding_api_key", api_keys['openai_api_key'])

    # 显示当前配置
    with st.expander("查看当前配置"):
        st.text(f"LLM Backend URL: {backend_url}")
        st.text(f"主模型 (深度思考): {config.get('deep_think_llm', 'N/A')}")
        st.text(f"快速模型 (快速思考): {config.get('quick_think_llm', 'N/A')}")
        st.text(f"Embedding URL: {embedding_url}")
        st.text(f"Embedding Model: {embedding_model}")

    if st.button("测试 API 连接"):
        # 清空之前的测试结果
        state_mgr.api_test_results = {}

        # 测试 LLM API
        col1, col2 = st.columns(2)
        with col1:
            if api_keys['openai_api_key'] and backend_url:
                llm_success, llm_msg = APIValidator.test_llm_api(
                    backend_url,
                    api_keys['openai_api_key'],
                    config["quick_think_llm"]
                )
                state_mgr.api_test_results['llm'] = {'success': llm_success, 'message': llm_msg}
                if llm_success:
                    st.success(f"✅ {llm_msg}")
                else:
                    st.error(f"❌ {llm_msg}")
            else:
                st.warning("⚠️ 请先配置 OpenAI API 密钥")
                state_mgr.api_test_results['llm'] = {'success': False, 'message': "未配置 API 密钥"}

        with col2:
            # 测试 Finnhub API
            if api_keys['finnhub_api_key']:
                finn_success, finn_msg = APIValidator.test_finnhub_api(api_keys['finnhub_api_key'])
                state_mgr.api_test_results['finnhub'] = {'success': finn_success, 'message': finn_msg}
                if finn_success:
                    st.success(f"✅ {finn_msg}")
                else:
                    st.error(f"❌ {finn_msg}")
            else:
                st.warning("⚠️ 请先配置 Finnhub API 密钥")
                state_mgr.api_test_results['finnhub'] = {'success': False, 'message': "未配置 API 密钥"}

        # 测试 Embedding API
        if embedding_api_key and embedding_url and embedding_model:
            embed_success, embed_msg = APIValidator.test_embedding_api(
                embedding_url,
                embedding_api_key,
                embedding_model
            )
            state_mgr.api_test_results['embedding'] = {'success': embed_success, 'message': embed_msg}
            if embed_success:
                st.success(f"✅ {embed_msg}")
            else:
                st.error(f"❌ {embed_msg}")
        else:
            st.warning("⚠️ Embedding API 配置不完整")
            state_mgr.api_test_results['embedding'] = {'success': False, 'message': "配置不完整"}

        # 测试 Binance API
        binance_success, binance_msg = APIValidator.test_binance_api(
            api_keys['binance_api_key'],
            api_keys['binance_api_secret']
        )
        state_mgr.api_test_results['binance'] = {'success': binance_success, 'message': binance_msg}
        if binance_success:
            st.success(f"✅ {binance_msg}")
        else:
            st.error(f"❌ {binance_msg}")

        # 标记已测试
        state_mgr.api_tested = True
        st.rerun()


def _render_agent_params(state_mgr) -> dict:
    """
    渲染智能体参数配置区域

    Args:
        state_mgr: 状态管理器实例

    Returns:
        智能体参数字典
    """
    st.header("⚙️ 智能体参数")

    # 选择资产类别
    asset_category = st.selectbox(
        "资产类别",
        ["加密货币", "科技股", "蓝筹股", "指数", "自定义"]
    )

    # 根据类别选择资产
    if asset_category == "自定义":
        ticker = st.text_input("资产代码", "BTC-USD")
        analysis_mode = st.radio("分析模式", ["单一资产", "多资产分析"])

        if analysis_mode == "多资产分析":
            custom_tickers = st.text_area(
                "资产代码（用逗号分隔）",
                "BTC-USD, ETH-USD, AAPL, TSLA",
                help="示例：BTC-USD, ETH-USD, AAPL, TSLA, GOOGL"
            )
            selected_tickers = [t.strip() for t in custom_tickers.split(",") if t.strip()]
        else:
            selected_tickers = [ticker]
    else:
        analysis_mode = st.radio("分析模式", ["单一资产", "多资产分析"])

        if analysis_mode == "多资产分析":
            selected_tickers = st.multiselect(
                "选择要分析的资产",
                POPULAR_ASSETS[asset_category],
                default=[POPULAR_ASSETS[asset_category][0]]
            )
        else:
            ticker = st.selectbox("资产", POPULAR_ASSETS[asset_category])
            selected_tickers = [ticker]

    analysis_date = st.date_input("分析日期", datetime.today())

    st.header("🧠 语言模型 (LLM)")

    # 使用session_state保存用户选择
    llm_provider = st.selectbox(
        "LLM 提供商",
        ["openai", "google", "anthropic"],
        index=["openai", "google", "anthropic"].index(state_mgr.llm_provider),
        key="llm_provider"
    )
    deep_think_llm = st.text_input(
        "主模型（深度思考）",
        value=state_mgr.deep_think_llm,
        key="deep_think_llm"
    )
    quick_think_llm = st.text_input(
        "快速模型（快速思考）",
        value=state_mgr.quick_think_llm,
        key="quick_think_llm"
    )

    run_analysis = st.button(f"🚀 分析{'多个市场' if len(selected_tickers) > 1 else '市场'}")

    return {
        'asset_category': asset_category,
        'analysis_mode': analysis_mode,
        'selected_tickers': selected_tickers,
        'analysis_date': analysis_date.strftime("%Y-%m-%d"),
        'llm_provider': llm_provider,
        'deep_think_llm': deep_think_llm,
        'quick_think_llm': quick_think_llm,
        'run_analysis': run_analysis
    }


def _render_history_loader(state_mgr):
    """
    渲染历史结果加载区域

    Args:
        state_mgr: 状态管理器实例
    """
    st.header("📂 加载历史结果")

    # 选择加载方式
    load_method = st.radio("选择加载方式", ["从文件上传", "从保存目录选择"])

    if load_method == "从文件上传":
        uploaded_file = st.file_uploader("选择JSON文件", type="json")
        if uploaded_file is not None:
            try:
                json_data = json.load(uploaded_file)
                state_mgr.loaded_results = json_data
                st.success("✅ 文件加载成功！")
            except Exception as e:
                st.error(f"❌ 加载文件时出错: {e}")

    elif load_method == "从保存目录选择":
        # 扫描eval_results目录
        eval_dir = Path("eval_results")
        if eval_dir.exists():
            # 获取所有ticker目录
            ticker_dirs = [d for d in eval_dir.iterdir() if d.is_dir()]
            if ticker_dirs:
                ticker_names = [d.name for d in ticker_dirs]
                selected_ticker_dir = st.selectbox("选择资产", ticker_names)

                # 获取该资产的所有JSON文件
                logs_dir = eval_dir / selected_ticker_dir / "TradingAgentsStrategy_logs"
                if logs_dir.exists():
                    json_files = list(logs_dir.glob("full_states_log_*.json"))
                    if json_files:
                        file_names = [f.name for f in json_files]
                        selected_file = st.selectbox("选择文件", file_names)

                        if st.button("📥 加载文件"):
                            file_path = logs_dir / selected_file
                            try:
                                with open(file_path, 'r', encoding='utf-8') as f:
                                    json_data = json.load(f)
                                state_mgr.loaded_results = json_data
                                st.success(f"✅ 成功加载 {selected_file}")
                            except Exception as e:
                                st.error(f"❌ 加载文件时出错: {e}")
                    else:
                        st.info("该资产没有保存的结果文件")
                else:
                    st.info("该资产没有日志目录")
            else:
                st.info("没有找到任何已保存的结果")
        else:
            st.info("eval_results 目录不存在")
