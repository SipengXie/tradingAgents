"""
UI 常量配置
包含所有 UI 相关的常量定义，如组件配置、资产列表等
"""

# 组件配置字典 - 用于学习结果展示
COMPONENT_CONFIG = {
    'BULL_RESEARCHER': {'icon': '🐂', 'name': '看涨研究员'},
    'BEAR_RESEARCHER': {'icon': '🐻', 'name': '看跌研究员'},
    'TRADER': {'icon': '💼', 'name': '交易员'},
    'INVEST_JUDGE': {'icon': '⚖️', 'name': '投资判官'},
    'RISK_MANAGER': {'icon': '🛡️', 'name': '风险管理员'}
}

# 各资产类别的热门资产列表
POPULAR_ASSETS = {
    "加密货币": ["BTC-USD", "ETH-USD", "ADA-USD", "SOL-USD", "MATIC-USD", "DOT-USD", "AVAX-USD", "LINK-USD"],
    "科技股": ["AAPL", "GOOGL", "MSFT", "TSLA", "NVDA", "META", "AMZN", "NFLX"],
    "蓝筹股": ["JPM", "JNJ", "KO", "PG", "WMT", "V", "MA", "DIS"],
    "指数": ["SPY", "QQQ", "IWM", "VTI", "GLD", "TLT", "VIX", "DXY"],
    "自定义": []
}

# 日期格式
DATE_FORMAT = "%Y-%m-%d"
