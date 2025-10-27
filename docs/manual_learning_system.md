# 手动学习系统 (Manual Learning System)

## 概述

手动学习系统允许用户手动选择特定的决策报告并输入实际的盈亏值（PnL），从而触发针对性的学习反思过程。这个系统提供了比自动学习更精确的控制，让你能够针对特定的交易场景进行学习。

## 系统架构

### 核心组件

1. **扩展的学习引擎** (`scripts/learning_engine.py`)
   - 支持自动和手动学习模式
   - 提供交互式学习会话
   - 兼容现有的反思机制

2. **命令行工具** (`scripts/manual_learning_cli.py`)
   - 友好的CLI界面
   - 决策日志搜索和浏览
   - 快速学习执行

## 功能特性

### ✅ 已实现的功能

- **决策日志管理**
  - 自动扫描所有可用的决策日志
  - 按市场、日期、决策ID分类
  - 详细的日志信息展示

- **手动学习执行**
  - 选择特定决策日志
  - 输入自定义PnL值
  - 添加学习笔记
  - 触发完整的反思过程

- **学习历史记录**
  - 保存所有学习会话
  - 查询历史学习记录
  - 学习结果追踪

- **多种使用方式**
  - RESTful API接口
  - 命令行工具
  - 交互式会话
  - 程序化调用

## 使用方法

### 1. 命令行工具 (推荐)

#### 列出所有决策日志
```bash
cd /home/ubuntu/sipeng/tradingAgents
source venv/bin/activate
python scripts/manual_learning_cli.py list
```

#### 搜索特定市场的日志
```bash
python scripts/manual_learning_cli.py search BTC
```

#### 查看日志详情
```bash
python scripts/manual_learning_cli.py detail path/to/decision_log.json
```

#### 执行手动学习
```bash
python scripts/manual_learning_cli.py learn path/to/decision_log.json 5.25 --notes "Profitable BTC trade"
```

#### 交互式学习会话
```bash
python scripts/manual_learning_cli.py interactive
```

### 2. 扩展的学习引擎

#### 列出可用日志
```bash
python scripts/learning_engine.py --list-logs
```

#### 手动学习模式
```bash
python scripts/learning_engine.py --mode manual --decision-log path/to/log.json --pnl 3.14 --notes "Test learning"
```

#### 交互式模式
```bash
python scripts/learning_engine.py --mode interactive
```

#### 自动模式（原有功能）
```bash
python scripts/learning_engine.py --mode auto
```

## 测试系统

### 测试手动学习功能
```bash
# 测试决策日志列表
python scripts/manual_learning_cli.py list

# 测试手动学习
python scripts/learning_engine.py --mode manual --decision-log path/to/log.json --pnl 5.25
```

## 文件结构

```
scripts/
├── manual_learning_cli.py          # CLI工具
└── learning_engine.py              # 扩展的学习引擎

eval_results/
├── manual_learning_YYYYMMDD_HHMMSS.json  # 学习结果文件
└── {MARKET}/
    └── TradingAgentsStrategy_logs/
        └── full_states_log_YYYY-MM-DD.json  # 决策日志
```

## 数据格式

### 决策日志信息
```json
{
  "file_path": "/path/to/log.json",
  "market": "BTC-USD",
  "date": "2025-01-15",
  "decision_id": "decision_123456",
  "timestamp": "2025-01-15T10:30:00",
  "summary": "Trend: Bullish | Action: BUY | Confidence: High",
  "file_size": 2048
}
```

### 学习记录
```json
{
  "success": true,
  "decision_id": "decision_123456",
  "decision_log_path": "/path/to/log.json",
  "input_pnl": 5.25,
  "user_notes": "Profitable trade analysis",
  "reflections": {
    "bull_researcher": "Reflection content...",
    "bear_researcher": "Reflection content...",
    "trader": "Reflection content...",
    "invest_judge": "Reflection content...",
    "risk_manager": "Reflection content..."
  },
  "timestamp": "2025-01-15T11:00:00"
}
```

## 最佳实践

### 1. 学习会话规划
- **选择代表性案例**：选择盈利和亏损的典型交易
- **记录详细笔记**：为每次学习添加上下文信息
- **定期回顾**：查看学习历史，识别模式

### 2. PnL值输入
- **使用实际值**：输入真实的盈亏数据
- **考虑时间因素**：包括持仓时间的影响
- **标准化单位**：统一使用USDC作为计量单位

### 3. 决策日志选择
- **关键决策点**：选择重要的交易决策时刻
- **多样化场景**：涵盖不同市场条件和策略
- **时间分布**：选择不同时期的决策进行学习

## 故障排除

### 常见问题

#### 1. 找不到决策日志
```bash
# 检查日志目录
ls -la eval_results/*/TradingAgentsStrategy_logs/

# 确认日志格式
python scripts/manual_learning_cli.py list
```

#### 2. 学习执行失败
```bash
# 验证日志文件
python scripts/manual_learning_cli.py detail path/to/log.json

# 检查PnL值格式
python scripts/manual_learning_cli.py learn path/to/log.json 5.25
```

### 调试模式

#### 启用详细日志
```bash
# CLI工具调试
python -u scripts/manual_learning_cli.py learn path/to/log.json 5.25
```

## 扩展和定制

### 自定义学习逻辑
1. 修改`manual_learning()`函数
2. 扩展反思机制
3. 添加新的数据字段

## 总结

手动学习系统成功实现了以下核心功能：

✅ **决策日志管理** - 自动扫描和列出所有可用的决策日志
✅ **手动学习执行** - 基于用户输入的PnL值触发学习反思
✅ **命令行界面** - 提供友好的CLI工具进行操作
✅ **交互式会话** - 支持交互式选择和学习
✅ **兼容现有系统** - 与原有的自动学习模式并存

这个系统为交易策略的持续改进提供了强大的工具，允许针对特定交易场景进行精确的学习和反思。
