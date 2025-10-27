import streamlit as st
import os
import sys
from datetime import datetime
from dotenv import load_dotenv
import requests
from openai import OpenAI
import finnhub
import json
import re
import asyncio
from pathlib import Path

# Add project root to sys.path
project_root = Path(__file__).resolve().parent
sys.path.insert(0, str(project_root))

# 导入交易框架所需的组件
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG
from tradingagents.agents.trader.chat_trader import create_chat_trader
from langchain_openai import ChatOpenAI

# 导入手动学习功能
try:
    from scripts.learning_engine import list_available_decision_logs, manual_learning
    MANUAL_LEARNING_AVAILABLE = True
except ImportError:
    MANUAL_LEARNING_AVAILABLE = False

# API 测试函数
def test_llm_api(backend_url, api_key, model):
    """测试 LLM API 是否可用"""
    try:
        client = OpenAI(
            base_url=backend_url,
            api_key=api_key
        )
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": "Hello"}],
            max_tokens=10
        )
        return True, "LLM API 连接成功"
    except Exception as e:
        return False, f"LLM API 连接失败: {str(e)}"

def test_embedding_api(embedding_url, api_key, model):
    """测试 Embedding API 是否可用"""
    try:
        client = OpenAI(
            base_url=embedding_url,
            api_key=api_key
        )
        response = client.embeddings.create(
            model=model,
            input="test"
        )
        return True, "Embedding API 连接成功"
    except Exception as e:
        return False, f"Embedding API 连接失败: {str(e)}"

def test_finnhub_api(api_key):
    """测试 Finnhub API 是否可用"""
    try:
        finnhub_client = finnhub.Client(api_key=api_key)
        # 测试获取苹果股票报价
        quote = finnhub_client.quote('AAPL')
        if quote and 'c' in quote:
            return True, "Finnhub API 连接成功"
        else:
            return False, "Finnhub API 返回数据异常"
    except Exception as e:
        return False, f"Finnhub API 连接失败: {str(e)}"

def test_binance_api(api_key, api_secret):
    """测试 Binance API 是否可用"""
    try:
        from tradingagents.dataflows.binance_utils import BinanceAPIWrapper

        # 创建 API 包装器
        api = BinanceAPIWrapper(api_key=api_key, api_secret=api_secret)

        # 测试基本连接
        ping_result = api.ping()
        if ping_result != {}:
            return False, "Binance API ping 响应异常"

        # 测试服务器时间
        server_time = api.get_server_time()
        if not server_time or 'serverTime' not in server_time:
            return False, "Binance API 服务器时间获取失败"

        # 如果提供了密钥，测试认证
        if api_key and api_secret:
            try:
                # 测试获取账户信息
                account = api.client.get_account()
                if account and 'balances' in account:
                    return True, "Binance API 连接成功（已认证）"
            except Exception as auth_error:
                # 认证失败但基本连接成功
                if "APIError" in str(auth_error):
                    return True, f"Binance API 连接成功（认证失败: {str(auth_error)[:50]}...）"

        return True, "Binance API 连接成功（公共接口）"

    except ImportError:
        return False, "Binance 库未安装，请运行: pip install python-binance"
    except Exception as e:
        return False, f"Binance API 连接失败: {str(e)}"

# 手动学习辅助函数
def format_file_size(size_bytes):
    """格式化文件大小"""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    else:
        return f"{size_bytes / (1024 * 1024):.1f} MB"

def format_decision_summary(log_data):
    """生成决策摘要"""
    try:
        # 处理不同的日志格式
        if isinstance(log_data, dict):
            if 'decision_id' in log_data:
                decision_data = log_data
            else:
                decision_data = next(iter(log_data.values())) if log_data else {}
        else:
            return "无法解析决策数据"

        # 提取关键信息
        market_analysis = decision_data.get('market_analysis', {})
        trading_decision = decision_data.get('trading_decision', {})

        summary_parts = []

        if isinstance(market_analysis, dict):
            trend = market_analysis.get('trend', 'Unknown')
            summary_parts.append(f"趋势: {trend}")

        if isinstance(trading_decision, dict):
            action = trading_decision.get('action', 'Unknown')
            confidence = trading_decision.get('confidence', 'Unknown')
            summary_parts.append(f"操作: {action}")
            summary_parts.append(f"置信度: {confidence}")

        return " | ".join(summary_parts) if summary_parts else "无摘要信息"

    except Exception as e:
        return f"摘要生成错误: {str(e)}"


def load_learning_records():
    """加载所有手动学习记录"""
    learning_records = []
    eval_results_dir = Path("eval_results")

    if not eval_results_dir.exists():
        return learning_records

    # 查找所有手动学习记录文件
    for record_file in eval_results_dir.glob("manual_learning_*.json"):
        try:
            with open(record_file, 'r', encoding='utf-8') as f:
                record = json.load(f)
                record['file_name'] = record_file.name
                record['file_path'] = str(record_file)
                learning_records.append(record)
        except Exception as e:
            st.warning(f"无法读取学习记录文件 {record_file}: {e}")

    # 按时间戳排序（最新的在前）
    learning_records.sort(key=lambda x: x.get('timestamp', ''), reverse=True)
    return learning_records


