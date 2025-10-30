"""
API 状态面板组件
显示所有 API 的连接状态
"""

import streamlit as st


def render_api_status_panel(api_test_results: dict):
    """
    渲染 API 连接状态面板

    Args:
        api_test_results: API 测试结果字典
    """
    if not api_test_results:
        return

    with st.container():
        st.subheader("📡 API 连接状态")
        cols = st.columns(4)

        # LLM 状态
        with cols[0]:
            llm_status = api_test_results.get('llm', {})
            if llm_status.get('success'):
                st.success("✅ LLM API 正常")
            else:
                st.error("❌ LLM API 异常")
                if llm_status.get('message'):
                    st.caption(llm_status['message'])

        # Finnhub 状态
        with cols[1]:
            finn_status = api_test_results.get('finnhub', {})
            if finn_status.get('success'):
                st.success("✅ Finnhub API 正常")
            else:
                st.error("❌ Finnhub API 异常")
                if finn_status.get('message'):
                    st.caption(finn_status['message'])

        # Embedding 状态
        with cols[2]:
            embed_status = api_test_results.get('embedding', {})
            if embed_status.get('success'):
                st.success("✅ Embedding API 正常")
            else:
                st.error("❌ Embedding API 异常")
                if embed_status.get('message'):
                    st.caption(embed_status['message'])

        # Binance 状态
        with cols[3]:
            binance_status = api_test_results.get('binance', {})
            if binance_status.get('success'):
                st.success("✅ Binance API 正常")
            else:
                st.error("❌ Binance API 异常")
                if binance_status.get('message'):
                    st.caption(binance_status['message'])

        st.divider()
