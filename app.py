import streamlit as st
import os
from datetime import datetime
from dotenv import load_dotenv
import requests
from openai import OpenAI
import finnhub
import json
from pathlib import Path

# 导入交易框架所需的组件
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

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

# 在主页面显示 API 状态
if st.session_state.api_tested and st.session_state.api_test_results:
    with st.container():
        st.subheader("📡 API 连接状态")
        cols = st.columns(3)
        
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
        
        st.divider()

# --- 侧边栏配置 ---
with st.sidebar:
    st.header("🔑 API 配置")
    if os.path.exists('.env'):
        load_dotenv()

    openai_api_key = st.text_input("OpenAI API 密钥", type="password", value=os.getenv("OPENAI_API_KEY") or "")
    finnhub_api_key = st.text_input("Finnhub API 密钥", type="password", value=os.getenv("FINNHUB_API_KEY") or "")
    
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
        st.text(f"LLM Model: {config.get('quick_think_llm', 'N/A')}")
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
    llm_provider = st.selectbox("LLM 提供商", ["openai", "google", "anthropic"], index=0)
    deep_think_llm = st.text_input("主模型（深度思考）", "gpt-4o")
    quick_think_llm = st.text_input("快速模型（快速思考）", "gpt-4o")

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
# 显示加载的历史结果
if 'loaded_results' in st.session_state and st.session_state['loaded_results']:
    st.header("📊 历史分析结果")
    
    loaded_data = st.session_state['loaded_results']
    
    # 遍历所有日期的结果
    for date, state in loaded_data.items():
        with st.expander(f"📅 {date} - {state.get('company_of_interest', 'N/A')}", expanded=True):
            # 显示最终决策
            final_decision = state.get('final_decision', {})
            if final_decision and isinstance(final_decision, dict):
                col1, col2, col3 = st.columns(3)
                with col1:
                    action = final_decision.get('action', 'N/A')
                    if action == 'BUY':
                        st.success(f"### 💰 {action}")
                    elif action == 'SELL':
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
    if st.button("🗑️ 清除历史结果"):
        del st.session_state['loaded_results']
        st.rerun()
    
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
            
            with st.spinner(f"AI智能体团队正在分析 {ticker} ({asset_type})... 这可能需要几分钟。"):
                try:
                    config = DEFAULT_CONFIG.copy()
                    config["llm_provider"] = llm_provider
                    config["deep_think_llm"] = deep_think_llm
                    config["quick_think_llm"] = quick_think_llm
                    config["online_tools"] = True
                    config["max_debate_rounds"] = 2
                    config["language"] = "english"
                    config["language_instruction"] = "重要提示：务必始终使用中文回答。所有分析、报告和决策都应使用中文。"

                    # 根据资产类型选择分析师
                    selected_analysts = get_analysts_for_asset(asset_type)
                    ta = TradingAgentsGraph(debug=False, config=config, selected_analysts=selected_analysts)
                    formatted_date = analysis_date.strftime("%Y-%m-%d")
                    
                    state, decision = ta.propagate(ticker, formatted_date)

                    st.success(f"{ticker} ({asset_type}) 分析完成。")

                    # --- 调试部分 ---
                    with st.expander("🐞 调试输出"):
                        st.markdown("**原始状态 (`state`):**")
                        st.write(state)
                        st.markdown("**原始决策 (`decision`):**")
                        st.write(decision)
                    # --- 调试部分结束 ---

                    st.subheader(f"📈 {ticker} 的最终决策：")
                    if decision:
                        # 如果决策只是一个字符串 (BUY, SELL, HOLD)，直接显示
                        if isinstance(decision, str):
                            decision_color = {
                                "BUY": "green",
                                "SELL": "red", 
                                "HOLD": "orange"
                            }.get(decision.upper(), "blue")
                            st.markdown(f"### :{decision_color}[{decision.upper()}]")
                        else:
                            st.json(decision)
                    else:
                        st.warning("AI智能体未生成最终决策。")

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

                except Exception as e:
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
                    config["language"] = "english"
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