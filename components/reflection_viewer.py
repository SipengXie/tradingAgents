"""
反思结果查看器组件
显示 AI 组件的反思结果
"""

import streamlit as st
from config.ui_constants import COMPONENT_CONFIG


def render_reflections(reflections: dict, expanded: bool = False):
    """
    渲染 AI 组件的反思结果

    Args:
        reflections: 反思内容字典，键为组件名称，值为反思内容
        expanded: 展开器是否默认展开
    """
    if not reflections:
        st.write("无反思内容")
        return

    # 按预定义顺序显示组件反思
    for component_key in COMPONENT_CONFIG.keys():
        if component_key in reflections:
            config = COMPONENT_CONFIG[component_key]
            reflection = reflections[component_key]
            with st.expander(f"{config['icon']} {config['name']} ({component_key})", expanded=expanded):
                if reflection:
                    st.write(reflection)
                else:
                    st.write("无反思内容")

    # 显示其他未预定义的组件
    other_components = set(reflections.keys()) - set(COMPONENT_CONFIG.keys())
    for component in other_components:
        reflection = reflections[component]
        with st.expander(f"🤖 {component.upper()}", expanded=expanded):
            if reflection:
                st.write(reflection)
            else:
                st.write("无反思内容")
