"""
学习中心组件
包含手动学习、学习报告浏览和自动学习状态
"""

import streamlit as st
import json
import asyncio
from datetime import datetime
from pathlib import Path
from components.decision_log_viewer import DecisionLogViewer
from components.reflection_viewer import render_reflections
from modules.learning_manager import LearningRecordManager
from utils.formatters import parse_date

# 尝试导入手动学习功能
try:
    from scripts.learning_engine import list_available_decision_logs, manual_learning
    MANUAL_LEARNING_AVAILABLE = True
except ImportError:
    MANUAL_LEARNING_AVAILABLE = False


def render_learning_center(state_mgr):
    """
    渲染学习中心主界面

    Args:
        state_mgr: 状态管理器实例
    """
    with st.expander("🧠 学习中心 (Learning Center)", expanded=True):
        if MANUAL_LEARNING_AVAILABLE:
            # 学习中心选项卡
            tab1, tab2, tab3 = st.tabs(["🎓 手动学习", "📚 学习报告浏览", "📊 自动学习状态"])

            with tab1:
                render_manual_learning_tab(state_mgr)

            with tab2:
                render_learning_reports_tab()

            with tab3:
                render_auto_learning_tab()

        else:
            st.warning("⚠️ 手动学习功能不可用，请检查 scripts/learning_engine.py 是否存在")


def render_manual_learning_tab(state_mgr):
    """
    渲染手动学习选项卡

    Args:
        state_mgr: 状态管理器实例
    """
    # 加载决策日志
    @st.cache_data
    def load_manual_decision_logs():
        """加载所有可用的决策日志，并按日期从新到旧排序"""
        try:
            logs = list_available_decision_logs() or []
            # 解析日期并排序
            logs.sort(key=lambda x: parse_date(x.get('date', '1970-01-01')), reverse=True)
            # 标记已学习的日志
            learning_mgr = LearningRecordManager()
            logs = learning_mgr.mark_learned_logs(logs)
            return logs
        except Exception as e:
            st.error(f"加载决策日志失败: {e}")
            return []

    # 如果还没有加载日志，则加载
    if not state_mgr.manual_decision_logs:
        state_mgr.manual_decision_logs = load_manual_decision_logs()

    all_logs = state_mgr.manual_decision_logs

    # 过滤选项
    col_filter, col_refresh = st.columns([3, 1])
    with col_filter:
        show_learned = st.checkbox(
            "显示已学习的日志",
            value=state_mgr.show_learned_logs,
            key="show_learned_checkbox"
        )
        state_mgr.show_learned_logs = show_learned

    with col_refresh:
        if st.button("🔄 刷新日志", key="refresh_logs"):
            # 清除缓存和 session state
            st.cache_data.clear()
            state_mgr.manual_decision_logs = []
            st.rerun()

    # 根据过滤选项显示日志
    if show_learned:
        logs = all_logs
    else:
        logs = [log for log in all_logs if not log.get('is_learned', False)]

    if not logs:
        st.warning("⚠️ 没有找到决策日志文件")
        st.info("请确保 eval_results 目录中存在决策日志文件")
    else:
        st.success(f"✅ 找到 {len(logs)} 个决策日志")

        # 市场过滤
        markets = list(set(log['market'] for log in logs))
        selected_market = st.selectbox("选择市场", markets, key="manual_market")

        # 过滤日志并按日期倒序
        filtered_logs = [log for log in logs if log['market'] == selected_market]
        filtered_logs.sort(key=lambda x: parse_date(x.get('date', '1970-01-01')), reverse=True)

        # 日志选择
        if filtered_logs:
            def option_label(idx):
                log = filtered_logs[idx]
                did = log.get('decision_id') or 'Unknown'
                learned_status = "✅" if log.get('is_learned', False) else "🆕"
                return f"{learned_status} {log.get('date','Unknown')} | {did[:20]}..."

            selected_index = st.selectbox(
                "选择决策日志",
                range(len(filtered_logs)),
                format_func=option_label,
                key="manual_log_select"
            )

            if st.button("选择此日志", key="manual_select_log"):
                state_mgr.manual_selected_log = filtered_logs[selected_index]
                st.rerun()

    # 显示选中的日志和学习界面
    if state_mgr.manual_selected_log:
        _render_selected_log_interface(state_mgr)


