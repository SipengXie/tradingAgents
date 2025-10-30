"""
日志解析器
提供决策日志的解析和提取功能
"""

import re


def extract_risk(text: str) -> str | None:
    """
    从文本中提取风险管理相关内容

    Args:
        text: 原始文本

    Returns:
        提取的风险管理内容，未找到则返回 None
    """
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


def extract_proposal(text: str) -> str | None:
    """
    从文本中提取交易提案

    Args:
        text: 原始文本

    Returns:
        提取的交易提案，未找到则返回 None
    """
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
