# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

TradingAgents-Pro 是一个多智能体金融分析系统，用于分析和预测金融市场走势。系统使用 LangChain 和 LangGraph 框架构建，支持加密货币、股票和指数的综合分析。

## 开发环境设置

### 依赖安装
```bash
# 使用 pip 安装
pip install -r requirements.txt

# 或使用 uv（推荐）
uv pip install -r requirements.txt
```

### 环境变量配置
```bash
# 复制示例文件
cp .env.example .env

# 编辑 .env 文件，配置必要的 API 密钥
# 必需：OPENAI_API_KEY 或其他 LLM 提供商的密钥
# 可选：FINNHUB_API_KEY（用于基本面数据）
```

## 常用命令

### 运行应用
```bash
# Web 界面（Streamlit）
streamlit run app.py

# CLI 界面
python cli/main.py --ticker BTC-USD --date 2024-01-15

# 直接运行主程序
python main.py
```

### 开发测试
```bash
# 运行单个智能体分析（示例）
python -c "from tradingagents.agents.analysts.market_analyst import create_market_analyst; analyst = create_market_analyst(); print(analyst.invoke({'ticker': 'BTC-USD', 'date': '2024-01-15'}))"

# 测试数据获取
python -c "from tradingagents.dataflows.ticker_utils import get_ticker_data; print(get_ticker_data('BTC-USD', '2024-01-15'))"

# 运行测试（根据 CONTRIBUTING.md）
pytest tests/

# 代码格式化
black tradingagents/
flake8 tradingagents/

# Debug 模式运行
streamlit run app.py --logger.level=debug
```

## 架构说明

### 核心组件
1. **agents/** - 智能体实现
   - analysts/ - 分析师智能体（市场、新闻、社交媒体、基本面）
   - researchers/ - 研究员智能体（看涨、看跌观点）
   - managers/ - 管理者智能体（研究经理、风险经理）
   - risk_mgmt/ - 风险管理智能体（激进、保守、中立策略）
   - trader/ - 交易员智能体（最终决策）

2. **graph/** - 工作流定义
   - trading_graph.py - 主要的多智能体协作流程
   - conditional_logic.py - 条件逻辑处理
   - propagation.py - 状态传播机制
   - reflection.py - 反思学习机制
   - signal_processing.py - 信号处理逻辑

3. **dataflows/** - 数据处理
   - ticker_utils.py - 资产数据获取（yfinance）
   - finnhub_utils.py - Finnhub 新闻数据
   - googlenews_utils.py - Google 新闻数据
   - reddit_utils.py - Reddit 社交媒体数据
   - binance_utils.py - 币安交易数据
   - crypto_interface.py - 加密货币接口
   - data_cache/ - 数据缓存机制

4. **utils/** - 工具集
   - agent_utils.py - 智能体工具函数
   - agent_states.py - 状态管理
   - memory.py - ChromaDB 记忆系统
   - crypto_utils.py - 加密货币工具
   - paradex_tools.py - Paradex 交易工具

### 工作流程
1. 数据收集：从多个数据源获取市场数据、新闻、社交媒体信息
2. 并行分析：多个分析师智能体同时工作
3. 研究辩论：看涨/看跌研究员基于分析进行辩论
4. 风险评估：风险管理团队从不同角度评估风险
5. 最终决策：交易员综合所有信息做出决策

## 关键配置

### LLM 配置（tradingagents/default_config.py）
```python
# 支持的 LLM 提供商
LLM_PROVIDER = "openai"  # 可选：openai, anthropic, google, ollama, openai_compatible

# 模型设置
deep_think_llm = "x-ai/grok-4"  # 深度思考模型
quick_think_llm = "google/gemini-2.5-flash"  # 快速响应模型

# OpenRouter 后端（默认）
backend_url = "https://openrouter.ai/api/v1"

# 嵌入模型配置
embedding_url = "https://api.siliconflow.cn/v1"
embedding_model = "BAAI/bge-m3"

# 系统语言
LANGUAGE = "chinese"  # 所有分析和报告使用中文
```

### 智能体参数
```python
# 辩论轮数
max_debate_rounds = 1  # 研究员辩论轮次
max_risk_discuss_rounds = 1  # 风险管理讨论轮次

# 记忆系统
memory_persist_dir = "tradingagents/memory_db"  # ChromaDB 持久化目录
```

### 数据源优先级
系统会按以下优先级尝试获取数据：
1. 币安 API（加密货币）
2. Yahoo Finance
3. 本地缓存数据

## 交易集成

### Paradex 交易
```python
# 查看 Paradex 成交记录
python scripts/paradex_fills.py

# 测试 Paradex 交易功能
python scripts/test_paradex_trader.py
```

### 支持的交易所
- Binance（现货交易）
- Paradex（衍生品交易）

## 注意事项

1. **API 密钥管理**：永远不要将 API 密钥提交到版本控制
2. **数据缓存**：系统会自动缓存数据以减少 API 调用
3. **中文输出**：系统配置为中文输出，所有智能体响应都应使用中文
4. **错误处理**：数据获取失败时会使用备用数据源或返回默认值
5. **资产类型识别**：系统会自动识别加密货币、股票或指数并调整分析策略
6. **内存管理**：ChromaDB 会持久化智能体记忆，可通过删除 memory_db 目录清空
7. **模型选择**：可通过环境变量或配置文件切换不同的 LLM 提供商和模型