def _render_selected_log_interface(state_mgr):
    """
    渲染选中日志的学习界面

    Args:
        state_mgr: 状态管理器实例
    """
    selected_log = state_mgr.manual_selected_log
    learning_mgr = LearningRecordManager()

    # 标题和删除按钮行
    col_info, col_delete = st.columns([4, 1])
    with col_info:
        st.info(f"已选择: {selected_log['market']} - {selected_log['date']}")
    with col_delete:
        if not state_mgr.delete_confirm:
            if st.button("🗑️ 删除日志", key="delete_log_btn", type="secondary"):
                state_mgr.delete_confirm = True
                st.rerun()
        else:
            st.warning("⚠️ 确认删除？")
            col_yes, col_no = st.columns(2)
            with col_yes:
                if st.button("✅ 确认", key="delete_confirm_yes", type="primary"):
                    # 执行删除
                    with st.spinner("正在删除..."):
                        success, message = learning_mgr.delete_decision_log(selected_log['file_path'])

                        if success:
                            deleted_count, errors = learning_mgr.delete_related_learning_records(
                                selected_log['file_path']
                            )

                            st.success(message)
                            if deleted_count > 0:
                                st.success(f"同时删除了 {deleted_count} 条相关学习记录")
                            if errors:
                                for error in errors:
                                    st.warning(error)

                            # 清除选择和缓存
                            state_mgr.manual_selected_log = None
                            state_mgr.delete_confirm = False
                            state_mgr.manual_decision_logs = []
                            st.cache_data.clear()
                            st.rerun()
                        else:
                            st.error(message)
                            state_mgr.delete_confirm = False

            with col_no:
                if st.button("❌ 取消", key="delete_confirm_no"):
                    state_mgr.delete_confirm = False
                    st.rerun()

    # 加载并渲染日志内容
    try:
        with open(selected_log['file_path'], 'r', encoding='utf-8') as f:
            log_data = json.load(f)
    except Exception as e:
        log_data = None
        st.error(f"读取日志失败: {e}")

    if log_data:
        # 使用 DecisionLogViewer 渲染日志
        viewer = DecisionLogViewer(log_data, selected_log)
        viewer.render()

    # PnL输入和学习执行
    col_a, col_b = st.columns([1, 1])

    with col_a:
        pnl_value = st.number_input(
            "输入实际盈亏值 (USDC)",
            value=0.0,
            step=0.01,
            format="%.4f",
            help="输入该决策对应的实际盈亏值，支持正负数",
            key="manual_pnl"
        )

    with col_b:
        user_notes = st.text_area(
            "学习备注 (可选)",
            placeholder="添加关于此次学习的备注信息...",
            height=100,
            key="manual_notes"
        )

    # 学习按钮和结果
    if st.button(
        "🎓 开始手动学习",
        type="primary",
        disabled=state_mgr.manual_learning_in_progress,
        key="manual_start_learning"
    ):
        state_mgr.manual_learning_in_progress = True
        state_mgr.manual_learning_result = None

        with st.spinner("AI智能体正在进行反思学习..."):
            try:
                # 使用 asyncio.run() 来运行异步函数
                result = asyncio.run(manual_learning(
                    state_mgr.manual_selected_log['file_path'],
                    pnl_value,
                    user_notes
                ))
                state_mgr.manual_learning_result = result
                state_mgr.manual_learning_in_progress = False
                st.success("✅ 手动学习完成！")

                # 保存学习记录到文件
                if result.get('success'):
                    _save_learning_record(result, selected_log)

                st.rerun()
            except Exception as e:
                st.error(f"学习过程中出现错误: {e}")
                state_mgr.manual_learning_in_progress = False

    # 显示学习结果
    if state_mgr.manual_learning_result:
        _render_learning_result(state_mgr)


def _save_learning_record(result: dict, selected_log: dict):
    """
    保存学习记录到文件

    Args:
        result: 学习结果
        selected_log: 选中的日志元信息
    """
    try:
        # 创建 eval_results 目录
        eval_results_dir = Path("eval_results")
        eval_results_dir.mkdir(exist_ok=True)

        # 生成文件名
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"manual_learning_{timestamp}.json"
        save_path = eval_results_dir / filename

        # 添加额外的元数据
        save_data = result.copy()
        save_data['market'] = selected_log.get('market', 'Unknown')
        save_data['date'] = selected_log.get('date', 'Unknown')
        save_data['timestamp'] = datetime.now().isoformat()

        # 保存到文件
        with open(save_path, 'w', encoding='utf-8') as f:
            json.dump(save_data, f, indent=2, ensure_ascii=False)

        st.info(f"💾 学习记录已保存到: {filename}")

    except Exception as e:
        st.error(f"⚠️ 保存学习记录时出错: {str(e)}")


