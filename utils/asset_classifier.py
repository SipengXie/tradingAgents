"""
资产分类器
识别资产类型并返回相应的分析师配置
"""


class AssetClassifier:
    """资产类型识别和分析师配置"""

    @staticmethod
    def detect_asset_type(ticker: str) -> str:
        """
        检测资产类型

        Args:
            ticker: 资产代码

        Returns:
            资产类型：'crypto', 'index', 或 'stock'
        """
        if ticker.endswith("-USD") or ticker.endswith("-EUR") or ticker.endswith("-USDT"):
            return "crypto"
        elif ticker in ["SPY", "QQQ", "IWM", "VTI", "GLD", "TLT", "VIX", "DXY"]:
            return "index"
        else:
            return "stock"

    @staticmethod
    def get_analysts_for_asset(asset_type: str) -> list[str]:
        """
        根据资产类型获取需要的分析师列表

        Args:
            asset_type: 资产类型

        Returns:
            分析师代码列表
        """
        if asset_type == "crypto":
            # 加密货币不需要基本面分析
            return ["market", "social", "news"]
        elif asset_type == "index":
            # 指数不需要社交和基本面分析
            return ["market", "news"]
        else:
            # 股票需要完整分析
            return ["market", "social", "news", "fundamentals"]
