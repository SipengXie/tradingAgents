---
name: langchain
description: LangChain Python framework for building LLM applications. Use for chains, agents, memory, embeddings, vector stores, RAG, and LLM application development.
---

# LangChain Skill

全面的 LangChain 开发指南，基于官方文档自动生成。

## 何时使用此技能

在以下场景触发此技能：

**LLM 应用开发：**
- 构建 AI 代理（agents）和工具调用系统
- 实现 RAG（检索增强生成）系统
- 创建多代理系统和协作工作流
- 设计链式推理和 LCEL（LangChain Expression Language）

**具体任务：**
- 创建和管理提示工程（prompt engineering）
- 实现记忆系统（短期/长期/语义/情景记忆）
- 集成向量存储和嵌入（embeddings）
- 构建聊天机器人和对话系统
- 使用 LangSmith 进行追踪、评估和调试
- 开发 LangGraph 应用程序

**技术集成：**
- 与 OpenAI、Anthropic Claude、Google 等 LLM 提供商集成
- 工具定义和函数调用
- 状态管理和检查点（checkpointing）
- OAuth 认证和代理授权

## 快速参考

### 1. 创建简单 Agent

```python
from langchain.agents import create_agent

def get_weather(city: str) -> str:
    """获取指定城市的天气信息"""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="anthropic:claude-sonnet-4-5",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)
```

**说明：** 最简单的 agent 创建方式，只需提供模型名称、工具列表和系统提示。

### 2. 定义工具（Tools）

```python
from langchain.tools import tool

@tool
def multiply(a: int, b: int) -> int:
    """将 a 和 b 相乘。

    Args:
        a: 第一个整数
        b: 第二个整数
    """
    return a * b

@tool
def add(a: int, b: int) -> int:
    """将 a 和 b 相加。

    Args:
        a: 第一个整数
        b: 第二个整数
    """
    return a + b

@tool
def divide(a: int, b: int) -> float:
    """将 a 除以 b。

    Args:
        a: 第一个整数
        b: 第二个整数
    """
    return a / b
```

**说明：** 使用 `@tool` 装饰器定义工具。工具的文档字符串（docstring）非常重要，会被 LLM 用来理解何时调用该工具。

### 3. 使用 MessagesState 管理对话状态

```python
from langchain.agents import MessagesState
from langchain_core.messages import AIMessage

def list_tables(state: MessagesState):
    tool_call = {
        "name": "sql_db_list_tables",
        "args": {},
        "id": "abc123",
        "type": "tool_call",
    }
    tool_call_message = AIMessage(content="", tool_calls=[tool_call])

    list_tables_tool = next(
        tool for tool in tools if tool.name == "sql_db_list_tables"
    )
    tool_message = list_tables_tool.invoke(tool_call)
    response = AIMessage(f"Available tables: {tool_message.content}")

    return {"messages": [tool_call_message, tool_message, response]}
```

**说明：** `MessagesState` 是 LangGraph 中管理对话历史的核心状态类型。函数返回字典来更新状态。

### 4. 安装和初始化

```bash
# 安装核心包
pip install langchain

# 安装特定提供商（示例：Anthropic）
pip install langchain-anthropic

# 安装社区工具
pip install langchain-community
```

```python
# 使用 Anthropic Claude
from langchain_anthropic import ChatAnthropic

model = ChatAnthropic(model="claude-sonnet-4-5")
response = model.invoke("Hello, how are you?")
```

**说明：** LangChain 采用模块化设计，核心包和提供商包分离安装。

### 5. 子代理（Sub-agent）作为工具

```python
from typing import Annotated
from langchain.agents import AgentState
from langchain.tools import InjectedToolCallId
from langgraph.types import Command

@tool(
    "subagent1_name",
    description="子代理描述 - 说明何时调用此子代理"
)
def call_subagent(
    query: str,
    tool_call_id: Annotated[str, InjectedToolCallId]
) -> Command:
    """调用子代理来处理特定任务"""
    # 运行子代理
    result = subagent.invoke({"messages": [query]})

    # 返回结果给主代理
    return Command(
        update={"custom_state_key": result},
        goto="next_node"
    )
```

**说明：** 在多代理系统中，子代理可以作为工具被主代理调用。使用 `Command` 来控制状态更新和流程跳转。

### 6. OAuth 认证（代理授权）