def get_learned_decision_logs():
    """获取已经学习过的决策日志路径集合"""
    learned_logs = set()
    learning_records = load_learning_records()

    for record in learning_records:
        if record.get('success') and record.get('decision_log_path'):
            learned_logs.add(record['decision_log_path'])

    return learned_logs


def filter_unlearned_logs(all_logs):
    """过滤出未学习过的决策日志"""
    learned_logs = get_learned_decision_logs()
    unlearned_logs = []

    for log in all_logs:
        if log.get('file_path') not in learned_logs:
            unlearned_logs.append(log)

    return unlearned_logs


def mark_learned_logs(all_logs):
    """标记已学习的决策日志"""
    learned_logs = get_learned_decision_logs()

    for log in all_logs:
        log['is_learned'] = log.get('file_path') in learned_logs

    return all_logs

# --- Streamlit 页面配置 ---
st.set_page_config(
    page_title="AI 交易助手",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🤖 AI 金融资产交易助手")
st.markdown("该应用使用AI智能体团队分析资产市场并提出交易决策。请输入您的API密钥和分析参数以开始。")

# 初始化 session state
if 'api_tested' not in st.session_state:
    st.session_state.api_tested = False
    st.session_state.api_test_results = {}

# 初始化聊天相关的session state
if 'chat_messages' not in st.session_state:
    st.session_state.chat_messages = []
if 'chat_context' not in st.session_state:
    st.session_state.chat_context = None
if 'show_chat' not in st.session_state:
    st.session_state.show_chat = False
if 'analysis_in_progress' not in st.session_state:
    st.session_state.analysis_in_progress = False

# 在主页面显示 API 状态
if st.session_state.api_tested and st.session_state.api_test_results:
    with st.container():
        st.subheader("📡 API 连接状态")
        cols = st.columns(4)
        
        # LLM 状态
        with cols[0]:
            llm_status = st.session_state.api_test_results.get('llm', {})
            if llm_status.get('success'):
                st.success("✅ LLM API 正常")
            else:
                st.error("❌ LLM API 异常")
                if llm_status.get('message'):
                    st.caption(llm_status['message'])
        
        # Finnhub 状态
        with cols[1]:
            finn_status = st.session_state.api_test_results.get('finnhub', {})
            if finn_status.get('success'):
                st.success("✅ Finnhub API 正常")
            else:
                st.error("❌ Finnhub API 异常")
                if finn_status.get('message'):
                    st.caption(finn_status['message'])
        
        # Embedding 状态
        with cols[2]:
            embed_status = st.session_state.api_test_results.get('embedding', {})
            if embed_status.get('success'):
                st.success("✅ Embedding API 正常")
            else:
                st.error("❌ Embedding API 异常")
                if embed_status.get('message'):
                    st.caption(embed_status['message'])
        
        # Binance 状态
        with cols[3]:
            binance_status = st.session_state.api_test_results.get('binance', {})
            if binance_status.get('success'):
                st.success("✅ Binance API 正常")
            else:
                st.error("❌ Binance API 异常")
                if binance_status.get('message'):
                    st.caption(binance_status['message'])
        
        st.divider()

# --- 学习中心 ---
with st.expander("🧠 学习中心 (Learning Center)", expanded=True):
    if MANUAL_LEARNING_AVAILABLE:
        # 学习中心选项卡
        tab1, tab2, tab3 = st.tabs(["🎓 手动学习", "📚 学习报告浏览", "📊 自动学习状态"])

        with tab1:

            # 初始化手动学习相关的session state
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

            # 加载决策日志
            @st.cache_data
            def load_manual_decision_logs():
                """加载所有可用的决策日志，并按日期从新到旧排序"""
                try:
                    logs = list_available_decision_logs() or []
                    # 解析日期并排序（YYYY-MM-DD）
                    def parse_date(d):
                        try:
                            return datetime.strptime(d, "%Y-%m-%d")
                        except Exception:
                            return datetime.min
                    logs.sort(key=lambda x: parse_date(x.get('date', '1970-01-01')), reverse=True)
                    # 标记已学习的日志
                    logs = mark_learned_logs(logs)
                    return logs
                except Exception as e:
                    st.error(f"加载决策日志失败: {e}")
                    return []

            # 如果还没有加载日志，则加载
            if not st.session_state.manual_decision_logs:
                st.session_state.manual_decision_logs = load_manual_decision_logs()

            all_logs = st.session_state.manual_decision_logs

            # 过滤选项
            col_filter, col_refresh = st.columns([3, 1])
            with col_filter:
                show_learned = st.checkbox("显示已学习的日志", value=st.session_state.show_learned_logs, key="show_learned_checkbox")
                st.session_state.show_learned_logs = show_learned

            with col_refresh:
                if st.button("🔄 刷新日志", key="refresh_logs"):
                    # 清除缓存和 session state
                    st.cache_data.clear()
                    st.session_state.manual_decision_logs = []
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

            # 简化的日志选择
            # 市场过滤
            markets = list(set(log['market'] for log in logs))
            selected_market = st.selectbox("选择市场", markets, key="manual_market")

            # 过滤日志并按日期倒序
            filtered_logs = [log for log in logs if log['market'] == selected_market]
            def parse_date(d):
                try:
                    return datetime.strptime(d, "%Y-%m-%d")
                except Exception:
                    return datetime.min
            filtered_logs.sort(key=lambda x: parse_date(x.get('date', '1970-01-01')), reverse=True)

            # 日志选择（使用排序后的结果）
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
                    st.session_state.manual_selected_log = filtered_logs[selected_index]
                    st.rerun()

            # 显示选中的日志和学习界面
            if st.session_state.manual_selected_log:
                selected_log = st.session_state.manual_selected_log
                st.info(f"已选择: {selected_log['market']} - {selected_log['date']}")

                # 加载并渲染日志内容
                try:
                    with open(selected_log['file_path'], 'r', encoding='utf-8') as f:
                        log_data = json.load(f)
                except Exception as e:
                    log_data = None
                    st.error(f"读取日志失败: {e}")

                if log_data:
                    # 兼容两种结构：直接是对象 或 {date: state}
                    if isinstance(log_data, dict) and 'decision_id' in log_data:
                        decision_data = log_data
                    elif isinstance(log_data, dict):
                        # 取第一个键值
                        decision_data = next(iter(log_data.values())) if log_data else {}
                    else:
                        decision_data = {}

                    # 关键信息
                    with st.expander("🔑 关键信息", expanded=True):
                        colk1, colk2 = st.columns(2)
                        with colk1:
                            st.write(f"决策ID: {decision_data.get('decision_id', 'Unknown')}")
                            st.write(f"时间戳: {decision_data.get('timestamp', 'Unknown')}")
                        with colk2:
                            st.write(f"市场: {selected_log.get('market', 'Unknown')}")
                            st.write(f"日期: {selected_log.get('date', 'Unknown')}")

                    # 市场技术分析（若无专用字段则退化到 market_report 全文）
                    market_report_text = decision_data.get('market_report')
                    technical_analysis = (
                        decision_data.get('market_technical_analysis')
                        or decision_data.get('technical_analysis')
                        or decision_data.get('market_analysis')
                        or market_report_text
                    )
                    with st.expander("📊 市场技术分析", expanded=False):
                        st.write(technical_analysis or "无市场技术分析信息")

                    # 社交情绪分析
                    sentiment_analysis = (
                        decision_data.get('social_sentiment_analysis')
                        or decision_data.get('sentiment_analysis')
                        or decision_data.get('social_analysis')
                        or decision_data.get('sentiment_report')
                    )
                    with st.expander("📱 社交情绪分析", expanded=False):
                        st.write(sentiment_analysis or "无社交情绪分析信息")

                    # 新闻分析
                    news_analysis = (decision_data.get('news_analysis') or
                                   decision_data.get('market_news') or
                                   decision_data.get('news_report'))
                    with st.expander("📰 新闻分析", expanded=False):
                        st.write(news_analysis or "无新闻分析信息")

                    # 研究员辩论 - 看涨 vs 看跌（来自 investment_debate_state）
                    debate_state = decision_data.get('investment_debate_state') or {}
                    bull_researcher = (
                        debate_state.get('bull_history')
                        or decision_data.get('bull_researcher')
                        or decision_data.get('bull_analysis')
                        or decision_data.get('bullish_view')
                    )
                    bear_researcher = (
                        debate_state.get('bear_history')
                        or decision_data.get('bear_researcher')
                        or decision_data.get('bear_analysis')
                        or decision_data.get('bearish_view')
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

                    # 定义提取函数
                    def extract_risk(text: str):
                        if not text:
                            return None
                        # 支持中文、英文常见标题
                        patterns = [
                            r"[\n\r]+\*\*?风险管理[\u4e00-\u9fa5]*\*\*?[\s\S]*?(?=\n\*\*|\n##|$)",
                            r"[\n\r]+\*\*?风险管理建议\*\*?[\s\S]*?(?=\n\*\*|\n##|$)",
                            r"[\n\r]+\*\*?Risk Management\*\*?[\s\S]*?(?=\n\*\*|\n##|$)",
                        ]
                        for p in patterns:
                            m = re.search(p, text)
                            if m:
                                return m.group(0).strip()
                        return None

                    def extract_proposal(text: str):
                        if not text:
                            return None
                        patterns = [
                            r"FINAL\s+TRADING\s+PROPOSAL[:：]\s*([A-Z\u4e00-\u9fa5a-z]+)",
                            r"最终交易建(议|案)[:：]\s*([\u4e00-\u9fa5A-Za-z]+)",
                            r"FINAL\s+TRADE\s+DECISION[:：]\s*([A-Z\u4e00-\u9fa5a-z]+)",
                            r"最终交易决策[:：]\s*([\u4e00-\u9fa5A-Za-z]+)",
                        ]
                        for p in patterns:
                            m = re.search(p, text)
                            if m:
                                # Join all groups as a concise proposal line
                                return " ".join([g for g in m.groups() if g])
                        return None

                    # 风险管理评估
                    risk_assessment = (
                        decision_data.get('risk_management_assessment')
                        or decision_data.get('risk_analysis')
                        or decision_data.get('risk_management')
                        or extract_risk(market_report_text)
                    )
                    with st.expander("🛡️ 风险管理评估", expanded=False):
                        st.write(risk_assessment or "无风险管理评估信息")

                    # 交易员提案
                    trader_proposal = (
                        decision_data.get('trader_proposal')
                        or decision_data.get('trading_proposal')
                        or decision_data.get('trading_decision')
                        or decision_data.get('final_decision')
                        or decision_data.get('final_trade_decision')
                        or extract_proposal(market_report_text)
                    )
                    with st.expander("💼 交易员提案", expanded=False):
                        st.write(trader_proposal or "无交易员提案信息")

                    # 原始JSON
                    with st.expander("📄 原始JSON", expanded=False):
                        st.json(decision_data)

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
                if st.button("🎓 开始手动学习", type="primary",
                           disabled=st.session_state.manual_learning_in_progress, key="manual_start_learning"):
                    st.session_state.manual_learning_in_progress = True
                    st.session_state.manual_learning_result = None

                    with st.spinner("AI智能体正在进行反思学习..."):
                        try:
                            # 使用 asyncio.run() 来运行异步函数
                            result = asyncio.run(manual_learning(
                                st.session_state.manual_selected_log['file_path'],
                                pnl_value,
                                user_notes
                            ))
                            st.session_state.manual_learning_result = result
                            st.session_state.manual_learning_in_progress = False
                            st.success("✅ 手动学习完成！")
                            st.rerun()
                        except Exception as e:
                            st.error(f"学习过程中出现错误: {e}")
                            st.session_state.manual_learning_in_progress = False

                # 显示学习结果
                if st.session_state.manual_learning_result:
                    result = st.session_state.manual_learning_result

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
                        # 定义组件显示顺序和图标
                        component_config = {
                            'BULL_RESEARCHER': {'icon': '🐂', 'name': '看涨研究员'},
                            'BEAR_RESEARCHER': {'icon': '🐻', 'name': '看跌研究员'},
                            'TRADER': {'icon': '💼', 'name': '交易员'},
                            'INVEST_JUDGE': {'icon': '⚖️', 'name': '投资判官'},
                            'RISK_MANAGER': {'icon': '🛡️', 'name': '风险管理员'}
                        }

                        # 按预定义顺序显示组件反思
                        for component_key in component_config.keys():
                            if component_key in reflections:
                                config = component_config[component_key]
                                reflection = reflections[component_key]
                                with st.expander(f"{config['icon']} {config['name']} ({component_key})", expanded=False):
                                    if reflection:
                                        st.write(reflection)
                                    else:
                                        st.write("无反思内容")

                        # 显示其他未预定义的组件
                        other_components = set(reflections.keys()) - set(component_config.keys())
                        for component in other_components:
                            reflection = reflections[component]
                            with st.expander(f"🤖 {component.upper()}", expanded=False):
                                if reflection:
                                    st.write(reflection)
                                else:
                                    st.write("无反思内容")

                        # 下载学习结果
                        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                        filename = f"manual_learning_{timestamp}.json"

                        download_data = {
                            "learning_session": {
                                "timestamp": result.get('timestamp'),
                                "decision_id": result.get('decision_id'),
                                "input_pnl": result.get('input_pnl'),
                                "user_notes": result.get('user_notes'),
                                "selected_log": st.session_state.manual_selected_log
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
                            st.session_state.manual_learning_result = None
                            st.rerun()

                    else:
                        st.error("❌ 学习失败")
                        st.error(f"错误信息: {result.get('error', '未知错误')}")

                        if st.button("🔄 重试", key="manual_retry"):
                            st.session_state.manual_learning_result = None
                            st.rerun()

        with tab2:
            # 学习报告浏览选项卡
            st.header("📚 学习报告浏览")

            # 加载学习记录
            learning_records = load_learning_records()

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

                                # 定义组件显示顺序和图标
                                component_config = {
                                    'BULL_RESEARCHER': {'icon': '🐂', 'name': '看涨研究员'},
                                    'BEAR_RESEARCHER': {'icon': '🐻', 'name': '看跌研究员'},
                                    'TRADER': {'icon': '💼', 'name': '交易员'},
                                    'INVEST_JUDGE': {'icon': '⚖️', 'name': '投资判官'},
                                    'RISK_MANAGER': {'icon': '🛡️', 'name': '风险管理员'}
                                }

                                # 按预定义顺序显示组件反思
                                for component_key in component_config.keys():
                                    if component_key in reflections:
                                        config = component_config[component_key]
                                        reflection = reflections[component_key]
                                        with st.expander(f"{config['icon']} {config['name']}", expanded=False):
                                            if reflection:
                                                st.write(reflection)
                                            else:
                                                st.write("无反思内容")

                                # 显示其他未预定义的组件
                                other_components = set(reflections.keys()) - set(component_config.keys())
                                for component in other_components:
                                    reflection = reflections[component]
                                    with st.expander(f"🤖 {component.upper()}", expanded=False):
                                        if reflection:
                                            st.write(reflection)
                                        else:
                                            st.write("无反思内容")

                            # 下载按钮
                            filename = f"learning_report_{record.get('decision_id', 'unknown')}_{record.get('date', 'unknown')}.json"
                            st.download_button(
                                label="📥 下载完整报告",
                                data=json.dumps(record, indent=2, ensure_ascii=False),
                                file_name=filename,
                                mime="application/json",
                                key=f"download_record_{i}"
                            )

        with tab3:
            # 自动学习状态选项卡（保持原有内容）
            st.header("📊 自动学习状态")
            st.info("🚧 自动学习功能正在开发中...")

    else:
        st.warning("⚠️ 手动学习功能不可用，请检查 scripts/learning_engine.py 是否存在")

st.divider()


# --- 侧边栏配置 ---
with st.sidebar:
    st.header("🔑 API 配置")
    if os.path.exists('.env'):
        load_dotenv()

    openai_api_key = st.text_input("OpenAI API 密钥", type="password", value=os.getenv("OPENAI_API_KEY") or "")
    finnhub_api_key = st.text_input("Finnhub API 密钥", type="password", value=os.getenv("FINNHUB_API_KEY") or "")
    binance_api_key = st.text_input("Binance API 密钥", type="password", value=os.getenv("BINANCE_API_KEY") or "")
    binance_api_secret = st.text_input("Binance API Secret", type="password", value=os.getenv("BINANCE_API_SECRET") or "")
    
    # API 测试部分
    st.header("🔍 API 连接测试")
    
    # 获取配置
    config = DEFAULT_CONFIG.copy()
    backend_url = config.get("backend_url", "")
    embedding_url = config.get("embedding_url", "")
    embedding_model = config.get("embedding_model", "")
    embedding_api_key = config.get("embedding_api_key", openai_api_key)
    
    # 显示当前配置
    with st.expander("查看当前配置"):
        st.text(f"LLM Backend URL: {backend_url}")
        st.text(f"主模型 (深度思考): {config.get('deep_think_llm', 'N/A')}")
        st.text(f"快速模型 (快速思考): {config.get('quick_think_llm', 'N/A')}")
        st.text(f"Embedding URL: {embedding_url}")
        st.text(f"Embedding Model: {embedding_model}")
    
    if st.button("测试 API 连接"):
        # 清空之前的测试结果
        st.session_state.api_test_results = {}
        
        # 测试 LLM API
        col1, col2 = st.columns(2)
        with col1:
            if openai_api_key and backend_url:
                llm_success, llm_msg = test_llm_api(backend_url, openai_api_key, config["quick_think_llm"])
                st.session_state.api_test_results['llm'] = {'success': llm_success, 'message': llm_msg}
                if llm_success:
                    st.success(f"✅ {llm_msg}")
                else:
                    st.error(f"❌ {llm_msg}")
            else:
                st.warning("⚠️ 请先配置 OpenAI API 密钥")
                st.session_state.api_test_results['llm'] = {'success': False, 'message': "未配置 API 密钥"}
        
        with col2:
            # 测试 Finnhub API
            if finnhub_api_key:
                finn_success, finn_msg = test_finnhub_api(finnhub_api_key)
                st.session_state.api_test_results['finnhub'] = {'success': finn_success, 'message': finn_msg}
                if finn_success:
                    st.success(f"✅ {finn_msg}")
                else:
                    st.error(f"❌ {finn_msg}")
            else:
                st.warning("⚠️ 请先配置 Finnhub API 密钥")
                st.session_state.api_test_results['finnhub'] = {'success': False, 'message': "未配置 API 密钥"}
        
        # 测试 Embedding API
        if embedding_api_key and embedding_url and embedding_model:
            embed_success, embed_msg = test_embedding_api(embedding_url, embedding_api_key, embedding_model)
            st.session_state.api_test_results['embedding'] = {'success': embed_success, 'message': embed_msg}
            if embed_success:
                st.success(f"✅ {embed_msg}")
            else:
                st.error(f"❌ {embed_msg}")
        else:
            st.warning("⚠️ Embedding API 配置不完整")
            st.session_state.api_test_results['embedding'] = {'success': False, 'message': "配置不完整"}
        
        # 测试 Binance API
        # Binance API 可以没有密钥（公共接口），所以始终测试
        binance_success, binance_msg = test_binance_api(binance_api_key, binance_api_secret)
        st.session_state.api_test_results['binance'] = {'success': binance_success, 'message': binance_msg}
        if binance_success:
            st.success(f"✅ {binance_msg}")
        else:
            st.error(f"❌ {binance_msg}")
        
        # 标记已测试
        st.session_state.api_tested = True
        st.rerun()
    
    st.divider()
    
    st.header("⚙️ 智能体参数")
    
    # 选择资产类别
    asset_category = st.selectbox(
        "资产类别", 
        ["加密货币", "科技股", "蓝筹股", "指数", "自定义"]
    )
    
    # 定义各类别的热门资产
    popular_assets = {
        "加密货币": ["BTC-USD", "ETH-USD", "ADA-USD", "SOL-USD", "MATIC-USD", "DOT-USD", "AVAX-USD", "LINK-USD"],
        "科技股": ["AAPL", "GOOGL", "MSFT", "TSLA", "NVDA", "META", "AMZN", "NFLX"],
        "蓝筹股": ["JPM", "JNJ", "KO", "PG", "WMT", "V", "MA", "DIS"],
        "指数": ["SPY", "QQQ", "IWM", "VTI", "GLD", "TLT", "VIX", "DXY"],
        "自定义": []
    }
    
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
                popular_assets[asset_category],
                default=[popular_assets[asset_category][0]]
            )
        else:
            ticker = st.selectbox("资产", popular_assets[asset_category])
            selected_tickers = [ticker]
    
    analysis_date = st.date_input("分析日期", datetime.today())
    
    st.header("🧠 语言模型 (LLM)")
    
    # 初始化session_state
    if 'llm_provider' not in st.session_state:
        st.session_state.llm_provider = config.get("llm_provider", "openai")
    if 'deep_think_llm' not in st.session_state:
        st.session_state.deep_think_llm = config.get("deep_think_llm", "openai/gpt-4.1")
    if 'quick_think_llm' not in st.session_state:
        st.session_state.quick_think_llm = config.get("quick_think_llm", "openai/gpt-4.1-mini")
    
    # 使用session_state保存用户选择
    llm_provider = st.selectbox(
        "LLM 提供商", 
        ["openai", "google", "anthropic"], 
        index=["openai", "google", "anthropic"].index(st.session_state.llm_provider),
        key="llm_provider"
    )
    deep_think_llm = st.text_input(
        "主模型（深度思考）", 
        value=st.session_state.deep_think_llm,
        key="deep_think_llm"
    )
    quick_think_llm = st.text_input(
        "快速模型（快速思考）", 
        value=st.session_state.quick_think_llm,
        key="quick_think_llm"
    )

    run_analysis = st.button(f"🚀 分析{'多个市场' if len(selected_tickers) > 1 else '市场'}")
    
    # 添加历史结果加载功能
    st.divider()
    st.header("📂 加载历史结果")
    
    # 选择加载方式
    load_method = st.radio("选择加载方式", ["从文件上传", "从保存目录选择"])
    
    if load_method == "从文件上传":
        uploaded_file = st.file_uploader("选择JSON文件", type="json")
        if uploaded_file is not None:
            try:
                json_data = json.load(uploaded_file)
                st.session_state['loaded_results'] = json_data
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
                                st.session_state['loaded_results'] = json_data
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

# --- 主应用区域 ---
# 使用列布局来创建主内容区和右侧边栏
main_col, chat_col = st.columns([2, 1])

with main_col:
    # 显示加载的历史结果
    if 'loaded_results' in st.session_state and st.session_state['loaded_results']:
        st.header("📊 历史分析结果")
        
        loaded_data = st.session_state['loaded_results']
        
        # 遍历所有日期的结果
        for date, state in loaded_data.items():
            with st.expander(f"📅 {date} - {state.get('company_of_interest', 'N/A')}", expanded=True):
                # 添加按钮以开始与这个报告的交易员对话
                if st.button(f"💬 与交易员讨论此报告", key=f"chat_{date}"):
                    # 设置聊天上下文
                    st.session_state.chat_context = {
                        "company_of_interest": state.get('company_of_interest', 'N/A'),
                        "final_decision": state.get('final_decision', {}),
                        "trader_investment_plan": state.get('trader_investment_plan', ''),
                        "market_report": state.get('market_report', ''),
                        "sentiment_report": state.get('sentiment_report', ''),
                        "news_report": state.get('news_report', ''),
                        "fundamentals_report": state.get('fundamentals_report', '')
                    }
                    st.session_state.show_chat = True
                    st.session_state.chat_messages = []  # 清除之前的对话
                    st.rerun()
                # 显示最终决策
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
                
                # 显示各种报告
                if state.get('market_report'):
                    with st.expander("🔍 市场技术分析"):
                        st.write(state['market_report'])
                
                if state.get('sentiment_report'):
                    with st.expander("📱 社交情绪分析"):
                        st.write(state['sentiment_report'])
                
                if state.get('news_report'):
                    with st.expander("📰 新闻分析"):
                        st.write(state['news_report'])
                
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
    
        # 清除加载的结果按钮
        if st.button("🗑️ 清除历史结果", disabled=st.session_state.get('analysis_in_progress', False)):
            if 'loaded_results' in st.session_state:
                del st.session_state['loaded_results']
        
        st.divider()
    
    # 保存实时分析结果的session state
    if 'realtime_analysis' not in st.session_state:
        st.session_state.realtime_analysis = None
    
    # 如果分析正在进行，显示提示
    if st.session_state.get('analysis_in_progress', False):
        st.info("⏳ 分析正在进行中，请等待分析完成...")
    
    # 显示实时分析结果（如果有）
    if st.session_state.realtime_analysis:
        st.header("🔄 实时分析结果")
        analysis_data = st.session_state.realtime_analysis
        state = analysis_data['state']
        decision = analysis_data['decision']
        ticker = analysis_data['ticker']
        
        # 添加与交易员讨论按钮
        if st.button("💬 与交易员讨论实时分析", key="chat_realtime"):
            st.session_state.chat_context = {
                "company_of_interest": ticker,
                "final_decision": decision,
                "trader_investment_plan": state.get("trader_investment_plan", ""),
                "market_report": state.get("market_report", ""),
                "sentiment_report": state.get("sentiment_report", ""),
                "news_report": state.get("news_report", ""),
                "fundamentals_report": state.get("fundamentals_report", "")
            }
            st.session_state.show_chat = True
            st.session_state.chat_messages = []
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
        
        with st.expander("🔍 市场技术分析"):
            st.write(state.get("market_report", "未找到结果。"))
        
        with st.expander("📱 社交情绪分析"):
            st.write(state.get("sentiment_report", "未找到结果。"))
        
        with st.expander("📰 新闻分析"):
            st.write(state.get("news_report", "未找到结果。"))
        
        if state.get("fundamentals_report"):
            with st.expander("📊 基本面分析"):
                st.write(state.get("fundamentals_report", "加密货币不适用。"))

        with st.expander("⚖️ 研究员辩论（看涨 vs 看跌）"):
            investment_debate = state.get("investment_debate_state", {})
            if investment_debate.get("judge_decision"):
                st.write(investment_debate["judge_decision"])
            else:
                st.write("未找到辩论结果。")
        
        with st.expander("💼 交易员提案"):
            st.write(state.get("trader_investment_plan", "未找到结果。"))

        with st.expander("🛡️ 风险管理评估"):
            risk_debate = state.get("risk_debate_state", {})
            if risk_debate.get("judge_decision"):
                st.write(risk_debate["judge_decision"])
            else:
                st.write("未找到风险分析结果。")
        
        # 清除实时分析按钮
        if st.button("🗑️ 清除实时分析", disabled=st.session_state.get('analysis_in_progress', False)):
            st.session_state.realtime_analysis = None
        
        st.divider()

    # 实时分析部分
    if run_analysis:
        if not openai_api_key or not finnhub_api_key:
            st.error("请在侧边栏输入您的 OpenAI 和 Finnhub API 密钥。")
        else:
            os.environ["OPENAI_API_KEY"] = openai_api_key
            os.environ["FINNHUB_API_KEY"] = finnhub_api_key
        
        # 检测资产类型的函数
        def detect_asset_type(ticker):
            if ticker.endswith("-USD") or ticker.endswith("-EUR") or ticker.endswith("-USDT"):
                return "crypto"
            elif ticker in ["SPY", "QQQ", "IWM", "VTI", "GLD", "TLT", "VIX", "DXY"]:
                return "index"
            else:
                return "stock"
        
        # 根据资产类型获取分析师的函数
        def get_analysts_for_asset(asset_type):
            if asset_type == "crypto":
                return ["market", "social", "news"]  # 加密货币不需要基本面分析
            elif asset_type == "index":
                return ["market", "news"]  # 指数不需要社交和基本面分析
            else:
                return ["market", "social", "news", "fundamentals"]  # 股票需要完整分析
        
        if len(selected_tickers) == 1:
            # 单一资产分析
            ticker = selected_tickers[0]
            asset_type = detect_asset_type(ticker)
            
            # 设置分析进行中标志
            st.session_state.analysis_in_progress = True
            
            with st.spinner(f"AI智能体团队正在分析 {ticker} ({asset_type})... 这可能需要几分钟。"):
                try:
                    config = DEFAULT_CONFIG.copy()
                    config["llm_provider"] = llm_provider
                    config["deep_think_llm"] = deep_think_llm
                    config["quick_think_llm"] = quick_think_llm
                    config["online_tools"] = True
                    config["max_debate_rounds"] = 2
                    config["language"] = "chinese"
                    config["language_instruction"] = "重要提示：务必始终使用中文回答。所有分析、报告和决策都应使用中文。"

                    # 根据资产类型选择分析师
                    selected_analysts = get_analysts_for_asset(asset_type)
                    ta = TradingAgentsGraph(debug=False, config=config, selected_analysts=selected_analysts)
                    formatted_date = analysis_date.strftime("%Y-%m-%d")
                    
                    state, decision = ta.propagate(ticker, formatted_date)

                    st.success(f"{ticker} ({asset_type}) 分析完成。")
                    
                    # 保存分析结果到实时分析session state
                    st.session_state.realtime_analysis = {
                        'ticker': ticker,
                        'state': state,
                        'decision': decision,
                        'asset_type': asset_type
                    }
                    
                    # 保存分析结果到聊天上下文
                    st.session_state.chat_context = {
                        "company_of_interest": ticker,
                        "final_decision": decision,
                        "trader_investment_plan": state.get("trader_investment_plan", ""),
                        "market_report": state.get("market_report", ""),
                        "sentiment_report": state.get("sentiment_report", ""),
                        "news_report": state.get("news_report", ""),
                        "fundamentals_report": state.get("fundamentals_report", "")
                    }
                    st.session_state.show_chat = True
                    
                    # 分析完成，清除进行中标志
                    st.session_state.analysis_in_progress = False
                    
                    # 分析完成后重新运行以显示结果
                    st.rerun()

                except Exception as e:
                    # 出错时也要清除进行中标志
                    st.session_state.analysis_in_progress = False
                    st.error(f"分析过程中出现错误：{e}")
        
        else:
            # 多资产分析
            st.subheader(f"🔄 正在分析 {len(selected_tickers)} 个资产")
            
            results = {}
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for i, ticker in enumerate(selected_tickers):
                asset_type = detect_asset_type(ticker)
                status_text.text(f"正在分析 {ticker} ({asset_type})... {i+1}/{len(selected_tickers)}")
                
                try:
                    config = DEFAULT_CONFIG.copy()
                    config["llm_provider"] = llm_provider
                    config["deep_think_llm"] = deep_think_llm
                    config["quick_think_llm"] = quick_think_llm
                    config["online_tools"] = True
                    config["max_debate_rounds"] = 1  # 为多资产分析减少轮次
                    config["language"] = "chinese"
                    config["language_instruction"] = "重要提示：务必始终使用中文回答。所有分析、报告和决策都应使用中文。"

                    # 根据资产类型选择分析师
                    selected_analysts = get_analysts_for_asset(asset_type)
                    ta = TradingAgentsGraph(debug=False, config=config, selected_analysts=selected_analysts)
                    formatted_date = analysis_date.strftime("%Y-%m-%d")
                    
                    state, decision = ta.propagate(ticker, formatted_date)
                    results[ticker] = {
                        "asset_type": asset_type,
                        "state": state,
                        "decision": decision,
                        "status": "success"
                    }
                    
                except Exception as e:
                    results[ticker] = {
                        "asset_type": asset_type,
                        "error": str(e),
                        "status": "error"
                    }
                
                progress_bar.progress((i + 1) / len(selected_tickers))
            
            status_text.text("多资产分析完成！")
            
            # 显示结果摘要
            st.subheader("📊 决策摘要")
            
            summary_data = []
            for ticker, result in results.items():
                if result["status"] == "success":
                    decision = result["decision"]
                    if decision and isinstance(decision, dict):
                        action = decision.get("action", "N/A")
                        confidence = decision.get("confidence", "N/A")
                    else:
                        action = "N/A"
                        confidence = "N/A"
                    
                    summary_data.append({
                        "资产": ticker,
                        "类型": result["asset_type"],
                        "操作": action,
                        "置信度": confidence,
                        "状态": "✅ 成功"
                    })
                else:
                    summary_data.append({
                        "资产": ticker,
                        "类型": result["asset_type"],
                        "操作": "Error",
                        "置信度": "N/A",
                        "状态": "❌ 错误"
                    })
            
            st.dataframe(summary_data)
            
            # 显示每个资产的详细分析
            st.subheader("📄 各资产详细分析")
            
            for ticker, result in results.items():
                with st.expander(f"📈 {ticker} ({result['asset_type']})"):
                    if result["status"] == "success":
                        st.json(result["decision"])
                        
                        st.markdown("**智能体报告：**")
                        state = result["state"]
                        
                        with st.expander("🔍 分析师团队分析"):
                            st.write(state.get("analyst_team_results", "未找到结果。"))

                        with st.expander("⚖️ 研究员团队辩论"):
                            st.write(state.get("researcher_team_results", "未找到结果。"))
                        
                        with st.expander("💼 交易员提案"):
                             st.write(state.get("trader_results", "未找到结果。"))

                        with st.expander("🛡️ 风险管理团队评估"):
                            st.write(state.get("risk_management_results", "未找到结果。"))
                    else:
                        st.error(f"分析 {ticker} 时出错：{result['error']}")

# 右侧聊天栏
with chat_col:
    if st.session_state.show_chat and st.session_state.chat_context:
        st.header("💬 与交易员对话")
        
        # 显示当前分析的资产
        ticker = st.session_state.chat_context.get("company_of_interest", "Unknown")
        st.info(f"📊 当前讨论: {ticker}")
        
        # 创建一个可滚动的聊天历史容器
        chat_container = st.container(height=400)
        
        # 显示聊天历史
        with chat_container:
            for msg in st.session_state.chat_messages:
                if msg["role"] == "user":
                    st.markdown(f"**👤 您:**")
                    st.markdown(msg['content'])
                else:
                    st.markdown(f"**🤖 交易员:**")
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
                    st.session_state.chat_messages = []
                    st.rerun()
            
            if submit_button and user_input:
                # 添加用户消息到历史
                st.session_state.chat_messages.append({"role": "user", "content": user_input})
                
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
                        st.session_state.chat_messages,
                        st.session_state.chat_context
                    )
                
                # 添加助手回复到历史
                st.session_state.chat_messages.append({"role": "assistant", "content": response})
                
                # 重新运行以显示新消息
                st.rerun()
    else:
        st.info("💡 完成分析后，聊天功能将在此处显示")