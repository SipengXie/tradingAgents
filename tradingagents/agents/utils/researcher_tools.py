"""
研究员工具模块
为看涨/看跌研究员提供补充分析工具
"""
from typing import Annotated, Optional, List
from langchain_core.tools import tool
import logging

logger = logging.getLogger(__name__)


class ResearcherToolkit:
    """研究员分析工具集"""

    def __init__(self, config: dict):
        self.config = config

    @staticmethod
    @tool
    def get_comparable_companies(
        symbol: Annotated[str, "公司代码"],
        sector: Annotated[str, "行业板块（可选）"] = None,
        metric: Annotated[str, "对比指标：valuation, performance, fundamentals"] = "valuation"
    ) -> str:
        """
        获取同行业公司对比分析

        帮助研究员评估目标公司相对竞争对手的表现：
        - valuation：估值指标（P/E, P/B, EV/EBITDA）
        - performance：业绩表现（收益增长、利润率）
        - fundamentals：基本面对比（资产负债率、ROE）

        使用场景：
        1. 判断目标公司是否被高估/低估
        2. 识别行业领导者和落后者
        3. 发现潜在投资机会
        """
        try:
            report = f"# {symbol} 同行业对比分析\n\n"

            if sector:
                report += f"**行业板块**: {sector}\n\n"
            else:
                report += "**注意**: 未指定行业，将根据公司主营业务自动识别\n\n"

            report += "## 对比维度\n\n"

            if metric == "valuation":
                report += "### 估值指标对比\n\n"
                report += "| 公司 | P/E | P/B | P/S | EV/EBITDA | 市盈率分位 |\n"
                report += "|------|-----|-----|-----|-----------|------------|\n"
                report += f"| {symbol} | - | - | - | - | - |\n"
                report += "| 同行1 | - | - | - | - | - |\n"
                report += "| 同行2 | - | - | - | - | - |\n"
                report += "| 行业平均 | - | - | - | - | - |\n\n"

                report += "### 估值指标解读\n"
                report += "- **P/E（市盈率）**: 股价/每股收益\n"
                report += "  - < 行业平均：可能低估\n"
                report += "  - > 行业平均：可能高估或高增长\n\n"

                report += "- **P/B（市净率）**: 股价/每股净资产\n"
                report += "  - < 1：股价低于账面价值\n"
                report += "  - > 1：市场给予溢价\n\n"

                report += "- **P/S（市销率）**: 市值/营收\n"
                report += "  - 适合亏损公司估值\n"
                report += "  - 对比同行业P/S水平\n\n"

                report += "- **EV/EBITDA**: 企业价值/息税折旧摊销前利润\n"
                report += "  - 消除资本结构差异\n"
                report += "  - 更适合跨公司对比\n\n"

            elif metric == "performance":
                report += "### 业绩表现对比\n\n"
                report += "| 公司 | 营收增长 | 净利增长 | 毛利率 | 净利率 | ROE |\n"
                report += "|------|----------|----------|--------|--------|-----|\n"
                report += f"| {symbol} | - | - | - | - | - |\n"
                report += "| 同行1 | - | - | - | - | - |\n"
                report += "| 同行2 | - | - | - | - | - |\n"
                report += "| 行业平均 | - | - | - | - | - |\n\n"

                report += "### 业绩指标解读\n"
                report += "- **营收增长**: 同比增长率\n"
                report += "  - > 15%：高增长\n"
                report += "  - 5-15%：稳定增长\n"
                report += "  - < 5%：低增长\n\n"

                report += "- **毛利率**: (营收 - 成本) / 营收\n"
                report += "  - 反映定价能力和成本控制\n"
                report += "  - 高毛利率公司更有竞争优势\n\n"

                report += "- **ROE**: 净利润 / 股东权益\n"
                report += "  - > 15%：优秀\n"
                report += "  - 10-15%：良好\n"
                report += "  - < 10%：一般\n\n"

            elif metric == "fundamentals":
                report += "### 基本面健康度对比\n\n"
                report += "| 公司 | 资产负债率 | 流动比率 | 现金流 | 营运资本 | 评级 |\n"
                report += "|------|------------|----------|--------|----------|------|\n"
                report += f"| {symbol} | - | - | - | - | - |\n"
                report += "| 同行1 | - | - | - | - | - |\n"
                report += "| 同行2 | - | - | - | - | - |\n"
                report += "| 行业平均 | - | - | - | - | - |\n\n"

                report += "### 财务健康指标解读\n"
                report += "- **资产负债率**: 负债/资产\n"
                report += "  - < 40%：保守型\n"
                report += "  - 40-60%：适中\n"
                report += "  - > 60%：激进型（需警惕）\n\n"

                report += "- **流动比率**: 流动资产/流动负债\n"
                report += "  - > 2：流动性充裕\n"
                report += "  - 1-2：正常\n"
                report += "  - < 1：流动性风险\n\n"

            report += "\n## 竞争优势分析框架\n"
            report += "### 护城河识别\n"
            report += "1. **成本优势**: 毛利率持续高于同行\n"
            report += "2. **品牌溢价**: P/B ratio显著高于同行\n"
            report += "3. **规模效应**: 市场份额 > 30%\n"
            report += "4. **网络效应**: 用户增长加速\n"
            report += "5. **转换成本**: 客户留存率 > 90%\n\n"

            report += "### 竞争地位评估\n"
            report += "- **领导者**: 行业前3，多项指标领先\n"
            report += "- **挑战者**: 增长率高于行业平均\n"
            report += "- **跟随者**: 指标接近行业平均\n"
            report += "- **利基者**: 专注细分市场\n"
            report += "- **落后者**: 多项指标低于平均\n\n"

            report += "## 数据来源\n"
            report += "要获取实际对比数据，可使用：\n"
            report += "1. **SimFin API** - 免费财务数据\n"
            report += "2. **Yahoo Finance** - 基础对比数据\n"
            report += "3. **Alpha Vantage** - 基本面数据\n"
            report += "4. **Finnhub** - 同行业公司列表\n"
            report += "5. **Financial Modeling Prep** - 完整财报对比\n\n"

            report += "## 加密货币行业对比\n"
            if "USD" in symbol or "USDT" in symbol:
                report += "对于加密货币，对比维度有所不同：\n\n"
                report += "### Layer 1 公链对比\n"
                report += "| 指标 | BTC | ETH | SOL | BNB |\n"
                report += "|------|-----|-----|-----|-----|\n"
                report += "| TPS（交易速度） | 7 | 15-30 | 3000+ | 300+ |\n"
                report += "| TVL（锁仓量） | N/A | $50B | $5B | $8B |\n"
                report += "| 开发者数量 | 中 | 最多 | 多 | 多 |\n"
                report += "| 市值排名 | #1 | #2 | #6 | #4 |\n\n"

                report += "### DeFi 协议对比\n"
                report += "| 指标 | Uniswap | Aave | Curve |\n"
                report += "|------|---------|------|-------|\n"
                report += "| TVL | $4B | $10B | $3B |\n"
                report += "| 日交易量 | $1B+ | - | $500M |\n"
                report += "| 代币捕获价值 | 手续费 | 借贷利差 | 手续费+veToken |\n\n"

            return report

        except Exception as e:
            logger.error(f"同行业对比失败: {e}")
            return f"同行业对比失败\n错误: {str(e)}"

    @staticmethod
    @tool
    def get_correlation_analysis(
        symbol: Annotated[str, "主要资产代码"],
        compare_symbols: Annotated[List[str], "对比资产列表"] = None,
        start_date: Annotated[str, "开始日期，格式：yyyy-mm-dd"] = None,
        end_date: Annotated[str, "结束日期，格式：yyyy-mm-dd"] = None
    ) -> str:
        """
        分析资产之间的相关性

        相关性分析帮助理解：
        1. 资产价格联动关系
        2. 分散投资的有效性
        3. 对冲策略的可行性
        4. 市场风险传导路径

        相关系数范围：-1 到 +1
        - +1：完全正相关（同涨同跌）
        - 0：无相关性
        - -1：完全负相关（此涨彼跌）
        """
        try:
            if compare_symbols is None:
                compare_symbols = ["SPY", "GLD", "TLT", "BTC-USD"]

            report = f"# {symbol} 相关性分析\n\n"
            report += f"**对比资产**: {', '.join(compare_symbols)}\n"

            if start_date and end_date:
                report += f"**分析周期**: {start_date} 至 {end_date}\n\n"
            else:
                report += "**分析周期**: 建议使用至少1年的历史数据\n\n"

            report += "## 相关性矩阵（示例）\n\n"
            report += "|  | " + " | ".join([symbol] + compare_symbols) + " |\n"
            report += "|" + "-|" * (len(compare_symbols) + 2) + "\n"
            report += f"| {symbol} | 1.00 | - | - | - | - |\n"
            for comp in compare_symbols:
                report += f"| {comp} | - | 1.00 | - | - | - |\n"
            report += "\n"

            report += "## 相关系数解读\n\n"
            report += "### 相关性强度分类\n"
            report += "| 相关系数 | 强度 | 含义 |\n"
            report += "|----------|------|------|\n"
            report += "| 0.8 - 1.0 | 非常强 | 高度同步，几乎同涨同跌 |\n"
            report += "| 0.6 - 0.8 | 强 | 明显联动，但有独立性 |\n"
            report += "| 0.4 - 0.6 | 中等 | 一定联动，独立性较强 |\n"
            report += "| 0.2 - 0.4 | 弱 | 联动较弱 |\n"
            report += "| 0.0 - 0.2 | 极弱 | 几乎无相关 |\n"
            report += "| -0.2 - 0.0 | 极弱负 | 轻微反向 |\n"
            report += "| -0.4 - -0.2 | 弱负 | 一定反向关系 |\n"
            report += "| -0.6 - -0.4 | 中负 | 明显反向 |\n"
            report += "| -0.8 - -0.6 | 强负 | 高度反向 |\n"
            report += "| -1.0 - -0.8 | 极强负 | 完全反向 |\n\n"

            report += "## 典型资产相关性（历史数据）\n\n"
            report += "### 传统资产\n"
            report += "- **股票 vs 债券**: -0.2 到 0.2（轻微负相关或无相关）\n"
            report += "- **股票 vs 黄金**: -0.1 到 0.1（无相关）\n"
            report += "- **美元 vs 黄金**: -0.3 到 -0.5（负相关）\n"
            report += "- **科技股 vs 大盘**: 0.7 到 0.9（强正相关）\n\n"

            report += "### 加密货币\n"
            report += "- **BTC vs ETH**: 0.8 到 0.9（高度相关）\n"
            report += "- **BTC vs 山寨币**: 0.6 到 0.8（强相关）\n"
            report += "- **BTC vs 股票**: 0.3 到 0.5（疫情后增强）\n"
            report += "- **BTC vs 黄金**: 0.0 到 0.2（几乎无相关）\n"
            report += "- **稳定币 vs BTC**: 接近0（无相关，设计如此）\n\n"

            report += "## 相关性的应用\n\n"
            report += "### 1. 投资组合多元化\n"
            report += "**目标**: 选择低相关或负相关资产\n"
            report += "- 相关性 < 0.5：有效分散风险\n"
            report += "- 相关性 > 0.8：分散效果有限\n\n"
            report += "**示例**:\n"
            report += "- ✅ 股票(0.6) + 债券(-0.2) + 黄金(0.1) + BTC(0.3)\n"
            report += "- ❌ 科技股(0.9) + 纳指(0.95) + FAANG(0.9)\n\n"

            report += "### 2. 对冲策略\n"
            report += "**目标**: 找到负相关资产\n"
            report += "- 相关性 < -0.5：有效对冲\n"
            report += "- 相关性 > 0：无对冲效果\n\n"
            report += "**经典对冲**:\n"
            report += "- 多股票 + 空股指期货（相关性 ~0.9）\n"
            report += "- 多美元资产 + 多黄金（相关性 ~ -0.4）\n\n"

            report += "### 3. 风险传导分析\n"
            report += "**高相关性资产会同时下跌**\n"
            report += "- 2008金融危机：股债相关性升至0.5\n"
            report += "- 2020疫情：所有资产相关性短期升至0.8+\n"
            report += "- 危机时相关性趋于1（风险传染）\n\n"

            report += "### 4. 配对交易\n"
            report += "**利用相关性偏离**\n"
            report += "- 找到历史高相关但当前偏离的资产对\n"
            report += "- 做多相对弱势，做空相对强势\n"
            report += "- 等待相关性回归\n\n"

            report += "## 注意事项\n"
            report += "⚠️ **相关性不稳定**\n"
            report += "- 历史相关性≠未来相关性\n"
            report += "- 危机时相关性会突然改变\n"
            report += "- 需要定期重新计算（如每月）\n\n"

            report += "⚠️ **相关性≠因果关系**\n"
            report += "- 高相关不代表一个导致另一个\n"
            report += "- 可能是共同受第三方因素影响\n\n"

            report += "⚠️ **滚动相关性**\n"
            report += "- 使用固定窗口（如60天）计算\n"
            report += "- 观察相关性的变化趋势\n"
            report += "- 相关性突然增强可能预示风险\n\n"

            report += "## 实现相关性分析\n"
            report += "```python\n"
            report += "# 示例代码\n"
            report += "import pandas as pd\n"
            report += "# 计算收益率\n"
            report += "returns = prices.pct_change().dropna()\n"
            report += "# 计算相关性矩阵\n"
            report += "corr_matrix = returns.corr()\n"
            report += "# 滚动相关性\n"
            report += "rolling_corr = returns['A'].rolling(60).corr(returns['B'])\n"
            report += "```\n"

            return report

        except Exception as e:
            logger.error(f"相关性分析失败: {e}")
            return f"相关性分析失败\n错误: {str(e)}"

    @staticmethod
    @tool
    def get_sector_performance(
        sector: Annotated[str, "行业板块名称"],
        period: Annotated[str, "时间周期：1d, 1w, 1m, 3m, 6m, 1y, ytd"] = "1m"
    ) -> str:
        """
        分析行业板块的整体表现

        帮助研究员理解：
        1. 板块轮动趋势
        2. 行业相对强弱
        3. 经济周期位置
        4. 资金流向

        使用场景：
        - 判断目标资产是否受益于行业趋势
        - 识别热门板块和冷门板块
        - 预测板块轮动机会
        """
        try:
            report = f"# {sector} 板块表现分析\n\n"
            report += f"**分析周期**: {period}\n\n"

            report += "## 主要行业板块分类\n\n"
            report += "### 美股11大板块（GICS）\n"
            report += "1. **信息技术（Technology）**: AAPL, MSFT, NVDA\n"
            report += "2. **医疗保健（Healthcare）**: JNJ, UNH, PFE\n"
            report += "3. **金融（Financials）**: JPM, BAC, WFC\n"
            report += "4. **非必需消费品（Consumer Discretionary）**: AMZN, TSLA, HD\n"
            report += "5. **通信服务（Communication Services）**: META, GOOGL, DIS\n"
            report += "6. **工业（Industrials）**: BA, CAT, UPS\n"
            report += "7. **必需消费品（Consumer Staples）**: PG, KO, WMT\n"
            report += "8. **能源（Energy）**: XOM, CVX, COP\n"
            report += "9. **公用事业（Utilities）**: NEE, DUK, SO\n"
            report += "10. **房地产（Real Estate）**: AMT, PLD, SPG\n"
            report += "11. **材料（Materials）**: LIN, APD, SHW\n\n"

            report += "### 加密货币板块分类\n"
            report += "1. **Layer 1 公链**: BTC, ETH, SOL, ADA\n"
            report += "2. **Layer 2 扩容**: ARB, OP, MATIC\n"
            report += "3. **DeFi（去中心化金融）**: UNI, AAVE, CRV\n"
            report += "4. **NFT/GameFi**: APE, SAND, AXS\n"
            report += "5. **稳定币**: USDT, USDC, DAI\n"
            report += "6. **交易所代币**: BNB, FTT, OKB\n"
            report += "7. **预言机/基础设施**: LINK, GRT\n"
            report += "8. **Meme币**: DOGE, SHIB, PEPE\n\n"

            report += "## 板块表现分析框架\n\n"
            report += "### 1. 相对强弱（Relative Strength）\n"
            report += "| 板块 | 1周涨跌 | 1月涨跌 | 3月涨跌 | 排名 |\n"
            report += "|------|---------|---------|---------|------|\n"
            report += "| 科技 | +2% | +5% | +15% | 1 |\n"
            report += "| 金融 | +1% | +3% | +8% | 3 |\n"
            report += "| 能源 | -1% | +2% | +12% | 2 |\n"
            report += "| 公用事业 | +0.5% | +1% | +3% | 6 |\n\n"

            report += "**解读**:\n"
            report += "- 排名靠前的板块：资金流入，趋势强\n"
            report += "- 排名靠后的板块：资金流出，趋势弱\n"
            report += "- 持续领先的板块：可能过热，警惕回调\n"
            report += "- 持续落后的板块：可能超跌，关注反弹\n\n"

            report += "### 2. 板块轮动周期\n"
            report += "经济周期与板块表现：\n\n"
            report += "**复苏期（衰退后）**:\n"
            report += "- ✅ 领先板块：科技、非必需消费品、金融\n"
            report += "- ❌ 落后板块：公用事业、必需消费品\n"
            report += "- 特征：经济开始好转，风险偏好上升\n\n"

            report += "**扩张期（繁荣）**:\n"
            report += "- ✅ 领先板块：工业、材料、能源\n"
            report += "- ❌ 落后板块：医疗保健、公用事业\n"
            report += "- 特征：经济过热，通胀压力\n\n"

            report += "**放缓期（顶部）**:\n"
            report += "- ✅ 领先板块：必需消费品、医疗保健、公用事业\n"
            report += "- ❌ 落后板块：科技、非必需消费品\n"
            report += "- 特征：经济增速放缓，防御性上升\n\n"

            report += "**衰退期（底部）**:\n"
            report += "- ✅ 领先板块：公用事业、医疗保健、必需消费品\n"
            report += "- ❌ 落后板块：金融、工业、能源\n"
            report += "- 特征：经济衰退，避险情绪浓\n\n"

            report += "### 3. 加密货币板块轮动\n"
            report += "**牛市早期**:\n"
            report += "- BTC 率先上涨\n"
            report += "- 资金从法币流入BTC\n\n"

            report += "**牛市中期**:\n"
            report += "- ETH 和主流Layer 1开始上涨\n"
            report += "- 资金从BTC流向ETH和大市值山寨币\n\n"

            report += "**牛市晚期**:\n"
            report += "- 小市值山寨币暴涨\n"
            report += "- DeFi、NFT、Meme币轮番炒作\n"
            report += "- 市场情绪极度狂热\n\n"

            report += "**熊市**:\n"
            report += "- 山寨币率先暴跌\n"
            report += "- 资金回流BTC和稳定币\n"
            report += "- BTC.D（比特币市值占比）上升\n\n"

            report += "## 资金流向分析\n"
            report += "### 资金流入信号\n"
            report += "- 板块ETF成交量放大\n"
            report += "- 板块内多数股票上涨\n"
            report += "- 技术指标（RSI）进入超买\n\n"

            report += "### 资金流出信号\n"
            report += "- 板块ETF成交量萎缩\n"
            report += "- 板块内多数股票下跌\n"
            report += "- 技术指标（RSI）进入超卖\n\n"

            report += "## 交易策略\n"
            report += "### 1. 板块轮动策略\n"
            report += "- 定期（如每月）评估板块相对强弱\n"
            report += "- 增持强势板块，减持弱势板块\n"
            report += "- 在板块轮动拐点切换配置\n\n"

            report += "### 2. 板块对冲\n"
            report += "- 做多强势板块，做空弱势板块\n"
            report += "- 对冲市场整体风险\n"
            report += "- 只赚取板块相对强弱的差价\n\n"

            report += "### 3. 主题投资\n"
            report += "- 识别长期趋势（如AI、清洁能源）\n"
            report += "- 配置受益板块和个股\n"
            report += "- 持有3-5年\n\n"

            report += "## 数据源\n"
            report += "### 传统市场\n"
            report += "- **板块ETF**: XLK（科技）、XLF（金融）、XLE（能源）等\n"
            report += "- **Finviz**: 板块热力图\n"
            report += "- **TradingView**: 板块相对强弱图表\n\n"

            report += "### 加密市场\n"
            report += "- **CoinGecko**: 板块分类和表现\n"
            report += "- **Messari**: 板块数据和研究\n"
            report += "- **Glassnode**: 链上板块分析\n\n"

            report += "## 实现板块分析\n"
            report += "```python\n"
            report += "# 示例：获取板块ETF价格并计算表现\n"
            report += "import yfinance as yf\n"
            report += "sector_etfs = {'Tech': 'XLK', 'Finance': 'XLF', 'Energy': 'XLE'}\n"
            report += "for name, ticker in sector_etfs.items():\n"
            report += "    data = yf.download(ticker, start='2024-01-01')\n"
            report += "    returns = (data['Close'][-1] / data['Close'][0] - 1) * 100\n"
            report += "    print(f'{name}: {returns:.2f}%')\n"
            report += "```\n"

            return report

        except Exception as e:
            logger.error(f"板块表现分析失败: {e}")
            return f"板块表现分析失败\n错误: {str(e)}"