```python
# 用户级别的 token（适用于此用户下的所有代理）
auth_result = await client.authenticate(
    provider="{provider_id}",
    scopes=["scopeA"],
    user_id="your_user_id"
)

if auth_result.needs_auth:
    print(f"请在此完成 OAuth: {auth_result.auth_url}")
    # 等待完成
    completed_auth = await client.wait_for_completion(auth_result.auth_id)
    token = completed_auth.token
else:
    token = auth_result.token
```

**说明：** LangSmith 支持为代理配置 OAuth，允许代理代表用户访问第三方服务。

### 7. LangSmith 追踪

```python
import os

# 设置环境变量启用追踪
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "your-api-key"
os.environ["LANGCHAIN_PROJECT"] = "your-project-name"

# 所有 LangChain 调用会自动追踪
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini")
response = model.invoke("Explain AI agents")

# 追踪会自动显示在 LangSmith UI 中
```

**说明：** 设置环境变量后，所有 LangChain 操作会自动追踪到 LangSmith，便于调试和监控。

### 8. 自定义 Runnable 名称

```python
from langchain_core.runnables import RunnablePassthrough

chain = (
    RunnablePassthrough()
    | model
    | output_parser
).with_config(run_name="MyCustomChain")

# 在 LangSmith 中会显示为 "MyCustomChain"
```

**说明：** 使用 `with_config(run_name=...)` 为链赋予自定义名称，便于在 LangSmith 中识别。

### 9. 多代理模式选择

| 模式 | 工作方式 | 控制流 | 使用场景 |
|------|---------|--------|---------|
| **Tool Calling** | 监督者代理将其他代理作为工具调用 | 集中式：所有路由通过主代理 | 任务编排、结构化工作流 |
| **Handoffs** | 当前代理转移控制权给另一个代理 | 分散式：代理可以改变活跃代理 | 多领域对话、专家接管 |

**说明：** 两种模式可以混合使用 - 使用 handoffs 进行代理切换，同时每个代理可以调用子代理作为工具。

### 10. LangGraph 本地运行

```bash
# 1. 安装 LangGraph CLI
pip install langgraph-cli

# 2. 创建应用目录
mkdir my-app && cd my-app

# 3. 创建 .env 文件
echo "ANTHROPIC_API_KEY=your-api-key" > .env

# 4. 启动 LangGraph Server
langgraph dev

# 5. 测试 API
curl http://localhost:8123/health
```

**说明：** LangGraph CLI 提供本地开发服务器，支持热重载和 API 测试。

## 参考文件

本技能包含 `references/` 目录中的全面文档：

### **getting_started.md** (29 页)
入门指南和快速开始教程：
- 提示工程（Prompt Engineering）快速开始
- LangSmith 追踪设置和使用
- RAG（检索增强生成）应用构建
- 记忆系统概念（短期、长期、语义、情景、程序性记忆）
- LangGraph 本地运行指南
- 安装和环境配置

**何时查看：** 刚开始使用 LangChain 或需要了解核心概念和快速启动项目时。

### **agents.md** (131 页)
代理系统的详细文档：
- 工具定义和装饰器使用
- 多代理系统模式（Tool Calling vs Handoffs）
- 上下文工程和状态管理
- 子代理作为工具的实现
- 输入/输出控制和自定义
- OAuth 认证和代理授权
- YouTube 工具和社区集成
- 状态图（StateGraph）构建

**何时查看：** 构建单个或多个代理系统、实现工具调用、管理复杂工作流时。

### **models.md** (803 页)
模型、评估和集成的全面文档：
- LangSmith 评估系统
- 数据集管理和注释
- 多种 LLM 提供商集成（OpenAI、Anthropic、Google 等）
- 文档加载器（YouTube、PDF、音频等）
- Studio 使用指南
- 社区工具和扩展

**何时查看：** 选择和配置 LLM 模型、进行评估、集成第三方服务、加载各种数据源时。

## 使用此技能

### 初学者

**从这里开始：**
1. 阅读 `getting_started.md` 了解核心概念
2. 查看上方的快速参考示例 1-4（创建 agent、定义工具、管理状态）
3. 尝试快速参考示例 10（LangGraph 本地运行）
4. 实践简单的聊天机器人或工具调用示例

**建议学习路径：**
- 基础概念 → 简单 agent → 工具定义 → 状态管理 → LangSmith 追踪

### 中级用户

