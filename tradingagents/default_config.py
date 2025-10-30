import os
import logging
from urllib.parse import urlparse
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

logger = logging.getLogger(__name__)


def validate_url(url: str, allowed_schemes=None, allowed_domains=None) -> bool:
    """
    验证URL的安全性

    Args:
        url: 要验证的URL
        allowed_schemes: 允许的协议列表（默认只允许https）
        allowed_domains: 允许的域名列表（默认为空表示允许所有）

    Returns:
        bool: URL是否安全
    """
    if not url or not isinstance(url, str):
        return False

    if allowed_schemes is None:
        allowed_schemes = ['https']

    try:
        result = urlparse(url)

        # 检查协议
        if result.scheme not in allowed_schemes:
            logger.warning(f"URL scheme '{result.scheme}' not in allowed schemes {allowed_schemes}: {url}")
            return False

        # 检查是否有主机名
        if not result.netloc:
            logger.warning(f"URL missing netloc: {url}")
            return False

        # 如果指定了允许的域名，进行检查
        if allowed_domains:
            if not any(domain in result.netloc for domain in allowed_domains):
                logger.warning(f"URL domain '{result.netloc}' not in allowed domains {allowed_domains}: {url}")
                return False

        return True

    except Exception as e:
        logger.error(f"URL validation failed for '{url}': {e}")
        return False


def get_safe_url(env_var: str, default_url: str, allowed_domains=None) -> str:
    """
    从环境变量安全地获取URL，如果验证失败则使用默认值

    Args:
        env_var: 环境变量名
        default_url: 默认URL
        allowed_domains: 允许的域名列表

    Returns:
        str: 验证通过的URL
    """
    url = os.getenv(env_var, default_url)

    # 对于localhost和开发环境，允许http
    is_localhost = 'localhost' in url or '127.0.0.1' in url
    allowed_schemes = ['https', 'http'] if is_localhost else ['https']

    if validate_url(url, allowed_schemes=allowed_schemes, allowed_domains=allowed_domains):
        return url
    else:
        logger.warning(f"Invalid URL from {env_var}: {url}, using default: {default_url}")
        return default_url


# 定义允许的API域名白名单
ALLOWED_API_DOMAINS = [
    'openrouter.ai',
    'api.openai.com',
    'api.anthropic.com',
    'generativelanguage.googleapis.com',
    'api.siliconflow.cn',
    'api.deepseek.com',
    'localhost',
    '127.0.0.1'
]

DEFAULT_CONFIG = {
    "project_dir": os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
    "results_dir": os.getenv("TRADINGAGENTS_RESULTS_DIR", "./results"),
    "data_dir": "./data",
    "data_cache_dir": os.path.join(
        os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
        "dataflows/data_cache",
    ),
    # Memory persistence settings
    "memory_persist_dir": os.path.join(
        os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
        "memory_db",
    ),
    # LLM settings
    "llm_provider": "openai",
    "deep_think_llm": "deepseek/deepseek-v3.2-exp",
    "quick_think_llm": "google/gemini-2.5-flash",
    "backend_url": get_safe_url(
        "TRADINGAGENTS_BACKEND_URL",
        "https://openrouter.ai/api/v1",
        ALLOWED_API_DOMAINS
    ),
    # Embedding settings
    "embedding_url": get_safe_url(
        "TRADINGAGENTS_EMBEDDING_URL",
        "https://api.siliconflow.cn/v1",
        ALLOWED_API_DOMAINS
    ),
    "embedding_model": os.getenv("TRADINGAGENTS_EMBEDDING_MODEL", "BAAI/bge-m3"),
    "embedding_api_key": os.getenv("TRADINGAGENTS_EMBEDDING_API_KEY", os.getenv("TRADINGAGENTS_API_KEY")),
    # Debate and discussion settings
    "max_debate_rounds": 1,
    "max_risk_discuss_rounds": 1,
    "max_recur_limit": 100,
    # Tool settings
    "online_tools": True,
    # Language settings
    "language": "chinese",
    "language_instruction": "重要提示：务必始终使用中文回答。所有分析、报告和决策都应使用中文。"
}
