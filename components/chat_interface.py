"""
聊天界面组件
与交易员进行对话交互
"""

import streamlit as st
from langchain_openai import ChatOpenAI
from tradingagents.agents.trader.chat_trader import create_chat_trader
from tradingagents.default_config import DEFAULT_CONFIG


def render_chat_interface(state_mgr, openai_api_key: str):
    """
    渲染聊天界面

    Args:
        state_mgr: 状态管理器实例
        openai_api_key: OpenAI API 密钥
    """
    if not state_mgr.show_chat or not state_mgr.chat_context:
        st.info("💡 完成分析后，聊天功能将在此处显示")
        return

    st.header("💬 与交易员对话")

    # 显示当前分析的资产
    ticker = state_mgr.chat_context.get("company_of_interest", "Unknown")
    st.info(f"📊 当前讨论: {ticker}")

    # 创建一个可滚动的聊天历史容器
    chat_container = st.container(height=400)

    # 显示聊天历史
    with chat_container:
        for msg in state_mgr.chat_messages:
            if msg["role"] == "user":
                st.markdown("**👤 您:**")
                st.markdown(msg['content'])
            else:
                st.markdown("**🤖 交易员:**")
                st.markdown(msg['content'])
            st.divider()

    # 聊天输入区域
    with st.form(key="chat_form", clear_on_submit=True):
        user_input = st.text_area("输入您的问题:", key="chat_textarea", height=100)
        col1, col2 = st.columns([3, 1])
        with col1:
            submit_button = st.form_submit_button("发送", type="primary", use_container_width=True)
        with col2:
            if st.form_submit_button("🗑️", use_container_width=True):
                state_mgr.clear_chat_messages()
                st.rerun()

        if submit_button and user_input:
            # 添加用户消息到历史
            messages = state_mgr.chat_messages
            messages.append({"role": "user", "content": user_input})
            state_mgr.chat_messages = messages

            # 创建LLM实例
            llm_config = DEFAULT_CONFIG.copy()

            # 使用OpenRouter的配置
            llm = ChatOpenAI(
                model=llm_config["deep_think_llm"],
                temperature=0.7,
                openai_api_key=openai_api_key,
                base_url=llm_config["backend_url"]  # 使用OpenRouter URL
            )

            # 创建聊天交易员
            chat_trader = create_chat_trader(llm)

            # 获取回复
            with st.spinner("交易员正在思考..."):
                response = chat_trader(
                    state_mgr.chat_messages,
                    state_mgr.chat_context
                )

            # 添加助手回复到历史
            messages.append({"role": "assistant", "content": response})
            state_mgr.chat_messages = messages

            # 重新运行以显示新消息
            st.rerun()