**深入特定功能：**
1. 参考 `agents.md` 学习多代理模式
2. 实现子代理作为工具（快速参考示例 5）
3. 设置 OAuth 认证（快速参考示例 6）
4. 使用 LangSmith 进行追踪和调试（快速参考示例 7-8）
5. 探索记忆系统和 RAG 应用

**优化建议：**
- 使用自定义运行名称便于调试
- 实现适当的错误处理和重试逻辑
- 选择合适的多代理模式（Tool Calling vs Handoffs）

### 高级用户

**构建生产级应用：**
1. 参考 `models.md` 进行模型选择和评估
2. 实现复杂的多代理系统（混合模式）
3. 构建自定义工具和集成
4. 设置全面的评估和监控
5. 优化上下文工程和提示策略

**最佳实践：**
- 为每个子代理定义清晰的职责范围
- 使用 LangSmith 数据集进行动态 few-shot 示例选择
- 实现程序性记忆（自我修改提示）
- 监控代理性能和成本

## 核心概念

### Agent（代理）
代理是能够使用工具、进行推理并做出决策的 LLM 应用。代理可以：
- 调用外部工具和 API
- 维护对话状态和记忆
- 根据上下文做出决策
- 与其他代理协作

### Tools（工具）
工具是代理可以调用的函数。好的工具定义包括：
- 清晰的函数名（描述性）
- 详细的文档字符串（docstring）
- 明确的参数类型和说明
- 可靠的错误处理

### Multi-Agent Patterns（多代理模式）

**Tool Calling（工具调用）：**
- 中央监督者代理控制所有流程
- 子代理作为工具被调用
- 集中式决策和路由
- 适合结构化、可预测的工作流

**Handoffs（切换）：**
- 代理之间转移控制权
- 分散式决策
- 代理可以直接与用户交互
- 适合多领域对话和专家协作

### LangGraph
LangGraph 是构建有状态、多步骤 LLM 应用的框架：
- **StateGraph**：定义应用的状态转换
- **MessagesState**：管理对话历史
- **Nodes**：处理逻辑的单元
- **Edges**：定义流程路径
- **Checkpointing**：保存和恢复状态

### Memory（记忆）

**短期记忆（Short-term）：**
- 对话历史和上下文
- 使用 MessagesState 管理

**长期记忆（Long-term）：**
- 持久化存储
- 用户偏好和历史交互

**语义记忆（Semantic）：**
- 事实和知识
- 用户画像和配置

**情景记忆（Episodic）：**
- 过去的经验和任务
- Few-shot 示例

**程序性记忆（Procedural）：**
- 任务执行规则
- 自我修改的提示

### LCEL (LangChain Expression Language)
LCEL 是用于链接组件的声明式语法：
```python
chain = prompt | model | output_parser
```

### RAG (Retrieval Augmented Generation)
RAG 通过检索相关文档来增强 LLM 响应：
1. 嵌入（Embedding）文档
2. 存储到向量数据库
3. 检索相关内容
4. 传递给 LLM 生成答案

### LangSmith
LangSmith 是 LangChain 的可观测性平台：
- **追踪（Tracing）**：记录每次调用
- **评估（Evaluation）**：测试应用质量
- **监控（Monitoring）**：生产环境监控
- **调试（Debugging）**：分析问题和优化

## 资源

### references/
从官方文档提取的组织化文档，包含：
- 详细解释和概念
- 带语言标注的代码示例
- 原始文档链接
- 快速导航目录

### scripts/
在此添加常用自动化脚本的辅助工具。

### assets/
在此添加模板、样板代码或示例项目。

## 注意事项

- 本技能从官方文档自动生成
- 参考文件保留了源文档的结构和示例
- 代码示例包含语言检测以提供更好的语法高亮
- 快速参考模式从文档中的常见用法示例提取

## 导航提示

**寻找示例？**
- 查看上方的快速参考部分（10 个实用示例）
- 浏览 `references/` 中的相关文件

**需要深入了解？**
- `getting_started.md` - 基础概念和教程
- `agents.md` - 代理系统详细指南
- `models.md` - 模型集成和评估

**调试问题？**
1. 启用 LangSmith 追踪（快速参考示例 7）
2. 检查工具定义的文档字符串
3. 验证状态更新逻辑
4. 查看参考文档中的相关章节

## 更新

要使用最新文档刷新此技能：
1. 使用相同配置重新运行爬虫
2. 技能将使用最新信息重新构建
