# OpenRouter Web Search 集成说明

## 概述

本项目已经改进了新闻获取功能，支持 OpenRouter 的 Web Search API。系统会自动检测 backend URL 并选择合适的 API 调用方式。

## 工作原理

### 自动检测机制

当 `backend_url` 包含 "openrouter" 时，系统会自动使用 OpenRouter 的 Web Search 格式：

1. **首选方案**：使用 `:online` 后缀
   ```python
   model = "openai/gpt-4o-mini:online"
   ```

2. **备选方案**：使用 `plugins` 参数
   ```python
   extra_body = {
       "plugins": [{"id": "web", "max_results": 5}]
   }
   ```

### 兼容性

- ✅ 支持 OpenRouter 的所有模型
- ✅ 保持与原有 API 的向后兼容性
- ✅ 自动处理不同的响应格式

## 使用方法

### 1. 配置环境变量

在 `.env` 文件中设置：
```env
OPENAI_API_KEY=your_openrouter_api_key
TRADINGAGENTS_BACKEND_URL=https://openrouter.ai/api/v1
```

### 2. 使用新闻获取函数

```python
from tradingagents.dataflows import interface

# 获取股票新闻
stock_news = interface.get_stock_news_openai("AAPL", "2024-01-15")

# 获取全球新闻
global_news = interface.get_global_news_openai("2024-01-15")

# 获取基本面数据
fundamentals = interface.get_fundamentals_openai("AAPL", "2024-01-15")
```

### 3. 测试集成

运行测试脚本验证集成是否正常：
```bash
python test_openrouter_integration.py
```

## 支持的模型

推荐使用以下模型进行 Web Search：

- `openai/gpt-4o-mini` - 成本效益高
- `openai/gpt-4o` - 更高质量的结果
- `perplexity/sonar` - 原生支持搜索

## 注意事项

1. **API 密钥**：确保使用有效的 OpenRouter API 密钥
2. **成本**：Web Search 会产生额外费用（约 $0.02 每次请求）
3. **速率限制**：遵守 OpenRouter 的速率限制政策

## 故障排除

如果遇到问题，请检查：

1. API 密钥是否正确设置
2. backend_url 是否正确配置
3. 网络连接是否正常
4. 查看日志中的具体错误信息

## 相关文件

- `tradingagents/dataflows/interface.py` - 核心实现
- `test_openrouter_integration.py` - 集成测试
- `test_news_api_formats.py` - API 格式测试