def _render_learning_result(state_mgr):
    """
    渲染学习结果

    Args:
        state_mgr: 状态管理器实例
    """
    result = state_mgr.manual_learning_result

    if result.get('success'):
        st.success("🎯 学习结果")

        # 显示学习摘要
        col_x, col_y, col_z = st.columns(3)

        with col_x:
            st.metric("决策ID", result.get('decision_id', 'N/A'))

        with col_y:
            st.metric("输入PnL", f"{result.get('input_pnl', 0):.4f} USDC")

        with col_z:
            reflections = result.get('reflections', {})
            st.metric("学习组件", len(reflections))

        # 显示各组件的反思结果
        if reflections:
            render_reflections(reflections, expanded=False)

        # 下载学习结果
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"manual_learning_{timestamp}.json"

        download_data = {
            "learning_session": {
                "timestamp": result.get('timestamp'),
                "decision_id": result.get('decision_id'),
                "input_pnl": result.get('input_pnl'),
                "user_notes": result.get('user_notes'),
                "selected_log": state_mgr.manual_selected_log
            },
            "reflections": reflections
        }

        st.download_button(
            label="📥 下载学习结果 (JSON)",
            data=json.dumps(download_data, indent=2, ensure_ascii=False),
            file_name=filename,
            mime="application/json",
            key="manual_download"
        )

        if st.button("🗑️ 清除学习结果", key="manual_clear_result"):
            state_mgr.clear_manual_learning_result()
            st.rerun()

    else:
        st.error("❌ 学习失败")
        st.error(f"错误信息: {result.get('error', '未知错误')}")

        if st.button("🔄 重试", key="manual_retry"):
            state_mgr.manual_learning_result = None
            st.rerun()


def render_learning_reports_tab():
    """渲染学习报告浏览选项卡"""
    st.header("📚 学习报告浏览")

    # 加载学习记录
    learning_mgr = LearningRecordManager()
    learning_records = learning_mgr.load_learning_records()

    if not learning_records:
        st.info("📝 还没有学习记录。完成手动学习后，记录将显示在这里。")
    else:
        st.success(f"✅ 找到 {len(learning_records)} 条学习记录")

        # 搜索和过滤选项
        col_search, col_filter = st.columns([2, 1])

        with col_search:
            search_term = st.text_input("🔍 搜索学习记录", placeholder="输入决策ID、市场或日期...")

        with col_filter:
            # PnL过滤
            pnl_filter = st.selectbox("PnL过滤", ["全部", "盈利 (>0)", "亏损 (<0)", "持平 (=0)"])

        # 应用过滤
        filtered_records = learning_records

        if search_term:
            filtered_records = [
                record for record in filtered_records
                if search_term.lower() in str(record.get('decision_id', '')).lower()
                or search_term.lower() in str(record.get('market', '')).lower()
                or search_term.lower() in str(record.get('date', '')).lower()
            ]

        if pnl_filter != "全部":
            if pnl_filter == "盈利 (>0)":
                filtered_records = [r for r in filtered_records if r.get('pnl_value', 0) > 0]
            elif pnl_filter == "亏损 (<0)":
                filtered_records = [r for r in filtered_records if r.get('pnl_value', 0) < 0]
            elif pnl_filter == "持平 (=0)":
                filtered_records = [r for r in filtered_records if r.get('pnl_value', 0) == 0]

        # 显示过滤后的记录
        if not filtered_records:
            st.warning("没有找到匹配的学习记录")
        else:
            st.write(f"显示 {len(filtered_records)} 条记录")

            # 学习记录列表
            for i, record in enumerate(filtered_records):
                with st.expander(
                    f"📖 {record.get('date', 'Unknown')} | "
                    f"{record.get('market', 'Unknown')} | "
                    f"PnL: {record.get('pnl_value', 0):.2f} | "
                    f"{record.get('decision_id', 'Unknown')[:20]}...",
                    expanded=False
                ):
                    # 基本信息
                    col_info1, col_info2 = st.columns(2)
                    with col_info1:
                        st.write(f"**决策ID:** {record.get('decision_id', 'Unknown')}")
                        st.write(f"**市场:** {record.get('market', 'Unknown')}")
                        st.write(f"**日期:** {record.get('date', 'Unknown')}")
                    with col_info2:
                        st.write(f"**PnL值:** {record.get('pnl_value', 0):.2f}")
                        st.write(f"**学习时间:** {record.get('timestamp', 'Unknown')}")
                        st.write(f"**状态:** {'✅ 成功' if record.get('success') else '❌ 失败'}")

                    # 用户笔记
                    if record.get('user_notes'):
                        st.markdown("**📝 用户笔记:**")
                        st.write(record.get('user_notes'))

                    # AI组件反思
                    reflections = record.get('reflections', {})
                    if reflections:
                        st.markdown("**🤖 AI组件反思:**")
                        render_reflections(reflections, expanded=False)

                    # 下载按钮
                    filename = f"learning_report_{record.get('decision_id', 'unknown')}_{record.get('date', 'unknown')}.json"
                    st.download_button(
                        label="📥 下载完整报告",
                        data=json.dumps(record, indent=2, ensure_ascii=False),
                        file_name=filename,
                        mime="application/json",
                        key=f"download_record_{i}"
                    )


def render_auto_learning_tab():
    """渲染自动学习状态选项卡"""
    st.header("📊 自动学习状态")
    st.info("🚧 自动学习功能正在开发中...")
