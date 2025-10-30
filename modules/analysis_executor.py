"""
分析执行器
执行单资产和多资产的市场分析
"""

import streamlit as st
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG
from utils.asset_classifier import AssetClassifier


class AnalysisExecutor:
    """分析执行器"""

    def __init__(self, config: dict):
        """
        初始化分析执行器

        Args:
            config: 分析配置字典
        """
        self.config = config
        self.asset_classifier = AssetClassifier()

    def build_trading_config(self, llm_provider: str, deep_think_llm: str,
                            quick_think_llm: str, max_debate_rounds: int = 2) -> dict:
        """
        构建交易配置

        Args:
            llm_provider: LLM 提供商
            deep_think_llm: 深度思考模型
            quick_think_llm: 快速思考模型
            max_debate_rounds: 辩论轮数

        Returns:
            配置字典
        """
        config = DEFAULT_CONFIG.copy()
        config["llm_provider"] = llm_provider
        config["deep_think_llm"] = deep_think_llm
        config["quick_think_llm"] = quick_think_llm
        config["online_tools"] = True
        config["max_debate_rounds"] = max_debate_rounds
        config["language"] = "chinese"
        config["language_instruction"] = "重要提示：务必始终使用中文回答。所有分析、报告和决策都应使用中文。"
        return config

    def execute_single_analysis(self, ticker: str, analysis_date: str,
                                llm_provider: str, deep_think_llm: str,
                                quick_think_llm: str) -> dict:
        """
        执行单资产分析

        Args:
            ticker: 资产代码
            analysis_date: 分析日期
            llm_provider: LLM 提供商
            deep_think_llm: 深度思考模型
            quick_think_llm: 快速思考模型

        Returns:
            分析结果字典，包含 ticker, state, decision, asset_type
        """
        asset_type = self.asset_classifier.detect_asset_type(ticker)

        with st.spinner(f"AI智能体团队正在分析 {ticker} ({asset_type})... 这可能需要几分钟。"):
            try:
                config = self.build_trading_config(
                    llm_provider, deep_think_llm, quick_think_llm, max_debate_rounds=2
                )

                # 根据资产类型选择分析师
                selected_analysts = self.asset_classifier.get_analysts_for_asset(asset_type)
                ta = TradingAgentsGraph(debug=False, config=config, selected_analysts=selected_analysts)

                state, decision = ta.propagate(ticker, analysis_date)

                st.success(f"{ticker} ({asset_type}) 分析完成。")

                return {
                    'ticker': ticker,
                    'state': state,
                    'decision': decision,
                    'asset_type': asset_type
                }

            except Exception as e:
                st.error(f"分析过程中出现错误：{e}")
                return None

    def execute_multi_analysis(self, tickers: list[str], analysis_date: str,
                               llm_provider: str, deep_think_llm: str,
                               quick_think_llm: str) -> dict:
        """
        执行多资产分析

        Args:
            tickers: 资产代码列表
            analysis_date: 分析日期
            llm_provider: LLM 提供商
            deep_think_llm: 深度思考模型
            quick_think_llm: 快速思考模型

        Returns:
            结果字典，键为 ticker，值为分析结果
        """
        st.subheader(f"🔄 正在分析 {len(tickers)} 个资产")

        results = {}
        progress_bar = st.progress(0)
        status_text = st.empty()

        for i, ticker in enumerate(tickers):
            asset_type = self.asset_classifier.detect_asset_type(ticker)
            status_text.text(f"正在分析 {ticker} ({asset_type})... {i+1}/{len(tickers)}")

            try:
                config = self.build_trading_config(
                    llm_provider, deep_think_llm, quick_think_llm, max_debate_rounds=1
                )

                # 根据资产类型选择分析师
                selected_analysts = self.asset_classifier.get_analysts_for_asset(asset_type)
                ta = TradingAgentsGraph(debug=False, config=config, selected_analysts=selected_analysts)

                state, decision = ta.propagate(ticker, analysis_date)
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

            progress_bar.progress((i + 1) / len(tickers))

        status_text.text("多资产分析完成！")

        # 显示结果摘要
        self._render_multi_analysis_summary(results)

        # 显示详细分析
        self._render_multi_analysis_details(results)

        return results

    def _render_multi_analysis_summary(self, results: dict):
        """渲染多资产分析摘要"""
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

    def _render_multi_analysis_details(self, results: dict):
        """渲染多资产分析详情"""
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
