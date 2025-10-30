"""
加密货币专用工具集
提供Binance和备用数据源的访问接口
"""
from typing import Annotated, Optional
from langchain_core.tools import tool
from tradingagents.dataflows import crypto_interface
import logging

logger = logging.getLogger(__name__)


class CryptoToolkit:
    """加密货币交易工具集"""
    
    def __init__(self, config: dict):
        self.config = config
        
    @staticmethod
    @tool
    def get_crypto_market_data(
        symbol: Annotated[str, "加密货币交易对，如 BTCUSDT, ETHUSDT"],
        start_date: Annotated[str, "开始日期，格式：yyyy-mm-dd"],
        end_date: Annotated[str, "结束日期，格式：yyyy-mm-dd"],
        interval: Annotated[str, "K线间隔：1m,5m,15m,30m,1h,4h,1d,1w"] = "1h",
        data_source: Annotated[str, "数据源：binance（优先）或 finnhub"] = "binance"
    ) -> str:
        """
        获取加密货币市场数据（OHLCV）
        
        优先从Binance获取实时数据，如果失败则使用Finnhub备用数据源。
        返回包含开盘价、最高价、最低价、收盘价、成交量的数据。
        """
        try:
            if data_source == "binance":
                result = crypto_interface.get_binance_market_data(
                    symbol, start_date, end_date, interval
                )
                # 检查是否是错误报告
                if "执行失败" in result:
                    logger.info("Binance失败，尝试使用Finnhub备用数据源")
                    return crypto_interface.get_finnhub_crypto_data(
                        symbol, start_date, end_date
                    )
                return result
            else:
                return crypto_interface.get_finnhub_crypto_data(
                    symbol, start_date, end_date
                )
        except Exception as e:
            logger.error(f"获取市场数据失败: {e}")
            return f"获取 {symbol} 市场数据失败\n错误: {str(e)}\n\n请检查:\n1. 交易对符号是否正确\n2. 日期范围是否有效\n3. 网络连接是否正常"
    
    @staticmethod
    @tool
    def get_crypto_funding_rate(
        symbol: Annotated[str, "永续合约交易对，如 BTCUSDT"],
        limit: Annotated[int, "返回记录数量"] = 100
    ) -> str:
        """
        获取加密货币永续合约资金费率历史
        
        资金费率是永续合约特有的机制，正值表示多头向空头支付费用，
        负值表示空头向多头支付费用。高资金费率可能预示市场过热。
        """
        return crypto_interface.get_binance_funding_rate(symbol, limit)
    
    @staticmethod
    @tool
    def get_crypto_liquidations(
        symbol: Annotated[str, "交易对，如 BTCUSDT"],
        start_time: Annotated[Optional[str], "开始时间，格式：yyyy-mm-dd HH:MM:SS"] = None,
        end_time: Annotated[Optional[str], "结束时间，格式：yyyy-mm-dd HH:MM:SS"] = None,
        limit: Annotated[int, "返回记录数量"] = 100
    ) -> str:
        """
        获取加密货币清算数据
        
        清算数据反映了市场的杠杆水平和风险状况。
        大量清算可能导致价格剧烈波动。
        """
        return crypto_interface.get_binance_liquidations(
            symbol, start_time, end_time, limit
        )
    
    @staticmethod
    @tool
    def get_crypto_orderbook_depth(
        symbol: Annotated[str, "交易对，如 BTCUSDT"],
        limit: Annotated[int, "深度档位：5,10,20,50,100,500,1000,5000"] = 20
    ) -> str:
        """
        获取加密货币订单簿深度数据
        
        显示买卖盘的深度信息，帮助分析：
        - 支撑和阻力位
        - 市场流动性
        - 大单分布（鲸鱼活动）
        """
        return crypto_interface.get_binance_orderbook(symbol, limit)
    
    @staticmethod
    @tool
    def get_crypto_open_interest(
        symbol: Annotated[str, "期货交易对，如 BTCUSDT"],
        period: Annotated[str, "时间周期：5m,15m,30m,1h,2h,4h,6h,12h,1d"] = "1h",
        limit: Annotated[int, "返回记录数量"] = 30
    ) -> str:
        """
        获取加密货币期货持仓量数据
        
        持仓量（Open Interest）反映市场参与度和趋势强度：
        - 上升趋势+持仓量增加 = 趋势延续
        - 上升趋势+持仓量减少 = 趋势可能反转
        """
        return crypto_interface.get_binance_open_interest(symbol, period, limit)
    
    @staticmethod
    @tool
    def get_crypto_long_short_ratio(
        symbol: Annotated[str, "交易对，如 BTCUSDT"],
        period: Annotated[str, "时间周期：5m,15m,30m,1h,2h,4h,6h,12h,1d"] = "1h",
        limit: Annotated[int, "返回记录数量"] = 30
    ) -> str:
        """
        获取加密货币多空比数据
        
        显示市场参与者的多空持仓比例：
        - 比值 > 1：多头占优
        - 比值 < 1：空头占优
        - 极端值可能预示反转
        """
        return crypto_interface.get_binance_long_short_ratio(symbol, period, limit)
    
    @staticmethod
    @tool
    def get_crypto_technical_indicators(
        symbol: Annotated[str, "交易对，如 BTCUSDT"],
        interval: Annotated[str, "K线间隔：15m,30m,1h,4h,1d"] = "1h",
        indicators: Annotated[list[str], "指标列表：rsi,macd,boll,ema,volume_profile"] = None,
        start_date: Annotated[str, "开始日期（格式：YYYY-MM-DD），可选"] = None,
        end_date: Annotated[str, "结束日期（格式：YYYY-MM-DD），可选"] = None
    ) -> str:
        """
        获取加密货币技术指标分析
        
        专为加密货币优化的技术指标：
        - RSI：相对强弱指数（加密货币版本使用14周期）
        - MACD：异同移动平均线（适配24/7交易）
        - Bollinger Bands：布林带（使用20周期，2倍标准差）
        - EMA：指数移动平均线（9/21/55/200）
        - Volume Profile：成交量分布
        
        注意：如果不提供日期参数，将使用最近60天的数据来计算指标
        """
        if indicators is None:
            indicators = ["rsi", "macd", "boll", "volume_profile"]
        
        return crypto_interface.get_crypto_technical_analysis(
            symbol, interval, indicators, start_date, end_date
        )
    
    @staticmethod
    @tool
    def get_crypto_whale_trades(
        symbol: Annotated[str, "交易对，如 BTCUSDT"],
        min_amount: Annotated[float, "最小交易金额（USDT）"] = 100000,
        limit: Annotated[int, "返回记录数量"] = 50
    ) -> str:
        """
        获取加密货币大额交易（鲸鱼交易）
        
        追踪大额交易活动：
        - 大额买入：可能推动价格上涨
        - 大额卖出：可能造成价格压力
        - 异常大单：可能是市场操纵或机构活动
        """
        return crypto_interface.get_binance_whale_trades(symbol, min_amount, limit)
    
    @staticmethod
    @tool
    def get_crypto_market_sentiment(
        symbol: Annotated[str, "交易对，如 BTCUSDT"],
        source: Annotated[str, "数据源：fear_greed, social, funding"] = "fear_greed"
    ) -> str:
        """
        获取加密货币市场情绪指标

        多维度情绪分析：
        - fear_greed：恐惧贪婪指数（0-100）
        - social：社交媒体情绪
        - funding：资金费率情绪
        """
        return crypto_interface.get_crypto_sentiment(symbol, source)

    @staticmethod
    @tool
    def get_crypto_onchain_metrics(
        symbol: Annotated[str, "加密货币符号，如 BTC, ETH"],
        metrics: Annotated[list[str], "指标列表：active_addresses, transactions, tvl, whale_activity"] = None
    ) -> str:
        """
        获取加密货币链上指标

        提供区块链网络活动的关键指标：
        - active_addresses：活跃地址数（网络参与度）
        - transactions：链上交易数量（网络使用情况）
        - tvl：总锁仓量（DeFi项目）
        - whale_activity：大户地址活动（大额转账）

        这些指标帮助评估：
        1. 网络健康度和增长
        2. 实际使用情况 vs 投机
        3. 机构和鲸鱼的行为模式
        """
        if metrics is None:
            metrics = ["active_addresses", "transactions", "tvl", "whale_activity"]

        try:
            # 清理符号格式（移除USDT等后缀）
            clean_symbol = symbol.replace("USDT", "").replace("USD", "").replace("-", "")

            # 这里应该调用链上数据API（如Glassnode, Dune Analytics）
            # 由于API key限制，提供基础分析框架

            report = f"# {clean_symbol} 链上指标分析\n\n"
            report += "**注意**：当前为基础分析模式。完整链上数据需要配置Glassnode或Dune Analytics API。\n\n"

            for metric in metrics:
                if metric == "active_addresses":
                    report += "## 活跃地址数\n"
                    report += "- **指标说明**：每日唯一活跃地址数量，反映网络参与度\n"
                    report += "- **分析建议**：活跃地址持续增长表明生态健康；突然激增可能预示价格波动\n"
                    report += "- **数据源**：需要 Glassnode API 或链浏览器数据\n\n"

                elif metric == "transactions":
                    report += "## 链上交易量\n"
                    report += "- **指标说明**：每日交易笔数，反映网络使用强度\n"
                    report += "- **分析建议**：高交易量 + 低手续费 = 健康网络；高交易量 + 高手续费 = 可能拥堵\n"
                    report += "- **数据源**：需要区块链浏览器API\n\n"

                elif metric == "tvl":
                    report += "## 总锁仓量（TVL）\n"
                    report += "- **指标说明**：DeFi协议中锁定的资产总价值\n"
                    report += "- **分析建议**：TVL增长表明生态繁荣；TVL/市值比衡量估值合理性\n"
                    report += "- **数据源**：需要 DeFiLlama API\n\n"

                elif metric == "whale_activity":
                    report += "## 大户地址活动\n"
                    report += "- **指标说明**：持有大量代币的地址的转账活动\n"
                    report += "- **分析建议**：大户集中买入看涨；大户分散卖出看跌\n"
                    report += "- **数据源**：需要 Whale Alert API 或链分析工具\n\n"

            report += "\n## 配置链上数据源\n"
            report += "要启用完整链上分析，请在环境变量中配置：\n"
            report += "- `GLASSNODE_API_KEY` - Glassnode 网络指标\n"
            report += "- `DUNE_API_KEY` - Dune Analytics 自定义查询\n"
            report += "- `DEFILLAMA_API_KEY` - DeFiLlama TVL数据\n"

            return report

        except Exception as e:
            logger.error(f"获取链上指标失败: {e}")
            return f"获取 {symbol} 链上指标失败\n错误: {str(e)}"

    @staticmethod
    @tool
    def get_crypto_tokenomics(
        symbol: Annotated[str, "加密货币符号，如 BTC, ETH"],
        analysis_type: Annotated[str, "分析类型：supply, distribution, inflation, unlock"] = "supply"
    ) -> str:
        """
        获取加密货币代币经济学分析

        分析代币的经济模型和供应机制：
        - supply：供应量分析（总量、流通量、销毁机制）
        - distribution：代币分配（团队、投资者、社区、基金会）
        - inflation：通胀率分析（增发速度、减半机制）
        - unlock：解锁计划（锁仓期、释放时间表）

        代币经济学直接影响价格：
        1. 稀缺性 vs 通胀压力
        2. 供应集中度（集中=高风险）
        3. 未来供应增加（解锁=抛压）
        """
        try:
            clean_symbol = symbol.replace("USDT", "").replace("USD", "").replace("-", "")

            report = f"# {clean_symbol} 代币经济学分析\n\n"

            # 提供一些知名币种的基础信息
            known_tokenomics = {
                "BTC": {
                    "total_supply": "2100万",
                    "circulating": "1960万",
                    "inflation_type": "递减（减半机制）",
                    "next_halving": "2024年4月",
                    "distribution": "完全由挖矿产生，无预挖",
                },
                "ETH": {
                    "total_supply": "无上限（EIP-1559后通缩）",
                    "circulating": "1.2亿",
                    "inflation_type": "动态（Staking奖励 - 燃烧）",
                    "mechanism": "EIP-1559燃烧机制",
                    "distribution": "预挖7200万（团队、基金会、众筹）",
                },
                "BNB": {
                    "total_supply": "最初2亿（持续销毁至1亿）",
                    "circulating": "1.5亿",
                    "inflation_type": "通缩（季度销毁）",
                    "distribution": "50% ICO，40% 团队，10% 天使投资",
                },
            }

            if clean_symbol in known_tokenomics:
                info = known_tokenomics[clean_symbol]

                if analysis_type == "supply":
                    report += "## 供应量分析\n"
                    report += f"- **总供应量**：{info.get('total_supply', '未知')}\n"
                    report += f"- **流通量**：{info.get('circulating', '未知')}\n"
                    report += f"- **供应机制**：{info.get('mechanism', info.get('inflation_type', '未知'))}\n\n"

                elif analysis_type == "inflation":
                    report += "## 通胀/通缩分析\n"
                    report += f"- **类型**：{info.get('inflation_type', '未知')}\n"
                    if "next_halving" in info:
                        report += f"- **下次减半**：{info['next_halving']}\n"
                    if "mechanism" in info:
                        report += f"- **机制**：{info['mechanism']}\n"
                    report += "\n"

                elif analysis_type == "distribution":
                    report += "## 代币分配\n"
                    report += f"- **初始分配**：{info.get('distribution', '未知')}\n\n"

                elif analysis_type == "unlock":
                    report += "## 解锁计划\n"
                    report += "- **注意**：详细解锁计划需要查询项目白皮书或Token Unlocks网站\n\n"

            else:
                report += f"**注意**：{clean_symbol} 的详细代币经济学信息需要查询：\n"
                report += "1. 项目官方白皮书\n"
                report += "2. CoinGecko / CoinMarketCap 代币信息\n"
                report += "3. Token Unlocks 网站（解锁计划）\n"
                report += "4. Messari Crypto 研究报告\n\n"

            report += "\n## 代币经济学评估框架\n"
            report += "### 供应侧分析\n"
            report += "- ✅ **通缩机制**（销毁、燃烧）= 长期看涨\n"
            report += "- ⚠️ **高通胀率** > 5% = 卖压风险\n"
            report += "- ❌ **大额解锁**即将到来 = 短期看跌\n\n"

            report += "### 分配分析\n"
            report += "- ✅ **分散分配**（社区 > 50%）= 去中心化\n"
            report += "- ⚠️ **团队持币** 20-40% = 中等风险\n"
            report += "- ❌ **高度集中** > 50%给少数地址 = 高风险\n"

            return report

        except Exception as e:
            logger.error(f"获取代币经济学失败: {e}")
            return f"获取 {symbol} 代币经济学失败\n错误: {str(e)}"

    @staticmethod
    @tool
    def get_crypto_development_metrics(
        symbol: Annotated[str, "加密货币符号，如 BTC, ETH"],
        repo_url: Annotated[str, "GitHub仓库URL（可选）"] = None
    ) -> str:
        """
        获取加密货币项目开发活跃度指标

        通过GitHub活动评估项目健康度：
        - 代码提交频率（commits）
        - 活跃开发者数量（contributors）
        - 代码更新频率（releases）
        - 社区参与度（stars, forks, issues）

        开发活跃度是基本面分析的重要指标：
        1. 持续开发 = 项目有生命力
        2. 开发者流失 = 项目可能衰退
        3. 高频更新 = 技术进步快
        """
        try:
            clean_symbol = symbol.replace("USDT", "").replace("USD", "").replace("-", "")

            report = f"# {clean_symbol} 开发活跃度分析\n\n"

            # 提供一些主流项目的GitHub信息
            known_repos = {
                "BTC": "bitcoin/bitcoin",
                "ETH": "ethereum/go-ethereum",
                "BNB": "bnb-chain/bsc",
                "SOL": "solana-labs/solana",
                "ADA": "IntersectMBO/cardano-node",
                "DOGE": "dogecoin/dogecoin",
                "DOT": "paritytech/polkadot",
            }

            repo = known_repos.get(clean_symbol, repo_url)

            if repo:
                report += f"## GitHub 仓库：`{repo}`\n\n"
                report += "**注意**：实时GitHub数据需要配置 `GITHUB_API_KEY`\n\n"

                report += "### 关键指标\n"
                report += "- **代码提交**：最近30天的commit数量\n"
                report += "- **活跃贡献者**：最近90天有贡献的开发者\n"
                report += "- **发布频率**：新版本发布的时间间隔\n"
                report += "- **社区参与**：Stars, Forks, Open Issues\n\n"

                report += "### 分析建议\n"
                report += "#### 健康项目特征：\n"
                report += "- ✅ 每周 > 10 commits\n"
                report += "- ✅ 活跃开发者 > 20人\n"
                report += "- ✅ 3-6个月一次主要版本\n"
                report += "- ✅ Issue响应时间 < 7天\n\n"

                report += "#### 警告信号：\n"
                report += "- ⚠️ 连续1个月无commits\n"
                report += "- ⚠️ 核心开发者减少 > 50%\n"
                report += "- ❌ 连续6个月无更新\n"
                report += "- ❌ 大量未解决的严重bug\n\n"

                report += f"### 查询实时数据\n"
                report += f"- GitHub: https://github.com/{repo}\n"
                report += f"- Insights: https://github.com/{repo}/graphs/contributors\n"
                report += f"- Releases: https://github.com/{repo}/releases\n"
            else:
                report += f"**未找到 {clean_symbol} 的GitHub仓库信息**\n\n"
                report += "请手动查询：\n"
                report += "1. CoinGecko 项目页面的 \"Links\" 部分\n"
                report += "2. 项目官网寻找 GitHub 链接\n"
                report += "3. Electric Capital 开发者报告\n"

            report += "\n## 配置开发指标数据源\n"
            report += "要启用实时GitHub分析，请配置：\n"
            report += "- `GITHUB_API_KEY` - GitHub Personal Access Token\n"
            report += "- 或使用 Electric Capital Developer Report API\n"

            return report

        except Exception as e:
            logger.error(f"获取开发指标失败: {e}")
            return f"获取 {symbol} 开发指标失败\n错误: {str(e)}"