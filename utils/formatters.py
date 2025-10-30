"""
格式化工具
提供各种数据格式化功能
"""

from datetime import datetime
from config.ui_constants import DATE_FORMAT


def format_file_size(size_bytes: int) -> str:
    """
    格式化文件大小为人类可读格式

    Args:
        size_bytes: 文件大小（字节）

    Returns:
        格式化后的字符串（如 "1.5 MB"）
    """
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    else:
        return f"{size_bytes / (1024 * 1024):.1f} MB"


def format_decision_summary(log_data: dict) -> str:
    """
    生成决策摘要

    Args:
        log_data: 决策日志数据

    Returns:
        决策摘要字符串
    """
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


def parse_date(date_str: str) -> datetime:
    """
    解析日期字符串为 datetime 对象

    Args:
        date_str: 日期字符串（格式：YYYY-MM-DD）

    Returns:
        datetime 对象，解析失败则返回最小日期
    """
    try:
        return datetime.strptime(date_str, DATE_FORMAT)
    except Exception:
        return datetime.min
