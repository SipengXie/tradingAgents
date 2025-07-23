import os

DEFAULT_CONFIG = {
    "project_dir": os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
    "results_dir": os.getenv("TRADINGAGENTS_RESULTS_DIR", "./results"),
    "data_dir": "./data",
    "data_cache_dir": os.path.join(
        os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
        "dataflows/data_cache",
    ),
    # LLM settings
    "llm_provider": "openai",
    "deep_think_llm": "openai/gpt-4.1",
    "quick_think_llm": "openai/gpt-4.1-mini",
    "backend_url": os.getenv("TRADINGAGENTS_BACKEND_URL", "https://openrouter.ai/api/v1"),
    # Embedding settings
    "embedding_url": os.getenv("TRADINGAGENTS_EMBEDDING_URL", "https://api.siliconflow.cn/v1"),
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
