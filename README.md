# 🤖 交易智能体 - 多智能体金融分析系统

![文本链接](https://static.comunicae.com/photos/notas/1247100/mejor-robot-de-forex-1024x536.jpg)

一个先进的金融分析系统，利用多个专业化 AI 智能体提供全面的分析和明智的投资决策。支持**加密货币**、**股票**和**指数**。

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)](https://streamlit.io/)
[![OpenAI](https://img.shields.io/badge/powered%20by-OpenAI-green.svg)](https://openai.com/)

## ✨ 主要特性

### 🧠 **多智能体集体智慧**
- **市场分析师**：使用专业指标（RSI、MACD、布林带）进行技术分析
- **新闻分析师**：处理金融新闻和宏观经济环境
- **社交媒体分析师**：分析 Reddit 和社交平台的市场情绪
- **基本面分析师**：财务报表、估值指标和企业健康指标

### 🥊 **辩论与共识系统**
- **看涨 vs 看跌研究员**：乐观与悲观观点的论证辩论
- **研究经理**：评估辩论并综合建议
- **风险管理团队**：三个层级的分析（激进、保守、中立）
- **风险裁判**：基于所有分析的最终平衡决策

### 🎯 **按资产类型智能适配**
- **加密货币**（BTC-USD、ETH-USD）：代币经济学、区块链采用度、网络分析
- **股票**（AAPL、TSLA、NVDA）：完整基本面分析、竞争分析、估值
- **指数**（SPY、QQQ、VTI）：行业分析、货币政策、机构资金流

### 🧠 **记忆与学习**
- 智能体从过往决策中学习
- 使用 ChromaDB 的持久记忆系统
- 基于历史经验的持续改进

## 🚀 安装与配置

### 先决条件
- Python 3.10+
- Anaconda/Miniconda（推荐）
- API 密钥：[OpenAI](https://platform.openai.com/) 和 [Finnhub](https://finnhub.io/)

### 1. 克隆仓库
```bash
git clone https://github.com/your-username/trading-agents.git
cd trading-agents
```

### 2. 创建虚拟环境
```bash
conda create -n trading-agents python=3.11
conda activate trading-agents
```

### 3. 安装依赖
```bash
pip install -r requirements.txt
```

### 4. 配置环境变量
在项目根目录创建 `.env` 文件：
```bash
# .env
OPENAI_API_KEY=你的_openai_密钥
FINNHUB_API_KEY=你的_finnhub_密钥

# 可选：自定义后端 URL 和嵌入配置
TRADINGAGENTS_BACKEND_URL=https://api.siliconflow.cn/v1
TRADINGAGENTS_EMBEDDING_URL=https://api.siliconflow.cn/v1
TRADINGAGENTS_EMBEDDING_MODEL=BAAI/bge-m3
TRADINGAGENTS_EMBEDDING_API_KEY=你的_embedding_api_密钥
```

### 5. 运行应用
```bash
streamlit run app.py
```

应用会自动在浏览器中打开，地址为 `http://localhost:8501`

## 🎮 使用方法

### Web 界面（Streamlit）
1. **配置 API**：密钥会自动从 `.env` 加载
2. **选择资产**：选择类别（加密货币、股票、指数）和具体代码
3. **配置分析**：
   - 单一或多资产模式
   - 分析日期
   - LLM 模型（GPT-4 等）
4. **执行分析**：点击"🚀 分析市场"
5. **查看结果**：最终决策 + 可展开的详细报告
6. **加载历史结果**：支持上传或从保存目录选择历史分析结果

### 命令行（CLI）
```bash
python cli/main.py --ticker BTC-USD --date 2024-01-15
```

## 📊 使用示例

### 加密货币分析
```python
# 分析比特币，关注代币经济学和采用度
ticker = "BTC-USD"
# 活跃智能体：市场、新闻、社交（无基本面）
```

### 股票分析
```python
# 分析苹果公司，进行完整基本面分析
ticker = "AAPL"  
# 活跃智能体：市场、新闻、社交、基本面
```

### 指数分析
```python
# 分析标普 500，关注宏观因素
ticker = "SPY"
# 活跃智能体：市场、新闻（简化）
```

## 🏗️ 系统架构

```
📦 tradingagents/
├── 🧠 agents/           # 专业化智能体
│   ├── analysts/        # 市场分析师
│   ├── researchers/     # 看涨/看跌研究员
│   ├── managers/        # 经理和裁判
│   └── risk_mgmt/       # 风险管理
├── 📊 dataflows/        # 数据连接器
├── 🔄 graph/           # 智能体间流程逻辑
└── ⚙️ utils/           # 工具和配置
```

## 🛠️ 自定义配置

### 修改智能体
提示词和行为可在以下位置调整：
- `tradingagents/agents/` - 每个智能体都有特定文件
- `tradingagents/default_config.py` - 全局配置

### 添加新指标
- 扩展 `tradingagents/dataflows/stockstats_utils.py`
- 修改 `tradingagents/agents/utils/agent_utils.py` 中的工具

### 更改 LLM 模型
```python
config = {
    "llm_provider": "openai",  # 或 "anthropic", "google"
    "deep_think_llm": "gpt-4",
    "quick_think_llm": "gpt-4-mini"
}
```

## 🤝 贡献

1. Fork 项目
2. 创建功能分支（`git checkout -b feature/AmazingFeature`）
3. 提交更改（`git commit -m 'Add some AmazingFeature'`）
4. 推送到分支（`git push origin feature/AmazingFeature`）
5. 开启 Pull Request

## 📄 许可证

本项目采用 MIT 许可证。详情见 [LICENSE](LICENSE) 文件。

## ⚠️ 免责声明

本软件仅供教育和研究目的使用。**不构成财务建议**。投资决策应基于您自己的研究和分析。创建者不对财务损失负责。

## 🙏 致谢

- 基于 [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) 框架
- 由 [OpenAI GPT 模型](https://openai.com/) 提供支持
- 金融数据来自 [Finnhub](https://finnhub.io/) 和 [Yahoo Finance](https://finance.yahoo.com/)

---
**⭐ 如果这个项目对您有帮助，请在 GitHub 上给个星标！**