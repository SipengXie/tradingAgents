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

3. **dataflows/** - 数据处理
   - ticker_utils.py - 资产数据获取（yfinance）
   - news_utils.py - 新闻数据获取（finnhub）
   - data_cache/ - 数据缓存机制

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
LLM_MODEL = "gpt-4o-mini"
TEMPERATURE = 0.0

# 系统语言
LANGUAGE = "Chinese"  # 所有分析和报告使用中文
```

### 智能体参数
```python
# 辩论轮数
DEBATE_ROUNDS = 3  # 研究员辩论轮次
DISCUSSION_ROUNDS = 3  # 风险管理讨论轮次

# 记忆系统
ENABLE_MEMORY = True  # 使用 ChromaDB 持久化记忆
```

## 注意事项

1. **API 密钥管理**：永远不要将 API 密钥提交到版本控制
2. **数据缓存**：系统会自动缓存数据以减少 API 调用
3. **中文输出**：系统配置为中文输出，所有智能体响应都应使用中文
4. **错误处理**：数据获取失败时会使用备用数据源或返回默认值
5. **资产类型识别**：系统会自动识别加密货币、股票或指数并调整分析策略