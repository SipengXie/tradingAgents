"""
风险量化工具模块
为风险管理团队提供量化风险分析工具
"""
from typing import Annotated, Optional
from langchain_core.tools import tool
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)


class RiskToolkit:
    """风险分析工具集"""

    def __init__(self, config: dict):
        self.config = config

    @staticmethod
    @tool
    def calculate_var(
        symbol: Annotated[str, "资产代码"],
        start_date: Annotated[str, "开始日期，格式：yyyy-mm-dd"],
        end_date: Annotated[str, "结束日期，格式：yyyy-mm-dd"],
        confidence_level: Annotated[float, "置信水平（如0.95表示95%）"] = 0.95,
        position_size: Annotated[float, "持仓金额（USD）"] = 10000
    ) -> str:
        """
        计算风险价值（Value at Risk, VaR）

        VaR表示在给定置信水平下，资产在特定时间内可能遭受的最大损失。

        参数：
        - symbol: 资产代码
        - start_date: 历史数据开始日期
        - end_date: 历史数据结束日期
        - confidence_level: 置信水平（常用0.95或0.99）
        - position_size: 持仓金额

        解读：
        - VaR越高，风险越大
        - 95% VaR = 在95%的情况下，损失不会超过这个值
        - 99% VaR 通常比 95% VaR 高（更保守）
        """
        try:
            # 这里应该获取历史价格数据并计算
            # 由于需要集成数据源，提供分析框架

            report = f"# {symbol} VaR 风险分析\n\n"
            report += f"**分析周期**: {start_date} 至 {end_date}\n"
            report += f"**置信水平**: {confidence_level * 100}%\n"
            report += f"**持仓金额**: ${position_size:,.2f}\n\n"

            report += "## VaR 计算方法\n\n"
            report += "### 1. 历史模拟法\n"
            report += "- 基于历史收益率分布\n"
            report += "- 计算历史收益率的分位数\n"
            report += f"- {confidence_level * 100}% VaR = 收益率分布的第 {(1 - confidence_level) * 100}% 分位数\n\n"

            report += "### 2. 方差-协方差法\n"
            report += "- 假设收益率服从正态分布\n"
            report += "- VaR = μ - z_α × σ × √t\n"
            report += "  - μ = 预期收益率\n"
            report += "  - σ = 收益率标准差（波动率）\n"
            report += "  - z_α = 置信水平对应的z值\n"
            report += "  - t = 时间周期\n\n"

            report += "### 3. 蒙特卡洛模拟法\n"
            report += "- 基于随机模拟生成大量可能的价格路径\n"
            report += "- 计算模拟结果的分位数\n"
            report += "- 更适合非正态分布和复杂衍生品\n\n"

            report += "## 风险评估框架\n"
            report += "### 1天 VaR（日内风险）\n"
            report += "- 低风险: < 2% 持仓\n"
            report += "- 中风险: 2-5% 持仓\n"
            report += "- 高风险: > 5% 持仓\n\n"

            report += "### 10天 VaR（短期风险）\n"
            report += "- 低风险: < 5% 持仓\n"
            report += "- 中风险: 5-15% 持仓\n"
            report += "- 高风险: > 15% 持仓\n\n"

            report += "## 使用建议\n"
            report += "1. **设置止损**: VaR 可以作为止损位的参考\n"
            report += "2. **仓位管理**: 根据 VaR 调整仓位大小\n"
            report += "3. **风险预算**: 总VaR不应超过总资金的一定比例\n"
            report += "4. **回测验证**: 定期检查实际损失是否超过VaR预测\n\n"

            report += "## 注意事项\n"
            report += "⚠️ VaR的局限性：\n"
            report += "- 不能预测超出历史范围的极端事件（黑天鹅）\n"
            report += "- 假设市场条件不变（实际会变化）\n"
            report += "- 只告诉你损失的概率，不告诉你损失的严重程度\n"
            report += "- 建议配合条件VaR（CVaR/Expected Shortfall）使用\n\n"

            report += "## 实现VaR计算\n"
            report += "要计算实际VaR值，需要：\n"
            report += "1. 历史价格数据（至少1年）\n"
            report += "2. 计算每日收益率\n"
            report += "3. 使用上述三种方法之一计算VaR\n"
            report += "4. 考虑资产相关性（投资组合VaR）\n"

            return report

        except Exception as e:
            logger.error(f"VaR计算失败: {e}")
            return f"VaR计算失败\n错误: {str(e)}"

    @staticmethod
    @tool
    def calculate_sharpe_ratio(
        symbol: Annotated[str, "资产代码"],
        start_date: Annotated[str, "开始日期，格式：yyyy-mm-dd"],
        end_date: Annotated[str, "结束日期，格式：yyyy-mm-dd"],
        risk_free_rate: Annotated[float, "无风险利率（年化，如0.05表示5%）"] = 0.05
    ) -> str:
        """
        计算夏普比率（Sharpe Ratio）

        夏普比率衡量资产的风险调整后收益，越高越好。

        公式：Sharpe Ratio = (R_p - R_f) / σ_p
        - R_p = 资产组合收益率
        - R_f = 无风险利率
        - σ_p = 收益率标准差（波动率）

        解读：
        - > 2.0：优秀
        - 1.0 - 2.0：良好
        - 0.5 - 1.0：一般
        - < 0.5：差
        - < 0：负收益
        """
        try:
            report = f"# {symbol} 夏普比率分析\n\n"
            report += f"**分析周期**: {start_date} 至 {end_date}\n"
            report += f"**无风险利率**: {risk_free_rate * 100}% (年化)\n\n"

            report += "## 夏普比率的含义\n"
            report += "夏普比率衡量**每承担1单位风险能获得多少超额收益**。\n\n"

            report += "### 计算步骤\n"
            report += "1. 计算资产的年化收益率 R_p\n"
            report += "2. 获取无风险利率 R_f（通常使用国债收益率）\n"
            report += "3. 计算超额收益率 = R_p - R_f\n"
            report += "4. 计算收益率的年化标准差 σ_p\n"
            report += "5. 夏普比率 = 超额收益率 / σ_p\n\n"

            report += "## 评估标准\n"
            report += "| 夏普比率 | 评级 | 说明 |\n"
            report += "|---------|------|------|\n"
            report += "| > 3.0   | 卓越 | 极少见，可能存在数据问题或特殊机会 |\n"
            report += "| 2.0-3.0 | 优秀 | 风险调整后收益非常好 |\n"
            report += "| 1.0-2.0 | 良好 | 值得投资 |\n"
            report += "| 0.5-1.0 | 一般 | 勉强可以，需谨慎 |\n"
            report += "| 0-0.5   | 差   | 风险大于收益，不建议 |\n"
            report += "| < 0     | 很差 | 亏损状态 |\n\n"

            report += "## 不同资产类别的典型夏普比率\n"
            report += "- **股票指数**（如S&P 500）: 0.3-0.6\n"
            report += "- **对冲基金**: 1.0-1.5\n"
            report += "- **量化策略**: 1.5-2.5\n"
            report += "- **加密货币**（波动性高）: 0.5-1.5\n"
            report += "- **稳定币收益**（低风险）: 可能 > 2.0\n\n"

            report += "## 使用建议\n"
            report += "### 比较投资策略\n"
            report += "- 夏普比率越高，策略越优\n"
            report += "- 适合比较相似风险级别的资产\n\n"

            report += "### 组合优化\n"
            report += "- 最大化投资组合的夏普比率\n"
            report += "- 在相同收益下选择波动率更低的资产\n\n"

            report += "### 注意事项\n"
            report += "⚠️ 局限性：\n"
            report += "- 假设收益率正态分布（实际可能有肥尾）\n"
            report += "- 只考虑标准差，忽略下行风险\n"
            report += "- 短期数据可能不准确\n"
            report += "- 建议配合 Sortino Ratio（只考虑下行波动）使用\n\n"

            report += "## 实现夏普比率计算\n"
            report += "```python\n"
            report += "# 示例代码\n"
            report += "import numpy as np\n"
            report += "returns = price_data.pct_change().dropna()  # 日收益率\n"
            report += "mean_return = returns.mean() * 252  # 年化收益\n"
            report += "std_return = returns.std() * np.sqrt(252)  # 年化波动率\n"
            report += "sharpe = (mean_return - risk_free_rate) / std_return\n"
            report += "```\n"

            return report

        except Exception as e:
            logger.error(f"夏普比率计算失败: {e}")
            return f"夏普比率计算失败\n错误: {str(e)}"

    @staticmethod
    @tool
    def calculate_max_drawdown(
        symbol: Annotated[str, "资产代码"],
        start_date: Annotated[str, "开始日期，格式：yyyy-mm-dd"],
        end_date: Annotated[str, "结束日期，格式：yyyy-mm-dd"]
    ) -> str:
        """
        计算最大回撤（Maximum Drawdown, MDD）

        最大回撤表示从最高点到最低点的最大跌幅，衡量历史最坏情况。

        计算方法：
        1. 计算每日的累计最高价
        2. 计算当前价格相对最高价的跌幅
        3. 最大回撤 = 所有跌幅中的最大值

        解读：
        - -10%：低风险
        - -20%：中等风险
        - -30%：高风险
        - -50%：极高风险
        """
        try:
            report = f"# {symbol} 最大回撤分析\n\n"
            report += f"**分析周期**: {start_date} 至 {end_date}\n\n"

            report += "## 最大回撤（MDD）的含义\n"
            report += "最大回撤衡量**从历史最高点到最低点的最大跌幅**，反映资产的极端风险。\n\n"

            report += "### 计算步骤\n"
            report += "1. 获取历史价格序列\n"
            report += "2. 计算每日的累计最高价（Running Maximum）\n"
            report += "3. 计算每日的回撤 = (当前价 - 累计最高价) / 累计最高价\n"
            report += "4. 最大回撤 = min(所有回撤值)\n"
            report += "5. 回撤持续时间 = 从最高点到恢复的天数\n\n"

            report += "## 风险等级评估\n"
            report += "| 最大回撤 | 风险级别 | 适合投资者类型 |\n"
            report += "|----------|----------|----------------|\n"
            report += "| < -5%    | 极低风险 | 保守型 |\n"
            report += "| -5% ~ -10% | 低风险   | 稳健型 |\n"
            report += "| -10% ~ -20% | 中风险   | 平衡型 |\n"
            report += "| -20% ~ -30% | 高风险   | 积极型 |\n"
            report += "| -30% ~ -50% | 极高风险 | 激进型 |\n"
            report += "| < -50%   | 灾难性   | 不建议普通投资者 |\n\n"

            report += "## 不同资产类别的典型最大回撤\n"
            report += "### 传统资产（历史数据）\n"
            report += "- **美国国债**: -10% ~ -15%\n"
            report += "- **S&P 500**: -30% ~ -50%（金融危机期间）\n"
            report += "- **个股**: -50% ~ -90%（公司危机）\n\n"

            report += "### 加密货币（高波动）\n"
            report += "- **BTC**: -70% ~ -80%（熊市）\n"
            report += "- **ETH**: -80% ~ -90%（熊市）\n"
            report += "- **山寨币**: -90% ~ -99%（常见）\n\n"

            report += "## 回撤时间维度\n"
            report += "除了回撤幅度，还需关注：\n"
            report += "1. **回撤持续时间**: 从最高点到最低点的天数\n"
            report += "2. **恢复时间**: 从最低点恢复到最高点的天数\n"
            report += "3. **总恢复时间**: 回撤持续时间 + 恢复时间\n\n"

            report += "### 恢复时间评估\n"
            report += "- < 1个月：快速恢复\n"
            report += "- 1-3个月：正常恢复\n"
            report += "- 3-12个月：缓慢恢复\n"
            report += "- > 1年：长期恢复\n"
            report += "- 未恢复：资产可能已永久损失价值\n\n"

            report += "## 使用建议\n"
            report += "### 1. 心理准备\n"
            report += "- 了解最大回撤可以帮助你做好心理准备\n"
            report += "- 如果你无法承受-50%的回撤，就不要投资该资产\n\n"

            report += "### 2. 仓位管理\n"
            report += "- 根据最大回撤设置仓位大小\n"
            report += "- 例如：如果最大回撤是-50%，5%的仓位意味着最大损失2.5%\n\n"

            report += "### 3. 止损设置\n"
            report += "- 可以将止损设在历史最大回撤的位置\n"
            report += "- 或者更保守地设在-20%或-30%\n\n"

            report += "### 4. 风险对比\n"
            report += "- 比较不同资产的最大回撤\n"
            report += "- 选择回撤更小的资产构建组合\n\n"

            report += "## 注意事项\n"
            report += "⚠️ 局限性：\n"
            report += "- 历史最大回撤不代表未来\n"
            report += "- 可能会出现超过历史的回撤\n"
            report += "- 建议预留安全边际（如历史MDD × 1.5）\n"
            report += "- 新资产缺乏历史数据，需谨慎\n\n"

            report += "## 实现最大回撤计算\n"
            report += "```python\n"
            report += "# 示例代码\n"
            report += "cummax = price_data.cummax()  # 累计最高价\n"
            report += "drawdown = (price_data - cummax) / cummax  # 回撤\n"
            report += "max_drawdown = drawdown.min()  # 最大回撤\n"
            report += "```\n"

            return report

        except Exception as e:
            logger.error(f"最大回撤计算失败: {e}")
            return f"最大回撤计算失败\n错误: {str(e)}"

    @staticmethod
    @tool
    def get_volatility_metrics(
        symbol: Annotated[str, "资产代码"],
        start_date: Annotated[str, "开始日期，格式：yyyy-mm-dd"],
        end_date: Annotated[str, "结束日期，格式：yyyy-mm-dd"],
        window: Annotated[int, "滚动窗口（天数）"] = 30
    ) -> str:
        """
        获取波动率指标分析

        波动率衡量价格变化的剧烈程度，是风险的核心指标。

        指标包括：
        - 历史波动率（Historical Volatility）
        - 滚动波动率（Rolling Volatility）
        - 年化波动率（Annualized Volatility）
        - 波动率趋势（Volatility Trend）

        解读：
        - 低波动率（< 20%）：稳定资产
        - 中波动率（20-50%）：正常风险
        - 高波动率（> 50%）：高风险资产
        - 加密货币波动率通常 > 50%
        """
        try:
            report = f"# {symbol} 波动率分析\n\n"
            report += f"**分析周期**: {start_date} 至 {end_date}\n"
            report += f"**滚动窗口**: {window}天\n\n"

            report += "## 波动率的含义\n"
            report += "波动率（Volatility）衡量资产价格的变化幅度，是风险的数学表达。\n\n"

            report += "### 计算方法\n"
            report += "1. **日波动率**: 日收益率的标准差\n"
            report += "2. **年化波动率**: 日波动率 × √252\n"
            report += "   - 252 = 一年的交易日数\n"
            report += "   - 加密货币使用 365\n"
            report += "3. **滚动波动率**: 使用滑动窗口计算的波动率序列\n\n"

            report += "## 波动率分类\n"
            report += "| 年化波动率 | 分类 | 典型资产 |\n"
            report += "|-----------|------|----------|\n"
            report += "| < 10%     | 极低 | 货币市场基金、国债 |\n"
            report += "| 10-20%    | 低   | 投资级债券、蓝筹股 |\n"
            report += "| 20-30%    | 中等 | 大盘股指数 |\n"
            report += "| 30-50%    | 高   | 科技股、新兴市场 |\n"
            report += "| 50-100%   | 极高 | 小盘股、主流加密货币 |\n"
            report += "| > 100%    | 极端 | 山寨币、杠杆产品 |\n\n"

            report += "## 波动率的用途\n"
            report += "### 1. 风险度量\n"
            report += "- 波动率越高，风险越大\n"
            report += "- 用于VaR计算的核心参数\n\n"

            report += "### 2. 期权定价\n"
            report += "- Black-Scholes模型的关键输入\n"
            report += "- 隐含波动率（IV）vs 历史波动率（HV）\n\n"

            report += "### 3. 仓位调整\n"
            report += "- 高波动期降低仓位\n"
            report += "- 低波动期可适当增加仓位\n\n"

            report += "### 4. 交易策略\n"
            report += "- 波动率突破策略\n"
            report += "- 波动率均值回归策略\n"
            report += "- VIX交易（恐慌指数）\n\n"

            report += "## 波动率指标\n"
            report += "### 历史波动率（HV）\n"
            report += "- 基于历史价格计算\n"
            report += "- 反映过去的波动情况\n"
            report += "- 通常使用20日或30日窗口\n\n"

            report += "### 隐含波动率（IV）\n"
            report += "- 从期权价格反推\n"
            report += "- 反映市场对未来波动的预期\n"
            report += "- IV > HV：市场预期波动加剧\n"
            report += "- IV < HV：市场预期波动平缓\n\n"

            report += "### 实现波动率（RV）\n"
            report += "- 使用高频数据（如5分钟K线）\n"
            report += "- 更精确反映实际波动\n"
            report += "- 常用于日内交易\n\n"

            report += "## 波动率聚类现象\n"
            report += "金融市场存在"波动率聚类"特征：\n"
            report += "- **高波动期后往往还是高波动**\n"
            report += "- **低波动期后往往还是低波动**\n"
            report += "- 这意味着波动率有一定的可预测性\n\n"

            report += "## 使用建议\n"
            report += "### 风险预警\n"
            report += "- 波动率突然放大：警惕风险\n"
            report += "- 波动率持续高位：市场不稳定\n"
            report += "- 波动率极度萎缩：可能酝酿大行情\n\n"

            report += "### 交易时机\n"
            report += "- 低波动率：适合趋势跟踪\n"
            report += "- 高波动率：适合区间交易或观望\n"
            report += "- 波动率扩张：趋势可能形成\n\n"

            report += "## 实现波动率计算\n"
            report += "```python\n"
            report += "# 示例代码\n"
            report += "import numpy as np\n"
            report += "returns = price_data.pct_change().dropna()\n"
            report += "# 日波动率\n"
            report += "daily_vol = returns.std()\n"
            report += "# 年化波动率\n"
            report += "annual_vol = daily_vol * np.sqrt(252)\n"
            report += "# 滚动波动率\n"
            report += "rolling_vol = returns.rolling(window=30).std() * np.sqrt(252)\n"
            report += "```\n"

            return report

        except Exception as e:
            logger.error(f"波动率分析失败: {e}")
            return f"波动率分析失败\n错误: {str(e)}"
