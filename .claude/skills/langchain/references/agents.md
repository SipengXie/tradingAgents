# Langchain - Agents

**Pages:** 131

---

## Note: YouTubeSearchTool might be in langchain or langchain_community

**URL:** llms-txt#note:-youtubesearchtool-might-be-in-langchain-or-langchain_community

from langchain.tools import YouTubeSearchTool # Or langchain_community.tools
bash  theme={null}
  pip install yt_dlp pydub librosa langchain-community # Requires langchain-community
  bash uv theme={null}
  uv add yt_dlp pydub librosa langchain-community # Requires langchain-community
  python  theme={null}
from langchain_community.document_loaders.blob_loaders.youtube_audio import YoutubeAudioLoader

**Examples:**

Example 1 (unknown):
```unknown
#### YouTube Audio Loader

Download audio from YouTube videos. Requires `yt_dlp`, `pydub`, `librosa`.

<CodeGroup>
```

Example 2 (unknown):
```unknown

```

Example 3 (unknown):
```unknown
</CodeGroup>

See [usage example and authorization instructions](/oss/python/integrations/document_loaders/youtube_audio).
```

---

## Default: user-scoped token (works for any agent under this user)

**URL:** llms-txt#default:-user-scoped-token-(works-for-any-agent-under-this-user)

auth_result = await client.authenticate(
    provider="{provider_id}",
    scopes=["scopeA"],
    user_id="your_user_id"
)

if auth_result.needs_auth:
    print(f"Complete OAuth at: {auth_result.auth_url}")
    # Wait for completion
    completed_auth = await client.wait_for_completion(auth_result.auth_id)
    token = completed_auth.token
else:
    token = auth_result.token
```

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/langsmith/agent-auth.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

---

## AIMessage(content='bar', ...)

**URL:** llms-txt#aimessage(content='bar',-...)

**Contents:**
  - InMemorySaver Checkpointer

python  theme={null}
from langgraph.checkpoint.memory import InMemorySaver

agent = create_agent(
    model,
    tools=[],
    checkpointer=InMemorySaver()
)

**Examples:**

Example 1 (unknown):
```unknown
### InMemorySaver Checkpointer

To enable persistence during testing, you can use the [`InMemorySaver`](https://reference.langchain.com/python/langgraph/checkpoints/#langgraph.checkpoint.memory.InMemorySaver) checkpointer. This allows you to simulate multiple turns to test state-dependent behavior:
```

---

## Example: create a predetermined tool call

**URL:** llms-txt#example:-create-a-predetermined-tool-call

def list_tables(state: MessagesState):
    tool_call = {
        "name": "sql_db_list_tables",
        "args": {},
        "id": "abc123",
        "type": "tool_call",
    }
    tool_call_message = AIMessage(content="", tool_calls=[tool_call])

list_tables_tool = next(tool for tool in tools if tool.name == "sql_db_list_tables")
    tool_message = list_tables_tool.invoke(tool_call)
    response = AIMessage(f"Available tables: {tool_message.content}")

return {"messages": [tool_call_message, tool_message, response]}

---

## Or if you'd like a token that can be used by any agent, set agent_scoped=False

**URL:** llms-txt#or-if-you'd-like-a-token-that-can-be-used-by-any-agent,-set-agent_scoped=false

auth_result = await client.authenticate(
    provider="{provider_id}",
    scopes=["scopeA"],
    user_id="your_user_id",
    agent_scoped=False
)
python  theme={null}
token = auth_result.token
python  theme={null}

**Examples:**

Example 1 (unknown):
```unknown
During execution, if authentication is required, the SDK will throw an [interrupt](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/add-human-in-the-loop/#pause-using-interrupt). The agent execution pauses and presents the OAuth URL to the user:

<img src="https://mintcdn.com/langchain-5e9cc07a/Xbr8HuVd9jPi6qTU/images/langgraph-auth-interrupt.png?fit=max&auto=format&n=Xbr8HuVd9jPi6qTU&q=85&s=94f84dd7ec822ca69f9a27b4458dca9f" alt="Studio interrupt showing OAuth URL" data-og-width="1197" width="1197" data-og-height="530" height="530" data-path="images/langgraph-auth-interrupt.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/Xbr8HuVd9jPi6qTU/images/langgraph-auth-interrupt.png?w=280&fit=max&auto=format&n=Xbr8HuVd9jPi6qTU&q=85&s=8e2f6ddeb7ae2b7e3f349a23ed69270a 280w, https://mintcdn.com/langchain-5e9cc07a/Xbr8HuVd9jPi6qTU/images/langgraph-auth-interrupt.png?w=560&fit=max&auto=format&n=Xbr8HuVd9jPi6qTU&q=85&s=ed5f6697e44784a6a937f6bfd3248780 560w, https://mintcdn.com/langchain-5e9cc07a/Xbr8HuVd9jPi6qTU/images/langgraph-auth-interrupt.png?w=840&fit=max&auto=format&n=Xbr8HuVd9jPi6qTU&q=85&s=bb34295ee4128adb77cdf6dd1a76d88a 840w, https://mintcdn.com/langchain-5e9cc07a/Xbr8HuVd9jPi6qTU/images/langgraph-auth-interrupt.png?w=1100&fit=max&auto=format&n=Xbr8HuVd9jPi6qTU&q=85&s=09df9030e048467ca35ab70bf73b2272 1100w, https://mintcdn.com/langchain-5e9cc07a/Xbr8HuVd9jPi6qTU/images/langgraph-auth-interrupt.png?w=1650&fit=max&auto=format&n=Xbr8HuVd9jPi6qTU&q=85&s=ebfe20351ac52045b30713007da5ba61 1650w, https://mintcdn.com/langchain-5e9cc07a/Xbr8HuVd9jPi6qTU/images/langgraph-auth-interrupt.png?w=2500&fit=max&auto=format&n=Xbr8HuVd9jPi6qTU&q=85&s=ff3b2fcebfdb6fc76e7269d8aef34077 2500w" />

After the user completes OAuth authentication and we receive the callback from the provider, they will see the auth success page.

<img src="https://mintcdn.com/langchain-5e9cc07a/Xbr8HuVd9jPi6qTU/images/github-auth-success.png?fit=max&auto=format&n=Xbr8HuVd9jPi6qTU&q=85&s=72e6492f074507bc8888804066205fcb" alt="GitHub OAuth success page" data-og-width="447" width="447" data-og-height="279" height="279" data-path="images/github-auth-success.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/Xbr8HuVd9jPi6qTU/images/github-auth-success.png?w=280&fit=max&auto=format&n=Xbr8HuVd9jPi6qTU&q=85&s=031b2f9d30e4da4240059cb25fba6d15 280w, https://mintcdn.com/langchain-5e9cc07a/Xbr8HuVd9jPi6qTU/images/github-auth-success.png?w=560&fit=max&auto=format&n=Xbr8HuVd9jPi6qTU&q=85&s=eb4d01516b4691158a47a8b2632d22e3 560w, https://mintcdn.com/langchain-5e9cc07a/Xbr8HuVd9jPi6qTU/images/github-auth-success.png?w=840&fit=max&auto=format&n=Xbr8HuVd9jPi6qTU&q=85&s=e49b04f99e4c2f485769443da039bca1 840w, https://mintcdn.com/langchain-5e9cc07a/Xbr8HuVd9jPi6qTU/images/github-auth-success.png?w=1100&fit=max&auto=format&n=Xbr8HuVd9jPi6qTU&q=85&s=930aee5e270d2fcb4d6bdfb001150d81 1100w, https://mintcdn.com/langchain-5e9cc07a/Xbr8HuVd9jPi6qTU/images/github-auth-success.png?w=1650&fit=max&auto=format&n=Xbr8HuVd9jPi6qTU&q=85&s=3b5dc841251462c3ed140800564c0ad8 1650w, https://mintcdn.com/langchain-5e9cc07a/Xbr8HuVd9jPi6qTU/images/github-auth-success.png?w=2500&fit=max&auto=format&n=Xbr8HuVd9jPi6qTU&q=85&s=0e53fbc4c56b16bf1db88c98ab2e631d 2500w" />

The agent then resumes execution from the point it left off at, and the token can be used for any API calls. We store and refresh OAuth tokens so that future uses of the service by either the user or agent do not require an OAuth flow.
```

Example 2 (unknown):
```unknown
#### Outside LangGraph context

Provide the `auth_url` to the user for out-of-band OAuth flows.
```

---

## Define tools

**URL:** llms-txt#define-tools

@tool
def multiply(a: int, b: int) -> int:
    """Multiply `a` and `b`.

Args:
        a: First int
        b: Second int
    """
    return a * b

@tool
def add(a: int, b: int) -> int:
    """Adds `a` and `b`.

Args:
        a: First int
        b: Second int
    """
    return a + b

@tool
def divide(a: int, b: int) -> float:
    """Divide `a` and `b`.

Args:
        a: First int
        b: Second int
    """
    return a / b

---

## Multi-agent

**URL:** llms-txt#multi-agent

**Contents:**
- Multi-agent patterns
- Choosing a pattern
- Customizing agent context
- Tool calling
  - Implementation
  - Where to customize
  - Control the input to the subagent
  - Control the output from the subagent

Source: https://docs.langchain.com/oss/python/langchain/multi-agent

**Multi-agent systems** break a complex application into multiple specialized agents that work together to solve problems.
Instead of relying on a single agent to handle every step, **multi-agent architectures** allow you to compose smaller, focused agents into a coordinated workflow.

Multi-agent systems are useful when:

* A single agent has too many tools and makes poor decisions about which to use.
* Context or memory grows too large for one agent to track effectively.
* Tasks require **specialization** (e.g., a planner, researcher, math expert).

## Multi-agent patterns

| Pattern                           | How it works                                                                                                                                                     | Control flow                                               | Example use case                                 |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------ |
| [**Tool Calling**](#tool-calling) | A **supervisor** agent calls other agents as *tools*. The “tool” agents don’t talk to the user directly — they just run their task and return results.           | Centralized: all routing passes through the calling agent. | Task orchestration, structured workflows.        |
| [**Handoffs**](#handoffs)         | The current agent decides to **transfer control** to another agent. The active agent changes, and the user may continue interacting directly with the new agent. | Decentralized: agents can change who is active.            | Multi-domain conversations, specialist takeover. |

<Card title="Tutorial: Build a supervisor agent" icon="sitemap" href="/oss/python/langchain/supervisor" arrow cta="Learn more">
  Learn how to build a personal assistant using the supervisor pattern, where a central supervisor agent coordinates specialized worker agents.
  This tutorial demonstrates:

* Creating specialized sub-agents for different domains (calendar and email)
  * Wrapping sub-agents as tools for centralized orchestration
  * Adding human-in-the-loop review for sensitive actions
</Card>

## Choosing a pattern

| Question                                              | Tool Calling | Handoffs |
| ----------------------------------------------------- | ------------ | -------- |
| Need centralized control over workflow?               | ✅ Yes        | ❌ No     |
| Want agents to interact directly with the user?       | ❌ No         | ✅ Yes    |
| Complex, human-like conversation between specialists? | ❌ Limited    | ✅ Strong |

<Tip>
  You can mix both patterns — use **handoffs** for agent switching, and have each agent **call subagents as tools** for specialized tasks.
</Tip>

## Customizing agent context

At the heart of multi-agent design is **context engineering** - deciding what information each agent sees. LangChain gives you fine-grained control over:

* Which parts of the conversation or state are passed to each agent.
* Specialized prompts tailored to subagents.
* Inclusion/exclusion of intermediate reasoning.
* Customizing input/output formats per agent.

The quality of your system **heavily depends** on context engineering. The goal is to ensure that each agent has access to the correct data it needs to perform its task, whether it’s acting as a tool or as an active agent.

In **tool calling**, one agent (the “**controller**”) treats other agents as *tools* to be invoked when needed. The controller manages orchestration, while tool agents perform specific tasks and return results.

1. The **controller** receives input and decides which tool (subagent) to call.
2. The **tool agent** runs its task based on the controller’s instructions.
3. The **tool agent** returns results to the controller.
4. The **controller** decides the next step or finishes.

<Tip>
  Agents used as tools are generally **not expected** to continue conversation with the user.
  Their role is to perform a task and return results to the controller agent.
  If you need subagents to be able to converse with the user, use **handoffs** instead.
</Tip>

Below is a minimal example where the main agent is given access to a single subagent via a tool definition:

1. The main agent invokes `call_subagent1` when it decides the task matches the subagent’s description.
2. The subagent runs independently and returns its result.
3. The main agent receives the result and continues orchestration.

### Where to customize

There are several points where you can control how context is passed between the main agent and its subagents:

1. **Subagent name** (`"subagent1_name"`): This is how the main agent refers to the subagent. Since it influences prompting, choose it carefully.
2. **Subagent description** (`"subagent1_description"`): This is what the main agent “knows” about the subagent. It directly shapes how the main agent decides when to call it.
3. **Input to the subagent**: You can customize this input to better shape how the subagent interprets tasks. In the example above, we pass the agent-generated `query` directly.
4. **Output from the subagent**: This is the **response** passed back to the main agent. You can adjust what is returned to control how the main agent interprets results. In the example above, we return the final message text, but you could return additional state or metadata.

### Control the input to the subagent

There are two main levers to control the input that the main agent passes to a subagent:

* **Modify the prompt** – Adjust the main agent's prompt or the tool metadata (i.e., sub-agent's name and description) to better guide when and how it calls the subagent.
* **Context injection** – Add input that isn’t practical to capture in a static prompt (e.g., full message history, prior results, task metadata) by adjusting the tool call to pull from the agent’s state.

### Control the output from the subagent

Two common strategies for shaping what the main agent receives back from a subagent:

* **Modify the prompt** – Refine the subagent’s prompt to specify exactly what should be returned.
  * Useful when outputs are incomplete, too verbose, or missing key details.
  * A common failure mode is that the subagent performs tool calls or reasoning but does **not include the results** in its final message. Remind it that the controller (and user) only see the final output, so all relevant info must be included there.
* **Custom output formatting** – adjust or enrich the subagent's response in code before handing it back to the main agent.
  * Example: pass specific state keys back to the main agent in addition to the final text.
  * This requires wrapping the result in a [`Command`](https://reference.langchain.com/python/langgraph/types/#langgraph.types.Command) (or equivalent structure) so you can merge custom state with the subagent’s response.

```python  theme={null}
from typing import Annotated
from langchain.agents import AgentState
from langchain.tools import InjectedToolCallId
from langgraph.types import Command

@tool(
    "subagent1_name",
    description="subagent1_description"
)

**Examples:**

Example 1 (unknown):
```unknown
<Tip>
  Agents used as tools are generally **not expected** to continue conversation with the user.
  Their role is to perform a task and return results to the controller agent.
  If you need subagents to be able to converse with the user, use **handoffs** instead.
</Tip>

### Implementation

Below is a minimal example where the main agent is given access to a single subagent via a tool definition:
```

Example 2 (unknown):
```unknown
In this pattern:

1. The main agent invokes `call_subagent1` when it decides the task matches the subagent’s description.
2. The subagent runs independently and returns its result.
3. The main agent receives the result and continues orchestration.

### Where to customize

There are several points where you can control how context is passed between the main agent and its subagents:

1. **Subagent name** (`"subagent1_name"`): This is how the main agent refers to the subagent. Since it influences prompting, choose it carefully.
2. **Subagent description** (`"subagent1_description"`): This is what the main agent “knows” about the subagent. It directly shapes how the main agent decides when to call it.
3. **Input to the subagent**: You can customize this input to better shape how the subagent interprets tasks. In the example above, we pass the agent-generated `query` directly.
4. **Output from the subagent**: This is the **response** passed back to the main agent. You can adjust what is returned to control how the main agent interprets results. In the example above, we return the final message text, but you could return additional state or metadata.

### Control the input to the subagent

There are two main levers to control the input that the main agent passes to a subagent:

* **Modify the prompt** – Adjust the main agent's prompt or the tool metadata (i.e., sub-agent's name and description) to better guide when and how it calls the subagent.
* **Context injection** – Add input that isn’t practical to capture in a static prompt (e.g., full message history, prior results, task metadata) by adjusting the tool call to pull from the agent’s state.
```

Example 3 (unknown):
```unknown
### Control the output from the subagent

Two common strategies for shaping what the main agent receives back from a subagent:

* **Modify the prompt** – Refine the subagent’s prompt to specify exactly what should be returned.
  * Useful when outputs are incomplete, too verbose, or missing key details.
  * A common failure mode is that the subagent performs tool calls or reasoning but does **not include the results** in its final message. Remind it that the controller (and user) only see the final output, so all relevant info must be included there.
* **Custom output formatting** – adjust or enrich the subagent's response in code before handing it back to the main agent.
  * Example: pass specific state keys back to the main agent in addition to the final text.
  * This requires wrapping the result in a [`Command`](https://reference.langchain.com/python/langgraph/types/#langgraph.types.Command) (or equivalent structure) so you can merge custom state with the subagent’s response.
```

---

## MCP endpoint in LangGraph Server

**URL:** llms-txt#mcp-endpoint-in-langgraph-server

**Contents:**
- Requirements
- Usage overview
  - Client
- Expose an agent as MCP tool
  - Setting name and description
  - Schema

Source: https://docs.langchain.com/langsmith/server-mcp

The Model Context Protocol (MCP) is an open protocol for describing tools and data sources in a model-agnostic format, enabling LLMs to discover and use them via a structured API.

[LangGraph Server](/langsmith/langgraph-server) implements MCP using the [Streamable HTTP transport](https://spec.modelcontextprotocol.io/specification/2025-03-26/basic/transports/#streamable-http). This allows LangGraph **agents** to be exposed as **MCP tools**, making them usable with any MCP-compliant client supporting Streamable HTTP.

The MCP endpoint is available at `/mcp` on [LangGraph Server](/langsmith/langgraph-server).

You can set up [custom authentication middleware](/langsmith/custom-auth) to authenticate a user with an MCP server to get access to user-scoped tools within your LangSmith deployment.

An example architecture for this flow:

To use MCP, ensure you have the following dependencies installed:

* `langgraph-api >= 0.2.3`
* `langgraph-sdk >= 0.1.61`

* Upgrade to use langgraph-api>=0.2.3. If you are deploying LangSmith, this will be done for you automatically if you create a new revision.
* MCP tools (agents) will be automatically exposed.
* Connect with any MCP-compliant client that supports Streamable HTTP.

Use an MCP-compliant client to connect to the LangGraph server. The following examples show how to connect using different programming languages.

<Tabs>
  <Tab title="JavaScript/TypeScript">

> **Note**
    > Replace `serverUrl` with your LangGraph server URL and configure authentication headers as needed.

<Tab title="Python">
    Install the adapter with:

Here is an example of how to connect to a remote MCP endpoint and use an agent as a tool:

## Expose an agent as MCP tool

When deployed, your agent will appear as a tool in the MCP endpoint
with this configuration:

* **Tool name**: The agent's name.
* **Tool description**: The agent's description.
* **Tool input schema**: The agent's input schema.

### Setting name and description

You can set the name and description of your agent in `langgraph.json`:

After deployment, you can update the name and description using the LangGraph SDK.

Define clear, minimal input and output schemas to avoid exposing unnecessary internal complexity to the LLM.

The default [MessagesState](/oss/python/langgraph/graph-api#messagesstate) uses `AnyMessage`, which supports many message types but is too general for direct LLM exposure.

Instead, define **custom agents or workflows** that use explicitly typed input and output structures.

For example, a workflow answering documentation questions might look like this:

```python  theme={null}
from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict

**Examples:**

Example 1 (unknown):
```unknown
## Requirements

To use MCP, ensure you have the following dependencies installed:

* `langgraph-api >= 0.2.3`
* `langgraph-sdk >= 0.1.61`

Install them with:

<CodeGroup>
```

Example 2 (unknown):
```unknown

```

Example 3 (unknown):
```unknown
</CodeGroup>

## Usage overview

To enable MCP:

* Upgrade to use langgraph-api>=0.2.3. If you are deploying LangSmith, this will be done for you automatically if you create a new revision.
* MCP tools (agents) will be automatically exposed.
* Connect with any MCP-compliant client that supports Streamable HTTP.

### Client

Use an MCP-compliant client to connect to the LangGraph server. The following examples show how to connect using different programming languages.

<Tabs>
  <Tab title="JavaScript/TypeScript">
```

Example 4 (unknown):
```unknown
> **Note**
    > Replace `serverUrl` with your LangGraph server URL and configure authentication headers as needed.
```

---

## Execute tool and create result message

**URL:** llms-txt#execute-tool-and-create-result-message

weather_result = "Sunny, 72°F"
tool_message = ToolMessage(
    content=weather_result,
    tool_call_id="call_123"  # Must match the call ID
)

---

## ./src/agent/webapp.py

**URL:** llms-txt#./src/agent/webapp.py

**Contents:**
- Configure `langgraph.json`
- Start server
- Deploying
- Next steps

from fastapi import FastAPI

@app.get("/hello")
def read_root():
    return {"Hello": "World"}

json  theme={null}
{
  "dependencies": ["."],
  "graphs": {
    "agent": "./src/agent/graph.py:graph"
  },
  "env": ".env",
  "http": {
    "app": "./src/agent/webapp.py:app"
  }
  // Other configuration options like auth, store, etc.
}
bash  theme={null}
langgraph dev --no-browser
```

If you navigate to `localhost:2024/hello` in your browser (`2024` is the default development port), you should see the `/hello` endpoint returning `{"Hello": "World"}`.

<Note>
  **Shadowing default endpoints**
  The routes you create in the app are given priority over the system defaults, meaning you can shadow and redefine the behavior of any default endpoint.
</Note>

You can deploy this app as-is to LangSmith or to your self-hosted platform.

Now that you've added a custom route to your deployment, you can use this same technique to further customize how your server behaves, such as defining custom [custom middleware](/langsmith/custom-middleware) and [custom lifespan events](/langsmith/custom-lifespan).

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/langsmith/custom-routes.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

**Examples:**

Example 1 (unknown):
```unknown
## Configure `langgraph.json`

Add the following to your `langgraph.json` configuration file. Make sure the path points to the FastAPI application instance `app` in the `webapp.py` file you created above.
```

Example 2 (unknown):
```unknown
## Start server

Test the server out locally:
```

---

## After model hook

**URL:** llms-txt#after-model-hook

@after_model
def log_after_model(state: AgentState, runtime: Runtime[Context]) -> dict | None:  # [!code highlight]
    print(f"Completed request for user: {runtime.context.user_name}")  # [!code highlight]
    return None

agent = create_agent(
    model="openai:gpt-5-nano",
    tools=[...],
    middleware=[dynamic_system_prompt, log_before_model, log_after_model],  # [!code highlight]
    context_schema=Context
)

agent.invoke(
    {"messages": [{"role": "user", "content": "What's my name?"}]},
    context=Context(user_name="John Smith")
)
```

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/runtime.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

---

## Optional. You can swap Tavily for the free DuckDuckGo search tool if preferred.

**URL:** llms-txt#optional.-you-can-swap-tavily-for-the-free-duckduckgo-search-tool-if-preferred.

---

## Assumes you're in an interactive Python environmentfrom IPython.display import Image, display ...

**URL:** llms-txt#assumes-you're-in-an-interactive-python-environmentfrom-ipython.display-import-image,-display-...

python  theme={null}
from langchain.embeddings import init_embeddings
from langchain.tools import tool
from langchain_core.vectorstores import InMemoryVectorStore
from langchain.agents import create_agent

**Examples:**

Example 1 (unknown):
```unknown
<img src="https://mintcdn.com/langchain-5e9cc07a/Fr2lazPB4XVeEA7l/langsmith/images/refund-graph.png?fit=max&auto=format&n=Fr2lazPB4XVeEA7l&q=85&s=a65951850208fd3b03848629bdda8ae0" alt="Refund graph" data-og-width="256" width="256" data-og-height="333" height="333" data-path="langsmith/images/refund-graph.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/Fr2lazPB4XVeEA7l/langsmith/images/refund-graph.png?w=280&fit=max&auto=format&n=Fr2lazPB4XVeEA7l&q=85&s=8817f44b37322ab9a51fd01ee7902181 280w, https://mintcdn.com/langchain-5e9cc07a/Fr2lazPB4XVeEA7l/langsmith/images/refund-graph.png?w=560&fit=max&auto=format&n=Fr2lazPB4XVeEA7l&q=85&s=753a20158640cbeeeb81498d5c5ae95d 560w, https://mintcdn.com/langchain-5e9cc07a/Fr2lazPB4XVeEA7l/langsmith/images/refund-graph.png?w=840&fit=max&auto=format&n=Fr2lazPB4XVeEA7l&q=85&s=8d38bcff07b53e1f5648b3dd45cffa66 840w, https://mintcdn.com/langchain-5e9cc07a/Fr2lazPB4XVeEA7l/langsmith/images/refund-graph.png?w=1100&fit=max&auto=format&n=Fr2lazPB4XVeEA7l&q=85&s=50a7f863cf45d9df7b59cc3614fdb4e9 1100w, https://mintcdn.com/langchain-5e9cc07a/Fr2lazPB4XVeEA7l/langsmith/images/refund-graph.png?w=1650&fit=max&auto=format&n=Fr2lazPB4XVeEA7l&q=85&s=cfbda86ec83a651bfe8e38235579302d 1650w, https://mintcdn.com/langchain-5e9cc07a/Fr2lazPB4XVeEA7l/langsmith/images/refund-graph.png?w=2500&fit=max&auto=format&n=Fr2lazPB4XVeEA7l&q=85&s=56745d2e7603dca7fa233e1fd5818008 2500w" />

#### Lookup agent

For the lookup (i.e. question-answering) agent, we'll use a simple ReACT architecture and give the agent tools for looking up track names, artist names, and album names based on various filters. For example, you can look up albums by a particular artist, artists who released songs with a specific name, etc.
```

---

## This means that after 'tools' is called, 'agent' node is called next.

**URL:** llms-txt#this-means-that-after-'tools'-is-called,-'agent'-node-is-called-next.

workflow.add_edge("tools", 'agent')

---

## Evaluate a complex agent

**URL:** llms-txt#evaluate-a-complex-agent

**Contents:**
- Setup
  - Configure the environment
  - Download the database

Source: https://docs.langchain.com/langsmith/evaluate-complex-agent

<Info>
  [Agent evaluation](/langsmith/evaluation-concepts#agents) | [Evaluators](/langsmith/evaluation-concepts#evaluators) | [LLM-as-judge evaluators](/langsmith/evaluation-concepts#llm-as-judge)
</Info>

In this tutorial, we'll build a customer support bot that helps users navigate a digital music store. Then, we'll go through the three most effective types of evaluations to run on chat bots:

* [Final response](/langsmith/evaluation-concepts#evaluating-an-agents-final-response): Evaluate the agent's final response.
* [Trajectory](/langsmith/evaluation-concepts#evaluating-an-agents-trajectory): Evaluate whether the agent took the expected path (e.g., of tool calls) to arrive at the final answer.
* [Single step](/langsmith/evaluation-concepts#evaluating-a-single-step-of-an-agent): Evaluate any agent step in isolation (e.g., whether it selects the appropriate first tool for a given step).

We'll build our agent using [LangGraph](https://github.com/langchain-ai/langgraph), but the techniques and LangSmith functionality shown here are framework-agnostic.

### Configure the environment

Let's install the required dependencies:

Let's set up environment variables for OpenAI and [LangSmith](https://smith.langchain.com):

### Download the database

We will create a SQLite database for this tutorial. SQLite is a lightweight database that is easy to set up and use. We will load the `chinook` database, which is a sample database that represents a digital media store. Find more information about the database [here](https://www.sqlitetutorial.net/sqlite-sample-database/).

For convenience, we have hosted the database in a public GCS bucket:

Here's a sample of the data in the db:

```python  theme={null}
import sqlite3

**Examples:**

Example 1 (unknown):
```unknown

```

Example 2 (unknown):
```unknown
</CodeGroup>

Let's set up environment variables for OpenAI and [LangSmith](https://smith.langchain.com):
```

Example 3 (unknown):
```unknown
### Download the database

We will create a SQLite database for this tutorial. SQLite is a lightweight database that is easy to set up and use. We will load the `chinook` database, which is a sample database that represents a digital media store. Find more information about the database [here](https://www.sqlitetutorial.net/sqlite-sample-database/).

For convenience, we have hosted the database in a public GCS bucket:
```

Example 4 (unknown):
```unknown
Here's a sample of the data in the db:
```

---

## Set the entrypoint as 'agent'

**URL:** llms-txt#set-the-entrypoint-as-'agent'

---

## Write sample data to the store using the put method

**URL:** llms-txt#write-sample-data-to-the-store-using-the-put-method

store.put( # [!code highlight]
    ("users",),  # Namespace to group related data together (users namespace for user data)
    "user_123",  # Key within the namespace (user ID as key)
    {
        "name": "John Smith",
        "language": "English",
    }  # Data to store for the given user
)

@tool
def get_user_info(runtime: ToolRuntime[Context]) -> str:
    """Look up user info."""
    # Access the store - same as that provided to `create_agent`
    store = runtime.store # [!code highlight]
    user_id = runtime.context.user_id
    # Retrieve data from store - returns StoreValue object with value and metadata
    user_info = store.get(("users",), user_id) # [!code highlight]
    return str(user_info.value) if user_info else "Unknown user"

agent = create_agent(
    model="anthropic:claude-sonnet-4-5",
    tools=[get_user_info],
    # Pass store to agent - enables agent to access store when running tools
    store=store, # [!code highlight]
    context_schema=Context
)

---

## Human-in-the-loop using server API

**URL:** llms-txt#human-in-the-loop-using-server-api

**Contents:**
- Dynamic interrupts
- Static interrupts
- Learn more

Source: https://docs.langchain.com/langsmith/add-human-in-the-loop

To review, edit, and approve tool calls in an agent or workflow, use LangGraph's [human-in-the-loop](/oss/python/langgraph/interrupts) features.

## Dynamic interrupts

<Tabs>
  <Tab title="Python">

1. The graph is invoked with some initial state.
    2. When the graph hits the interrupt, it returns an interrupt object with the payload and metadata.
       3\. The graph is resumed with a `Command(resume=...)`, injecting the human's input and continuing execution.
  </Tab>

<Tab title="JavaScript">

1. The graph is invoked with some initial state.
    2. When the graph hits the interrupt, it returns an interrupt object with the payload and metadata.
    3. The graph is resumed with a `{ resume: ... }` command object, injecting the human's input and continuing execution.
  </Tab>

<Tab title="cURL">
    Create a thread:

Run the graph until the interrupt is hit.:

<Accordion title="Extended example: using `interrupt`">
  This is an example graph you can run in the LangGraph API server.
  See [LangSmith quickstart](/langsmith/deployment-quickstart) for more details.

1. `interrupt(...)` pauses execution at `human_node`, surfacing the given payload to a human.
  2. Any JSON serializable value can be passed to the [`interrupt`](https://reference.langchain.com/python/langgraph/types/#langgraph.types.interrupt) function. Here, a dict containing the text to revise.
  3. Once resumed, the return value of `interrupt(...)` is the human-provided input, which is used to update the state.

Once you have a running LangGraph API server, you can interact with it using
  [LangGraph SDK](/langsmith/langgraph-python-sdk)

<Tabs>
    <Tab title="Python">

1. The graph is invoked with some initial state.
      2. When the graph hits the interrupt, it returns an interrupt object with the payload and metadata.
         3\. The graph is resumed with a `Command(resume=...)`, injecting the human's input and continuing execution.
    </Tab>

<Tab title="JavaScript">

1. The graph is invoked with some initial state.
      2. When the graph hits the interrupt, it returns an interrupt object with the payload and metadata.
      3. The graph is resumed with a `{ resume: ... }` command object, injecting the human's input and continuing execution.
    </Tab>

<Tab title="cURL">
      Create a thread:

Run the graph until the interrupt is hit:

</Tab>
  </Tabs>
</Accordion>

Static interrupts (also known as static breakpoints) are triggered either before or after a node executes.

<Warning>
  Static interrupts are **not** recommended for human-in-the-loop workflows. They are best used for debugging and testing.
</Warning>

You can set static interrupts by specifying `interrupt_before` and `interrupt_after` at compile time:

1. The breakpoints are set during `compile` time.
2. `interrupt_before` specifies the nodes where execution should pause before the node is executed.
3. `interrupt_after` specifies the nodes where execution should pause after the node is executed.

Alternatively, you can set static interrupts at run time:

<Tabs>
  <Tab title="Python">

1. `client.runs.wait` is called with the `interrupt_before` and `interrupt_after` parameters. This is a run-time configuration and can be changed for every invocation.
    2. `interrupt_before` specifies the nodes where execution should pause before the node is executed.
    3. `interrupt_after` specifies the nodes where execution should pause after the node is executed.
  </Tab>

<Tab title="JavaScript">

1. `client.runs.wait` is called with the `interruptBefore` and `interruptAfter` parameters. This is a run-time configuration and can be changed for every invocation.
    2. `interruptBefore` specifies the nodes where execution should pause before the node is executed.
    3. `interruptAfter` specifies the nodes where execution should pause after the node is executed.
  </Tab>

<Tab title="cURL">
    
  </Tab>
</Tabs>

The following example shows how to add static interrupts:

<Tabs>
  <Tab title="Python">

1. The graph is run until the first breakpoint is hit.
    2. The graph is resumed by passing in `None` for the input. This will run the graph until the next breakpoint is hit.
  </Tab>

<Tab title="JavaScript">

1. The graph is run until the first breakpoint is hit.
    2. The graph is resumed by passing in `null` for the input. This will run the graph until the next breakpoint is hit.
  </Tab>

<Tab title="cURL">
    Create a thread:

Run the graph until the breakpoint:

* [Human-in-the-loop conceptual guide](/oss/python/langgraph/interrupts): learn more about LangGraph human-in-the-loop features.
* [Common patterns](/oss/python/langgraph/interrupts#common-patterns): learn how to implement patterns like approving/rejecting actions, requesting user input, tool call review, and validating human input.

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/langsmith/add-human-in-the-loop.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

**Examples:**

Example 1 (unknown):
```unknown
1. The graph is invoked with some initial state.
    2. When the graph hits the interrupt, it returns an interrupt object with the payload and metadata.
       3\. The graph is resumed with a `Command(resume=...)`, injecting the human's input and continuing execution.
  </Tab>

  <Tab title="JavaScript">
```

Example 2 (unknown):
```unknown
1. The graph is invoked with some initial state.
    2. When the graph hits the interrupt, it returns an interrupt object with the payload and metadata.
    3. The graph is resumed with a `{ resume: ... }` command object, injecting the human's input and continuing execution.
  </Tab>

  <Tab title="cURL">
    Create a thread:
```

Example 3 (unknown):
```unknown
Run the graph until the interrupt is hit.:
```

Example 4 (unknown):
```unknown
Resume the graph:
```

---

## Note: GooglePlacesTool might be in langchain or langchain_community depending on version

**URL:** llms-txt#note:-googleplacestool-might-be-in-langchain-or-langchain_community-depending-on-version

**Contents:**
  - Toolkits

from langchain.tools import GooglePlacesTool # Or langchain_community.tools
bash  theme={null}
  pip install google-search-results langchain-community # Requires langchain-community
  bash uv theme={null}
  uv add google-search-results langchain-community # Requires langchain-community
  python  theme={null}
from langchain_community.tools.google_scholar import GoogleScholarQueryRun
from langchain_community.utilities.google_scholar import GoogleScholarAPIWrapper
bash pip theme={null}
  pip install langchain-google-community
  bash uv theme={null}
  uv add langchain-google-community
  python  theme={null}
from langchain_google_community import GoogleSearchAPIWrapper
python  theme={null}
from langchain_community.tools import GoogleSearchRun, GoogleSearchResults
python  theme={null}
from langchain_community.agent_toolkits.load_tools import load_tools
tools = load_tools(["google-search"])
bash pip theme={null}
  pip install google-search-results langchain-community # Requires langchain-community
  bash uv theme={null}
  uv add google-search-results langchain-community # Requires langchain-community
  python  theme={null}
from langchain_community.tools.google_trends import GoogleTrendsQueryRun
from langchain_community.utilities.google_trends import GoogleTrendsAPIWrapper
bash pip theme={null}
  pip install langchain-google-community[gmail]
  bash uv theme={null}
  uv add langchain-google-community[gmail]
  python  theme={null}

**Examples:**

Example 1 (unknown):
```unknown
#### Google Scholar

Search academic papers. Requires `google-search-results` package and SerpApi key.

<CodeGroup>
```

Example 2 (unknown):
```unknown

```

Example 3 (unknown):
```unknown
</CodeGroup>

See [usage example and authorization instructions](/oss/python/integrations/tools/google_scholar).
```

Example 4 (unknown):
```unknown
#### Google Search

Perform web searches using Google Custom Search Engine (CSE). Requires `GOOGLE_API_KEY` and `GOOGLE_CSE_ID`.

Install `langchain-google-community`:

<CodeGroup>
```

---

## Use it as a custom subagent

**URL:** llms-txt#use-it-as-a-custom-subagent

**Contents:**
- The general-purpose subagent
  - When to use it
- Best practices
  - Write clear descriptions
  - Keep system prompts detailed
  - Minimize tool sets

custom_subagent = CompiledSubAgent(
    name="data-analyzer",
    description="Specialized agent for complex data analysis tasks",
    runnable=custom_graph
)

subagents = [custom_subagent]

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-20250514",
    tools=[internet_search],
    system_prompt=research_instructions,
    subagents=subagents
)
python  theme={null}
research_subagent = {
    "name": "research-agent",
    "description": "Conducts in-depth research using web search and synthesizes findings",
    "system_prompt": """You are a thorough researcher. Your job is to:

1. Break down the research question into searchable queries
    2. Use internet_search to find relevant information
    3. Synthesize findings into a comprehensive but concise summary
    4. Cite sources when making claims

Output format:
    - Summary (2-3 paragraphs)
    - Key findings (bullet points)
    - Sources (with URLs)

Keep your response under 500 words to maintain clean context.""",
    "tools": [internet_search],
}
python  theme={null}

**Examples:**

Example 1 (unknown):
```unknown
## The general-purpose subagent

In addition to any user-defined subagents, deep agents have access to a `general-purpose` subagent at all times. This subagent:

* Has the same system prompt as the main agent
* Has access to all the same tools
* Uses the same model (unless overridden)

### When to use it

The general-purpose subagent is ideal for context isolation without specialized behavior. The main agent can delegate a complex multi-step task to this subagent and get a concise result back without bloat from intermediate tool calls.

<Card title="Example">
  Instead of the main agent making 10 web searches and filling its context with results, it delegates to the general-purpose subagent: `task(name="general-purpose", task="Research quantum computing trends")`. The subagent performs all the searches internally and returns only a summary.
</Card>

## Best practices

### Write clear descriptions

The main agent uses descriptions to decide which subagent to call. Be specific:

✅ **Good:** `"Analyzes financial data and generates investment insights with confidence scores"`

❌ **Bad:** `"Does finance stuff"`

### Keep system prompts detailed

Include specific guidance on how to use tools and format outputs:
```

Example 2 (unknown):
```unknown
### Minimize tool sets

Only give subagents the tools they need. This improves focus and security:
```

---

## Application-specific evaluation approaches

**URL:** llms-txt#application-specific-evaluation-approaches

**Contents:**
- Agents
  - Evaluating an agent's final response
  - Evaluating a single step of an agent
  - Evaluating an agent's trajectory
- Retrieval augmented generation (RAG)
  - Dataset
  - Evaluator
  - Applying RAG Evaluation
  - RAG evaluation summary
- Summarization

Source: https://docs.langchain.com/langsmith/evaluation-approaches

Below, we will discuss evaluation of a few popular types of LLM applications.

[LLM-powered autonomous agents](https://lilianweng.github.io/posts/2023-06-23-agent/) combine three components (1) Tool calling, (2) Memory, and (3) Planning. Agents [use tool calling](https://python.langchain.com/v0.1/docs/modules/agents/agent_types/tool_calling/) with planning (e.g., often via prompting) and memory (e.g., often short-term message history) to generate responses. [Tool calling](https://python.langchain.com/v0.1/docs/modules/model_io/chat/function_calling/) allows a model to respond to a given prompt by generating two things: (1) a tool to invoke and (2) the input arguments required.

<img src="https://mintcdn.com/langchain-5e9cc07a/ImHGLQW1HnQYwnJV/langsmith/images/tool-use.png?fit=max&auto=format&n=ImHGLQW1HnQYwnJV&q=85&s=a1c10f940f40ad89c90de8fae3607c1f" alt="Tool use" data-og-width="1021" width="1021" data-og-height="424" height="424" data-path="langsmith/images/tool-use.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/ImHGLQW1HnQYwnJV/langsmith/images/tool-use.png?w=280&fit=max&auto=format&n=ImHGLQW1HnQYwnJV&q=85&s=e80012647614cd82cb468430e62fa9aa 280w, https://mintcdn.com/langchain-5e9cc07a/ImHGLQW1HnQYwnJV/langsmith/images/tool-use.png?w=560&fit=max&auto=format&n=ImHGLQW1HnQYwnJV&q=85&s=67a5febcec316bfe2935ba65506558a2 560w, https://mintcdn.com/langchain-5e9cc07a/ImHGLQW1HnQYwnJV/langsmith/images/tool-use.png?w=840&fit=max&auto=format&n=ImHGLQW1HnQYwnJV&q=85&s=e0b52fb90bdbc41332b09404823fbfca 840w, https://mintcdn.com/langchain-5e9cc07a/ImHGLQW1HnQYwnJV/langsmith/images/tool-use.png?w=1100&fit=max&auto=format&n=ImHGLQW1HnQYwnJV&q=85&s=8a4e6b4bda0f788f540ca240012c9e89 1100w, https://mintcdn.com/langchain-5e9cc07a/ImHGLQW1HnQYwnJV/langsmith/images/tool-use.png?w=1650&fit=max&auto=format&n=ImHGLQW1HnQYwnJV&q=85&s=d403f18524e0904c716d0cba9e928cac 1650w, https://mintcdn.com/langchain-5e9cc07a/ImHGLQW1HnQYwnJV/langsmith/images/tool-use.png?w=2500&fit=max&auto=format&n=ImHGLQW1HnQYwnJV&q=85&s=69133b8862e6738000f733ff7e34daae 2500w" />

Below is a tool-calling agent in [LangGraph](https://langchain-ai.github.io/langgraph/tutorials/introduction/). The `assistant node` is an LLM that determines whether to invoke a tool based upon the input. The `tool condition` sees if a tool was selected by the `assistant node` and, if so, routes to the `tool node`. The `tool node` executes the tool and returns the output as a tool message to the `assistant node`. This loop continues until as long as the `assistant node` selects a tool. If no tool is selected, then the agent directly returns the LLM response.

<img src="https://mintcdn.com/langchain-5e9cc07a/4kN8yiLrZX_amfFn/langsmith/images/langgraph-agent.png?fit=max&auto=format&n=4kN8yiLrZX_amfFn&q=85&s=37f3c09958c1e2543f633c59cc89df36" alt="Agent" data-og-width="1259" width="1259" data-og-height="492" height="492" data-path="langsmith/images/langgraph-agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/4kN8yiLrZX_amfFn/langsmith/images/langgraph-agent.png?w=280&fit=max&auto=format&n=4kN8yiLrZX_amfFn&q=85&s=59cecf5d27098da369bbf60d6a315437 280w, https://mintcdn.com/langchain-5e9cc07a/4kN8yiLrZX_amfFn/langsmith/images/langgraph-agent.png?w=560&fit=max&auto=format&n=4kN8yiLrZX_amfFn&q=85&s=81426ee5f37211859c572fe51d837c44 560w, https://mintcdn.com/langchain-5e9cc07a/4kN8yiLrZX_amfFn/langsmith/images/langgraph-agent.png?w=840&fit=max&auto=format&n=4kN8yiLrZX_amfFn&q=85&s=558ca3297a7697a12989f0bdcfd4a4d7 840w, https://mintcdn.com/langchain-5e9cc07a/4kN8yiLrZX_amfFn/langsmith/images/langgraph-agent.png?w=1100&fit=max&auto=format&n=4kN8yiLrZX_amfFn&q=85&s=39a3a80c152f99f133302fe79f4bf63d 1100w, https://mintcdn.com/langchain-5e9cc07a/4kN8yiLrZX_amfFn/langsmith/images/langgraph-agent.png?w=1650&fit=max&auto=format&n=4kN8yiLrZX_amfFn&q=85&s=46164054792e7f730cef4897fd9cbf57 1650w, https://mintcdn.com/langchain-5e9cc07a/4kN8yiLrZX_amfFn/langsmith/images/langgraph-agent.png?w=2500&fit=max&auto=format&n=4kN8yiLrZX_amfFn&q=85&s=553d05e97a4d052882b6381e1e8b0362 2500w" />

This sets up three general types of agent evaluations that users are often interested in:

* `Final Response`: Evaluate the agent's final response.
* `Single step`: Evaluate any agent step in isolation (e.g., whether it selects the appropriate tool).
* `Trajectory`: Evaluate whether the agent took the expected path (e.g., of tool calls) to arrive at the final answer.

<img src="https://mintcdn.com/langchain-5e9cc07a/E8FdemkcQxROovD9/langsmith/images/agent-eval.png?fit=max&auto=format&n=E8FdemkcQxROovD9&q=85&s=5fe3c96402623ed8a61118f22a6426b6" alt="Agent-eval" data-og-width="1825" width="1825" data-og-height="915" height="915" data-path="langsmith/images/agent-eval.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/E8FdemkcQxROovD9/langsmith/images/agent-eval.png?w=280&fit=max&auto=format&n=E8FdemkcQxROovD9&q=85&s=780c3ea6fecdbd41fa62017d3ac6042e 280w, https://mintcdn.com/langchain-5e9cc07a/E8FdemkcQxROovD9/langsmith/images/agent-eval.png?w=560&fit=max&auto=format&n=E8FdemkcQxROovD9&q=85&s=f43c0cd9d9b49ae1f2a7ead5f5e58bcd 560w, https://mintcdn.com/langchain-5e9cc07a/E8FdemkcQxROovD9/langsmith/images/agent-eval.png?w=840&fit=max&auto=format&n=E8FdemkcQxROovD9&q=85&s=360b12b491fb97fd46d444e440345737 840w, https://mintcdn.com/langchain-5e9cc07a/E8FdemkcQxROovD9/langsmith/images/agent-eval.png?w=1100&fit=max&auto=format&n=E8FdemkcQxROovD9&q=85&s=88fd055136cd48a538d908e3899daa6e 1100w, https://mintcdn.com/langchain-5e9cc07a/E8FdemkcQxROovD9/langsmith/images/agent-eval.png?w=1650&fit=max&auto=format&n=E8FdemkcQxROovD9&q=85&s=c3e40f0ba26f26f2688553596487ab57 1650w, https://mintcdn.com/langchain-5e9cc07a/E8FdemkcQxROovD9/langsmith/images/agent-eval.png?w=2500&fit=max&auto=format&n=E8FdemkcQxROovD9&q=85&s=7b238d8ce02b6d1ab3d6ff3fb2c62d4e 2500w" />

Below we will cover what these are, the components (inputs, outputs, evaluators) needed for each one, and when you should consider this. Note that you likely will want to do multiple (if not all!) of these types of evaluations - they are not mutually exclusive!

### Evaluating an agent's final response

One way to evaluate an agent is to assess its overall performance on a task. This basically involves treating the agent as a black box and simply evaluating whether or not it gets the job done.

The inputs should be the user input and (optionally) a list of tools. In some cases, tool are hardcoded as part of the agent and they don't need to be passed in. In other cases, the agent is more generic, meaning it does not have a fixed set of tools and tools need to be passed in at run time.

The output should be the agent's final response.

The evaluator varies depending on the task you are asking the agent to do. Many agents perform a relatively complex set of steps and the output a final text response. Similar to RAG, LLM-as-judge evaluators are often effective for evaluation in these cases because they can assess whether the agent got a job done directly from the text response.

However, there are several downsides to this type of evaluation. First, it usually takes a while to run. Second, you are not evaluating anything that happens inside the agent, so it can be hard to debug when failures occur. Third, it can sometimes be hard to define appropriate evaluation metrics.

### Evaluating a single step of an agent

Agents generally perform multiple actions. While it is useful to evaluate them end-to-end, it can also be useful to evaluate these individual actions. This generally involves evaluating a single step of the agent - the LLM call where it decides what to do.

The inputs should be the input to a single step. Depending on what you are testing, this could just be the raw user input (e.g., a prompt and / or a set of tools) or it can also include previously completed steps.

The outputs are just the output of that step, which is usually the LLM response. The LLM response often contains tool calls, indicating what action the agent should take next.

The evaluator for this is usually some binary score for whether the correct tool call was selected, as well as some heuristic for whether the input to the tool was correct. The reference tool can be simply specified as a string.

There are several benefits to this type of evaluation. It allows you to evaluate individual actions, which lets you hone in where your application may be failing. They are also relatively fast to run (because they only involve a single LLM call) and evaluation often uses simple heuristic evaluation of the selected tool relative to the reference tool. One downside is that they don't capture the full agent - only one particular step. Another downside is that dataset creation can be challenging, particular if you want to include past history in the agent input. It is pretty easy to generate a dataset for steps early on in an agent's trajectory (e.g., this may only include the input prompt), but it can be difficult to generate a dataset for steps later on in the trajectory (e.g., including numerous prior agent actions and responses).

### Evaluating an agent's trajectory

Evaluating an agent's trajectory involves evaluating all the steps an agent took.

The inputs are again the inputs to the overall agent (the user input, and optionally a list of tools).

The outputs are a list of tool calls, which can be formulated as an "exact" trajectory (e.g., an expected sequence of tool calls) or simply a set of tool calls that are expected (in any order).

The evaluator here is some function over the steps taken. Assessing the "exact" trajectory can use a single binary score that confirms an exact match for each tool name in the sequence. This is simple, but has some flaws. Sometimes there can be multiple correct paths. This evaluation also does not capture the difference between a trajectory being off by a single step versus being completely wrong.

To address these flaws, evaluation metrics can focused on the number of "incorrect" steps taken, which better accounts for trajectories that are close versus ones that deviate significantly. Evaluation metrics can also focus on whether all of the expected tools are called in any order.

However, none of these approaches evaluate the input to the tools; they only focus on the tools selected. In order to account for this, another evaluation technique is to pass the full agent's trajectory (along with a reference trajectory) as a set of messages (e.g., all LLM responses and tool calls) an LLM-as-judge. This can evaluate the complete behavior of the agent, but it is the most challenging reference to compile (luckily, using a framework like LangGraph can help with this!). Another downside is that evaluation metrics can be somewhat tricky to come up with.

## Retrieval augmented generation (RAG)

Retrieval Augmented Generation (RAG) is a powerful technique that involves retrieving relevant documents based on a user's input and passing them to a language model for processing. RAG enables AI applications to generate more informed and context-aware responses by leveraging external knowledge.

<Info>
  For a comprehensive review of RAG concepts, see our [`RAG From Scratch` series](https://github.com/langchain-ai/rag-from-scratch).
</Info>

When evaluating RAG applications, a key consideration is whether you have (or can easily obtain) reference answers for each input question. Reference answers serve as ground truth for assessing the correctness of the generated responses. However, even in the absence of reference answers, various evaluations can still be performed using reference-free RAG evaluation prompts (examples provided below).

`LLM-as-judge` is a commonly used evaluator for RAG because it's an effective way to evaluate factual accuracy or consistency between texts.

<img src="https://mintcdn.com/langchain-5e9cc07a/Fr2lazPB4XVeEA7l/langsmith/images/rag-types.png?fit=max&auto=format&n=Fr2lazPB4XVeEA7l&q=85&s=1252b1369be04ddb4c480af277443ac2" alt="rag-types.png" data-og-width="1696" width="1696" data-og-height="731" height="731" data-path="langsmith/images/rag-types.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/Fr2lazPB4XVeEA7l/langsmith/images/rag-types.png?w=280&fit=max&auto=format&n=Fr2lazPB4XVeEA7l&q=85&s=dda9fa7e589b9d37bd31a5ba63d1f0fb 280w, https://mintcdn.com/langchain-5e9cc07a/Fr2lazPB4XVeEA7l/langsmith/images/rag-types.png?w=560&fit=max&auto=format&n=Fr2lazPB4XVeEA7l&q=85&s=e16fca6e49aeb889cc9d6e04baca684a 560w, https://mintcdn.com/langchain-5e9cc07a/Fr2lazPB4XVeEA7l/langsmith/images/rag-types.png?w=840&fit=max&auto=format&n=Fr2lazPB4XVeEA7l&q=85&s=de442b611295218493a5783820794727 840w, https://mintcdn.com/langchain-5e9cc07a/Fr2lazPB4XVeEA7l/langsmith/images/rag-types.png?w=1100&fit=max&auto=format&n=Fr2lazPB4XVeEA7l&q=85&s=ad286f13e4a15ec892f5995a539daf5d 1100w, https://mintcdn.com/langchain-5e9cc07a/Fr2lazPB4XVeEA7l/langsmith/images/rag-types.png?w=1650&fit=max&auto=format&n=Fr2lazPB4XVeEA7l&q=85&s=64c7b545e34ac5d4bf975ee2f44af8df 1650w, https://mintcdn.com/langchain-5e9cc07a/Fr2lazPB4XVeEA7l/langsmith/images/rag-types.png?w=2500&fit=max&auto=format&n=Fr2lazPB4XVeEA7l&q=85&s=447cb995acde1f42ffeee2883c61a033 2500w" />

When evaluating RAG applications, you can have evaluators that require reference outputs and those that don't:

1. **Require reference output**: Compare the RAG chain's generated answer or retrievals against a reference answer (or retrievals) to assess its correctness.
2. **Don't require reference output**: Perform self-consistency checks using prompts that don't require a reference answer (represented by orange, green, and red in the above figure).

### Applying RAG Evaluation

When applying RAG evaluation, consider the following approaches:

1. `Offline evaluation`: Use offline evaluation for any prompts that rely on a reference answer. This is most commonly used for RAG answer correctness evaluation, where the reference is a ground truth (correct) answer.

2. `Online evaluation`: Employ online evaluation for any reference-free prompts. This allows you to assess the RAG application's performance in real-time scenarios.

3. `Pairwise evaluation`: Utilize pairwise evaluation to compare answers produced by different RAG chains. This evaluation focuses on user-specified criteria (e.g., answer format or style) rather than correctness, which can be evaluated using self-consistency or a ground truth reference.

### RAG evaluation summary

| Evaluator           | Detail                                            | Needs reference output | LLM-as-judge?                                                                         | Pairwise relevant |
| ------------------- | ------------------------------------------------- | ---------------------- | ------------------------------------------------------------------------------------- | ----------------- |
| Document relevance  | Are documents relevant to the question?           | No                     | Yes - [prompt](https://smith.langchain.com/hub/langchain-ai/rag-document-relevance)   | No                |
| Answer faithfulness | Is the answer grounded in the documents?          | No                     | Yes - [prompt](https://smith.langchain.com/hub/langchain-ai/rag-answer-hallucination) | No                |
| Answer helpfulness  | Does the answer help address the question?        | No                     | Yes - [prompt](https://smith.langchain.com/hub/langchain-ai/rag-answer-helpfulness)   | No                |
| Answer correctness  | Is the answer consistent with a reference answer? | Yes                    | Yes - [prompt](https://smith.langchain.com/hub/langchain-ai/rag-answer-vs-reference)  | No                |
| Pairwise comparison | How do multiple answer versions compare?          | No                     | Yes - [prompt](https://smith.langchain.com/hub/langchain-ai/pairwise-evaluation-rag)  | Yes               |

Summarization is one specific type of free-form writing. The evaluation aim is typically to examine the writing (summary) relative to a set of criteria.

`Developer curated examples` of texts to summarize are commonly used for evaluation (see a dataset example [here](https://smith.langchain.com/public/659b07af-1cab-4e18-b21a-91a69a4c3990/d)). However, `user logs` from a production (summarization) app can be used for online evaluation with any of the `Reference-free` evaluation prompts below.

`LLM-as-judge` is typically used for evaluation of summarization (as well as other types of writing) using `Reference-free` prompts that follow provided criteria to grade a summary. It is less common to provide a particular `Reference` summary, because summarization is a creative task and there are many possible correct answers.

`Online` or `Offline` evaluation are feasible because of the `Reference-free` prompt used. `Pairwise` evaluation is also a powerful way to perform comparisons between different summarization chains (e.g., different summarization prompts or LLMs):

| Use Case         | Detail                                                                     | Needs reference output | LLM-as-judge?                                                                                | Pairwise relevant |
| ---------------- | -------------------------------------------------------------------------- | ---------------------- | -------------------------------------------------------------------------------------------- | ----------------- |
| Factual accuracy | Is the summary accurate relative to the source documents?                  | No                     | Yes - [prompt](https://smith.langchain.com/hub/langchain-ai/summary-accurancy-evaluator)     | Yes               |
| Faithfulness     | Is the summary grounded in the source documents (e.g., no hallucinations)? | No                     | Yes - [prompt](https://smith.langchain.com/hub/langchain-ai/summary-hallucination-evaluator) | Yes               |
| Helpfulness      | Is summary helpful relative to user need?                                  | No                     | Yes - [prompt](https://smith.langchain.com/hub/langchain-ai/summary-helpfulness-evaluator)   | Yes               |

## Classification and tagging

Classification and tagging apply a label to a given input (e.g., for toxicity detection, sentiment analysis, etc). Classification/tagging evaluation typically employs the following components, which we will review in detail below:

A central consideration for classification/tagging evaluation is whether you have a dataset with `reference` labels or not. If not, users frequently want to define an evaluator that uses criteria to apply label (e.g., toxicity, etc) to an input (e.g., text, user-question, etc). However, if ground truth class labels are provided, then the evaluation objective is focused on scoring a classification/tagging chain relative to the ground truth class label (e.g., using metrics such as precision, recall, etc).

If ground truth reference labels are provided, then it's common to simply define a [custom heuristic evaluator](/langsmith/code-evaluator) to compare ground truth labels to the chain output. However, it is increasingly common given the emergence of LLMs simply use `LLM-as-judge` to perform the classification/tagging of an input based upon specified criteria (without a ground truth reference).

`Online` or `Offline` evaluation is feasible when using `LLM-as-judge` with the `Reference-free` prompt used. In particular, this is well suited to `Online` evaluation when a user wants to tag / classify application input (e.g., for toxicity, etc).

| Use Case  | Detail              | Needs reference output | LLM-as-judge? | Pairwise relevant |
| --------- | ------------------- | ---------------------- | ------------- | ----------------- |
| Accuracy  | Standard definition | Yes                    | No            | No                |
| Precision | Standard definition | Yes                    | No            | No                |
| Recall    | Standard definition | Yes                    | No            | No                |

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/langsmith/evaluation-approaches.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

---

## Agent reads /memories/project_notes.txt from previous conversation

**URL:** llms-txt#agent-reads-/memories/project_notes.txt-from-previous-conversation

**Contents:**
  - Research projects
- Store implementations
  - InMemoryStore (development)
  - PostgresStore (production)
- Best practices
  - Use descriptive paths

python  theme={null}
research_agent = create_deep_agent(
    store=store,
    use_longterm_memory=True,
    system_prompt="""You are a research assistant.

Save your research progress to /memories/research/:
    - /memories/research/sources.txt - List of sources found
    - /memories/research/notes.txt - Key findings and notes
    - /memories/research/report.md - Final report draft

This allows research to continue across multiple sessions."""
)
python  theme={null}
from langgraph.store.memory import InMemoryStore

store = InMemoryStore()
agent = create_deep_agent(store=store, use_longterm_memory=True)
python  theme={null}
from langgraph.store.postgres import PostgresStore
import os

store = PostgresStore(connection_string=os.environ["DATABASE_URL"])
agent = create_deep_agent(store=store, use_longterm_memory=True)
python  theme={null}

**Examples:**

Example 1 (unknown):
```unknown
### Research projects

Maintain research state across sessions:
```

Example 2 (unknown):
```unknown
## Store implementations

Any LangGraph `BaseStore` implementation works:

### InMemoryStore (development)

Good for testing and development, but data is lost on restart:
```

Example 3 (unknown):
```unknown
### PostgresStore (production)

For production, use a persistent store:
```

Example 4 (unknown):
```unknown
## Best practices

### Use descriptive paths

Organize long-term files with clear, hierarchical paths:
```

---

## Optional. You can swap OpenAI for any other tool-calling chat model.

**URL:** llms-txt#optional.-you-can-swap-openai-for-any-other-tool-calling-chat-model.

os.environ["OPENAI_API_KEY"] = "YOUR OPENAI API KEY"

---

## We need to pass the `tool_call_id` to the sub agent so it can use it to respond with the tool call result

**URL:** llms-txt#we-need-to-pass-the-`tool_call_id`-to-the-sub-agent-so-it-can-use-it-to-respond-with-the-tool-call-result

def call_subagent1(
    query: str,
    tool_call_id: Annotated[str, InjectedToolCallId],

---

## Second invocation: the first message is persisted (Sydney location), so the model returns GMT+10 time

**URL:** llms-txt#second-invocation:-the-first-message-is-persisted-(sydney-location),-so-the-model-returns-gmt+10-time

**Contents:**
- Integration Testing
  - Installing AgentEvals
  - Trajectory Match Evaluator
  - LLM-as-Judge Evaluator
  - Async Support
- LangSmith Integration
- Recording & Replaying HTTP Calls

agent.invoke(HumanMessage(content="What's my local time?"))
bash  theme={null}
pip install agentevals
python  theme={null}
  from langchain.agents import create_agent
  from langchain.tools import tool
  from langchain.messages import HumanMessage, AIMessage, ToolMessage
  from agentevals.trajectory.match import create_trajectory_match_evaluator

@tool
  def get_weather(city: str):
      """Get weather information for a city."""
      return f"It's 75 degrees and sunny in {city}."

agent = create_agent("openai:gpt-4o", tools=[get_weather])

evaluator = create_trajectory_match_evaluator(  # [!code highlight]
      trajectory_match_mode="strict",  # [!code highlight]
  )  # [!code highlight]

def test_weather_tool_called_strict():
      result = agent.invoke({
          "messages": [HumanMessage(content="What's the weather in San Francisco?")]
      })

reference_trajectory = [
          HumanMessage(content="What's the weather in San Francisco?"),
          AIMessage(content="", tool_calls=[
              {"id": "call_1", "name": "get_weather", "args": {"city": "San Francisco"}}
          ]),
          ToolMessage(content="It's 75 degrees and sunny in San Francisco.", tool_call_id="call_1"),
          AIMessage(content="The weather in San Francisco is 75 degrees and sunny."),
      ]

evaluation = evaluator(
          outputs=result["messages"],
          reference_outputs=reference_trajectory
      )
      # {
      #     'key': 'trajectory_strict_match',
      #     'score': True,
      #     'comment': None,
      # }
      assert evaluation["score"] is True
  python  theme={null}
  from langchain.agents import create_agent
  from langchain.tools import tool
  from langchain.messages import HumanMessage, AIMessage, ToolMessage
  from agentevals.trajectory.match import create_trajectory_match_evaluator

@tool
  def get_weather(city: str):
      """Get weather information for a city."""
      return f"It's 75 degrees and sunny in {city}."

@tool
  def get_events(city: str):
      """Get events happening in a city."""
      return f"Concert at the park in {city} tonight."

agent = create_agent("openai:gpt-4o", tools=[get_weather, get_events])

evaluator = create_trajectory_match_evaluator(  # [!code highlight]
      trajectory_match_mode="unordered",  # [!code highlight]
  )  # [!code highlight]

def test_multiple_tools_any_order():
      result = agent.invoke({
          "messages": [HumanMessage(content="What's happening in SF today?")]
      })

# Reference shows tools called in different order than actual execution
      reference_trajectory = [
          HumanMessage(content="What's happening in SF today?"),
          AIMessage(content="", tool_calls=[
              {"id": "call_1", "name": "get_events", "args": {"city": "SF"}},
              {"id": "call_2", "name": "get_weather", "args": {"city": "SF"}},
          ]),
          ToolMessage(content="Concert at the park in SF tonight.", tool_call_id="call_1"),
          ToolMessage(content="It's 75 degrees and sunny in SF.", tool_call_id="call_2"),
          AIMessage(content="Today in SF: 75 degrees and sunny with a concert at the park tonight."),
      ]

evaluation = evaluator(
          outputs=result["messages"],
          reference_outputs=reference_trajectory,
      )
      # {
      #     'key': 'trajectory_unordered_match',
      #     'score': True,
      # }
      assert evaluation["score"] is True
  python  theme={null}
  from langchain.agents import create_agent
  from langchain.tools import tool
  from langchain.messages import HumanMessage, AIMessage, ToolMessage
  from agentevals.trajectory.match import create_trajectory_match_evaluator

@tool
  def get_weather(city: str):
      """Get weather information for a city."""
      return f"It's 75 degrees and sunny in {city}."

@tool
  def get_detailed_forecast(city: str):
      """Get detailed weather forecast for a city."""
      return f"Detailed forecast for {city}: sunny all week."

agent = create_agent("openai:gpt-4o", tools=[get_weather, get_detailed_forecast])

evaluator = create_trajectory_match_evaluator(  # [!code highlight]
      trajectory_match_mode="superset",  # [!code highlight]
  )  # [!code highlight]

def test_agent_calls_required_tools_plus_extra():
      result = agent.invoke({
          "messages": [HumanMessage(content="What's the weather in Boston?")]
      })

# Reference only requires get_weather, but agent may call additional tools
      reference_trajectory = [
          HumanMessage(content="What's the weather in Boston?"),
          AIMessage(content="", tool_calls=[
              {"id": "call_1", "name": "get_weather", "args": {"city": "Boston"}},
          ]),
          ToolMessage(content="It's 75 degrees and sunny in Boston.", tool_call_id="call_1"),
          AIMessage(content="The weather in Boston is 75 degrees and sunny."),
      ]

evaluation = evaluator(
          outputs=result["messages"],
          reference_outputs=reference_trajectory,
      )
      # {
      #     'key': 'trajectory_superset_match',
      #     'score': True,
      #     'comment': None,
      # }
      assert evaluation["score"] is True
  python  theme={null}
  from langchain.agents import create_agent
  from langchain.tools import tool
  from langchain.messages import HumanMessage, AIMessage, ToolMessage
  from agentevals.trajectory.llm import create_trajectory_llm_as_judge, TRAJECTORY_ACCURACY_PROMPT

@tool
  def get_weather(city: str):
      """Get weather information for a city."""
      return f"It's 75 degrees and sunny in {city}."

agent = create_agent("openai:gpt-4o", tools=[get_weather])

evaluator = create_trajectory_llm_as_judge(  # [!code highlight]
      model="openai:o3-mini",  # [!code highlight]
      prompt=TRAJECTORY_ACCURACY_PROMPT,  # [!code highlight]
  )  # [!code highlight]

def test_trajectory_quality():
      result = agent.invoke({
          "messages": [HumanMessage(content="What's the weather in Seattle?")]
      })

evaluation = evaluator(
          outputs=result["messages"],
      )
      # {
      #     'key': 'trajectory_accuracy',
      #     'score': True,
      #     'comment': 'The provided agent trajectory is reasonable...'
      # }
      assert evaluation["score"] is True
  python  theme={null}
  evaluator = create_trajectory_llm_as_judge(
      model="openai:o3-mini",
      prompt=TRAJECTORY_ACCURACY_PROMPT_WITH_REFERENCE,
  )
  evaluation = judge_with_reference(
      outputs=result["messages"],
      reference_outputs=reference_trajectory,
  )
  python  theme={null}
  from agentevals.trajectory.llm import create_async_trajectory_llm_as_judge, TRAJECTORY_ACCURACY_PROMPT
  from agentevals.trajectory.match import create_async_trajectory_match_evaluator

async_judge = create_async_trajectory_llm_as_judge(
      model="openai:o3-mini",
      prompt=TRAJECTORY_ACCURACY_PROMPT,
  )

async_evaluator = create_async_trajectory_match_evaluator(
      trajectory_match_mode="strict",
  )

async def test_async_evaluation():
      result = await agent.ainvoke({
          "messages": [HumanMessage(content="What's the weather?")]
      })

evaluation = await async_judge(outputs=result["messages"])
      assert evaluation["score"] is True
  bash  theme={null}
export LANGSMITH_API_KEY="your_langsmith_api_key"
export LANGSMITH_TRACING="true"
python  theme={null}
  import pytest
  from langsmith import testing as t
  from agentevals.trajectory.llm import create_trajectory_llm_as_judge, TRAJECTORY_ACCURACY_PROMPT

trajectory_evaluator = create_trajectory_llm_as_judge(
      model="openai:o3-mini",
      prompt=TRAJECTORY_ACCURACY_PROMPT,
  )

@pytest.mark.langsmith
  def test_trajectory_accuracy():
      result = agent.invoke({
          "messages": [HumanMessage(content="What's the weather in SF?")]
      })

reference_trajectory = [
          HumanMessage(content="What's the weather in SF?"),
          AIMessage(content="", tool_calls=[
              {"id": "call_1", "name": "get_weather", "args": {"city": "SF"}},
          ]),
          ToolMessage(content="It's 75 degrees and sunny in SF.", tool_call_id="call_1"),
          AIMessage(content="The weather in SF is 75 degrees and sunny."),
      ]

# Log inputs, outputs, and reference outputs to LangSmith
      t.log_inputs({})
      t.log_outputs({"messages": result["messages"]})
      t.log_reference_outputs({"messages": reference_trajectory})

trajectory_evaluator(
          outputs=result["messages"],
          reference_outputs=reference_trajectory
      )
  bash  theme={null}
  pytest test_trajectory.py --langsmith-output
  python  theme={null}
  from langsmith import Client
  from agentevals.trajectory.llm import create_trajectory_llm_as_judge, TRAJECTORY_ACCURACY_PROMPT

trajectory_evaluator = create_trajectory_llm_as_judge(
      model="openai:o3-mini",
      prompt=TRAJECTORY_ACCURACY_PROMPT,
  )

def run_agent(inputs):
      """Your agent function that returns trajectory messages."""
      return agent.invoke(inputs)["messages"]

experiment_results = client.evaluate(
      run_agent,
      data="your_dataset_name",
      evaluators=[trajectory_evaluator]
  )
  py conftest.py theme={null}
import pytest

@pytest.fixture(scope="session")
def vcr_config():
    return {
        "filter_headers": [
            ("authorization", "XXXX"),
            ("x-api-key", "XXXX"),
            # ... other headers you want to mask
        ],
        "filter_query_parameters": [
            ("api_key", "XXXX"),
            ("key", "XXXX"),
        ],
    }
ini pytest.ini theme={null}
  [pytest]
  markers =
      vcr: record/replay HTTP via VCR
  addopts = --record-mode=once
  toml pyproject.toml theme={null}
  [tool.pytest.ini_options]
  markers = [
    "vcr: record/replay HTTP via VCR"
  ]
  addopts = "--record-mode=once"
  python  theme={null}
@pytest.mark.vcr()
def test_agent_trajectory():
    # ...
```

The first time you run this test, your agent will make real network calls and pytest will generate a cassette file `test_agent_trajectory.yaml` in the `tests/cassettes` directory. Subsequent runs will use that cassette to mock the real network calls, granted the agent's requests don't change from the previous run. If they do, the test will fail and you'll need to delete the cassette and rerun the test to record fresh interactions.

<Warning>
  When you modify prompts, add new tools, or change expected trajectories, your saved cassettes will become outdated and your existing tests **will fail**. You should delete the corresponding cassette files and rerun the tests to record fresh interactions.
</Warning>

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/test.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

**Examples:**

Example 1 (unknown):
```unknown
## Integration Testing

Many agent behaviors only emerge when using a real LLM, such as which tool the agent decides to call, how it formats responses, or whether a prompt modification affects the entire execution trajectory. LangChain's [`agentevals`](https://github.com/langchain-ai/agentevals) package provides evaluators specifically designed for testing agent trajectories with live models.

AgentEvals lets you easily evaluate the trajectory of your agent (the exact sequence of messages, including tool calls) by performing a **trajectory match** or by using an **LLM judge**:

<Card title="Trajectory match" icon="equals" arrow="true" href="#trajectory-match-evaluator">
  Hard-code a reference trajectory for a given input and validate the run via a step-by-step comparison.

  Ideal for testing well-defined workflows where you know the expected behavior. Use when you have specific expectations about which tools should be called and in what order. This approach is deterministic, fast, and cost-effective since it doesn't require additional LLM calls.
</Card>

<Card title="LLM-as-judge" icon="gavel" arrow="true" href="#llm-as-judge-evaluator">
  Use a LLM to qualitatively validate your agent's execution trajectory. The "judge" LLM reviews the agent's decisions against a prompt rubric (which can include a reference trajectory).

  More flexible and can assess nuanced aspects like efficiency and appropriateness, but requires an LLM call and is less deterministic. Use when you want to evaluate the overall quality and reasonableness of the agent's trajectory without strict tool call or ordering requirements.
</Card>

### Installing AgentEvals
```

Example 2 (unknown):
```unknown
Or, clone the [AgentEvals repository](https://github.com/langchain-ai/agentevals) directly.

### Trajectory Match Evaluator

AgentEvals offers the `create_trajectory_match_evaluator` function to match your agent's trajectory against a reference trajectory. There are four modes to choose from:

| Mode        | Description                                               | Use Case                                                              |
| ----------- | --------------------------------------------------------- | --------------------------------------------------------------------- |
| `strict`    | Exact match of messages and tool calls in the same order  | Testing specific sequences (e.g., policy lookup before authorization) |
| `unordered` | Same tool calls allowed in any order                      | Verifying information retrieval when order doesn't matter             |
| `subset`    | Agent calls only tools from reference (no extras)         | Ensuring agent doesn't exceed expected scope                          |
| `superset`  | Agent calls at least the reference tools (extras allowed) | Verifying minimum required actions are taken                          |

<Accordion title="Strict match">
  The `strict` mode ensures trajectories contain identical messages in the same order with the same tool calls, though it allows for differences in message content. This is useful when you need to enforce a specific sequence of operations, such as requiring a policy lookup before authorizing an action.
```

Example 3 (unknown):
```unknown
</Accordion>

<Accordion title="Unordered match">
  The `unordered` mode allows the same tool calls in any order, which is helpful when you want to verify that specific information was retrieved but don't care about the sequence. For example, an agent might need to check both weather and events for a city, but the order doesn't matter.
```

Example 4 (unknown):
```unknown
</Accordion>

<Accordion title="Subset and superset match">
  The `superset` and `subset` modes match partial trajectories. The `superset` mode verifies that the agent called at least the tools in the reference trajectory, allowing additional tool calls. The `subset` mode ensures the agent did not call any tools beyond those in the reference.
```

---

## Invoke the LLM with input that triggers the tool call

**URL:** llms-txt#invoke-the-llm-with-input-that-triggers-the-tool-call

msg = llm_with_tools.invoke("What is 2 times 3?")

---

## Tool that allows agent to update user information (useful for chat applications)

**URL:** llms-txt#tool-that-allows-agent-to-update-user-information-(useful-for-chat-applications)

@tool
def save_user_info(user_info: UserInfo, runtime: ToolRuntime[Context]) -> str:
    """Save user info."""
    # Access the store - same as that provided to `create_agent`
    store = runtime.store # [!code highlight]
    user_id = runtime.context.user_id # [!code highlight]
    # Store data in the store (namespace, key, data)
    store.put(("users",), user_id, user_info) # [!code highlight]
    return "Successfully saved user info."

agent = create_agent(
    model="anthropic:claude-sonnet-4-5",
    tools=[save_user_info],
    store=store, # [!code highlight]
    context_schema=Context
)

---

## Define the runtime context

**URL:** llms-txt#define-the-runtime-context

**Contents:**
- Create the configuration file
- Next

class GraphContext(TypedDict):
    model_name: Literal["anthropic", "openai"]

workflow = StateGraph(AgentState, context_schema=GraphContext)
workflow.add_node("agent", call_model)
workflow.add_node("action", tool_node)
workflow.add_edge(START, "agent")
workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "continue": "action",
        "end": END,
    },
)
workflow.add_edge("action", "agent")

graph = workflow.compile()
bash  theme={null}
my-app/
├── my_agent # all project code lies within here
│   ├── utils # utilities for your graph
│   │   ├── __init__.py
│   │   ├── tools.py # tools for your graph
│   │   ├── nodes.py # node functions for your graph
│   │   └── state.py # state definition of your graph
│   ├── __init__.py
│   └── agent.py # code for constructing your graph
├── .env
└── pyproject.toml
json  theme={null}
{
  "dependencies": ["."],
  "graphs": {
    "agent": "./my_agent/agent.py:graph"
  },
  "env": ".env"
}
bash  theme={null}
my-app/
├── my_agent # all project code lies within here
│   ├── utils # utilities for your graph
│   │   ├── __init__.py
│   │   ├── tools.py # tools for your graph
│   │   ├── nodes.py # node functions for your graph
│   │   └── state.py # state definition of your graph
│   ├── __init__.py
│   └── agent.py # code for constructing your graph
├── .env # environment variables
├── langgraph.json  # configuration file for LangGraph
└── pyproject.toml # dependencies for your project
```

After you setup your project and place it in a GitHub repository, it's time to [deploy your app](/langsmith/deployment-quickstart).

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/langsmith/setup-pyproject.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

**Examples:**

Example 1 (unknown):
```unknown
Example file directory:
```

Example 2 (unknown):
```unknown
## Create the configuration file

Create a [configuration file](/langsmith/cli#configuration-file) called `langgraph.json`. See the [configuration file reference](/langsmith/cli#configuration-file) for detailed explanations of each key in the JSON object of the configuration file.

Example `langgraph.json` file:
```

Example 3 (unknown):
```unknown
Note that the variable name of the `CompiledGraph` appears at the end of the value of each subkey in the top-level `graphs` key (i.e. `:<variable_name>`).

<Warning>
  **Configuration File Location**
  The configuration file must be placed in a directory that is at the same level or higher than the Python files that contain compiled graphs and associated dependencies.
</Warning>

Example file directory:
```

---

## tools = [DuckDuckGoSearchRun(rate_limiter=rate_limiter)]

**URL:** llms-txt#tools-=-[duckduckgosearchrun(rate_limiter=rate_limiter)]

**Contents:**
  - Simulate production data
- Convert Production Traces to Experiment
  - Select runs to backtest on

tools = [TavilySearchResults(max_results=5, rate_limiter=rate_limiter)]

agent = create_agent(gpt_3_5_turbo, tools=tools, system_prompt=instructions)
python  theme={null}
fake_production_inputs = [
    "Alan turing's early childhood",
    "Economic impacts of the European Union",
    "Underrated philosophers",
    "History of the Roxie theater in San Francisco",
    "ELI5: gravitational waves",
    "The arguments for and against a parliamentary system",
    "Pivotal moments in music history",
    "Big ideas in programming languages",
    "Big questions in biology",
    "The relationship between math and reality",
    "What makes someone funny",
]

agent.batch(
    [{"messages": [{"role": "user", "content": content}]} for content in fake_production_inputs],
)
python  theme={null}
from datetime import datetime, timedelta, timezone
from uuid import uuid4
from langsmith import Client
from langsmith.beta import convert_runs_to_test

**Examples:**

Example 1 (unknown):
```unknown
### Simulate production data

Now lets simulate some production data:
```

Example 2 (unknown):
```unknown
## Convert Production Traces to Experiment

The first step is to generate a dataset based on the production *inputs*. Then copy over all the traces to serve as a baseline experiment.

### Select runs to backtest on

You can select the runs to backtest on using the `filter` argument of `list_runs`. The `filter` argument uses the LangSmith [trace query syntax](/langsmith/trace-query-syntax) to select runs.
```

---

## Define a tool

**URL:** llms-txt#define-a-tool

def multiply(a: int, b: int) -> int:
    return a * b

---

## How to add semantic search to your agent deployment

**URL:** llms-txt#how-to-add-semantic-search-to-your-agent-deployment

**Contents:**
- Prerequisites
- Steps

Source: https://docs.langchain.com/langsmith/semantic-search

This guide explains how to add semantic search to your deployment's cross-thread [store](/oss/python/langgraph/persistence#memory-store), so that your agent can search for memories and other documents by semantic similarity.

* A deployment (refer to [how to set up an application for deployment](/langsmith/setup-app-requirements-txt)) and details on [hosting options](/langsmith/hosting).
* API keys for your embedding provider (in this case, OpenAI).
* `langchain >= 0.3.8` (if you specify using the string format below).

1. Update your `langgraph.json` configuration file to include the store configuration:

* Uses OpenAI's text-embedding-3-small model for generating embeddings
* Sets the embedding dimension to 1536 (matching the model's output)
* Indexes all fields in your stored data (`["$"]` means index everything, or specify specific fields like `["text", "metadata.title"]`)

1. To use the string embedding format above, make sure your dependencies include `langchain >= 0.3.8`:

```toml  theme={null}

**Examples:**

Example 1 (unknown):
```unknown
This configuration:

* Uses OpenAI's text-embedding-3-small model for generating embeddings
* Sets the embedding dimension to 1536 (matching the model's output)
* Indexes all fields in your stored data (`["$"]` means index everything, or specify specific fields like `["text", "metadata.title"]`)

1. To use the string embedding format above, make sure your dependencies include `langchain >= 0.3.8`:
```

---

## Model Context Protocol (MCP)

**URL:** llms-txt#model-context-protocol-(mcp)

**Contents:**
- Install
- Transport types
- Use MCP tools
- Custom MCP servers
- Stateful tool usage
- Additional resources

Source: https://docs.langchain.com/oss/python/langchain/mcp

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) is an open protocol that standardizes how applications provide tools and context to LLMs. LangChain agents can use tools defined on MCP servers using the [`langchain-mcp-adapters`](https://github.com/langchain-ai/langchain-mcp-adapters) library.

Install the `langchain-mcp-adapters` library to use MCP tools in LangGraph:

MCP supports different transport mechanisms for client-server communication:

* **stdio** – Client launches server as a subprocess and communicates via standard input/output. Best for local tools and simple setups.
* **Streamable HTTP** – Server runs as an independent process handling HTTP requests. Supports remote connections and multiple clients.
* **Server-Sent Events (SSE)** – a variant of streamable HTTP optimized for real-time streaming communication.

`langchain-mcp-adapters` enables agents to use tools defined across one or more MCP server.

<Note>
  `MultiServerMCPClient` is **stateless by default**. Each tool invocation creates a fresh MCP `ClientSession`, executes the tool, and then cleans up.
</Note>

## Custom MCP servers

To create your own MCP servers, you can use the `mcp` library. This library provides a simple way to define [tools](https://modelcontextprotocol.io/docs/learn/server-concepts#tools-ai-actions) and run them as servers.

Use the following reference implementations to test your agent with MCP tool servers.

## Stateful tool usage

For stateful servers that maintain context between tool calls, use `client.session()` to create a persistent `ClientSession`.

## Additional resources

* [MCP documentation](https://modelcontextprotocol.io/introduction)
* [MCP Transport documentation](https://modelcontextprotocol.io/docs/concepts/transports)
* [`langchain-mcp-adapters`](https://github.com/langchain-ai/langchain-mcp-adapters)

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/mcp.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

**Examples:**

Example 1 (unknown):
```unknown

```

Example 2 (unknown):
```unknown
</CodeGroup>

## Transport types

MCP supports different transport mechanisms for client-server communication:

* **stdio** – Client launches server as a subprocess and communicates via standard input/output. Best for local tools and simple setups.
* **Streamable HTTP** – Server runs as an independent process handling HTTP requests. Supports remote connections and multiple clients.
* **Server-Sent Events (SSE)** – a variant of streamable HTTP optimized for real-time streaming communication.

## Use MCP tools

`langchain-mcp-adapters` enables agents to use tools defined across one or more MCP server.
```

Example 3 (unknown):
```unknown
<Note>
  `MultiServerMCPClient` is **stateless by default**. Each tool invocation creates a fresh MCP `ClientSession`, executes the tool, and then cleans up.
</Note>

## Custom MCP servers

To create your own MCP servers, you can use the `mcp` library. This library provides a simple way to define [tools](https://modelcontextprotocol.io/docs/learn/server-concepts#tools-ai-actions) and run them as servers.

<CodeGroup>
```

Example 4 (unknown):
```unknown

```

---

## Node for making sure the 'followup' key is set before our agent run completes.

**URL:** llms-txt#node-for-making-sure-the-'followup'-key-is-set-before-our-agent-run-completes.

def compile_followup(state: State) -> dict:
    """Set the followup to be the last message if it hasn't explicitly been set."""
    if not state.get("followup"):
        return {"followup": state["messages"][-1].content}
    return {}

---

## > User is John Smith.

**URL:** llms-txt#>-user-is-john-smith.

**Contents:**
  - Prompt
  - Before model
  - After model

python  theme={null}
from langchain.tools import tool, ToolRuntime
from langchain_core.runnables import RunnableConfig
from langchain.messages import ToolMessage
from langchain.agents import create_agent, AgentState
from langgraph.types import Command
from pydantic import BaseModel

class CustomState(AgentState):  # [!code highlight]
    user_name: str

class CustomContext(BaseModel):
    user_id: str

@tool
def update_user_info(
    runtime: ToolRuntime[CustomContext, CustomState],
) -> Command:
    """Look up and update user info."""
    user_id = runtime.context.user_id  # [!code highlight]
    name = "John Smith" if user_id == "user_123" else "Unknown user"
    return Command(update={
        "user_name": name,
        # update the message history
        "messages": [
            ToolMessage(
                "Successfully looked up user information",
                tool_call_id=runtime.tool_call_id
            )
        ]
    })

@tool
def greet(
    runtime: ToolRuntime[CustomContext, CustomState]
) -> str:
    """Use this to greet the user once you found their info."""
    user_name = runtime.state["user_name"]
    return f"Hello {user_name}!"
  # [!code highlight]
agent = create_agent(
    model="openai:gpt-5-nano",
    tools=[update_user_info, greet],
    state_schema=CustomState,
    context_schema=CustomContext,  # [!code highlight]
)

agent.invoke(
    {"messages": [{"role": "user", "content": "greet the user"}]},
    context=CustomContext(user_id="user_123"),
)
python  theme={null}
from langchain.messages import AnyMessage
from langchain.agents import create_agent, AgentState
from typing import TypedDict

class CustomContext(TypedDict):
    user_name: str

from langchain.agents.middleware import dynamic_prompt, ModelRequest

def get_weather(city: str) -> str:
    """Get the weather in a city."""
    return f"The weather in {city} is always sunny!"

@dynamic_prompt
def dynamic_system_prompt(request: ModelRequest) -> str:
    user_name = request.runtime.context["user_name"]
    system_prompt = f"You are a helpful assistant. Address the user as {user_name}."
    return system_prompt

agent = create_agent(
    model="openai:gpt-5-nano",
    tools=[get_weather],
    middleware=[dynamic_system_prompt],
    context_schema=CustomContext,
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What is the weather in SF?"}]},
    context=CustomContext(user_name="John Smith"),
)
for msg in result["messages"]:
    msg.pretty_print()
shell title="Output" theme={null}
================================ Human Message =================================

What is the weather in SF?
================================== Ai Message ==================================
Tool Calls:
  get_weather (call_WFQlOGn4b2yoJrv7cih342FG)
 Call ID: call_WFQlOGn4b2yoJrv7cih342FG
  Args:
    city: San Francisco
================================= Tool Message =================================
Name: get_weather

The weather in San Francisco is always sunny!
================================== Ai Message ==================================

Hi John Smith, the weather in San Francisco is always sunny!
mermaid  theme={null}
%%{
    init: {
        "fontFamily": "monospace",
        "flowchart": {
        "curve": "basis"
        },
        "themeVariables": {"edgeLabelBackground": "transparent"}
    }
}%%
graph TD
    S(["\_\_start\_\_"])
    PRE(before_model)
    MODEL(model)
    TOOLS(tools)
    END(["\_\_end\_\_"])
    S --> PRE
    PRE --> MODEL
    MODEL -.-> TOOLS
    MODEL -.-> END
    TOOLS --> PRE
    classDef blueHighlight fill:#0a1c25,stroke:#0a455f,color:#bae6fd;
    class S blueHighlight;
    class END blueHighlight;
python  theme={null}
from langchain.messages import RemoveMessage
from langgraph.graph.message import REMOVE_ALL_MESSAGES
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents import create_agent, AgentState
from langchain.agents.middleware import before_model
from langgraph.runtime import Runtime
from typing import Any

@before_model
def trim_messages(state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
    """Keep only the last few messages to fit context window."""
    messages = state["messages"]

if len(messages) <= 3:
        return None  # No changes needed

first_msg = messages[0]
    recent_messages = messages[-3:] if len(messages) % 2 == 0 else messages[-4:]
    new_messages = [first_msg] + recent_messages

return {
        "messages": [
            RemoveMessage(id=REMOVE_ALL_MESSAGES),
            *new_messages
        ]
    }

agent = create_agent(
    model,
    tools=tools,
    middleware=[trim_messages]
)

config: RunnableConfig = {"configurable": {"thread_id": "1"}}

agent.invoke({"messages": "hi, my name is bob"}, config)
agent.invoke({"messages": "write a short poem about cats"}, config)
agent.invoke({"messages": "now do the same but for dogs"}, config)
final_response = agent.invoke({"messages": "what's my name?"}, config)

final_response["messages"][-1].pretty_print()
"""
================================== Ai Message ==================================

Your name is Bob. You told me that earlier.
If you'd like me to call you a nickname or use a different name, just say the word.
"""
mermaid  theme={null}
%%{
    init: {
        "fontFamily": "monospace",
        "flowchart": {
        "curve": "basis"
        },
        "themeVariables": {"edgeLabelBackground": "transparent"}
    }
}%%
graph TD
    S(["\_\_start\_\_"])
    MODEL(model)
    POST(after_model)
    TOOLS(tools)
    END(["\_\_end\_\_"])
    S --> MODEL
    MODEL --> POST
    POST -.-> END
    POST -.-> TOOLS
    TOOLS --> MODEL
    classDef blueHighlight fill:#0a1c25,stroke:#0a455f,color:#bae6fd;
    class S blueHighlight;
    class END blueHighlight;
    class POST greenHighlight;
python  theme={null}
from langchain.messages import RemoveMessage
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents import create_agent, AgentState
from langchain.agents.middleware import after_model
from langgraph.runtime import Runtime

@after_model
def validate_response(state: AgentState, runtime: Runtime) -> dict | None:
    """Remove messages containing sensitive words."""
    STOP_WORDS = ["password", "secret"]
    last_message = state["messages"][-1]
    if any(word in last_message.content for word in STOP_WORDS):
        return {"messages": [RemoveMessage(id=last_message.id)]}
    return None

agent = create_agent(
    model="openai:gpt-5-nano",
    tools=[],
    middleware=[validate_response],
    checkpointer=InMemorySaver(),
)
```

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/short-term-memory.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

**Examples:**

Example 1 (unknown):
```unknown
#### Write short-term memory from tools

To modify the agent's short-term memory (state) during execution, you can return state updates directly from the tools.

This is useful for persisting intermediate results or making information accessible to subsequent tools or prompts.
```

Example 2 (unknown):
```unknown
### Prompt

Access short term memory (state) in middleware to create dynamic prompts based on conversation history or custom state fields.
```

Example 3 (unknown):
```unknown

```

Example 4 (unknown):
```unknown
### Before model

Access short term memory (state) in [`@before_model`](https://reference.langchain.com/python/langchain/middleware/#langchain.agents.middleware.before_model) middleware to process messages before model calls.
```

---

## ❌ Bad: Too many tools

**URL:** llms-txt#❌-bad:-too-many-tools

**Contents:**
  - Choose models by task
  - Return concise results
- Common patterns
  - Multiple specialized subagents
- Troubleshooting
  - Subagent not being called
  - Context still getting bloated
  - Wrong subagent being selected

email_agent = {
    "name": "email-sender",
    "tools": [send_email, web_search, database_query, file_upload],  # Unfocused
}
python  theme={null}
subagents = [
    {
        "name": "contract-reviewer",
        "description": "Reviews legal documents and contracts",
        "system_prompt": "You are an expert legal reviewer...",
        "tools": [read_document, analyze_contract],
        "model": "anthropic:claude-sonnet-4-20250514",  # Large context for long documents
    },
    {
        "name": "financial-analyst",
        "description": "Analyzes financial data and market trends",
        "system_prompt": "You are an expert financial analyst...",
        "tools": [get_stock_price, analyze_fundamentals],
        "model": "openai:gpt-4o",  # Better for numerical analysis
    },
]
python  theme={null}
data_analyst = {
    "system_prompt": """Analyze the data and return:
    1. Key insights (3-5 bullet points)
    2. Overall confidence score
    3. Recommended next actions

Do NOT include:
    - Raw data
    - Intermediate calculations
    - Detailed tool outputs

Keep response under 300 words."""
}
python  theme={null}
from deepagents import create_deep_agent

subagents = [
    {
        "name": "data-collector",
        "description": "Gathers raw data from various sources",
        "system_prompt": "Collect comprehensive data on the topic",
        "tools": [web_search, api_call, database_query],
    },
    {
        "name": "data-analyzer",
        "description": "Analyzes collected data for insights",
        "system_prompt": "Analyze data and extract key insights",
        "tools": [statistical_analysis],
    },
    {
        "name": "report-writer",
        "description": "Writes polished reports from analysis",
        "system_prompt": "Create professional reports from insights",
        "tools": [format_document],
    },
]

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-20250514",
    system_prompt="You coordinate data analysis and reporting. Use subagents for specialized tasks.",
    subagents=subagents
)
python  theme={null}
   # ✅ Good
   {"name": "research-specialist", "description": "Conducts in-depth research on specific topics using web search. Use when you need detailed information that requires multiple searches."}

# ❌ Bad
   {"name": "helper", "description": "helps with stuff"}
   python  theme={null}
   agent = create_deep_agent(
       system_prompt="""...your instructions...

IMPORTANT: For complex tasks, delegate to your subagents using the task() tool.
       This keeps your context clean and improves results.""",
       subagents=[...]
   )
   python  theme={null}
   system_prompt="""...

IMPORTANT: Return only the essential summary.
   Do NOT include raw data, intermediate search results, or detailed tool outputs.
   Your response should be under 500 words."""
   python  theme={null}
   system_prompt="""When you gather large amounts of data:
   1. Save raw data to /data/raw_results.txt
   2. Process and analyze the data
   3. Return only the analysis summary

This keeps context clean."""
   python  theme={null}
subagents = [
    {
        "name": "quick-researcher",
        "description": "For simple, quick research questions that need 1-2 searches. Use when you need basic facts or definitions.",
    },
    {
        "name": "deep-researcher",
        "description": "For complex, in-depth research requiring multiple searches, synthesis, and analysis. Use for comprehensive reports.",
    }
]
```

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/subagents.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

**Examples:**

Example 1 (unknown):
```unknown
### Choose models by task

Different models excel at different tasks:
```

Example 2 (unknown):
```unknown
### Return concise results

Instruct subagents to return summaries, not raw data:
```

Example 3 (unknown):
```unknown
## Common patterns

### Multiple specialized subagents

Create specialized subagents for different domains:
```

Example 4 (unknown):
```unknown
**Workflow:**

1. Main agent creates high-level plan
2. Delegates data collection to data-collector
3. Passes results to data-analyzer
4. Sends insights to report-writer
5. Compiles final output

Each subagent works with clean context focused only on its task.

## Troubleshooting

### Subagent not being called

**Problem**: Main agent tries to do work itself instead of delegating.

**Solutions**:

1. **Make descriptions more specific:**
```

---

## Agent can read /memories/preferences.txt from the first thread

**URL:** llms-txt#agent-can-read-/memories/preferences.txt-from-the-first-thread

**Contents:**
- Use cases
  - User preferences
  - Self-improving instructions
  - Knowledge base

python  theme={null}
agent = create_deep_agent(
    store=store,
    use_longterm_memory=True,
    system_prompt="""When users tell you their preferences, save them to
    /memories/user_preferences.txt so you remember them in future conversations."""
)
python  theme={null}
agent = create_deep_agent(
    store=store,
    use_longterm_memory=True,
    system_prompt="""You have a file at /memories/instructions.txt with additional
    instructions and preferences.

Read this file at the start of conversations to understand user preferences.

When users provide feedback like "please always do X" or "I prefer Y",
    update /memories/instructions.txt using the edit_file tool."""
)
python  theme={null}

**Examples:**

Example 1 (unknown):
```unknown
## Use cases

### User preferences

Store user preferences that persist across sessions:
```

Example 2 (unknown):
```unknown
### Self-improving instructions

An agent can update its own instructions based on feedback:
```

Example 3 (unknown):
```unknown
Over time, the instructions file accumulates user preferences, helping the agent improve.

### Knowledge base

Build up knowledge over multiple conversations:
```

---

## Agent Chat UI

**URL:** llms-txt#agent-chat-ui

**Contents:**
- Agent Chat UI
  - Features
  - Quick start
  - Local development
  - Connect to your agent

Source: https://docs.langchain.com/oss/python/langgraph/ui

LangChain provides a powerful prebuilt user interface that work seamlessly with agents created using [`create_agent`](/oss/python/langchain/agents). This UI is designed to provide rich, interactive experiences for your agents with minimal setup, whether you're running locally or in a deployed context (such as [LangSmith](/langsmith/)).

[Agent Chat UI](https://github.com/langchain-ai/agent-chat-ui) is a Next.js application that provides a conversational interface for interacting with any LangChain agent. It supports real-time chat, tool visualization, and advanced features like time-travel debugging and state forking.

Agent Chat UI is open source and can be adapted to your application needs.

<Frame>
  <iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/lInrwVnZ83o?si=Uw66mPtCERJm0EjU" title="Agent Chat UI" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</Frame>

<Accordion title="Tool visualization">
  Studio automatically renders tool calls and results in an intuitive interface.

<Frame>
        <img src="https://mintcdn.com/langchain-5e9cc07a/zA84oCipUuW8ow2z/oss/images/studio_tools.gif?s=64e762e917f092960472b61a862a81cb" alt="Tool visualization in Studio" data-og-width="1280" width="1280" data-og-height="833" height="833" data-path="oss/images/studio_tools.gif" data-optimize="true" data-opv="3" />
  </Frame>
</Accordion>

<Accordion title="Time-travel debugging">
  Navigate through conversation history and fork from any point

<Frame>
        <img src="https://mintcdn.com/langchain-5e9cc07a/TCDks4pdsHdxWmuJ/oss/images/studio_fork.gif?s=0bb5a397d4b2ed3ff8ec62b9d0f92e3e" alt="Time-travel debugging in Studio" data-og-width="1280" width="1280" data-og-height="833" height="833" data-path="oss/images/studio_fork.gif" data-optimize="true" data-opv="3" />
  </Frame>
</Accordion>

<Accordion title="State inspection">
  View and modify agent state at any point during execution

<Frame>
        <img src="https://mintcdn.com/langchain-5e9cc07a/zA84oCipUuW8ow2z/oss/images/studio_state.gif?s=908d69765b0655cb532620c6e0fa96c8" alt="State inspection in Studio" data-og-width="1280" width="1280" data-og-height="833" height="833" data-path="oss/images/studio_state.gif" data-optimize="true" data-opv="3" />
  </Frame>
</Accordion>

<Accordion title="Human-in-the-loop">
  Built-in support for reviewing and responding to agent requests

<Frame>
        <img src="https://mintcdn.com/langchain-5e9cc07a/TCDks4pdsHdxWmuJ/oss/images/studio_hitl.gif?s=ce7ce6378caf4db29ea6062b9aff0220" alt="Human-in-the-Loop in Studio" data-og-width="1280" width="1280" data-og-height="833" height="833" data-path="oss/images/studio_hitl.gif" data-optimize="true" data-opv="3" />
  </Frame>
</Accordion>

<Tip>
  You can use generative UI in the Agent Chat UI. For more information, see [Implement generative user interfaces with LangGraph](/langsmith/generative-ui-react).
</Tip>

The fastest way to get started is using the hosted version:

1. **Visit [Agent Chat UI](https://agentchat.vercel.app)**
2. **Connect your agent** by entering your deployment URL or local server address
3. **Start chatting** - the UI will automatically detect and render tool calls and interrupts

### Local development

For customization or local development, you can run Agent Chat UI locally:

### Connect to your agent

Agent Chat UI can connect to both [local](/oss/python/langgraph/studio#setup-local-langgraph-server) and [deployed agents](/oss/python/langgraph/deploy).

After starting Agent Chat UI, you'll need to configure it to connect to your agent:

1. **Graph ID**: Enter your graph name (find this under `graphs` in your `langgraph.json` file)
2. **Deployment URL**: Your LangGraph server's endpoint (e.g., `http://localhost:2024` for local development, or your deployed agent's URL)
3. **LangSmith API key (optional)**: Add your LangSmith API key (not required if you're using a local LangGraph server)

Once configured, Agent Chat UI will automatically fetch and display any interrupted threads from your agent.

<Tip>
  Agent Chat UI has out-of-the-box support for rendering tool calls and tool result messages. To customize what messages are shown, see [Hiding Messages in the Chat](https://github.com/langchain-ai/agent-chat-ui?tab=readme-ov-file#hiding-messages-in-the-chat).
</Tip>

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/ui.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

**Examples:**

Example 1 (unknown):
```unknown

```

---

## The agent can now track additional state beyond messages

**URL:** llms-txt#the-agent-can-now-track-additional-state-beyond-messages

**Contents:**
  - Streaming
  - Middleware

result = agent.invoke({
    "messages": [{"role": "user", "content": "I prefer technical explanations"}],
    "user_preferences": {"style": "technical", "verbosity": "detailed"},
})
python  theme={null}
for chunk in agent.stream({
    "messages": [{"role": "user", "content": "Search for AI news and summarize the findings"}]
}, stream_mode="values"):
    # Each chunk contains the full state at that point
    latest_message = chunk["messages"][-1]
    if latest_message.content:
        print(f"Agent: {latest_message.content}")
    elif latest_message.tool_calls:
        print(f"Calling tools: {[tc['name'] for tc in latest_message.tool_calls]}")
```

<Tip>
  For more details on streaming, see [Streaming](/oss/python/langchain/streaming).
</Tip>

[Middleware](/oss/python/langchain/middleware) provides powerful extensibility for customizing agent behavior at different stages of execution. You can use middleware to:

* Process state before the model is called (e.g., message trimming, context injection)
* Modify or validate the model's response (e.g., guardrails, content filtering)
* Handle tool execution errors with custom logic
* Implement dynamic model selection based on state or context
* Add custom logging, monitoring, or analytics

Middleware integrates seamlessly into the agent's execution graph, allowing you to intercept and modify data flow at key points without changing the core agent logic.

<Tip>
  For comprehensive middleware documentation including decorators like [`@before_model`](https://reference.langchain.com/python/langchain/middleware/#langchain.agents.middleware.before_model), [`@after_model`](https://reference.langchain.com/python/langchain/middleware/#langchain.agents.middleware.after_model), and [`@wrap_tool_call`](https://reference.langchain.com/python/langchain/middleware/#langchain.agents.middleware.wrap_tool_call), see [Middleware](/oss/python/langchain/middleware).
</Tip>

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/agents.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

**Examples:**

Example 1 (unknown):
```unknown
<Note>
  As of `langchain 1.0`, custom state schemas **must** be `TypedDict` types. Pydantic models and dataclasses are no longer supported. See the [v1 migration guide](/oss/python/migrate/langchain-v1#state-type-restrictions) for more details.
</Note>

<Tip>
  To learn more about memory, see [Memory](/oss/python/concepts/memory). For information on implementing long-term memory that persists across sessions, see [Long-term memory](/oss/python/langchain/long-term-memory).
</Tip>

### Streaming

We've seen how the agent can be called with `invoke` to get a final response. If the agent executes multiple steps, this may take a while. To show intermediate progress, we can stream back messages as they occur.
```

---

## Agent tools

**URL:** llms-txt#agent-tools

@tool
def lookup_track( ...

@tool
def lookup_album( ...

@tool
def lookup_artist( ...

---

## Use tools in a prompt

**URL:** llms-txt#use-tools-in-a-prompt

**Contents:**
- When to use tools
- Built-in tools
  - OpenAI Tools
  - Anthropic Tools
- Adding and using tools
  - Add a tool
  - Use a built-in tool
  - Create a custom tool
- Tool choice settings

Source: https://docs.langchain.com/langsmith/use-tools

Tools allow language models to interact with external systems and perform actions beyond just generating text. In the LangSmith playground, you can use two types of tools:

1. **Built-in tools**: Pre-configured tools provided by model providers (like OpenAI and Anthropic) that are ready to use. These include capabilities like web search, code interpretation, and more.

2. **Custom tools**: Functions you define to perform specific tasks. These are useful when you need to integrate with your own systems or create specialized functionality. When you define custom tools within the LangSmith Playground, you can verify that the model correctly identifies and calls these tools with the correct arguments. Soon we plan to support executing these custom tool calls directly.

* Use **built-in tools** when you need common capabilities like web search or code interpretation. These are built and maintained by the model providers.

* Use **custom tools** when you want to test and validate your own tool designs, including:

* Validating which tools the model chooses to use and seeing the specific arguments it provides in tool calls
  * Simulating tool interactions

The LangSmith Playground has native support for a variety of tools from OpenAI and Anthropic. If you want to use a tool that isn't explicitly listed in the Playground, you can still add it by manually specifying its `type` and any required arguments.

* **Web search**: [Search the web for real-time information](https://platform.openai.com/docs/guides/tools-web-search?api-mode=responses)
* **Image generation**: [Generate images based on a text prompt](https://platform.openai.com/docs/guides/tools-image-generation)
* **MCP**: [Gives the model access to tools hosted on a remote MCP server](https://platform.openai.com/docs/guides/tools-remote-mcp)
* [View all OpenAI tools](https://platform.openai.com/docs/guides/tools?api-mode=responses)

* **Web search**: [Search the web for up-to-date information](https://docs.claude.com/en/docs/agents-and-tools/tool-use/web-search-tool)
* [View all Anthropic tools](https://docs.claude.com/en/docs/agents-and-tools/tool-use/overview)

## Adding and using tools

To add a tool to your prompt, click the `+ Tool` button at the bottom of the prompt editor. <img src="https://mintcdn.com/langchain-5e9cc07a/E8FdemkcQxROovD9/langsmith/images/add-tool.png?fit=max&auto=format&n=E8FdemkcQxROovD9&q=85&s=b922d9b219cff1bbc726bc2f6b82d6b6" alt="" data-og-width="753" width="753" data-og-height="351" height="351" data-path="langsmith/images/add-tool.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/E8FdemkcQxROovD9/langsmith/images/add-tool.png?w=280&fit=max&auto=format&n=E8FdemkcQxROovD9&q=85&s=d08cf08da323465b8340f5395f93cb94 280w, https://mintcdn.com/langchain-5e9cc07a/E8FdemkcQxROovD9/langsmith/images/add-tool.png?w=560&fit=max&auto=format&n=E8FdemkcQxROovD9&q=85&s=c54feb8a827ef4d7858061f252200fc1 560w, https://mintcdn.com/langchain-5e9cc07a/E8FdemkcQxROovD9/langsmith/images/add-tool.png?w=840&fit=max&auto=format&n=E8FdemkcQxROovD9&q=85&s=59fbdea1f87fc501812417a5457ff249 840w, https://mintcdn.com/langchain-5e9cc07a/E8FdemkcQxROovD9/langsmith/images/add-tool.png?w=1100&fit=max&auto=format&n=E8FdemkcQxROovD9&q=85&s=f850e2a4dacb21cba0939bd017ce2106 1100w, https://mintcdn.com/langchain-5e9cc07a/E8FdemkcQxROovD9/langsmith/images/add-tool.png?w=1650&fit=max&auto=format&n=E8FdemkcQxROovD9&q=85&s=5b40ff17dd48d154c83b5063bab9f673 1650w, https://mintcdn.com/langchain-5e9cc07a/E8FdemkcQxROovD9/langsmith/images/add-tool.png?w=2500&fit=max&auto=format&n=E8FdemkcQxROovD9&q=85&s=6c48a7e9d6c921f206fc9ff777d94ed6 2500w" />

### Use a built-in tool

1. In the tool section, select the built-in tool you want to use. You'll only see the tools that are compatible with the provider and model you've chosen.
2. When the model calls the tool, the playground will display the response

<img src="https://mintcdn.com/langchain-5e9cc07a/1RIJxfRpkszanJLL/langsmith/images/web-search-tool.gif?s=2fb882f785abc26d0e5412557cc982ca" alt="" data-og-width="1036" width="1036" data-og-height="720" height="720" data-path="langsmith/images/web-search-tool.gif" data-optimize="true" data-opv="3" />

### Create a custom tool

To create a custom tool, you'll need to provide:

* Name: A descriptive name for your tool
* Description: Clear explanation of what the tool does
* Arguments: The inputs your tool requires

<img src="https://mintcdn.com/langchain-5e9cc07a/aKRoUGXX6ygp4DlC/langsmith/images/custom-tool.gif?s=69638e515cd7c5be413cf13348e10974" alt="" data-og-width="1028" width="1028" data-og-height="720" height="720" data-path="langsmith/images/custom-tool.gif" data-optimize="true" data-opv="3" />

Note: When running a custom tool in the playground, the model will respond with a JSON object containing the tool name and the tool call. Currently, there's no way to connect this to a hosted tool via MCP.

<img src="https://mintcdn.com/langchain-5e9cc07a/ImHGLQW1HnQYwnJV/langsmith/images/tool-call.png?fit=max&auto=format&n=ImHGLQW1HnQYwnJV&q=85&s=44458ff5a2790122ffd7e8b62bf14032" alt="" data-og-width="1488" width="1488" data-og-height="747" height="747" data-path="langsmith/images/tool-call.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/ImHGLQW1HnQYwnJV/langsmith/images/tool-call.png?w=280&fit=max&auto=format&n=ImHGLQW1HnQYwnJV&q=85&s=add552eba8c2254b2b8631420e8a92ee 280w, https://mintcdn.com/langchain-5e9cc07a/ImHGLQW1HnQYwnJV/langsmith/images/tool-call.png?w=560&fit=max&auto=format&n=ImHGLQW1HnQYwnJV&q=85&s=807f9c730d6386d884a8b263d07de8c3 560w, https://mintcdn.com/langchain-5e9cc07a/ImHGLQW1HnQYwnJV/langsmith/images/tool-call.png?w=840&fit=max&auto=format&n=ImHGLQW1HnQYwnJV&q=85&s=6190625854497044bea5a486f155c1ab 840w, https://mintcdn.com/langchain-5e9cc07a/ImHGLQW1HnQYwnJV/langsmith/images/tool-call.png?w=1100&fit=max&auto=format&n=ImHGLQW1HnQYwnJV&q=85&s=eeee3567477764d44857923ff49d4d75 1100w, https://mintcdn.com/langchain-5e9cc07a/ImHGLQW1HnQYwnJV/langsmith/images/tool-call.png?w=1650&fit=max&auto=format&n=ImHGLQW1HnQYwnJV&q=85&s=ec4aaf0657a0b200d8822b346762d443 1650w, https://mintcdn.com/langchain-5e9cc07a/ImHGLQW1HnQYwnJV/langsmith/images/tool-call.png?w=2500&fit=max&auto=format&n=ImHGLQW1HnQYwnJV&q=85&s=1c6b56541dd156fdc5c06f3d9fb79648 2500w" />

## Tool choice settings

Some models provide control over which tools are called. To configure this:

1. Go to prompt settings
2. Navigate to tool settings
3. Select tool choice

To understand the available tool choice options, check the documentation for your specific provider. For example, [OpenAI's documentation on tool choice](https://platform.openai.com/docs/guides/function-calling/function-calling-behavior?api-mode=responses#tool-choice).

<img src="https://mintcdn.com/langchain-5e9cc07a/ImHGLQW1HnQYwnJV/langsmith/images/tool-choice.png?fit=max&auto=format&n=ImHGLQW1HnQYwnJV&q=85&s=8685dbafdab37ed9529f8dbeceab72e6" alt="" data-og-width="942" width="942" data-og-height="867" height="867" data-path="langsmith/images/tool-choice.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/ImHGLQW1HnQYwnJV/langsmith/images/tool-choice.png?w=280&fit=max&auto=format&n=ImHGLQW1HnQYwnJV&q=85&s=4d040577bbfae3816d23de7d16b2017d 280w, https://mintcdn.com/langchain-5e9cc07a/ImHGLQW1HnQYwnJV/langsmith/images/tool-choice.png?w=560&fit=max&auto=format&n=ImHGLQW1HnQYwnJV&q=85&s=e8b1220627a1dd668a6c7e66bb8881b2 560w, https://mintcdn.com/langchain-5e9cc07a/ImHGLQW1HnQYwnJV/langsmith/images/tool-choice.png?w=840&fit=max&auto=format&n=ImHGLQW1HnQYwnJV&q=85&s=f99a56b4e513d33c4595b9665e5a3d0e 840w, https://mintcdn.com/langchain-5e9cc07a/ImHGLQW1HnQYwnJV/langsmith/images/tool-choice.png?w=1100&fit=max&auto=format&n=ImHGLQW1HnQYwnJV&q=85&s=c62de52814917a4d6f65a05c9b44a670 1100w, https://mintcdn.com/langchain-5e9cc07a/ImHGLQW1HnQYwnJV/langsmith/images/tool-choice.png?w=1650&fit=max&auto=format&n=ImHGLQW1HnQYwnJV&q=85&s=6d4ff53eb7fa66b94c24e285dc89ba5f 1650w, https://mintcdn.com/langchain-5e9cc07a/ImHGLQW1HnQYwnJV/langsmith/images/tool-choice.png?w=2500&fit=max&auto=format&n=ImHGLQW1HnQYwnJV&q=85&s=591da66f1402ffa38645cec70ba12e0a 2500w" />

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/langsmith/use-tools.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

---

## Or use individual tools

**URL:** llms-txt#or-use-individual-tools

**Contents:**
  - Chat Loaders
- 3rd Party Integrations
  - SearchApi
  - SerpApi
  - Serper.dev
  - YouTube

from langchain_google_community.gmail.create_draft import GmailCreateDraft
from langchain_google_community.gmail.get_message import GmailGetMessage
from langchain_google_community.gmail.get_thread import GmailGetThread
from langchain_google_community.gmail.search import GmailSearch
from langchain_google_community.gmail.send_message import GmailSendMessage
bash pip theme={null}
  pip install langchain-google-community[gmail]
  bash uv theme={null}
  uv add langchain-google-community[gmail]
  python  theme={null}
from langchain_google_community import GMailLoader
python  theme={null}
from langchain_community.utilities import SearchApiAPIWrapper
python  theme={null}
from langchain_community.utilities import SerpAPIWrapper
python  theme={null}
from langchain_community.utilities import GoogleSerperAPIWrapper
bash pip theme={null}
  pip install youtube_search langchain # Requires base langchain
  bash uv theme={null}
  uv add youtube_search langchain # Requires base langchain
  python  theme={null}

**Examples:**

Example 1 (unknown):
```unknown
### Chat Loaders

#### Gmail

> Load chat history from Gmail threads.

Install with Gmail dependencies:

<CodeGroup>
```

Example 2 (unknown):
```unknown

```

Example 3 (unknown):
```unknown
</CodeGroup>

See [usage example and authorization instructions](/oss/python/integrations/chat_loaders/gmail).
```

Example 4 (unknown):
```unknown
## 3rd Party Integrations

Access Google services via third-party APIs.

### SearchApi

> [SearchApi](https://www.searchapi.io/) provides API access to Google search, YouTube, etc. Requires `langchain-community`.

See [usage examples and authorization instructions](/oss/python/integrations/tools/searchapi).
```

---

## Agents

**URL:** llms-txt#agents

**Contents:**
- Core components
  - Model
  - Tools
  - System prompt

Source: https://docs.langchain.com/oss/python/langchain/agents

Agents combine language models with [tools](/oss/python/langchain/tools) to create systems that can reason about tasks, decide which tools to use, and iteratively work towards solutions.

[`create_agent`](https://reference.langchain.com/python/langchain/agents/#langchain.agents.create_agent) provides a production-ready agent implementation.

[An LLM Agent runs tools in a loop to achieve a goal](https://simonwillison.net/2025/Sep/18/agents/).
An agent runs until a stop condition is met - i.e., when the model emits a final output or an iteration limit is reached.

<Info>
  [`create_agent`](https://reference.langchain.com/python/langchain/agents/#langchain.agents.create_agent) builds a **graph**-based agent runtime using [LangGraph](/oss/python/langgraph/overview). A graph consists of nodes (steps) and edges (connections) that define how your agent processes information. The agent moves through this graph, executing nodes like the model node (which calls the model), the tools node (which executes tools), or middleware.

Learn more about the [Graph API](/oss/python/langgraph/graph-api).
</Info>

The [model](/oss/python/langchain/models) is the reasoning engine of your agent. It can be specified in multiple ways, supporting both static and dynamic model selection.

Static models are configured once when creating the agent and remain unchanged throughout execution. This is the most common and straightforward approach.

To initialize a static model from a <Tooltip tip="A string that follows the format `provider:model` (e.g. openai:gpt-5)" cta="See mappings" href="https://reference.langchain.com/python/langchain/models/#langchain.chat_models.init_chat_model(model_provider)">model identifier string</Tooltip>:

<Tip>
  Model identifier strings support automatic inference (e.g., `"gpt-5"` will be inferred as `"openai:gpt-5"`). Refer to the [reference](https://reference.langchain.com/python/langchain/models/#langchain.chat_models.init_chat_model\(model_provider\)) to see a full list of model identifier string mappings.
</Tip>

For more control over the model configuration, initialize a model instance directly using the provider package. In this example, we use [`ChatOpenAI`](https://reference.langchain.com/python/integrations/langchain_openai/ChatOpenAI/). See [Chat models](/oss/python/integrations/chat) for other available chat model classes.

Model instances give you complete control over configuration. Use them when you need to set specific [parameters](/oss/python/langchain/models#parameters) like `temperature`, `max_tokens`, `timeouts`, `base_url`, and other provider-specific settings. Refer to the [reference](/oss/python/integrations/providers/all_providers) to see available params and methods on your model.

Dynamic models are selected at <Tooltip tip="The execution environment of your agent, containing immutable configuration and contextual data that persists throughout the agent's execution (e.g., user IDs, session details, or application-specific configuration).">runtime</Tooltip> based on the current <Tooltip tip="The data that flows through your agent's execution, including messages, custom fields, and any information that needs to be tracked and potentially modified during processing (e.g., user preferences or tool usage stats).">state</Tooltip> and context. This enables sophisticated routing logic and cost optimization.

To use a dynamic model, create middleware using the [`@wrap_model_call`](https://reference.langchain.com/python/langchain/middleware/#langchain.agents.middleware.wrap_model_call) decorator that modifies the model in the request:

<Warning>
  Pre-bound models (models with [`bind_tools`](https://reference.langchain.com/python/langchain_core/language_models/#langchain_core.language_models.chat_models.BaseChatModel.bind_tools) already called) are not supported when using structured output. If you need dynamic model selection with structured output, ensure the models passed to the middleware are not pre-bound.
</Warning>

<Tip>
  For model configuration details, see [Models](/oss/python/langchain/models). For dynamic model selection patterns, see [Dynamic model in middleware](/oss/python/langchain/middleware#dynamic-model).
</Tip>

Tools give agents the ability to take actions. Agents go beyond simple model-only tool binding by facilitating:

* Multiple tool calls in sequence (triggered by a single prompt)
* Parallel tool calls when appropriate
* Dynamic tool selection based on previous results
* Tool retry logic and error handling
* State persistence across tool calls

For more information, see [Tools](/oss/python/langchain/tools).

Pass a list of tools to the agent.

If an empty tool list is provided, the agent will consist of a single LLM node without tool-calling capabilities.

#### Tool error handling

To customize how tool errors are handled, use the [`@wrap_tool_call`](https://reference.langchain.com/python/langchain/middleware/#langchain.agents.middleware.wrap_tool_call) decorator to create middleware:

The agent will return a [`ToolMessage`](https://reference.langchain.com/python/langchain/messages/#langchain.messages.ToolMessage) with the custom error message when a tool fails:

#### Tool use in the ReAct loop

Agents follow the ReAct ("Reasoning + Acting") pattern, alternating between brief reasoning steps with targeted tool calls and feeding the resulting observations into subsequent decisions until they can deliver a final answer.

<Accordion title="Example of ReAct loop">
  Prompt: Identify the current most popular wireless headphones and verify availability.

* **Reasoning**: "Popularity is time-sensitive, I need to use the provided search tool."
  * **Acting**: Call `search_products("wireless headphones")`

* **Reasoning**: "I need to confirm availability for the top-ranked item before answering."
  * **Acting**: Call `check_inventory("WH-1000XM5")`

* **Reasoning**: "I have the most popular model and its stock status. I can now answer the user's question."
  * **Acting**: Produce final answer

<Tip>
  To learn more about tools, see [Tools](/oss/python/langchain/tools).
</Tip>

You can shape how your agent approaches tasks by providing a prompt. The [`system_prompt`](https://reference.langchain.com/python/langchain/agents/#langchain.agents.create_agent\(system_prompt\)) parameter can be provided as a string:

When no [`system_prompt`](https://reference.langchain.com/python/langchain/agents/#langchain.agents.create_agent\(system_prompt\)) is provided, the agent will infer its task from the messages directly.

#### Dynamic system prompt

For more advanced use cases where you need to modify the system prompt based on runtime context or agent state, you can use [middleware](/oss/python/langchain/middleware).

The [`@dynamic_prompt`](https://reference.langchain.com/python/langchain/middleware/#langchain.agents.middleware.dynamic_prompt) decorator creates middleware that generates system prompts dynamically based on the model request:

```python wrap theme={null}
from typing import TypedDict

from langchain.agents import create_agent
from langchain.agents.middleware import dynamic_prompt, ModelRequest

class Context(TypedDict):
    user_role: str

@dynamic_prompt
def user_role_prompt(request: ModelRequest) -> str:
    """Generate system prompt based on user role."""
    user_role = request.runtime.context.get("user_role", "user")
    base_prompt = "You are a helpful assistant."

if user_role == "expert":
        return f"{base_prompt} Provide detailed technical responses."
    elif user_role == "beginner":
        return f"{base_prompt} Explain concepts simply and avoid jargon."

agent = create_agent(
    model="openai:gpt-4o",
    tools=[web_search],
    middleware=[user_role_prompt],
    context_schema=Context
)

**Examples:**

Example 1 (unknown):
```unknown
<Info>
  [`create_agent`](https://reference.langchain.com/python/langchain/agents/#langchain.agents.create_agent) builds a **graph**-based agent runtime using [LangGraph](/oss/python/langgraph/overview). A graph consists of nodes (steps) and edges (connections) that define how your agent processes information. The agent moves through this graph, executing nodes like the model node (which calls the model), the tools node (which executes tools), or middleware.

  Learn more about the [Graph API](/oss/python/langgraph/graph-api).
</Info>

## Core components

### Model

The [model](/oss/python/langchain/models) is the reasoning engine of your agent. It can be specified in multiple ways, supporting both static and dynamic model selection.

#### Static model

Static models are configured once when creating the agent and remain unchanged throughout execution. This is the most common and straightforward approach.

To initialize a static model from a <Tooltip tip="A string that follows the format `provider:model` (e.g. openai:gpt-5)" cta="See mappings" href="https://reference.langchain.com/python/langchain/models/#langchain.chat_models.init_chat_model(model_provider)">model identifier string</Tooltip>:
```

Example 2 (unknown):
```unknown
<Tip>
  Model identifier strings support automatic inference (e.g., `"gpt-5"` will be inferred as `"openai:gpt-5"`). Refer to the [reference](https://reference.langchain.com/python/langchain/models/#langchain.chat_models.init_chat_model\(model_provider\)) to see a full list of model identifier string mappings.
</Tip>

For more control over the model configuration, initialize a model instance directly using the provider package. In this example, we use [`ChatOpenAI`](https://reference.langchain.com/python/integrations/langchain_openai/ChatOpenAI/). See [Chat models](/oss/python/integrations/chat) for other available chat model classes.
```

Example 3 (unknown):
```unknown
Model instances give you complete control over configuration. Use them when you need to set specific [parameters](/oss/python/langchain/models#parameters) like `temperature`, `max_tokens`, `timeouts`, `base_url`, and other provider-specific settings. Refer to the [reference](/oss/python/integrations/providers/all_providers) to see available params and methods on your model.

#### Dynamic model

Dynamic models are selected at <Tooltip tip="The execution environment of your agent, containing immutable configuration and contextual data that persists throughout the agent's execution (e.g., user IDs, session details, or application-specific configuration).">runtime</Tooltip> based on the current <Tooltip tip="The data that flows through your agent's execution, including messages, custom fields, and any information that needs to be tracked and potentially modified during processing (e.g., user preferences or tool usage stats).">state</Tooltip> and context. This enables sophisticated routing logic and cost optimization.

To use a dynamic model, create middleware using the [`@wrap_model_call`](https://reference.langchain.com/python/langchain/middleware/#langchain.agents.middleware.wrap_model_call) decorator that modifies the model in the request:
```

Example 4 (unknown):
```unknown
<Warning>
  Pre-bound models (models with [`bind_tools`](https://reference.langchain.com/python/langchain_core/language_models/#langchain_core.language_models.chat_models.BaseChatModel.bind_tools) already called) are not supported when using structured output. If you need dynamic model selection with structured output, ensure the models passed to the middleware are not pre-bound.
</Warning>

<Tip>
  For model configuration details, see [Models](/oss/python/langchain/models). For dynamic model selection patterns, see [Dynamic model in middleware](/oss/python/langchain/middleware#dynamic-model).
</Tip>

### Tools

Tools give agents the ability to take actions. Agents go beyond simple model-only tool binding by facilitating:

* Multiple tool calls in sequence (triggered by a single prompt)
* Parallel tool calls when appropriate
* Dynamic tool selection based on previous results
* Tool retry logic and error handling
* State persistence across tool calls

For more information, see [Tools](/oss/python/langchain/tools).

#### Defining tools

Pass a list of tools to the agent.
```

---

## Run the agent

**URL:** llms-txt#run-the-agent

**Contents:**
- Build a real-world agent

agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)
python wrap theme={null}
    SYSTEM_PROMPT = """You are an expert weather forecaster, who speaks in puns.

You have access to two tools:

- get_weather_for_location: use this to get the weather for a specific location
    - get_user_location: use this to get the user's location

If a user asks you for the weather, make sure you know the location. If you can tell from the question that they mean wherever they are, use the get_user_location tool to find their location."""
    python  theme={null}
    from dataclasses import dataclass
    from langchain.tools import tool, ToolRuntime

@tool
    def get_weather_for_location(city: str) -> str:
        """Get weather for a given city."""
        return f"It's always sunny in {city}!"

@dataclass
    class Context:
        """Custom runtime context schema."""
        user_id: str

@tool
    def get_user_location(runtime: ToolRuntime[Context]) -> str:
        """Retrieve user information based on user ID."""
        user_id = runtime.context.user_id
        return "Florida" if user_id == "1" else "SF"
    python  theme={null}
    from langchain.chat_models import init_chat_model

model = init_chat_model(
        "anthropic:claude-sonnet-4-5",
        temperature=0.5,
        timeout=10,
        max_tokens=1000
    )
    python  theme={null}
    from dataclasses import dataclass

# We use a dataclass here, but Pydantic models are also supported.
    @dataclass
    class ResponseFormat:
        """Response schema for the agent."""
        # A punny response (always required)
        punny_response: str
        # Any interesting information about the weather if available
        weather_conditions: str | None = None
    python  theme={null}
    from langgraph.checkpoint.memory import InMemorySaver

checkpointer = InMemorySaver()
    python  theme={null}
    agent = create_agent(
        model=model,
        system_prompt=SYSTEM_PROMPT,
        tools=[get_user_location, get_weather_for_location],
        context_schema=Context,
        response_format=ResponseFormat,
        checkpointer=checkpointer
    )

# `thread_id` is a unique identifier for a given conversation.
    config = {"configurable": {"thread_id": "1"}}

response = agent.invoke(
        {"messages": [{"role": "user", "content": "what is the weather outside?"}]},
        config=config,
        context=Context(user_id="1")
    )

print(response['structured_response'])
    # ResponseFormat(
    #     punny_response="Florida is still having a 'sun-derful' day! The sunshine is playing 'ray-dio' hits all day long! I'd say it's the perfect weather for some 'solar-bration'! If you were hoping for rain, I'm afraid that idea is all 'washed up' - the forecast remains 'clear-ly' brilliant!",
    #     weather_conditions="It's always sunny in Florida!"
    # )

# Note that we can continue the conversation using the same `thread_id`.
    response = agent.invoke(
        {"messages": [{"role": "user", "content": "thank you!"}]},
        config=config,
        context=Context(user_id="1")
    )

print(response['structured_response'])
    # ResponseFormat(
    #     punny_response="You're 'thund-erfully' welcome! It's always a 'breeze' to help you stay 'current' with the weather. I'm just 'cloud'-ing around waiting to 'shower' you with more forecasts whenever you need them. Have a 'sun-sational' day in the Florida sunshine!",
    #     weather_conditions=None
    # )
    python  theme={null}
  from dataclasses import dataclass

from langchain.agents import create_agent
  from langchain.chat_models import init_chat_model
  from langchain.tools import tool, ToolRuntime
  from langgraph.checkpoint.memory import InMemorySaver

# Define system prompt
  SYSTEM_PROMPT = """You are an expert weather forecaster, who speaks in puns.

You have access to two tools:

- get_weather_for_location: use this to get the weather for a specific location
  - get_user_location: use this to get the user's location

If a user asks you for the weather, make sure you know the location. If you can tell from the question that they mean wherever they are, use the get_user_location tool to find their location."""

# Define context schema
  @dataclass
  class Context:
      """Custom runtime context schema."""
      user_id: str

# Define tools
  @tool
  def get_weather_for_location(city: str) -> str:
      """Get weather for a given city."""
      return f"It's always sunny in {city}!"

@tool
  def get_user_location(runtime: ToolRuntime[Context]) -> str:
      """Retrieve user information based on user ID."""
      user_id = runtime.context.user_id
      return "Florida" if user_id == "1" else "SF"

# Configure model
  model = init_chat_model(
      "anthropic:claude-sonnet-4-5",
      temperature=0
  )

# Define response format
  @dataclass
  class ResponseFormat:
      """Response schema for the agent."""
      # A punny response (always required)
      punny_response: str
      # Any interesting information about the weather if available
      weather_conditions: str | None = None

# Set up memory
  checkpointer = InMemorySaver()

# Create agent
  agent = create_agent(
      model=model,
      system_prompt=SYSTEM_PROMPT,
      tools=[get_user_location, get_weather_for_location],
      context_schema=Context,
      response_format=ResponseFormat,
      checkpointer=checkpointer
  )

# Run agent
  # `thread_id` is a unique identifier for a given conversation.
  config = {"configurable": {"thread_id": "1"}}

response = agent.invoke(
      {"messages": [{"role": "user", "content": "what is the weather outside?"}]},
      config=config,
      context=Context(user_id="1")
  )

print(response['structured_response'])
  # ResponseFormat(
  #     punny_response="Florida is still having a 'sun-derful' day! The sunshine is playing 'ray-dio' hits all day long! I'd say it's the perfect weather for some 'solar-bration'! If you were hoping for rain, I'm afraid that idea is all 'washed up' - the forecast remains 'clear-ly' brilliant!",
  #     weather_conditions="It's always sunny in Florida!"
  # )

# Note that we can continue the conversation using the same `thread_id`.
  response = agent.invoke(
      {"messages": [{"role": "user", "content": "thank you!"}]},
      config=config,
      context=Context(user_id="1")
  )

print(response['structured_response'])
  # ResponseFormat(
  #     punny_response="You're 'thund-erfully' welcome! It's always a 'breeze' to help you stay 'current' with the weather. I'm just 'cloud'-ing around waiting to 'shower' you with more forecasts whenever you need them. Have a 'sun-sational' day in the Florida sunshine!",
  #     weather_conditions=None
  # )
  ```
</Expandable>

Congratulations! You now have an AI agent that can:

* **Understand context** and remember conversations
* **Use multiple tools** intelligently
* **Provide structured responses** in a consistent format
* **Handle user-specific information** through context
* **Maintain conversation state** across interactions

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/quickstart.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

**Examples:**

Example 1 (unknown):
```unknown
<Info>
  For this example, you will need to set up a [Claude (Anthropic)](https://www.anthropic.com/) account and get an API key. Then, set the `ANTHROPIC_API_KEY` environment variable in your terminal.
</Info>

## Build a real-world agent

Next, build a practical weather forecasting agent that demonstrates key production concepts:

1. **Detailed system prompts** for better agent behavior
2. **Create tools** that integrate with external data
3. **Model configuration** for consistent responses
4. **Structured output** for predictable results
5. **Conversational memory** for chat-like interactions
6. **Create and run the agent** create a fully functional agent

Let's walk through each step:

<Steps>
  <Step title="Define the system prompt">
    The system prompt defines your agent’s role and behavior. Keep it specific and actionable:
```

Example 2 (unknown):
```unknown
</Step>

  <Step title="Create tools">
    [Tools](/oss/python/langchain/tools) let a model interact with external systems by calling functions you define.
    Tools can depend on [runtime context](/oss/python/langchain/runtime) and also interact with [agent memory](/oss/python/langchain/short-term-memory).

    Notice below how the `get_user_location` tool uses runtime context:
```

Example 3 (unknown):
```unknown
<Tip>
      Tools should be well-documented: their name, description, and argument names become part of the model's prompt.
      LangChain's [`@tool` decorator](https://reference.langchain.com/python/langchain/tools/#langchain.tools.tool) adds metadata and enables runtime injection via the `ToolRuntime` parameter.
    </Tip>
  </Step>

  <Step title="Configure your model">
    Set up your [language model](/oss/python/langchain/models) with the right [parameters](/oss/python/langchain/models#parameters) for your use case:
```

Example 4 (unknown):
```unknown
</Step>

  <Step title="Define response format">
    Optionally, define a structured response format if you need the agent responses to match
    a specific schema.
```

---

## Agent definition

**URL:** llms-txt#agent-definition

graph_builder = StateGraph(State)
graph_builder.add_node(intent_classifier)

---

## state we defined for the refund agent can also be passed to our lookup agent.

**URL:** llms-txt#state-we-defined-for-the-refund-agent-can-also-be-passed-to-our-lookup-agent.

qa_graph = create_agent(qa_llm, tools=[lookup_track, lookup_artist, lookup_album])

display(Image(qa_graph.get_graph(xray=True).draw_mermaid_png()))
python  theme={null}

**Examples:**

Example 1 (unknown):
```unknown

```

Example 2 (unknown):
```unknown
<img src="https://mintcdn.com/langchain-5e9cc07a/Fr2lazPB4XVeEA7l/langsmith/images/qa-graph.png?fit=max&auto=format&n=Fr2lazPB4XVeEA7l&q=85&s=fa838edc78b2b29e8c29807d8c3dd7fd" alt="QA Graph" data-og-width="214" width="214" data-og-height="249" height="249" data-path="langsmith/images/qa-graph.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/Fr2lazPB4XVeEA7l/langsmith/images/qa-graph.png?w=280&fit=max&auto=format&n=Fr2lazPB4XVeEA7l&q=85&s=920e82f376d6bbbcfe02c07ac7a45b80 280w, https://mintcdn.com/langchain-5e9cc07a/Fr2lazPB4XVeEA7l/langsmith/images/qa-graph.png?w=560&fit=max&auto=format&n=Fr2lazPB4XVeEA7l&q=85&s=938d3bd8c19abfe27ea5efd1c996494c 560w, https://mintcdn.com/langchain-5e9cc07a/Fr2lazPB4XVeEA7l/langsmith/images/qa-graph.png?w=840&fit=max&auto=format&n=Fr2lazPB4XVeEA7l&q=85&s=e46ece85318d4c376cd6bb632bf41ab4 840w, https://mintcdn.com/langchain-5e9cc07a/Fr2lazPB4XVeEA7l/langsmith/images/qa-graph.png?w=1100&fit=max&auto=format&n=Fr2lazPB4XVeEA7l&q=85&s=3e3c715ef37db24fd0cbf8eb4ca19190 1100w, https://mintcdn.com/langchain-5e9cc07a/Fr2lazPB4XVeEA7l/langsmith/images/qa-graph.png?w=1650&fit=max&auto=format&n=Fr2lazPB4XVeEA7l&q=85&s=e3270477acbc50eb9e4e9736a5ec6afc 1650w, https://mintcdn.com/langchain-5e9cc07a/Fr2lazPB4XVeEA7l/langsmith/images/qa-graph.png?w=2500&fit=max&auto=format&n=Fr2lazPB4XVeEA7l&q=85&s=667b26bb91f33aaacbeb0a2ea749825a 2500w" />

#### Parent agent

Now let's define a parent agent that combines our two task-specific agents. The only job of the parent agent is to route to one of the sub-agents by classifying the user's current intent, and to compile the output into a followup message.
```

---

## The prebuilt ReACT agent only expects State to have a 'messages' key, so the

**URL:** llms-txt#the-prebuilt-react-agent-only-expects-state-to-have-a-'messages'-key,-so-the

---

## Build a RAG agent with LangChain

**URL:** llms-txt#build-a-rag-agent-with-langchain

**Contents:**
- Overview
  - Concepts
  - Preview
- Setup
  - Installation
  - LangSmith
  - Components
- 1. Indexing
  - Loading documents

Source: https://docs.langchain.com/oss/python/langchain/rag

One of the most powerful applications enabled by LLMs is sophisticated question-answering (Q\&A) chatbots. These are applications that can answer questions about specific source information. These applications use a technique known as Retrieval Augmented Generation, or [RAG](/oss/python/langchain/retrieval/).

This tutorial will show how to build a simple Q\&A application over an unstructured text data source. We will demonstrate:

1. A RAG [agent](#rag-agents) that executes searches with a simple tool. This is a good general-purpose implementation.
2. A two-step RAG [chain](#rag-chains) that uses just a single LLM call per query. This is a fast and effective method for simple queries.

We will cover the following concepts:

* **Indexing**: a pipeline for ingesting data from a source and indexing it. *This usually happens in a separate process.*

* **Retrieval and generation**: the actual RAG process, which takes the user query at run time and retrieves the relevant data from the index, then passes that to the model.

Once we've indexed our data, we will use an [agent](/oss/python/langchain/agents) as our orchestration framework to implement the retrieval and generation steps.

<Note>
  The indexing portion of this tutorial will largely follow the [semantic search tutorial](/oss/python/langchain/knowledge-base).

If your data is already available for search (i.e., you have a function to execute a search), or you're comfortable with the content from that tutorial, feel free to skip to the section on [retrieval and generation](#2-retrieval-and-generation)
</Note>

In this guide we'll build an app that answers questions about the website's content. The specific website we will use is the [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) blog post by Lilian Weng, which allows us to ask questions about the contents of the post.

We can create a simple indexing pipeline and RAG chain to do this in \~40 lines of code. See below for the full code snippet:

<Accordion title="Expand for full code snippet">

Check out the [LangSmith trace](https://smith.langchain.com/public/a117a1f8-c96c-4c16-a285-00b85646118e/r).
</Accordion>

This tutorial requires these langchain dependencies:

For more details, see our [Installation guide](/oss/python/langchain/install).

Many of the applications you build with LangChain will contain multiple steps with multiple invocations of LLM calls. As these applications get more complex, it becomes crucial to be able to inspect what exactly is going on inside your chain or agent. The best way to do this is with [LangSmith](https://smith.langchain.com).

After you sign up at the link above, make sure to set your environment variables to start logging traces:

Or, set them in Python:

We will need to select three components from LangChain's suite of integrations.

<Tabs>
  <Tab title="OpenAI">
    👉 Read the [OpenAI chat model integration docs](/oss/python/integrations/chat/openai/)

</CodeGroup>
  </Tab>

<Tab title="Anthropic">
    👉 Read the [Anthropic chat model integration docs](/oss/python/integrations/chat/anthropic/)

</CodeGroup>
  </Tab>

<Tab title="Azure">
    👉 Read the [Azure chat model integration docs](/oss/python/integrations/chat/azure_chat_openai/)

</CodeGroup>
  </Tab>

<Tab title="Google Gemini">
    👉 Read the [Google GenAI chat model integration docs](/oss/python/integrations/chat/google_generative_ai/)

</CodeGroup>
  </Tab>

<Tab title="AWS Bedrock">
    👉 Read the [AWS Bedrock chat model integration docs](/oss/python/integrations/chat/bedrock/)

</CodeGroup>
  </Tab>
</Tabs>

Select an embeddings model:

<Tabs>
  <Tab title="OpenAI">

<Tab title="Google Gemini">

<Tab title="Google Vertex">

<Tab title="HuggingFace">

<Tab title="MistralAI">

<Tab title="Voyage AI">

<Tab title="IBM watsonx">

Select a vector store:

<Tabs>
  <Tab title="In-memory">

<Tab title="AstraDB">

<Tab title="MongoDB">

<Tab title="PGVector">

<Tab title="PGVectorStore">

<Tab title="Pinecone">

<Note>
  **This section is an abbreviated version of the content in the [semantic search tutorial](/oss/python/langchain/knowledge-base).**

If your data is already indexed and available for search (i.e., you have a function to execute a search), or if you're comfortable with [document loaders](/oss/python/langchain/retrieval#document_loaders), [embeddings](/oss/python/langchain/retrieval#embedding_models), and [vector stores](/oss/python/langchain/retrieval#vectorstores), feel free to skip to the next section on [retrieval and generation](/oss/python/langchain/rag#2-retrieval-and-generation).
</Note>

Indexing commonly works as follows:

1. **Load**: First we need to load our data. This is done with [Document Loaders](/oss/python/langchain/retrieval#document_loaders).
2. **Split**: [Text splitters](/oss/python/langchain/retrieval#text_splitters) break large `Documents` into smaller chunks. This is useful both for indexing data and passing it into a model, as large chunks are harder to search over and won't fit in a model's finite context window.
3. **Store**: We need somewhere to store and index our splits, so that they can be searched over later. This is often done using a [VectorStore](/oss/python/langchain/retrieval#vectorstores) and [Embeddings](/oss/python/langchain/retrieval#embedding_models) model.

<img src="https://mintcdn.com/langchain-5e9cc07a/I6RpA28iE233vhYX/images/rag_indexing.png?fit=max&auto=format&n=I6RpA28iE233vhYX&q=85&s=21403ce0d0c772da84dcc5b75cff4451" alt="index_diagram" data-og-width="2583" width="2583" data-og-height="1299" height="1299" data-path="images/rag_indexing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/I6RpA28iE233vhYX/images/rag_indexing.png?w=280&fit=max&auto=format&n=I6RpA28iE233vhYX&q=85&s=bf4eb8255b82a809dbbd2bc2a96d2ed7 280w, https://mintcdn.com/langchain-5e9cc07a/I6RpA28iE233vhYX/images/rag_indexing.png?w=560&fit=max&auto=format&n=I6RpA28iE233vhYX&q=85&s=4ebc538b2c4765b609f416025e4dbbda 560w, https://mintcdn.com/langchain-5e9cc07a/I6RpA28iE233vhYX/images/rag_indexing.png?w=840&fit=max&auto=format&n=I6RpA28iE233vhYX&q=85&s=1838328a870c7353c42bf1cc2290a779 840w, https://mintcdn.com/langchain-5e9cc07a/I6RpA28iE233vhYX/images/rag_indexing.png?w=1100&fit=max&auto=format&n=I6RpA28iE233vhYX&q=85&s=675f55e100bab5e2904d27db01775ccc 1100w, https://mintcdn.com/langchain-5e9cc07a/I6RpA28iE233vhYX/images/rag_indexing.png?w=1650&fit=max&auto=format&n=I6RpA28iE233vhYX&q=85&s=4b9e544a7a3ec168651558bce854eb60 1650w, https://mintcdn.com/langchain-5e9cc07a/I6RpA28iE233vhYX/images/rag_indexing.png?w=2500&fit=max&auto=format&n=I6RpA28iE233vhYX&q=85&s=f5aeaaaea103128f374c03b05a317263 2500w" />

### Loading documents

We need to first load the blog post contents. We can use [DocumentLoaders](/oss/python/langchain/retrieval#document_loaders) for this, which are objects that load in data from a source and return a list of [Document](https://reference.langchain.com/python/langchain_core/documents/#langchain_core.documents.base.Document) objects.

In this case we'll use the [`WebBaseLoader`](/oss/python/integrations/document_loaders/web_base), which uses `urllib` to load HTML from web URLs and `BeautifulSoup` to parse it to text. We can customize the HTML -> text parsing by passing in parameters into the `BeautifulSoup` parser via `bs_kwargs` (see [BeautifulSoup docs](https://beautiful-soup-4.readthedocs.io/en/latest/#beautifulsoup)). In this case only HTML tags with class “post-content”, “post-title”, or “post-header” are relevant, so we'll remove all others.

```python  theme={null}
import bs4
from langchain_community.document_loaders import WebBaseLoader

**Examples:**

Example 1 (unknown):
```unknown

```

Example 2 (unknown):
```unknown

```

Example 3 (unknown):
```unknown
Check out the [LangSmith trace](https://smith.langchain.com/public/a117a1f8-c96c-4c16-a285-00b85646118e/r).
</Accordion>

## Setup

### Installation

This tutorial requires these langchain dependencies:

<CodeGroup>
```

Example 4 (unknown):
```unknown

```

---

## Reference

**URL:** llms-txt#reference

**Contents:**
- Reference sites

Source: https://docs.langchain.com/oss/python/reference/overview

Comprehensive API reference documentation for the LangChain and LangGraph Python and TypeScript libraries.

<CardGroup cols={2}>
  <Card title="LangChain" icon="link" href="https://reference.langchain.com/python/langchain/">
    Complete API reference for LangChain Python, including chat models, tools, agents, and more.
  </Card>

<Card title="LangGraph" icon="diagram-project" href="https://reference.langchain.com/python/langgraph/">
    Complete API reference for LangGraph Python, including graph APIs, state management, checkpointing, and more.
  </Card>

<Card title="LangChain Integrations" icon="plug" href="https://reference.langchain.com/python/integrations/">
    LangChain packages to connect with popular LLM providers, vector stores, tools, and other services.
  </Card>

<Card title="MCP Adapter" icon="plug" href="https://reference.langchain.com/python/langchain_mcp_adapters/">
    Use Model Context Protocol (MCP) tools within LangChain and LangGraph applications.
  </Card>

<Card title="Deep Agents" icon="robot" href="https://reference.langchain.com/python/deepagents/">
    Build agents that can plan, use subagents, and leverage file systems for complex tasks
  </Card>
</CardGroup>

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/reference/overview.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

---

## Run backtests on a new version of an agent

**URL:** llms-txt#run-backtests-on-a-new-version-of-an-agent

**Contents:**
- Setup
  - Configure the environment

Source: https://docs.langchain.com/langsmith/run-backtests-new-agent

Deploying your application is just the beginning of a continuous improvement process. After you deploy to production, you'll want to refine your system by enhancing prompts, language models, tools, and architectures. Backtesting involves assessing new versions of your application using historical data and comparing the new outputs to the original ones. Compared to evaluations using pre-production datasets, backtesting offers a clearer indication of whether the new version of your application is an improvement over the current deployment.

Here are the basic steps for backtesting:

1. Select sample runs from your production tracing project to test against.
2. Transform the run inputs into a dataset and record the run outputs as an initial experiment against that dataset.
3. Execute your new system on the new dataset and compare the results of the experiments.

This process will provide you with a new dataset of representative inputs, which you can version and use for backtesting your models.

<Info>
  Often, you won't have definitive "ground truth" answers available. In such cases, you can manually label the outputs or use evaluators that don't rely on reference data. If your application allows for capturing ground-truth labels, for example by allowing users to leave feedback, we strongly recommend doing so.
</Info>

### Configure the environment

Install and set environment variables. This guide requires `langsmith>=0.2.4`.

<Info>
  For convenience we'll use the LangChain OSS framework in this tutorial, but the LangSmith functionality shown is framework-agnostic.
</Info>

```python  theme={null}
import getpass
import os

**Examples:**

Example 1 (unknown):
```unknown

```

Example 2 (unknown):
```unknown
</CodeGroup>
```

---

## Hybrid

**URL:** llms-txt#hybrid

**Contents:**
  - Workflow
  - Architecture
  - Compute Platforms
  - Egress to LangSmith and the control plane
- Listeners
  - Kubernetes cluster organization
  - LangSmith workspace organization
- Use Cases
  - Each LangSmith workspace → separate Kubernetes cluster
  - Separate clusters, with shared “dev” cluster

Source: https://docs.langchain.com/langsmith/hybrid

<Info>
  **Important**
  The hybrid option requires an [Enterprise](https://langchain.com/pricing) plan.
</Info>

The **hybrid** model splits LangSmith infrastructure between LangChain's cloud and yours:

* **Control plane** (LangSmith UI, APIs, and orchestration) runs in LangChain's cloud, managed by LangChain.
* **Data plane** (your <Tooltip tip="The server that runs your applications.">LangGraph Servers</Tooltip> and agent workloads) runs in your cloud, managed by you.

This combines the convenience of a managed interface with the flexibility of running workloads in your own environment.

<Note>
  Learn more about the [control plane](/langsmith/control-plane), [data plane](/langsmith/data-plane), and [LangGraph Server](/langsmith/langgraph-server) architecture concepts.
</Note>

| Component                                                                                                    | Responsibilities                                                                                                                               | Where it runs     | Who manages it |
| ------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | -------------- |
| <Tooltip tip="The LangSmith UI and APIs for managing deployments.">Control plane</Tooltip>                   | <ul><li>UI for creating deployments and revisions</li><li>APIs for managing deployments</li><li>Observability data storage</li></ul>           | LangChain's cloud | LangChain      |
| <Tooltip tip="The runtime environment where your LangGraph Servers and agents execute.">Data plane</Tooltip> | <ul><li>Listener to sync with control plane</li><li>LangGraph Servers (your agents)</li><li>Backing services (Postgres, Redis, etc.)</li></ul> | Your cloud        | You            |

When hosting LangSmith in a hybrid model, you authenticate with a [LangSmith API key](/langsmith/create-account-api-key).

1. Use the `langgraph-cli` or [Studio](/langsmith/studio) to test your graph locally.
2. Build a Docker image using the `langgraph build` command.
3. Deploy your LangGraph Server from the [control plane UI](/langsmith/control-plane#control-plane-ui).

<Note>
  Supported Compute Platforms: [Kubernetes](https://kubernetes.io/).<br />
  For setup, refer to the [Hybrid setup guide](/langsmith/deploy-hybrid).
</Note>

<img className="block dark:hidden" src="https://mintcdn.com/langchain-5e9cc07a/JOyLr_spVEW0t2KF/langsmith/images/hybrid-with-deployment-light.png?fit=max&auto=format&n=JOyLr_spVEW0t2KF&q=85&s=86d548632d33be3644bad7213287ac78" alt="Hybrid deployment: LangChain-hosted control plane (LangSmith UI/APIs) manages deployments. Your cloud runs a listener, LangGraph Server instances, and backing stores (Postgres/Redis) on Kubernetes." data-og-width="1784" width="1784" data-og-height="1782" height="1782" data-path="langsmith/images/hybrid-with-deployment-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/JOyLr_spVEW0t2KF/langsmith/images/hybrid-with-deployment-light.png?w=280&fit=max&auto=format&n=JOyLr_spVEW0t2KF&q=85&s=2fe7b82524e32a2ce1e3726ad3bce553 280w, https://mintcdn.com/langchain-5e9cc07a/JOyLr_spVEW0t2KF/langsmith/images/hybrid-with-deployment-light.png?w=560&fit=max&auto=format&n=JOyLr_spVEW0t2KF&q=85&s=807a35d47b9c8e740a96f0a8aa4389a1 560w, https://mintcdn.com/langchain-5e9cc07a/JOyLr_spVEW0t2KF/langsmith/images/hybrid-with-deployment-light.png?w=840&fit=max&auto=format&n=JOyLr_spVEW0t2KF&q=85&s=84333efa9a9e83305b93f4b6e770b2f8 840w, https://mintcdn.com/langchain-5e9cc07a/JOyLr_spVEW0t2KF/langsmith/images/hybrid-with-deployment-light.png?w=1100&fit=max&auto=format&n=JOyLr_spVEW0t2KF&q=85&s=1d8bd0547f7814cad914b1ddc6dbfa48 1100w, https://mintcdn.com/langchain-5e9cc07a/JOyLr_spVEW0t2KF/langsmith/images/hybrid-with-deployment-light.png?w=1650&fit=max&auto=format&n=JOyLr_spVEW0t2KF&q=85&s=09f181972952ab4362b3ac70b7934d59 1650w, https://mintcdn.com/langchain-5e9cc07a/JOyLr_spVEW0t2KF/langsmith/images/hybrid-with-deployment-light.png?w=2500&fit=max&auto=format&n=JOyLr_spVEW0t2KF&q=85&s=e2d292d67dbf1fdb68758fac293c0cc7 2500w" />

<img className="hidden dark:block" src="https://mintcdn.com/langchain-5e9cc07a/JOyLr_spVEW0t2KF/langsmith/images/hybrid-with-deployment-dark.png?fit=max&auto=format&n=JOyLr_spVEW0t2KF&q=85&s=829f0ef40c315c493ef8e30857e9abf5" alt="Hybrid deployment: LangChain-hosted control plane (LangSmith UI/APIs) manages deployments. Your cloud runs a listener, LangGraph Server instances, and backing stores (Postgres/Redis) on Kubernetes." data-og-width="1784" width="1784" data-og-height="1782" height="1782" data-path="langsmith/images/hybrid-with-deployment-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/JOyLr_spVEW0t2KF/langsmith/images/hybrid-with-deployment-dark.png?w=280&fit=max&auto=format&n=JOyLr_spVEW0t2KF&q=85&s=bdb7a126e3914a07ed1ff72b66e50e9a 280w, https://mintcdn.com/langchain-5e9cc07a/JOyLr_spVEW0t2KF/langsmith/images/hybrid-with-deployment-dark.png?w=560&fit=max&auto=format&n=JOyLr_spVEW0t2KF&q=85&s=14f4f01c71edca5ce1594f3f2145f0e4 560w, https://mintcdn.com/langchain-5e9cc07a/JOyLr_spVEW0t2KF/langsmith/images/hybrid-with-deployment-dark.png?w=840&fit=max&auto=format&n=JOyLr_spVEW0t2KF&q=85&s=04f8b60076c4ff6263af77da5a65ccc1 840w, https://mintcdn.com/langchain-5e9cc07a/JOyLr_spVEW0t2KF/langsmith/images/hybrid-with-deployment-dark.png?w=1100&fit=max&auto=format&n=JOyLr_spVEW0t2KF&q=85&s=50fe58a42273562591bf695d5cdbfe57 1100w, https://mintcdn.com/langchain-5e9cc07a/JOyLr_spVEW0t2KF/langsmith/images/hybrid-with-deployment-dark.png?w=1650&fit=max&auto=format&n=JOyLr_spVEW0t2KF&q=85&s=20025a5634783e2eb1d2ba177724ccc6 1650w, https://mintcdn.com/langchain-5e9cc07a/JOyLr_spVEW0t2KF/langsmith/images/hybrid-with-deployment-dark.png?w=2500&fit=max&auto=format&n=JOyLr_spVEW0t2KF&q=85&s=79e4e542803c26c38e5fffaf2bc961bf 2500w" />

### Compute Platforms

* **Kubernetes**: Hybrid supports running the data plane on any Kubernetes cluster.

<Tip>
  For setup in Kubernetes, refer to the [Hybrid setup guide](/langsmith/deploy-hybrid)
</Tip>

### Egress to LangSmith and the control plane

In the hybrid deployment model, your self-hosted data plane will send network requests to the control plane to poll for changes that need to be implemented in the data plane. Traces from data plane deployments also get sent to the LangSmith instance integrated with the control plane. This traffic to the control plane is encrypted, over HTTPS. The data plane authenticates with the control plane with a LangSmith API key.

In order to enable this egress, you may need to update internal firewall rules or cloud resources (such as Security Groups) to [allow certain IP addresses](/langsmith/cloud#ingress-into-langchain-saas).

<Warning>
  AWS/Azure PrivateLink or GCP Private Service Connect is currently not supported. This traffic will go over the internet.
</Warning>

In the hybrid option, one or more ["listener" applications](/langsmith/data-plane#listener-application) can run depending on how your LangSmith workspaces and Kubernetes clusters are organized.

### Kubernetes cluster organization

* One or more listeners can run in a Kubernetes cluster.
* A listener can deploy into one or more namespaces in that cluster.
* Cluster owners are responsible for planning listener layout and LangGraph Server deployments.

### LangSmith workspace organization

* A workspace can be associated with one or more listeners.
* A workspace can only deploy to Kubernetes clusters where all of its listeners are deployed.

Here are some common listener configurations (not strict requirements):

### Each LangSmith workspace → separate Kubernetes cluster

* Cluster `alpha` runs workspace `A`
* Cluster `beta` runs workspace `B`

### Separate clusters, with shared “dev” cluster

* Cluster `alpha` runs workspace `A`
* Cluster `beta` runs workspace `B`
* Cluster `dev` runs workspaces `A` and `B`
* Both workspaces have two listeners; cluster `dev` has two listener deployments

### One cluster, one namespace per workspace

* Cluster `alpha`, namespace `1` runs workspace `A`
* Cluster `alpha`, namespace `2` runs workspace `B`

### One cluster, single namespace for multiple workspaces

* Cluster `alpha` runs workspace `A`
* Cluster `alpha` runs workspace `B`

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/langsmith/hybrid.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

---

## Define the two nodes we will cycle between

**URL:** llms-txt#define-the-two-nodes-we-will-cycle-between

workflow.add_node("agent", call_model)
workflow.add_node("tools", tool_node)

---

## cache hit, system prompt is cached

**URL:** llms-txt#cache-hit,-system-prompt-is-cached

**Contents:**
  - Model call limit
  - Tool call limit

agent.invoke({"messages": [HumanMessage("What's my name?")]})
python  theme={null}
from langchain.agents import create_agent
from langchain.agents.middleware import ModelCallLimitMiddleware

agent = create_agent(
    model="openai:gpt-4o",
    tools=[...],
    middleware=[
        ModelCallLimitMiddleware(
            thread_limit=10,  # Max 10 calls per thread (across runs)
            run_limit=5,  # Max 5 calls per run (single invocation)
            exit_behavior="end",  # Or "error" to raise exception
        ),
    ],
)
python  theme={null}
from langchain.agents import create_agent
from langchain.agents.middleware import ToolCallLimitMiddleware

**Examples:**

Example 1 (unknown):
```unknown
<Accordion title="Configuration options">
  <ParamField body="type" type="string" default="ephemeral">
    Cache type. Only `"ephemeral"` is currently supported.
  </ParamField>

  <ParamField body="ttl" type="string" default="5m">
    Time to live for cached content. Valid values: `"5m"` or `"1h"`
  </ParamField>

  <ParamField body="min_messages_to_cache" type="number" default="0">
    Minimum number of messages before caching starts
  </ParamField>

  <ParamField body="unsupported_model_behavior" type="string" default="warn">
    Behavior when using non-Anthropic models. Options: `"ignore"`, `"warn"`, or `"raise"`
  </ParamField>
</Accordion>

### Model call limit

Limit the number of model calls to prevent infinite loops or excessive costs.

<Tip>
  **Perfect for:**

  * Preventing runaway agents from making too many API calls
  * Enforcing cost controls on production deployments
  * Testing agent behavior within specific call budgets
</Tip>
```

Example 2 (unknown):
```unknown
<Accordion title="Configuration options">
  <ParamField body="thread_limit" type="number">
    Maximum model calls across all runs in a thread. Defaults to no limit.
  </ParamField>

  <ParamField body="run_limit" type="number">
    Maximum model calls per single invocation. Defaults to no limit.
  </ParamField>

  <ParamField body="exit_behavior" type="string" default="end">
    Behavior when limit is reached. Options: `"end"` (graceful termination) or `"error"` (raise exception)
  </ParamField>
</Accordion>

### Tool call limit

Limit the number of tool calls to specific tools or all tools.

<Tip>
  **Perfect for:**

  * Preventing excessive calls to expensive external APIs
  * Limiting web searches or database queries
  * Enforcing rate limits on specific tool usage
</Tip>
```

---

## Test a ReAct agent with Pytest/Vitest and LangSmith

**URL:** llms-txt#test-a-react-agent-with-pytest/vitest-and-langsmith

**Contents:**
- Setup
  - Installation
  - Environment Variables
- Create your app
  - Define tools
  - Define agent
- Write tests
  - Test 1: Handle off-topic questions
  - Test 2: Simple tool calling
  - Test 3: Complex tool calling

Source: https://docs.langchain.com/langsmith/test-react-agent-pytest

This tutorial will show you how to use LangSmith's integrations with popular testing tools (Pytest, Vitest, and Jest) to evaluate your LLM application. We will create a ReAct agent that answers questions about publicly traded stocks and write a comprehensive test suite for it.

This tutorial uses [LangGraph](https://langchain-ai.github.io/langgraph/tutorials/introduction/) for agent orchestration, [OpenAI's GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [Tavily](https://tavily.com/) for search, [E2B's](https://e2b.dev/) code interpreter, and [Polygon](https://polygon.io/stocks) to retrieve stock data but it can be adapted for other frameworks, models and tools with minor modifications. Tavily, E2B and Polygon are free to sign up for.

First, install the packages required for making the agent:

Next, install the testing framework:

### Environment Variables

Set the following environment variables:

To define our React agent, we will use LangGraph/LangGraph.js for the orchestation and LangChain for the LLM and tools.

First we are going to define the tools we are going to use in our agent. There are going to be 3 tools:

* A search tool using Tavily
* A code interpreter tool using E2B
* A stock information tool using Polygon

Now that we have defined all of our tools, we can use [`create_agent`](https://reference.langchain.com/python/langchain/agents/#langchain.agents.create_agent) to create our agent.

Now that we have defined our agent, let's write a few tests to ensure basic functionality. In this tutorial we are going to test whether the agent's tool calling abilities are working, whether the agent knows to ignore irrelevant questions, and whether it is able to answer complex questions that involve using all of the tools.

We need to first set up a test file and add the imports needed at the top of the file.

### Test 1: Handle off-topic questions

The first test will be a simple check that the agent does not use tools on irrelevant queries.

### Test 2: Simple tool calling

For tool calling, we are going to verify that the agent calls the correct tool with the correct parameters.

### Test 3: Complex tool calling

Some tool calls are easier to test than others. With the ticker lookup, we can assert that the correct ticker is searched. With the coding tool, the inputs and outputs of the tool are much less constrained, and there are lots of ways to get to the right answer. In this case, it's simpler to test that the tool is used correctly by running the full agent and asserting that it both calls the coding tool and that it ends up with the right answer.

### Test 4: LLM-as-a-judge

We are going to ensure that the agent's answer is grounded in the search results by running an LLM-as-a-judge evaluation. In order to trace the LLM as a judge call separately from our agent, we will use the LangSmith provided `trace_feedback` context manager in Python and `wrapEvaluator` function in JS/TS.

Once you have setup your config files (if you are using Vitest or Jest), you can run your tests using the following commands:

<Accordion title="Config files for Vitest/Jest">
  <CodeGroup>

</CodeGroup>
</Accordion>

Remember to also add the config files for [Vitest](#config-files-for-vitestjest) and [Jest](#config-files-for-vitestjest) to your project.

<Accordion title="Agent code">
  <CodeGroup>

</CodeGroup>
</Accordion>

<Accordion title="Test code">
  <CodeGroup>

</CodeGroup>
</Accordion>

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/langsmith/test-react-agent-pytest.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

**Examples:**

Example 1 (unknown):
```unknown

```

Example 2 (unknown):
```unknown
</CodeGroup>

Next, install the testing framework:

<CodeGroup>
```

Example 3 (unknown):
```unknown

```

Example 4 (unknown):
```unknown

```

---

## Update memory

**URL:** llms-txt#update-memory

@tool
def save_user_info(user_id: str, user_info: dict[str, Any], runtime: ToolRuntime) -> str:
    """Save user info."""
    store = runtime.store
    store.put(("users",), user_id, user_info)
    return "Successfully saved user info."

store = InMemoryStore()
agent = create_agent(
    model,
    tools=[get_user_info, save_user_info],
    store=store
)

---

## Build a supervisor agent

**URL:** llms-txt#build-a-supervisor-agent

**Contents:**
- Overview
  - Why use a supervisor?
  - Concepts
- Setup
  - Installation
  - LangSmith
  - Components
- 1. Define tools
- 2. Create specialized sub-agents
  - Create a calendar agent

Source: https://docs.langchain.com/oss/python/langchain/supervisor

The **supervisor pattern** is a [multi-agent](/oss/python/langchain/multi-agent) architecture where a central supervisor agent coordinates specialized worker agents. This approach excels when tasks require different types of expertise. Rather than building one agent that manages tool selection across domains, you create focused specialists coordinated by a supervisor who understands the overall workflow.

In this tutorial, you'll build a personal assistant system that demonstrates these benefits through a realistic workflow. The system will coordinate two specialists with fundamentally different responsibilities:

* A **calendar agent** that handles scheduling, availability checking, and event management.
* An **email agent** that manages communication, drafts messages, and sends notifications.

We will also incorporate [human-in-the-loop review](/oss/python/langchain/human-in-the-loop) to allow users to approve, edit, and reject actions (such as outbound emails) as desired.

### Why use a supervisor?

Multi-agent architectures allow you to partition [tools](/oss/python/langchain/tools) across workers, each with their own individual prompts or instructions. Consider an agent with direct access to all calendar and email APIs: it must choose from many similar tools, understand exact formats for each API, and handle multiple domains simultaneously. If performance degrades, it may be helpful to separate related tools and associated prompts into logical groups (in part to manage iterative improvements).

We will cover the following concepts:

* [Multi-agent systems](/oss/python/langchain/multi-agent)
* [Human-in-the-loop review](/oss/python/langchain/human-in-the-loop)

This tutorial requires the `langchain` package:

For more details, see our [Installation guide](/oss/python/langchain/install).

Set up [LangSmith](https://smith.langchain.com) to inspect what is happening inside your agent. Then set the following environment variables:

We will need to select a chat model from LangChain's suite of integrations:

<Tabs>
  <Tab title="OpenAI">
    👉 Read the [OpenAI chat model integration docs](/oss/python/integrations/chat/openai/)

</CodeGroup>
  </Tab>

<Tab title="Anthropic">
    👉 Read the [Anthropic chat model integration docs](/oss/python/integrations/chat/anthropic/)

</CodeGroup>
  </Tab>

<Tab title="Azure">
    👉 Read the [Azure chat model integration docs](/oss/python/integrations/chat/azure_chat_openai/)

</CodeGroup>
  </Tab>

<Tab title="Google Gemini">
    👉 Read the [Google GenAI chat model integration docs](/oss/python/integrations/chat/google_generative_ai/)

</CodeGroup>
  </Tab>

<Tab title="AWS Bedrock">
    👉 Read the [AWS Bedrock chat model integration docs](/oss/python/integrations/chat/bedrock/)

</CodeGroup>
  </Tab>
</Tabs>

Start by defining the tools that require structured inputs. In real applications, these would call actual APIs (Google Calendar, SendGrid, etc.). For this tutorial, you'll use stubs to demonstrate the pattern.

## 2. Create specialized sub-agents

Next, we'll create specialized sub-agents that handle each domain.

### Create a calendar agent

The calendar agent understands natural language scheduling requests and translates them into precise API calls. It handles date parsing, availability checking, and event creation.

Test the calendar agent to see how it handles natural language scheduling:

The agent parses "next Tuesday at 2pm" into ISO format ("2024-01-16T14:00:00"), calculates the end time, calls `create_calendar_event`, and returns a natural language confirmation.

### Create an email agent

The email agent handles message composition and sending. It focuses on extracting recipient information, crafting appropriate subject lines and body text, and managing email communication.

Test the email agent with a natural language request:

The agent infers the recipient from the informal request, crafts a professional subject line and body, calls `send_email`, and returns a confirmation. Each sub-agent has a narrow focus with domain-specific tools and prompts, allowing it to excel at its specific task.

## 3. Wrap sub-agents as tools

Now wrap each sub-agent as a tool that the supervisor can invoke. This is the key architectural step that creates the layered system. The supervisor will see high-level tools like "schedule\_event", not low-level tools like "create\_calendar\_event".

The tool descriptions help the supervisor decide when to use each tool, so make them clear and specific. We return only the sub-agent's final response, as the supervisor doesn't need to see intermediate reasoning or tool calls.

## 4. Create the supervisor agent

Now create the supervisor that orchestrates the sub-agents. The supervisor only sees high-level tools and makes routing decisions at the domain level, not the individual API level.

## 5. Use the supervisor

Now test your complete system with complex requests that require coordination across multiple domains:

### Example 1: Simple single-domain request

The supervisor identifies this as a calendar task, calls `schedule_event`, and the calendar agent handles date parsing and event creation.

<Tip>
  For full transparency into the information flow, including prompts and responses for each chat model call, check out the [LangSmith trace](https://smith.langchain.com/public/91a9a95f-fba9-4e84-aff0-371861ad2f4a/r) for the above run.
</Tip>

### Example 2: Complex multi-domain request

The supervisor recognizes this requires both calendar and email actions, calls `schedule_event` for the meeting, then calls `manage_email` for the reminder. Each sub-agent completes its task, and the supervisor synthesizes both results into a coherent response.

<Tip>
  Refer to the [LangSmith trace](https://smith.langchain.com/public/95cd00a3-d1f9-4dba-9731-7bf733fb6a3c/r) to see the detailed information flow for the above run, including individual chat model prompts and responses.
</Tip>

### Complete working example

Here's everything together in a runnable script:

<Expandable title="View complete code" defaultOpen={false}>
  
</Expandable>

### Understanding the architecture

Your system has three layers. The bottom layer contains rigid API tools that require exact formats. The middle layer contains sub-agents that accept natural language, translate it to structured API calls, and return natural language confirmations. The top layer contains the supervisor that routes to high-level capabilities and synthesizes results.

This separation of concerns provides several benefits: each layer has a focused responsibility, you can add new domains without affecting existing ones, and you can test and iterate on each layer independently.

## 6. Add human-in-the-loop review

It can be prudent to incorporate [human-in-the-loop review](/oss/python/langchain/human-in-the-loop) of sensitive actions. LangChain includes [built-in middleware](/oss/python/langchain/human-in-the-loop#configuring-interrupts) to review tool calls, in this case the tools invoked by sub-agents.

Let's add human-in-the-loop review to both sub-agents:

* We configure the `create_calendar_event` and `send_email` tools to interrupt, permitting all [response types](/oss/python/langchain/human-in-the-loop) (`approve`, `edit`, `reject`)
* We add a [checkpointer](/oss/python/langchain/short-term-memory) **only to the top-level agent**. This is required to pause and resume execution.

Let's repeat the query. Note that we gather interrupt events into a list to access downstream:

This time we've interrupted execution. Let's inspect the interrupt events:

We can specify decisions for each interrupt by referring to its ID using a [`Command`](https://reference.langchain.com/python/langgraph/types/#langgraph.types.Command). Refer to the [human-in-the-loop guide](/oss/python/langchain/human-in-the-loop) for additional details. For demonstration purposes, here we will accept the calendar event, but edit the subject of the outbound email:

The run proceeds with our input.

## 7. Advanced: Control information flow

By default, sub-agents receive only the request string from the supervisor. You might want to pass additional context, such as conversation history or user preferences.

### Pass additional conversational context to sub-agents

This allows sub-agents to see the full conversation context, which can be useful for resolving ambiguities like "schedule it for the same time tomorrow" (referencing a previous conversation).

<Tip>
  You can see the full context received by the sub agent in the [chat model call](https://smith.langchain.com/public/c7d54882-afb8-4039-9c5a-4112d0f458b0/r/6803571e-af78-4c68-904a-ecf55771084d) of the LangSmith trace.
</Tip>

### Control what supervisor receives

You can also customize what information flows back to the supervisor:

**Important:** Make sure sub-agent prompts emphasize that their final message should contain all relevant information. A common failure mode is sub-agents that perform tool calls but don't include the results in their final response.

The supervisor pattern creates layers of abstraction where each layer has a clear responsibility. When designing a supervisor system, start with clear domain boundaries and give each sub-agent focused tools and prompts. Write clear tool descriptions for the supervisor, test each layer independently before integration, and control information flow based on your specific needs.

<Tip>
  **When to use the supervisor pattern**

Use the supervisor pattern when you have multiple distinct domains (calendar, email, CRM, database), each domain has multiple tools or complex logic, you want centralized workflow control, and sub-agents don't need to converse directly with users.

For simpler cases with just a few tools, use a single agent. When agents need to have conversations with users, use [handoffs](/oss/python/langchain/multi-agent#handoffs) instead. For peer-to-peer collaboration between agents, consider other multi-agent patterns.
</Tip>

Learn about [handoffs](/oss/python/langchain/multi-agent#handoffs) for agent-to-agent conversations, explore [context engineering](/oss/python/langchain/context-engineering) to fine-tune information flow, read the [multi-agent overview](/oss/python/langchain/multi-agent) to compare different patterns, and use [LangSmith](https://smith.langchain.com) to debug and monitor your multi-agent system.

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/supervisor.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

**Examples:**

Example 1 (unknown):
```unknown

```

Example 2 (unknown):
```unknown
</CodeGroup>

For more details, see our [Installation guide](/oss/python/langchain/install).

### LangSmith

Set up [LangSmith](https://smith.langchain.com) to inspect what is happening inside your agent. Then set the following environment variables:

<CodeGroup>
```

Example 3 (unknown):
```unknown

```

Example 4 (unknown):
```unknown
</CodeGroup>

### Components

We will need to select a chat model from LangChain's suite of integrations:

<Tabs>
  <Tab title="OpenAI">
    👉 Read the [OpenAI chat model integration docs](/oss/python/integrations/chat/openai/)
```

---

## Remember that langgraph graphs are also langchain runnables.

**URL:** llms-txt#remember-that-langgraph-graphs-are-also-langchain-runnables.

**Contents:**
- Evaluating intermediate steps
- Running and evaluating individual nodes
- Related
- Reference code

target = example_to_state | app

experiment_results = await aevaluate(
    target,
    data="weather agent",
    evaluators=[correct],
    max_concurrency=4,  # optional
    experiment_prefix="claude-3.5-baseline",  # optional
)
python  theme={null}
def right_tool(outputs: dict) -> bool:
    tool_calls = outputs["messages"][1].tool_calls
    return bool(tool_calls and tool_calls[0]["name"] == "search")

experiment_results = await aevaluate(
    target,
    data="weather agent",
    evaluators=[correct, right_tool],
    max_concurrency=4,  # optional
    experiment_prefix="claude-3.5-baseline",  # optional
)
python  theme={null}
from langsmith.schemas import Run, Example

def right_tool_from_run(run: Run, example: Example) -> dict:
    # Get documents and answer
    first_model_run = next(run for run in root_run.child_runs if run.name == "agent")
    tool_calls = first_model_run.outputs["messages"][-1].tool_calls
    right_tool = bool(tool_calls and tool_calls[0]["name"] == "search")
    return {"key": "right_tool", "value": right_tool}

experiment_results = await aevaluate(
    target,
    data="weather agent",
    evaluators=[correct, right_tool_from_run],
    max_concurrency=4,  # optional
    experiment_prefix="claude-3.5-baseline",  # optional
)
python  theme={null}
node_target = example_to_state | app.nodes["agent"]

node_experiment_results = await aevaluate(
    node_target,
    data="weather agent",
    evaluators=[right_tool_from_run],
    max_concurrency=4,  # optional
    experiment_prefix="claude-3.5-model-node",  # optional
)
python  theme={null}
  from typing import Annotated, Literal, TypedDict
  from langchain.chat_models import init_chat_model
  from langchain.tools import tool
  from langgraph.prebuilt import ToolNode
  from langgraph.graph import END, START, StateGraph
  from langgraph.graph.message import add_messages
  from langsmith import Client, aevaluate

# Define a graph
  class State(TypedDict):
      # Messages have the type "list". The 'add_messages' function
      # in the annotation defines how this state key should be updated
      # (in this case, it appends messages to the list, rather than overwriting them)
      messages: Annotated[list, add_messages]

# Define the tools for the agent to use
  @tool
  def search(query: str) -> str:
      """Call to surf the web."""
      # This is a placeholder, but don't tell the LLM that...
      if "sf" in query.lower() or "san francisco" in query.lower():
          return "It's 60 degrees and foggy."
      return "It's 90 degrees and sunny."

tools = [search]
  tool_node = ToolNode(tools)
  model = init_chat_model("claude-3-5-sonnet-latest").bind_tools(tools)

# Define the function that determines whether to continue or not
  def should_continue(state: State) -> Literal["tools", END]:
      messages = state['messages']
      last_message = messages[-1]

# If the LLM makes a tool call, then we route to the "tools" node
      if last_message.tool_calls:
          return "tools"

# Otherwise, we stop (reply to the user)
      return END

# Define the function that calls the model
  def call_model(state: State):
      messages = state['messages']
      response = model.invoke(messages)
      # We return a list, because this will get added to the existing list
      return {"messages": [response]}

# Define a new graph
  workflow = StateGraph(State)

# Define the two nodes we will cycle between
  workflow.add_node("agent", call_model)
  workflow.add_node("tools", tool_node)

# Set the entrypoint as 'agent'
  # This means that this node is the first one called
  workflow.add_edge(START, "agent")

# We now add a conditional edge
  workflow.add_conditional_edges(
      # First, we define the start node. We use 'agent'.
      # This means these are the edges taken after the 'agent' node is called.
      "agent",
      # Next, we pass in the function that will determine which node is called next.
      should_continue,
  )

# We now add a normal edge from 'tools' to 'agent'.
  # This means that after 'tools' is called, 'agent' node is called next.
  workflow.add_edge("tools", 'agent')

# Finally, we compile it!
  # This compiles it into a LangChain Runnable,
  # meaning you can use it as you would any other runnable.
  # Note that we're (optionally) passing the memory when compiling the graph
  app = workflow.compile()

questions = [
      "what's the weather in sf",
      "whats the weather in san fran",
      "whats the weather in tangier"
  ]

answers = [
      "It's 60 degrees and foggy.",
      "It's 60 degrees and foggy.",
      "It's 90 degrees and sunny.",
  ]

# Create a dataset
  ls_client = Client()
  dataset = ls_client.create_dataset(
      "weather agent",
      inputs=[{"question": q} for q in questions],
      outputs=[{"answers": a} for a in answers],
  )

# Define evaluators
  async def correct(outputs: dict, reference_outputs: dict) -> bool:
      instructions = (
          "Given an actual answer and an expected answer, determine whether"
          " the actual answer contains all of the information in the"
          " expected answer. Respond with 'CORRECT' if the actual answer"
          " does contain all of the expected information and 'INCORRECT'"
          " otherwise. Do not include anything else in your response."
      )
      # Our graph outputs a State dictionary, which in this case means
      # we'll have a 'messages' key and the final message should
      # be our actual answer.
      actual_answer = outputs["messages"][-1].content
      expected_answer = reference_outputs["answer"]
      user_msg = (
          f"ACTUAL ANSWER: {actual_answer}"
          f"\n\nEXPECTED ANSWER: {expected_answer}"
      )
      response = await judge_llm.ainvoke(
          [
              {"role": "system", "content": instructions},
              {"role": "user", "content": user_msg}
          ]
      )
      return response.content.upper() == "CORRECT"

def right_tool(outputs: dict) -> bool:
      tool_calls = outputs["messages"][1].tool_calls
      return bool(tool_calls and tool_calls[0]["name"] == "search")

# Run evaluation
  experiment_results = await aevaluate(
      target,
      data="weather agent",
      evaluators=[correct, right_tool],
      max_concurrency=4,  # optional
      experiment_prefix="claude-3.5-baseline",  # optional
  )
  ```
</Accordion>

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/langsmith/evaluate-graph.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

**Examples:**

Example 1 (unknown):
```unknown
## Evaluating intermediate steps

Often it is valuable to evaluate not only the final output of an agent but also the intermediate steps it has taken. What's nice about `langgraph` is that the output of a graph is a state object that often already carries information about the intermediate steps taken. Usually we can evaluate whatever we're interested in just by looking at the messages in our state. For example, we can look at the messages to assert that the model invoked the 'search' tool upon as a first step.

Requires `langsmith>=0.2.0`
```

Example 2 (unknown):
```unknown
If we need access to information about intermediate steps that isn't in state, we can look at the Run object. This contains the full traces for all node inputs and outputs:

<Check>
  See more about what arguments you can pass to custom evaluators in this [how-to guide](/langsmith/code-evaluator).
</Check>
```

Example 3 (unknown):
```unknown
## Running and evaluating individual nodes

Sometimes you want to evaluate a single node directly to save time and costs. `langgraph` makes it easy to do this. In this case we can even continue using the evaluators we've been using.
```

Example 4 (unknown):
```unknown
## Related

* [`langgraph` evaluation docs](https://langchain-ai.github.io/langgraph/tutorials/#evaluation)

## Reference code

<Accordion title="Click to see a consolidated code snippet">
```

---

## Create a developer agent

**URL:** llms-txt#create-a-developer-agent

developer = autogen.AssistantAgent(
    name="developer",
    llm_config={"config_list": config_list},
    system_message="""You are a senior software developer. Your role is to:
    1. Write clean, efficient code
    2. Address feedback from code reviews
    3. Explain your implementation decisions
    4. Implement requested features and fixes""",
)

---

## Get the tool call

**URL:** llms-txt#get-the-tool-call

**Contents:**
- Prompt chaining
- Parallelization
- Routing
- Orchestrator-worker
  - Creating workers in LangGraph

msg.tool_calls
python Graph API theme={null}
  from typing_extensions import TypedDict
  from langgraph.graph import StateGraph, START, END
  from IPython.display import Image, display

# Graph state
  class State(TypedDict):
      topic: str
      joke: str
      improved_joke: str
      final_joke: str

# Nodes
  def generate_joke(state: State):
      """First LLM call to generate initial joke"""

msg = llm.invoke(f"Write a short joke about {state['topic']}")
      return {"joke": msg.content}

def check_punchline(state: State):
      """Gate function to check if the joke has a punchline"""

# Simple check - does the joke contain "?" or "!"
      if "?" in state["joke"] or "!" in state["joke"]:
          return "Pass"
      return "Fail"

def improve_joke(state: State):
      """Second LLM call to improve the joke"""

msg = llm.invoke(f"Make this joke funnier by adding wordplay: {state['joke']}")
      return {"improved_joke": msg.content}

def polish_joke(state: State):
      """Third LLM call for final polish"""
      msg = llm.invoke(f"Add a surprising twist to this joke: {state['improved_joke']}")
      return {"final_joke": msg.content}

# Build workflow
  workflow = StateGraph(State)

# Add nodes
  workflow.add_node("generate_joke", generate_joke)
  workflow.add_node("improve_joke", improve_joke)
  workflow.add_node("polish_joke", polish_joke)

# Add edges to connect nodes
  workflow.add_edge(START, "generate_joke")
  workflow.add_conditional_edges(
      "generate_joke", check_punchline, {"Fail": "improve_joke", "Pass": END}
  )
  workflow.add_edge("improve_joke", "polish_joke")
  workflow.add_edge("polish_joke", END)

# Compile
  chain = workflow.compile()

# Show workflow
  display(Image(chain.get_graph().draw_mermaid_png()))

# Invoke
  state = chain.invoke({"topic": "cats"})
  print("Initial joke:")
  print(state["joke"])
  print("\n--- --- ---\n")
  if "improved_joke" in state:
      print("Improved joke:")
      print(state["improved_joke"])
      print("\n--- --- ---\n")

print("Final joke:")
      print(state["final_joke"])
  else:
      print("Joke failed quality gate - no punchline detected!")
  python Functional API theme={null}
  from langgraph.func import entrypoint, task

# Tasks
  @task
  def generate_joke(topic: str):
      """First LLM call to generate initial joke"""
      msg = llm.invoke(f"Write a short joke about {topic}")
      return msg.content

def check_punchline(joke: str):
      """Gate function to check if the joke has a punchline"""
      # Simple check - does the joke contain "?" or "!"
      if "?" in joke or "!" in joke:
          return "Fail"

@task
  def improve_joke(joke: str):
      """Second LLM call to improve the joke"""
      msg = llm.invoke(f"Make this joke funnier by adding wordplay: {joke}")
      return msg.content

@task
  def polish_joke(joke: str):
      """Third LLM call for final polish"""
      msg = llm.invoke(f"Add a surprising twist to this joke: {joke}")
      return msg.content

@entrypoint()
  def prompt_chaining_workflow(topic: str):
      original_joke = generate_joke(topic).result()
      if check_punchline(original_joke) == "Pass":
          return original_joke

improved_joke = improve_joke(original_joke).result()
      return polish_joke(improved_joke).result()

# Invoke
  for step in prompt_chaining_workflow.stream("cats", stream_mode="updates"):
      print(step)
      print("\n")
  python Graph API theme={null}
  # Graph state
  class State(TypedDict):
      topic: str
      joke: str
      story: str
      poem: str
      combined_output: str

# Nodes
  def call_llm_1(state: State):
      """First LLM call to generate initial joke"""

msg = llm.invoke(f"Write a joke about {state['topic']}")
      return {"joke": msg.content}

def call_llm_2(state: State):
      """Second LLM call to generate story"""

msg = llm.invoke(f"Write a story about {state['topic']}")
      return {"story": msg.content}

def call_llm_3(state: State):
      """Third LLM call to generate poem"""

msg = llm.invoke(f"Write a poem about {state['topic']}")
      return {"poem": msg.content}

def aggregator(state: State):
      """Combine the joke and story into a single output"""

combined = f"Here's a story, joke, and poem about {state['topic']}!\n\n"
      combined += f"STORY:\n{state['story']}\n\n"
      combined += f"JOKE:\n{state['joke']}\n\n"
      combined += f"POEM:\n{state['poem']}"
      return {"combined_output": combined}

# Build workflow
  parallel_builder = StateGraph(State)

# Add nodes
  parallel_builder.add_node("call_llm_1", call_llm_1)
  parallel_builder.add_node("call_llm_2", call_llm_2)
  parallel_builder.add_node("call_llm_3", call_llm_3)
  parallel_builder.add_node("aggregator", aggregator)

# Add edges to connect nodes
  parallel_builder.add_edge(START, "call_llm_1")
  parallel_builder.add_edge(START, "call_llm_2")
  parallel_builder.add_edge(START, "call_llm_3")
  parallel_builder.add_edge("call_llm_1", "aggregator")
  parallel_builder.add_edge("call_llm_2", "aggregator")
  parallel_builder.add_edge("call_llm_3", "aggregator")
  parallel_builder.add_edge("aggregator", END)
  parallel_workflow = parallel_builder.compile()

# Show workflow
  display(Image(parallel_workflow.get_graph().draw_mermaid_png()))

# Invoke
  state = parallel_workflow.invoke({"topic": "cats"})
  print(state["combined_output"])
  python Functional API theme={null}
  @task
  def call_llm_1(topic: str):
      """First LLM call to generate initial joke"""
      msg = llm.invoke(f"Write a joke about {topic}")
      return msg.content

@task
  def call_llm_2(topic: str):
      """Second LLM call to generate story"""
      msg = llm.invoke(f"Write a story about {topic}")
      return msg.content

@task
  def call_llm_3(topic):
      """Third LLM call to generate poem"""
      msg = llm.invoke(f"Write a poem about {topic}")
      return msg.content

@task
  def aggregator(topic, joke, story, poem):
      """Combine the joke and story into a single output"""

combined = f"Here's a story, joke, and poem about {topic}!\n\n"
      combined += f"STORY:\n{story}\n\n"
      combined += f"JOKE:\n{joke}\n\n"
      combined += f"POEM:\n{poem}"
      return combined

# Build workflow
  @entrypoint()
  def parallel_workflow(topic: str):
      joke_fut = call_llm_1(topic)
      story_fut = call_llm_2(topic)
      poem_fut = call_llm_3(topic)
      return aggregator(
          topic, joke_fut.result(), story_fut.result(), poem_fut.result()
      ).result()

# Invoke
  for step in parallel_workflow.stream("cats", stream_mode="updates"):
      print(step)
      print("\n")
  python Graph API theme={null}
  from typing_extensions import Literal
  from langchain.messages import HumanMessage, SystemMessage

# Schema for structured output to use as routing logic
  class Route(BaseModel):
      step: Literal["poem", "story", "joke"] = Field(
          None, description="The next step in the routing process"
      )

# Augment the LLM with schema for structured output
  router = llm.with_structured_output(Route)

# State
  class State(TypedDict):
      input: str
      decision: str
      output: str

# Nodes
  def llm_call_1(state: State):
      """Write a story"""

result = llm.invoke(state["input"])
      return {"output": result.content}

def llm_call_2(state: State):
      """Write a joke"""

result = llm.invoke(state["input"])
      return {"output": result.content}

def llm_call_3(state: State):
      """Write a poem"""

result = llm.invoke(state["input"])
      return {"output": result.content}

def llm_call_router(state: State):
      """Route the input to the appropriate node"""

# Run the augmented LLM with structured output to serve as routing logic
      decision = router.invoke(
          [
              SystemMessage(
                  content="Route the input to story, joke, or poem based on the user's request."
              ),
              HumanMessage(content=state["input"]),
          ]
      )

return {"decision": decision.step}

# Conditional edge function to route to the appropriate node
  def route_decision(state: State):
      # Return the node name you want to visit next
      if state["decision"] == "story":
          return "llm_call_1"
      elif state["decision"] == "joke":
          return "llm_call_2"
      elif state["decision"] == "poem":
          return "llm_call_3"

# Build workflow
  router_builder = StateGraph(State)

# Add nodes
  router_builder.add_node("llm_call_1", llm_call_1)
  router_builder.add_node("llm_call_2", llm_call_2)
  router_builder.add_node("llm_call_3", llm_call_3)
  router_builder.add_node("llm_call_router", llm_call_router)

# Add edges to connect nodes
  router_builder.add_edge(START, "llm_call_router")
  router_builder.add_conditional_edges(
      "llm_call_router",
      route_decision,
      {  # Name returned by route_decision : Name of next node to visit
          "llm_call_1": "llm_call_1",
          "llm_call_2": "llm_call_2",
          "llm_call_3": "llm_call_3",
      },
  )
  router_builder.add_edge("llm_call_1", END)
  router_builder.add_edge("llm_call_2", END)
  router_builder.add_edge("llm_call_3", END)

# Compile workflow
  router_workflow = router_builder.compile()

# Show the workflow
  display(Image(router_workflow.get_graph().draw_mermaid_png()))

# Invoke
  state = router_workflow.invoke({"input": "Write me a joke about cats"})
  print(state["output"])
  python Functional API theme={null}
  from typing_extensions import Literal
  from pydantic import BaseModel
  from langchain.messages import HumanMessage, SystemMessage

# Schema for structured output to use as routing logic
  class Route(BaseModel):
      step: Literal["poem", "story", "joke"] = Field(
          None, description="The next step in the routing process"
      )

# Augment the LLM with schema for structured output
  router = llm.with_structured_output(Route)

@task
  def llm_call_1(input_: str):
      """Write a story"""
      result = llm.invoke(input_)
      return result.content

@task
  def llm_call_2(input_: str):
      """Write a joke"""
      result = llm.invoke(input_)
      return result.content

@task
  def llm_call_3(input_: str):
      """Write a poem"""
      result = llm.invoke(input_)
      return result.content

def llm_call_router(input_: str):
      """Route the input to the appropriate node"""
      # Run the augmented LLM with structured output to serve as routing logic
      decision = router.invoke(
          [
              SystemMessage(
                  content="Route the input to story, joke, or poem based on the user's request."
              ),
              HumanMessage(content=input_),
          ]
      )
      return decision.step

# Create workflow
  @entrypoint()
  def router_workflow(input_: str):
      next_step = llm_call_router(input_)
      if next_step == "story":
          llm_call = llm_call_1
      elif next_step == "joke":
          llm_call = llm_call_2
      elif next_step == "poem":
          llm_call = llm_call_3

return llm_call(input_).result()

# Invoke
  for step in router_workflow.stream("Write me a joke about cats", stream_mode="updates"):
      print(step)
      print("\n")
  python Graph API theme={null}
  from typing import Annotated, List
  import operator

# Schema for structured output to use in planning
  class Section(BaseModel):
      name: str = Field(
          description="Name for this section of the report.",
      )
      description: str = Field(
          description="Brief overview of the main topics and concepts to be covered in this section.",
      )

class Sections(BaseModel):
      sections: List[Section] = Field(
          description="Sections of the report.",
      )

# Augment the LLM with schema for structured output
  planner = llm.with_structured_output(Sections)
  python Functional API theme={null}
  from typing import List

# Schema for structured output to use in planning
  class Section(BaseModel):
      name: str = Field(
          description="Name for this section of the report.",
      )
      description: str = Field(
          description="Brief overview of the main topics and concepts to be covered in this section.",
      )

class Sections(BaseModel):
      sections: List[Section] = Field(
          description="Sections of the report.",
      )

# Augment the LLM with schema for structured output
  planner = llm.with_structured_output(Sections)

@task
  def orchestrator(topic: str):
      """Orchestrator that generates a plan for the report"""
      # Generate queries
      report_sections = planner.invoke(
          [
              SystemMessage(content="Generate a plan for the report."),
              HumanMessage(content=f"Here is the report topic: {topic}"),
          ]
      )

return report_sections.sections

@task
  def llm_call(section: Section):
      """Worker writes a section of the report"""

# Generate section
      result = llm.invoke(
          [
              SystemMessage(content="Write a report section."),
              HumanMessage(
                  content=f"Here is the section name: {section.name} and description: {section.description}"
              ),
          ]
      )

# Write the updated section to completed sections
      return result.content

@task
  def synthesizer(completed_sections: list[str]):
      """Synthesize full report from sections"""
      final_report = "\n\n---\n\n".join(completed_sections)
      return final_report

@entrypoint()
  def orchestrator_worker(topic: str):
      sections = orchestrator(topic).result()
      section_futures = [llm_call(section) for section in sections]
      final_report = synthesizer(
          [section_fut.result() for section_fut in section_futures]
      ).result()
      return final_report

# Invoke
  report = orchestrator_worker.invoke("Create a report on LLM scaling laws")
  from IPython.display import Markdown
  Markdown(report)
  python  theme={null}
from langgraph.types import Send

**Examples:**

Example 1 (unknown):
```unknown
## Prompt chaining

Prompt chaining is when each LLM call processes the output of the previous call. It's often used for performing well-defined tasks that can be broken down into smaller, verifiable steps. Some examples include:

* Translating documents into different languages
* Verifying generated content for consistency

<img src="https://mintcdn.com/langchain-5e9cc07a/dL5Sn6Cmy9pwtY0V/oss/images/prompt_chain.png?fit=max&auto=format&n=dL5Sn6Cmy9pwtY0V&q=85&s=762dec147c31b8dc6ebb0857e236fc1f" alt="Prompt chaining" data-og-width="1412" width="1412" data-og-height="444" height="444" data-path="oss/images/prompt_chain.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/dL5Sn6Cmy9pwtY0V/oss/images/prompt_chain.png?w=280&fit=max&auto=format&n=dL5Sn6Cmy9pwtY0V&q=85&s=fda27cf4f997e350d4ce48be16049c47 280w, https://mintcdn.com/langchain-5e9cc07a/dL5Sn6Cmy9pwtY0V/oss/images/prompt_chain.png?w=560&fit=max&auto=format&n=dL5Sn6Cmy9pwtY0V&q=85&s=1374b6de11900d394fc73722a3a6040e 560w, https://mintcdn.com/langchain-5e9cc07a/dL5Sn6Cmy9pwtY0V/oss/images/prompt_chain.png?w=840&fit=max&auto=format&n=dL5Sn6Cmy9pwtY0V&q=85&s=25246c7111a87b5df5a2af24a0181efe 840w, https://mintcdn.com/langchain-5e9cc07a/dL5Sn6Cmy9pwtY0V/oss/images/prompt_chain.png?w=1100&fit=max&auto=format&n=dL5Sn6Cmy9pwtY0V&q=85&s=0c57da86a49cf966cc090497ade347f1 1100w, https://mintcdn.com/langchain-5e9cc07a/dL5Sn6Cmy9pwtY0V/oss/images/prompt_chain.png?w=1650&fit=max&auto=format&n=dL5Sn6Cmy9pwtY0V&q=85&s=a1b5c8fc644d7a80c0792b71769c97da 1650w, https://mintcdn.com/langchain-5e9cc07a/dL5Sn6Cmy9pwtY0V/oss/images/prompt_chain.png?w=2500&fit=max&auto=format&n=dL5Sn6Cmy9pwtY0V&q=85&s=8a3f66f0e365e503a85b30be48bc1a76 2500w" />

<CodeGroup>
```

Example 2 (unknown):
```unknown

```

Example 3 (unknown):
```unknown
</CodeGroup>

## Parallelization

With parallelization, LLMs work simultaneously on a task. This is either done by running multiple independent subtasks at the same time, or running the same task multiple times to check for different outputs. Parallelization is commonly used to:

* Split up subtasks and run them in parallel, which increases speed
* Run tasks multiple times to check for different outputs, which increases confidence

Some examples include:

* Running one subtask that processes a document for keywords, and a second subtask to check for formatting errors
* Running a task multiple times that scores a document for accuracy based on different criteria, like the number of citations, the number of sources used, and the quality of the sources

<img src="https://mintcdn.com/langchain-5e9cc07a/dL5Sn6Cmy9pwtY0V/oss/images/parallelization.png?fit=max&auto=format&n=dL5Sn6Cmy9pwtY0V&q=85&s=8afe3c427d8cede6fed1e4b2a5107b71" alt="parallelization.png" data-og-width="1020" width="1020" data-og-height="684" height="684" data-path="oss/images/parallelization.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/dL5Sn6Cmy9pwtY0V/oss/images/parallelization.png?w=280&fit=max&auto=format&n=dL5Sn6Cmy9pwtY0V&q=85&s=88e51062b14d9186a6f0ea246bc48635 280w, https://mintcdn.com/langchain-5e9cc07a/dL5Sn6Cmy9pwtY0V/oss/images/parallelization.png?w=560&fit=max&auto=format&n=dL5Sn6Cmy9pwtY0V&q=85&s=934941ca52019b7cbce7fbdd31d00f0f 560w, https://mintcdn.com/langchain-5e9cc07a/dL5Sn6Cmy9pwtY0V/oss/images/parallelization.png?w=840&fit=max&auto=format&n=dL5Sn6Cmy9pwtY0V&q=85&s=30b5c86c545d0e34878ff0a2c367dd0a 840w, https://mintcdn.com/langchain-5e9cc07a/dL5Sn6Cmy9pwtY0V/oss/images/parallelization.png?w=1100&fit=max&auto=format&n=dL5Sn6Cmy9pwtY0V&q=85&s=6227d2c39f332eaeda23f7db66871dd7 1100w, https://mintcdn.com/langchain-5e9cc07a/dL5Sn6Cmy9pwtY0V/oss/images/parallelization.png?w=1650&fit=max&auto=format&n=dL5Sn6Cmy9pwtY0V&q=85&s=283f3ee2924a385ab88f2cbfd9c9c48c 1650w, https://mintcdn.com/langchain-5e9cc07a/dL5Sn6Cmy9pwtY0V/oss/images/parallelization.png?w=2500&fit=max&auto=format&n=dL5Sn6Cmy9pwtY0V&q=85&s=69f6a97716b38998b7b399c3d8ac7d9c 2500w" />

<CodeGroup>
```

Example 4 (unknown):
```unknown

```

---

## Tools

**URL:** llms-txt#tools

from langchain.tools import tool

---

## How to run multiple agents on the same thread

**URL:** llms-txt#how-to-run-multiple-agents-on-the-same-thread

**Contents:**
- Setup
- Run assistants on thread
  - Run OpenAI assistant
  - Run default assistant

Source: https://docs.langchain.com/langsmith/same-thread

In LangSmith Deployment, a thread is not explicitly associated with a particular agent.
This means that you can run multiple agents on the same thread, which allows a different agent to continue from an initial agent's progress.

In this example, we will create two agents and then call them both on the same thread.
You'll see that the second agent will respond using information from the [checkpoint](/oss/python/langgraph/graph-api#checkpointer-state) generated in the thread by the first agent as context.

<Tabs>
  <Tab title="Python">
    
  </Tab>

<Tab title="Javascript">
    
  </Tab>

<Tab title="CURL">
    
  </Tab>
</Tabs>

We can see that these agents are different:

<Tabs>
  <Tab title="Python">
    
  </Tab>

<Tab title="Javascript">
    
  </Tab>

<Tab title="CURL">
    
  </Tab>
</Tabs>

<Tabs>
  <Tab title="Python">
    
  </Tab>

<Tab title="Javascript">
    
  </Tab>

<Tab title="CURL">
    
  </Tab>
</Tabs>

## Run assistants on thread

### Run OpenAI assistant

We can now run the OpenAI assistant on the thread first.

<Tabs>
  <Tab title="Python">
    
  </Tab>

<Tab title="Javascript">
    
  </Tab>

<Tab title="CURL">
    
  </Tab>
</Tabs>

### Run default assistant

Now, we can run it on the default assistant and see that this second assistant is aware of the initial question, and can answer the question, "and you?":

<Tabs>
  <Tab title="Python">
    
  </Tab>

<Tab title="Javascript">
    
  </Tab>

<Tab title="CURL">
    
  </Tab>
</Tabs>

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/langsmith/same-thread.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

**Examples:**

Example 1 (unknown):
```unknown
</Tab>

  <Tab title="Javascript">
```

Example 2 (unknown):
```unknown
</Tab>

  <Tab title="CURL">
```

Example 3 (unknown):
```unknown
</Tab>
</Tabs>

We can see that these agents are different:

<Tabs>
  <Tab title="Python">
```

Example 4 (unknown):
```unknown
</Tab>

  <Tab title="Javascript">
```

---

## pass the thread ID to persist agent outputs for future interactions

**URL:** llms-txt#pass-the-thread-id-to-persist-agent-outputs-for-future-interactions

**Contents:**
- 4. Prepare for deployment
- 5. Deploy to LangSmith

config = {"configurable": {"thread_id": "1"}}

for chunk in graph.stream(
    {
        "messages": [
            {
                "role": "user",
                "content": "Find numbers between 10 and 30 in fibonacci sequence",
            }
        ]
    },
    config,
):
    print(chunk)

user_proxy (to assistant):

Find numbers between 10 and 30 in fibonacci sequence

--------------------------------------------------------------------------------
assistant (to user_proxy):

To find numbers between 10 and 30 in the Fibonacci sequence, we can generate the Fibonacci sequence and check which numbers fall within this range. Here's a plan:

1. Generate Fibonacci numbers starting from 0.
2. Continue generating until the numbers exceed 30.
3. Collect and print the numbers that are between 10 and 30.

...
python {highlight={10}} theme={null}
for chunk in graph.stream(
    {
        "messages": [
            {
                "role": "user",
                "content": "Multiply the last number by 3",
            }
        ]
    },
    config,
):
    print(chunk)

user_proxy (to assistant):

Multiply the last number by 3
Context:
Find numbers between 10 and 30 in fibonacci sequence
The Fibonacci numbers between 10 and 30 are 13 and 21.

These numbers are part of the Fibonacci sequence, which is generated by adding the two preceding numbers to get the next number, starting from 0 and 1.

The sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

As you can see, 13 and 21 are the only numbers in this sequence that fall between 10 and 30.

--------------------------------------------------------------------------------
assistant (to user_proxy):

The last number in the Fibonacci sequence between 10 and 30 is 21. Multiplying 21 by 3 gives:

--------------------------------------------------------------------------------
{'call_autogen_agent': {'messages': {'role': 'assistant', 'content': 'The last number in the Fibonacci sequence between 10 and 30 is 21. Multiplying 21 by 3 gives:\n\n21 * 3 = 63\n\nTERMINATE'}}}

my-autogen-agent/
├── agent.py          # Your main agent code
├── requirements.txt  # Python dependencies
└── langgraph.json   # LangGraph configuration
python  theme={null}
    import os
    import autogen
    from langchain_core.messages import convert_to_openai_messages
    from langgraph.graph import StateGraph, MessagesState, START
    from langgraph.checkpoint.memory import MemorySaver

# AutoGen configuration
    config_list = [{"model": "gpt-4o", "api_key": os.environ["OPENAI_API_KEY"]}]

llm_config = {
        "timeout": 600,
        "cache_seed": 42,
        "config_list": config_list,
        "temperature": 0,
    }

# Create AutoGen agents
    autogen_agent = autogen.AssistantAgent(
        name="assistant",
        llm_config=llm_config,
    )

user_proxy = autogen.UserProxyAgent(
        name="user_proxy",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=10,
        is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
        code_execution_config={
            "work_dir": "/tmp/autogen_work",
            "use_docker": False,
        },
        llm_config=llm_config,
        system_message="Reply TERMINATE if the task has been solved at full satisfaction.",
    )

def call_autogen_agent(state: MessagesState):
        """Node function that calls the AutoGen agent"""
        messages = convert_to_openai_messages(state["messages"])
        last_message = messages[-1]
        carryover = messages[:-1] if len(messages) > 1 else []

response = user_proxy.initiate_chat(
            autogen_agent,
            message=last_message,
            carryover=carryover
        )

final_content = response.chat_history[-1]["content"]
        return {"messages": {"role": "assistant", "content": final_content}}

# Create and compile the graph
    def create_graph():
        checkpointer = MemorySaver()
        builder = StateGraph(MessagesState)
        builder.add_node("autogen", call_autogen_agent)
        builder.add_edge(START, "autogen")
        return builder.compile(checkpointer=checkpointer)

# Export the graph for LangSmith
    graph = create_graph()
    
    langgraph>=0.1.0
    pyautogen>=0.2.0
    langchain-core>=0.1.0
    langchain-openai>=0.0.5
    json  theme={null}
    {
    "dependencies": ["."],
    "graphs": {
        "autogen_agent": "./agent.py:graph"
    },
    "env": ".env"
    }
    bash pip theme={null}
  pip install -U langgraph-cli
  bash uv theme={null}
  uv add langgraph-cli
  
langgraph deploy --config langgraph.json
```

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/langsmith/autogen-integration.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

**Examples:**

Example 1 (unknown):
```unknown
**Output:**
```

Example 2 (unknown):
```unknown
Since we're leveraging LangGraph's [persistence](/oss/python/langgraph/persistence) features we can now continue the conversation using the same thread ID -- LangGraph will automatically pass previous history to the AutoGen agent:
```

Example 3 (unknown):
```unknown
**Output:**
```

Example 4 (unknown):
```unknown
## 4. Prepare for deployment

To deploy to LangSmith, create a file structure like the following:
```

---

## Define your tools

**URL:** llms-txt#define-your-tools

**Contents:**
- View traces in LangSmith
- Advanced usage
  - Custom metadata and tags

def get_flight_info(destination: str, departure_date: str) -> dict:
    """Get flight information for a destination."""
    return {
        "destination": destination,
        "departure_date": departure_date,
        "price": "$450",
        "duration": "5h 30m",
        "airline": "Example Airways"
    }

def get_hotel_recommendations(city: str, check_in: str) -> dict:
    """Get hotel recommendations for a city."""
    return {
        "city": city,
        "check_in": check_in,
        "hotels": [
            {"name": "Grand Plaza Hotel", "rating": 4.5, "price": "$120/night"},
            {"name": "City Center Inn", "rating": 4.2, "price": "$95/night"}
        ]
    }

async def main():
    # Create your ADK agent
    agent = LlmAgent(
        name="travel_assistant",
        tools=[get_flight_info, get_hotel_recommendations],
        model="gemini-2.5-flash-lite",
        instruction="You are a helpful travel assistant that can help with flights and hotels.",
    )

# Set up session service and runner
    session_service = InMemorySessionService()
    runner = Runner(
        app_name="travel_app",
        agent=agent,
        session_service=session_service
    )

# Create a session
    user_id = "traveler_456"
    session_id = "session_789"
    await session_service.create_session(
        app_name="travel_app",
        user_id=user_id,
        session_id=session_id
    )

# Send a message to the agent
    new_message = types.Content(
        parts=[types.Part(text="I need to book a flight to Paris for March 15th and find a good hotel.")],
        role="user",
    )

# Run the agent and process events
    events = runner.run(
        user_id=user_id,
        session_id=session_id,
        new_message=new_message,
    )

for event in events:
        print(event)

if __name__ == "__main__":
    asyncio.run(main())
python  theme={null}
from opentelemetry import trace

**Examples:**

Example 1 (unknown):
```unknown
## View traces in LangSmith

* **Agent conversations**: Complete conversation flows between users and your ADK agents.
* **Tool calls**: Individual function calls made by your agents.
* **Model interactions**: LLM requests and responses using Gemini models.
* **Session information**: User and session context for organizing related traces.
* **Model interactions**: LLM requests and responses using Gemini models

<img src="https://mintcdn.com/langchain-5e9cc07a/OEEzzB__isjPfBRD/langsmith/images/adk.png?fit=max&auto=format&n=OEEzzB__isjPfBRD&q=85&s=3495c7838ba7467b905a180fc9ce477b" alt="LangSmith dashboard with raw input from run and trace information." data-og-width="3022" width="3022" data-og-height="1444" height="1444" data-path="langsmith/images/adk.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/OEEzzB__isjPfBRD/langsmith/images/adk.png?w=280&fit=max&auto=format&n=OEEzzB__isjPfBRD&q=85&s=b6db8e92abed624dc492ee12d217b5d3 280w, https://mintcdn.com/langchain-5e9cc07a/OEEzzB__isjPfBRD/langsmith/images/adk.png?w=560&fit=max&auto=format&n=OEEzzB__isjPfBRD&q=85&s=1caecf02d785375c0cae8c97cccf093c 560w, https://mintcdn.com/langchain-5e9cc07a/OEEzzB__isjPfBRD/langsmith/images/adk.png?w=840&fit=max&auto=format&n=OEEzzB__isjPfBRD&q=85&s=3b7fe88b62d4c4bffa889bd79fa5fefd 840w, https://mintcdn.com/langchain-5e9cc07a/OEEzzB__isjPfBRD/langsmith/images/adk.png?w=1100&fit=max&auto=format&n=OEEzzB__isjPfBRD&q=85&s=d7a152d9255fc6d42f946b3601e79ecc 1100w, https://mintcdn.com/langchain-5e9cc07a/OEEzzB__isjPfBRD/langsmith/images/adk.png?w=1650&fit=max&auto=format&n=OEEzzB__isjPfBRD&q=85&s=1eb5ea91226c92628f474254eb177f80 1650w, https://mintcdn.com/langchain-5e9cc07a/OEEzzB__isjPfBRD/langsmith/images/adk.png?w=2500&fit=max&auto=format&n=OEEzzB__isjPfBRD&q=85&s=a98880df67b4dae4c56de2a3d27fefa7 2500w" />

## Advanced usage

### Custom metadata and tags

You can add custom metadata to your traces by setting span attributes in your ADK application:
```

---

## The system prompt will be set dynamically based on context

**URL:** llms-txt#the-system-prompt-will-be-set-dynamically-based-on-context

**Contents:**
- Invocation
- Advanced concepts
  - Structured output

result = agent.invoke(
    {"messages": [{"role": "user", "content": "Explain machine learning"}]},
    context={"user_role": "expert"}
)
python  theme={null}
result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
)
python wrap theme={null}
from pydantic import BaseModel
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy

class ContactInfo(BaseModel):
    name: str
    email: str
    phone: str

agent = create_agent(
    model="openai:gpt-4o-mini",
    tools=[search_tool],
    response_format=ToolStrategy(ContactInfo)
)

result = agent.invoke({
    "messages": [{"role": "user", "content": "Extract contact info from: John Doe, john@example.com, (555) 123-4567"}]
})

result["structured_response"]

**Examples:**

Example 1 (unknown):
```unknown
<Tip>
  For more details on message types and formatting, see [Messages](/oss/python/langchain/messages). For comprehensive middleware documentation, see [Middleware](/oss/python/langchain/middleware).
</Tip>

## Invocation

You can invoke an agent by passing an update to its [`State`](/oss/python/langgraph/graph-api#state). All agents include a [sequence of messages](/oss/python/langgraph/use-graph-api#messagesstate) in their state; to invoke the agent, pass a new message:
```

Example 2 (unknown):
```unknown
For streaming steps and / or tokens from the agent, refer to the [streaming](/oss/python/langchain/streaming) guide.

Otherwise, the agent follows the LangGraph [Graph API](/oss/python/langgraph/use-graph-api) and supports all associated methods.

## Advanced concepts

### Structured output

In some situations, you may want the agent to return an output in a specific format. LangChain provides strategies for structured output via the [`response_format`](https://reference.langchain.com/python/langchain/middleware/#langchain.agents.middleware.ModelRequest\(response_format\)) parameter.

#### ToolStrategy

`ToolStrategy` uses artificial tool calling to generate structured output. This works with any model that supports tool calling:
```

---

## Define your agents

**URL:** llms-txt#define-your-agents

market_researcher = Agent(
    role="Senior Market Researcher",
    goal="Analyze market trends and consumer behavior in the tech industry",
    backstory="""You are an experienced market researcher with 10+ years of experience
    analyzing technology markets. You excel at identifying emerging trends and
    understanding consumer needs.""",
    verbose=True,
    allow_delegation=False,
)

content_strategist = Agent(
    role="Content Marketing Strategist",
    goal="Create compelling marketing content based on research insights",
    backstory="""You are a creative content strategist who transforms complex market
    research into engaging marketing materials. You understand how to communicate
    technical concepts to different audiences.""",
    verbose=True,
    allow_delegation=False,
)

data_analyst = Agent(
    role="Data Analyst",
    goal="Provide statistical analysis and data-driven insights",
    backstory="""You are a skilled data analyst who can interpret complex datasets
    and provide actionable insights. You excel at finding patterns and trends
    in data that others might miss.""",
    verbose=True,
    allow_delegation=False,
)

---

## Self-host standalone servers

**URL:** llms-txt#self-host-standalone-servers

**Contents:**
- Prerequisites
- Kubernetes
- Docker
- Docker Compose

Source: https://docs.langchain.com/langsmith/deploy-standalone-server

This guide shows you how to deploy **standalone <Tooltip tip="The server that runs your LangGraph applications.">LangGraph Servers</Tooltip>** without the LangSmith UI or control plane. This is the most lightweight self-hosting option, ideal for running one or a few agents as independent services.

<Note>
  **This is the setup page for deploying LangGraph Servers directly without the LangSmith platform.**

Review the [self-hosted options](/langsmith/self-hosted) to understand:

* [Standalone Server](/langsmith/self-hosted#standalone-server): What this guide covers (no UI, just servers).
  * [LangSmith](/langsmith/self-hosted#langsmith): For the full LangSmith platform with UI.
  * [LangSmith with deployment](/langsmith/self-hosted#langsmith-with-deployment): For UI-based deployment management.

Before continuing, review the [standalone server overview](/langsmith/self-hosted#standalone-server).
</Note>

1. Use the [LangGraph CLI](/langsmith/cli) to [test your application locally](/langsmith/local-server).
2. Use the [LangGraph CLI](/langsmith/cli) to build a Docker image (i.e. `langgraph build`).
3. The following environment variables are needed for a data plane deployment.
4. `REDIS_URI`: Connection details to a Redis instance. Redis will be used as a pub-sub broker to enable streaming real time output from background runs. The value of `REDIS_URI` must be a valid [Redis connection URI](https://redis-py.readthedocs.io/en/stable/connections.html#redis.Redis.from_url).

<Note>
     **Shared Redis Instance**
     Multiple self-hosted deployments can share the same Redis instance. For example, for `Deployment A`, `REDIS_URI` can be set to `redis://<hostname_1>:<port>/1` and for `Deployment B`, `REDIS_URI` can be set to `redis://<hostname_1>:<port>/2`.

`1` and `2` are different database numbers within the same instance, but `<hostname_1>` is shared. **The same database number cannot be used for separate deployments**.
   </Note>
5. `DATABASE_URI`: Postgres connection details. Postgres will be used to store assistants, threads, runs, persist thread state and long term memory, and to manage the state of the background task queue with 'exactly once' semantics. The value of `DATABASE_URI` must be a valid [Postgres connection URI](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING-URIS).

<Note>
     **Shared Postgres Instance**
     Multiple self-hosted deployments can share the same Postgres instance. For example, for `Deployment A`, `DATABASE_URI` can be set to `postgres://<user>:<password>@/<database_name_1>?host=<hostname_1>` and for `Deployment B`, `DATABASE_URI` can be set to `postgres://<user>:<password>@/<database_name_2>?host=<hostname_1>`.

`<database_name_1>` and `database_name_2` are different databases within the same instance, but `<hostname_1>` is shared. **The same database cannot be used for separate deployments**.
   </Note>
6. `LANGSMITH_API_KEY`: LangSmith API key.
7. `LANGGRAPH_CLOUD_LICENSE_KEY`: LangSmith license key. This will be used to authenticate ONCE at server start up.
8. `LANGSMITH_ENDPOINT`: To send traces to a [self-hosted LangSmith](/langsmith/self-hosted) instance, set `LANGSMITH_ENDPOINT` to the hostname of the self-hosted LangSmith instance.
9. Egress to `https://beacon.langchain.com` from your network. This is required for license verification and usage reporting if not running in air-gapped mode. See the [Egress documentation](/langsmith/self-host-egress) for more details.

Use this [Helm chart](https://github.com/langchain-ai/helm/blob/main/charts/langgraph-cloud/README.md) to deploy a LangGraph Server to a Kubernetes cluster.

Run the following `docker` command:

<Note>
  * You need to replace `my-image` with the name of the image you built in the prerequisite steps (from `langgraph build`)

and you should provide appropriate values for `REDIS_URI`, `DATABASE_URI`, and `LANGSMITH_API_KEY`.

* If your application requires additional environment variables, you can pass them in a similar way.
</Note>

Docker Compose YAML file:

You can run the command `docker compose up` with this Docker Compose file in the same folder.

This will launch a LangGraph Server on port `8123` (if you want to change this, you can change this by changing the ports in the `langgraph-api` volume). You can test if the application is healthy by running:

Assuming everything is running correctly, you should see a response like:

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/langsmith/deploy-standalone-server.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

**Examples:**

Example 1 (unknown):
```unknown
<Note>
  * You need to replace `my-image` with the name of the image you built in the prerequisite steps (from `langgraph build`)

  and you should provide appropriate values for `REDIS_URI`, `DATABASE_URI`, and `LANGSMITH_API_KEY`.

  * If your application requires additional environment variables, you can pass them in a similar way.
</Note>

## Docker Compose

Docker Compose YAML file:
```

Example 2 (unknown):
```unknown
You can run the command `docker compose up` with this Docker Compose file in the same folder.

This will launch a LangGraph Server on port `8123` (if you want to change this, you can change this by changing the ports in the `langgraph-api` volume). You can test if the application is healthy by running:
```

Example 3 (unknown):
```unknown
Assuming everything is running correctly, you should see a response like:
```

---

## We now add a normal edge from 'tools' to 'agent'.

**URL:** llms-txt#we-now-add-a-normal-edge-from-'tools'-to-'agent'.

---

## INVALID_CHAT_HISTORY

**URL:** llms-txt#invalid_chat_history

**Contents:**
- Troubleshooting

Source: https://docs.langchain.com/oss/python/langgraph/errors/INVALID_CHAT_HISTORY

This error is raised in the prebuilt [create\_agent](https://reference.langchain.com/python/langchain/agents/#langchain.agents.create_agent) when the `call_model` graph node receives a malformed list of messages. Specifically, it is malformed when there are `AIMessages` with `tool_calls` (LLM requesting to call a tool) that do not have a corresponding [`ToolMessage`](https://reference.langchain.com/python/langchain/messages/#langchain.messages.ToolMessage) (result of a tool invocation to return to the LLM).

There could be a few reasons you're seeing this error:

1. You manually passed a malformed list of messages when invoking the graph, e.g. `graph.invoke({'messages': [AIMessage(..., tool_calls=[...])]})`
2. The graph was interrupted before receiving updates from the `tools` node (i.e. a list of [`ToolMessage`](https://reference.langchain.com/python/langchain/messages/#langchain.messages.ToolMessage))
   and you invoked it with an input that is not None or a ToolMessage,
   e.g. `graph.invoke({'messages': [HumanMessage(...)]}, config)`.
   This interrupt could have been triggered in one of the following ways:
   * You manually set `interrupt_before = ['tools']` in `create_agent`

* One of the tools raised an error that wasn't handled by the [`ToolNode`](https://reference.langchain.com/python/langgraph/agents/#langgraph.prebuilt.tool_node.ToolNode) (`"tools"`)

To resolve this, you can do one of the following:

1. Don't invoke the graph with a malformed list of messages
2. In case of an interrupt (manual or due to an error) you can:

* provide [`ToolMessage`](https://reference.langchain.com/python/langchain/messages/#langchain.messages.ToolMessage) objects that match existing tool calls and call `graph.invoke({'messages': [ToolMessage(...)]})`.
  **NOTE**: this will append the messages to the history and run the graph from the START node.
  * manually update the state and resume the graph from the interrupt:
    1. get the list of most recent messages from the graph state with `graph.get_state(config)`
    2. modify the list of messages to either remove unanswered tool calls from AIMessages

or add [`ToolMessage`](https://reference.langchain.com/python/langchain/messages/#langchain.messages.ToolMessage) objects with `tool_call_ids` that match unanswered tool calls 3. call `graph.update_state(config, {'messages': ...})` with the modified list of messages 4. resume the graph, e.g. call `graph.invoke(None, config)`

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/errors/INVALID_CHAT_HISTORY.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

---

## Deep Agents

**URL:** llms-txt#deep-agents

Source: https://docs.langchain.com/oss/python/reference/deepagents-python

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/reference/deepagents-python.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

---

## Agent will pause and wait for approval before executing sensitive tools

**URL:** llms-txt#agent-will-pause-and-wait-for-approval-before-executing-sensitive-tools

**Contents:**
- Custom guardrails
  - Before agent guardrails
  - After agent guardrails
  - Combine multiple guardrails
- Additional resources

result = agent.invoke(
    {"messages": [{"role": "user", "content": "Send an email to the team"}]},
    config=config
)

result = agent.invoke(
    Command(resume={"decisions": [{"type": "approve"}]}),
    config=config  # Same thread ID to resume the paused conversation
)
python title="Class syntax" theme={null}
  from typing import Any

from langchain.agents.middleware import AgentMiddleware, AgentState, hook_config
  from langgraph.runtime import Runtime

class ContentFilterMiddleware(AgentMiddleware):
      """Deterministic guardrail: Block requests containing banned keywords."""

def __init__(self, banned_keywords: list[str]):
          super().__init__()
          self.banned_keywords = [kw.lower() for kw in banned_keywords]

@hook_config(can_jump_to=["end"])
      def before_agent(self, state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
          # Get the first user message
          if not state["messages"]:
              return None

first_message = state["messages"][0]
          if first_message.type != "human":
              return None

content = first_message.content.lower()

# Check for banned keywords
          for keyword in self.banned_keywords:
              if keyword in content:
                  # Block execution before any processing
                  return {
                      "messages": [{
                          "role": "assistant",
                          "content": "I cannot process requests containing inappropriate content. Please rephrase your request."
                      }],
                      "jump_to": "end"
                  }

# Use the custom guardrail
  from langchain.agents import create_agent

agent = create_agent(
      model="openai:gpt-4o",
      tools=[search_tool, calculator_tool],
      middleware=[
          ContentFilterMiddleware(
              banned_keywords=["hack", "exploit", "malware"]
          ),
      ],
  )

# This request will be blocked before any processing
  result = agent.invoke({
      "messages": [{"role": "user", "content": "How do I hack into a database?"}]
  })
  python title="Decorator syntax" theme={null}
  from typing import Any

from langchain.agents.middleware import before_agent, AgentState, hook_config
  from langgraph.runtime import Runtime

banned_keywords = ["hack", "exploit", "malware"]

@before_agent(can_jump_to=["end"])
  def content_filter(state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
      """Deterministic guardrail: Block requests containing banned keywords."""
      # Get the first user message
      if not state["messages"]:
          return None

first_message = state["messages"][0]
      if first_message.type != "human":
          return None

content = first_message.content.lower()

# Check for banned keywords
      for keyword in banned_keywords:
          if keyword in content:
              # Block execution before any processing
              return {
                  "messages": [{
                      "role": "assistant",
                      "content": "I cannot process requests containing inappropriate content. Please rephrase your request."
                  }],
                  "jump_to": "end"
              }

# Use the custom guardrail
  from langchain.agents import create_agent

agent = create_agent(
      model="openai:gpt-4o",
      tools=[search_tool, calculator_tool],
      middleware=[content_filter],
  )

# This request will be blocked before any processing
  result = agent.invoke({
      "messages": [{"role": "user", "content": "How do I hack into a database?"}]
  })
  python title="Class syntax" theme={null}
  from langchain.agents.middleware import AgentMiddleware, AgentState, hook_config
  from langgraph.runtime import Runtime
  from langchain_core.messages import AIMessage
  from langchain.chat_models import init_chat_model
  from typing import Any

class SafetyGuardrailMiddleware(AgentMiddleware):
      """Model-based guardrail: Use an LLM to evaluate response safety."""

def __init__(self):
          super().__init__()
          self.safety_model = init_chat_model("openai:gpt-4o-mini")

@hook_config(can_jump_to=["end"])
      def after_agent(self, state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
          # Get the final AI response
          if not state["messages"]:
              return None

last_message = state["messages"][-1]
          if not isinstance(last_message, AIMessage):
              return None

# Use a model to evaluate safety
          safety_prompt = f"""Evaluate if this response is safe and appropriate.
          Respond with only 'SAFE' or 'UNSAFE'.

Response: {last_message.content}"""

result = self.safety_model.invoke([{"role": "user", "content": safety_prompt}])

if "UNSAFE" in result.content:
              return {
                  "messages": [{
                      "role": "assistant",
                      "content": "I cannot provide that response. Please rephrase your request."
                  }],
                  "jump_to": "end"
              }

# Use the safety guardrail
  from langchain.agents import create_agent

agent = create_agent(
      model="openai:gpt-4o",
      tools=[search_tool, calculator_tool],
      middleware=[SafetyGuardrailMiddleware()],
  )

result = agent.invoke({
      "messages": [{"role": "user", "content": "How do I make explosives?"}]
  })
  python title="Decorator syntax" theme={null}
  from langchain.agents.middleware import after_agent, AgentState, hook_config
  from langgraph.runtime import Runtime
  from langchain_core.messages import AIMessage
  from langchain.chat_models import init_chat_model
  from typing import Any

safety_model = init_chat_model("openai:gpt-4o-mini")

@after_agent(can_jump_to=["end"])
  def safety_guardrail(state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
      """Model-based guardrail: Use an LLM to evaluate response safety."""
      # Get the final AI response
      if not state["messages"]:
          return None

last_message = state["messages"][-1]
      if not isinstance(last_message, AIMessage):
          return None

# Use a model to evaluate safety
      safety_prompt = f"""Evaluate if this response is safe and appropriate.
      Respond with only 'SAFE' or 'UNSAFE'.

Response: {last_message.content}"""

result = safety_model.invoke([{"role": "user", "content": safety_prompt}])

if "UNSAFE" in result.content:
          return {
              "messages": [{
                  "role": "assistant",
                  "content": "I cannot provide that response. Please rephrase your request."
              }],
              "jump_to": "end"
          }

# Use the safety guardrail
  from langchain.agents import create_agent

agent = create_agent(
      model="openai:gpt-4o",
      tools=[search_tool, calculator_tool],
      middleware=[safety_guardrail],
  )

result = agent.invoke({
      "messages": [{"role": "user", "content": "How do I make explosives?"}]
  })
  python  theme={null}
from langchain.agents import create_agent
from langchain.agents.middleware import PIIMiddleware, HumanInTheLoopMiddleware

agent = create_agent(
    model="openai:gpt-4o",
    tools=[search_tool, send_email_tool],
    middleware=[
        # Layer 1: Deterministic input filter (before agent)
        ContentFilterMiddleware(banned_keywords=["hack", "exploit"]),

# Layer 2: PII protection (before and after model)
        PIIMiddleware("email", strategy="redact", apply_to_input=True),
        PIIMiddleware("email", strategy="redact", apply_to_output=True),

# Layer 3: Human approval for sensitive tools
        HumanInTheLoopMiddleware(interrupt_on={"send_email": True}),

# Layer 4: Model-based safety check (after agent)
        SafetyGuardrailMiddleware(),
    ],
)
```

## Additional resources

* [Middleware documentation](/oss/python/langchain/middleware) - Complete guide to custom middleware
* [Middleware API reference](https://reference.langchain.com/python/langchain/middleware/) - Complete guide to custom middleware
* [Human-in-the-loop](/oss/python/langchain/human-in-the-loop) - Add human review for sensitive operations
* [Testing agents](/oss/python/langchain/test) - Strategies for testing safety mechanisms

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/guardrails.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

**Examples:**

Example 1 (unknown):
```unknown
<Tip>
  See the [human-in-the-loop documentation](/oss/python/langchain/human-in-the-loop) for complete details on implementing approval workflows.
</Tip>

## Custom guardrails

For more sophisticated guardrails, you can create custom middleware that runs before or after the agent executes. This gives you full control over validation logic, content filtering, and safety checks.

### Before agent guardrails

Use "before agent" hooks to validate requests once at the start of each invocation. This is useful for session-level checks like authentication, rate limiting, or blocking inappropriate requests before any processing begins.

<CodeGroup>
```

Example 2 (unknown):
```unknown

```

Example 3 (unknown):
```unknown
</CodeGroup>

### After agent guardrails

Use "after agent" hooks to validate final outputs once before returning to the user. This is useful for model-based safety checks, quality validation, or final compliance scans on the complete agent response.

<CodeGroup>
```

Example 4 (unknown):
```unknown

```

---

## Agent building

**URL:** llms-txt#agent-building

from langchain.agents import create_agent

---

## Create a code reviewer agent

**URL:** llms-txt#create-a-code-reviewer-agent

code_reviewer = autogen.AssistantAgent(
    name="code_reviewer",
    llm_config={"config_list": config_list},
    system_message="""You are an expert code reviewer. Your role is to:
    1. Review code for bugs, security issues, and best practices
    2. Suggest improvements and optimizations
    3. Provide constructive feedback
    Always be thorough but constructive in your reviews.""",
)

---

## Build a SQL agent

**URL:** llms-txt#build-a-sql-agent

**Contents:**
- Overview
  - Concepts
- Setup
  - Installation
  - LangSmith
- 1. Select an LLM
- 2. Configure the database
- 3. Add tools for database interactions
- 5. Use `create_agent`
- 6. Run the agent

Source: https://docs.langchain.com/oss/python/langchain/sql-agent

In this tutorial, you will learn how to build an agent that can answer questions about a SQL database using LangChain [agents](/oss/python/langchain/agents).

At a high level, the agent will:

<Steps>
  <Step title="Fetch the available tables and schemas from the database" />

<Step title="Decide which tables are relevant to the question" />

<Step title="Fetch the schemas for the relevant tables" />

<Step title="Generate a query based on the question and information from the schemas" />

<Step title="Double-check the query for common mistakes using an LLM" />

<Step title="Execute the query and return the results" />

<Step title="Correct mistakes surfaced by the database engine until the query is successful" />

<Step title="Formulate a response based on the results" />
</Steps>

<Warning>
  Building Q\&A systems of SQL databases requires executing model-generated SQL queries. There are inherent risks in doing this. Make sure that your database connection permissions are always scoped as narrowly as possible for your agent's needs. This will mitigate, though not eliminate, the risks of building a model-driven system.
</Warning>

We will cover the following concepts:

* [Tools](/oss/python/langchain/tools) for reading from SQL databases
* LangChain [agents](/oss/python/langchain/agents)
* [Human-in-the-loop](/oss/python/langchain/human-in-the-loop) processes

<CodeGroup>
  
</CodeGroup>

Set up [LangSmith](https://smith.langchain.com) to inspect what is happening inside your chain or agent. Then set the following environment variables:

Select a model that supports [tool-calling](/oss/python/integrations/providers/overview):

<Tabs>
  <Tab title="OpenAI">
    👉 Read the [OpenAI chat model integration docs](/oss/python/integrations/chat/openai/)

</CodeGroup>
  </Tab>

<Tab title="Anthropic">
    👉 Read the [Anthropic chat model integration docs](/oss/python/integrations/chat/anthropic/)

</CodeGroup>
  </Tab>

<Tab title="Azure">
    👉 Read the [Azure chat model integration docs](/oss/python/integrations/chat/azure_chat_openai/)

</CodeGroup>
  </Tab>

<Tab title="Google Gemini">
    👉 Read the [Google GenAI chat model integration docs](/oss/python/integrations/chat/google_generative_ai/)

</CodeGroup>
  </Tab>

<Tab title="AWS Bedrock">
    👉 Read the [AWS Bedrock chat model integration docs](/oss/python/integrations/chat/bedrock/)

</CodeGroup>
  </Tab>
</Tabs>

The output shown in the examples below used OpenAI.

## 2. Configure the database

You will be creating a [SQLite database](https://www.sqlitetutorial.net/sqlite-sample-database/) for this tutorial. SQLite is a lightweight database that is easy to set up and use. We will be loading the `chinook` database, which is a sample database that represents a digital media store.

For convenience, we have hosted the database (`Chinook.db`) on a public GCS bucket.

We will use a handy SQL database wrapper available in the `langchain_community` package to interact with the database. The wrapper provides a simple interface to execute SQL queries and fetch results:

## 3. Add tools for database interactions

Use the `SQLDatabase` wrapper available in the `langchain_community` package to interact with the database. The wrapper provides a simple interface to execute SQL queries and fetch results:

## 5. Use `create_agent`

Use [`create_agent`](https://reference.langchain.com/python/langchain/agents/#langchain.agents.create_agent) to build a [ReAct agent](https://arxiv.org/pdf/2210.03629) with minimal code. The agent will interpret the request and generate a SQL command, which the tools will execute. If the command has an error, the error message is returned to the model. The model can then examine the original request and the new error message and generate a new command. This can continue until the LLM generates the command successfully or reaches an end count. This pattern of providing a model with feedback - error messages in this case - is very powerful.

Initialize the agent with a descriptive system prompt to customize its behavior:

Now, create an agent with the model, tools, and prompt:

Run the agent on a sample query and observe its behavior:

The agent correctly wrote a query, checked the query, and ran it to inform its final response.

<Note>
  You can inspect all aspects of the above run, including steps taken, tools invoked, what prompts were seen by the LLM, and more in the [LangSmith trace](https://smith.langchain.com/public/cd2ce887-388a-4bb1-a29d-48208ce50d15/r).
</Note>

### (Optional) Use Studio

[Studio](/langsmith/studio) provides a "client side" loop as well as memory so you can run this as a chat interface and query the database. You can ask questions like "Tell me the scheme of the database" or "Show me the invoices for the 5 top customers". You will see the SQL command that is generated and the resulting output. The details of how to get that started are below.

<Accordion title="Run your agent in Studio">
  In addition to the previously mentioned packages, you will need to:

In directory you will run in, you will need a `langgraph.json` file with the following contents:

Create a file `sql_agent.py` and insert this:

## 6. Implement human-in-the-loop review

It can be prudent to check the agent's SQL queries before they are executed for any unintended actions or inefficiencies.

LangChain agents feature support for built-in [human-in-the-loop middleware](/oss/python/langchain/human-in-the-loop) to add oversight to agent tool calls. Let's configure the agent to pause for human review on calling the `sql_db_query` tool:

<Note>
  We've added a [checkpointer](/oss/python/langchain/short-term-memory) to our agent to allow execution to be paused and resumed. See the [human-in-the-loop guide](/oss/python/langchain/human-in-the-loop) for detalis on this as well as available middleware configurations.
</Note>

On running the agent, it will now pause for review before executing the `sql_db_query` tool:

We can resume execution, in this case accepting the query, using [Command](/oss/python/langgraph/use-graph-api#combine-control-flow-and-state-updates-with-command):

Refer to the [human-in-the-loop guide](/oss/python/langchain/human-in-the-loop) for details.

For deeper customization, check out [this tutorial](/oss/python/langgraph/sql-agent) for implementing a SQL agent directly using LangGraph primitives.

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/sql-agent.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

**Examples:**

Example 1 (unknown):
```unknown
</CodeGroup>

### LangSmith

Set up [LangSmith](https://smith.langchain.com) to inspect what is happening inside your chain or agent. Then set the following environment variables:
```

Example 2 (unknown):
```unknown
## 1. Select an LLM

Select a model that supports [tool-calling](/oss/python/integrations/providers/overview):

<Tabs>
  <Tab title="OpenAI">
    👉 Read the [OpenAI chat model integration docs](/oss/python/integrations/chat/openai/)
```

Example 3 (unknown):
```unknown
<CodeGroup>
```

Example 4 (unknown):
```unknown

```

---

## Agent model

**URL:** llms-txt#agent-model

qa_llm = init_chat_model("claude-3-5-sonnet-latest")

---

## Run the agent - all steps will be traced automatically

**URL:** llms-txt#run-the-agent---all-steps-will-be-traced-automatically

**Contents:**
- Trace selectively

response = agent.invoke({
    "messages": [{"role": "user", "content": "Search for the latest AI news and email a summary to john@example.com"}]
})
python  theme={null}
import langsmith as ls

**Examples:**

Example 1 (unknown):
```unknown
By default, the trace will be logged to the project with the name `default`. To configure a custom project name, see [Log to a project](#log-to-a-project).

## Trace selectively

You may opt to trace specific invocations or parts of your application using LangSmith's `tracing_context` context manager:
```

---

## Define the tools our agent can use

**URL:** llms-txt#define-the-tools-our-agent-can-use

---

## Get Tavily API key: https://tavily.com

**URL:** llms-txt#get-tavily-api-key:-https://tavily.com

**Contents:**
  - Define the application

os.environ["TAVILY_API_KEY"] = "YOUR TAVILY API KEY"
python  theme={null}
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain_community.tools import DuckDuckGoSearchRun, TavilySearchResults
from langchain_core.rate_limiters import InMemoryRateLimiter

**Examples:**

Example 1 (unknown):
```unknown
### Define the application

For this example lets create a simple Tweet-writing application that has access to some internet search tools:
```

---

## Use decorators in agent

**URL:** llms-txt#use-decorators-in-agent

**Contents:**
  - Available decorators
  - When to use decorators
- Class-based middleware
  - Two hook styles
  - Custom state schema

agent = create_agent(
    model="openai:gpt-4o",
    middleware=[log_before_model, validate_output, retry_model, personalized_prompt],
    tools=[...],
)
python  theme={null}
from langchain.agents.middleware import AgentMiddleware, AgentState
from langgraph.runtime import Runtime
from typing import Any

class LoggingMiddleware(AgentMiddleware):
    def before_model(self, state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
        print(f"About to call model with {len(state['messages'])} messages")
        return None

def after_model(self, state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
        print(f"Model returned: {state['messages'][-1].content}")
        return None
python  theme={null}
from langchain.agents.middleware import AgentMiddleware, AgentState
from langchain.messages import AIMessage
from langgraph.runtime import Runtime
from typing import Any

class MessageLimitMiddleware(AgentMiddleware):
    def __init__(self, max_messages: int = 50):
        super().__init__()
        self.max_messages = max_messages

def before_model(self, state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
        if len(state["messages"]) == self.max_messages:
            return {
                "messages": [AIMessage("Conversation limit reached.")],
                "jump_to": "end"
            }
        return None
python  theme={null}
from langchain.agents.middleware import AgentMiddleware, ModelRequest, ModelResponse
from typing import Callable

class RetryMiddleware(AgentMiddleware):
    def __init__(self, max_retries: int = 3):
        super().__init__()
        self.max_retries = max_retries

def wrap_model_call(
        self,
        request: ModelRequest,
        handler: Callable[[ModelRequest], ModelResponse],
    ) -> ModelResponse:
        for attempt in range(self.max_retries):
            try:
                return handler(request)
            except Exception as e:
                if attempt == self.max_retries - 1:
                    raise
                print(f"Retry {attempt + 1}/{self.max_retries} after error: {e}")
python  theme={null}
from langchain.agents.middleware import AgentMiddleware, ModelRequest, ModelResponse
from langchain.chat_models import init_chat_model
from typing import Callable

class DynamicModelMiddleware(AgentMiddleware):
    def wrap_model_call(
        self,
        request: ModelRequest,
        handler: Callable[[ModelRequest], ModelResponse],
    ) -> ModelResponse:
        # Use different model based on conversation length
        if len(request.messages) > 10:
            request.model = init_chat_model("openai:gpt-4o")
        else:
            request.model = init_chat_model("openai:gpt-4o-mini")

return handler(request)
python  theme={null}
from langchain.tools.tool_node import ToolCallRequest
from langchain.agents.middleware import AgentMiddleware
from langchain_core.messages import ToolMessage
from langgraph.types import Command
from typing import Callable

class ToolMonitoringMiddleware(AgentMiddleware):
    def wrap_tool_call(
        self,
        request: ToolCallRequest,
        handler: Callable[[ToolCallRequest], ToolMessage | Command],
    ) -> ToolMessage | Command:
        print(f"Executing tool: {request.tool_call['name']}")
        print(f"Arguments: {request.tool_call['args']}")

try:
            result = handler(request)
            print(f"Tool completed successfully")
            return result
        except Exception as e:
            print(f"Tool failed: {e}")
            raise
python  theme={null}
from langchain.agents.middleware import AgentState, AgentMiddleware
from typing_extensions import NotRequired
from typing import Any

class CustomState(AgentState):
    model_call_count: NotRequired[int]
    user_id: NotRequired[str]

class CallCounterMiddleware(AgentMiddleware[CustomState]):
    state_schema = CustomState

def before_model(self, state: CustomState, runtime) -> dict[str, Any] | None:
        # Access custom state properties
        count = state.get("model_call_count", 0)

if count > 10:
            return {"jump_to": "end"}

def after_model(self, state: CustomState, runtime) -> dict[str, Any] | None:
        # Update custom state
        return {"model_call_count": state.get("model_call_count", 0) + 1}
python  theme={null}
agent = create_agent(
    model="openai:gpt-4o",
    middleware=[CallCounterMiddleware()],
    tools=[...],
)

**Examples:**

Example 1 (unknown):
```unknown
### Available decorators

**Node-style** (run at specific execution points):

* `@before_agent` - Before agent starts (once per invocation)
* [`@before_model`](https://reference.langchain.com/python/langchain/middleware/#langchain.agents.middleware.before_model) - Before each model call
* [`@after_model`](https://reference.langchain.com/python/langchain/middleware/#langchain.agents.middleware.after_model) - After each model response
* `@after_agent` - After agent completes (once per invocation)

**Wrap-style** (intercept and control execution):

* [`@wrap_model_call`](https://reference.langchain.com/python/langchain/middleware/#langchain.agents.middleware.wrap_model_call) - Around each model call
* [`@wrap_tool_call`](https://reference.langchain.com/python/langchain/middleware/#langchain.agents.middleware.wrap_tool_call) - Around each tool call

**Convenience decorators**:

* [`@dynamic_prompt`](https://reference.langchain.com/python/langchain/middleware/#langchain.agents.middleware.dynamic_prompt) - Generates dynamic system prompts (equivalent to [`@wrap_model_call`](https://reference.langchain.com/python/langchain/middleware/#langchain.agents.middleware.wrap_model_call) that modifies the prompt)

### When to use decorators

<CardGroup cols={2}>
  <Card title="Use decorators when" icon="check">
    • You need a single hook<br />
    • No complex configuration
  </Card>

  <Card title="Use classes when" icon="code">
    • Multiple hooks needed<br />
    • Complex configuration<br />
    • Reuse across projects (config on init)
  </Card>
</CardGroup>

## Class-based middleware

### Two hook styles

<CardGroup cols={2}>
  <Card title="Node-style hooks" icon="diagram-project">
    Run sequentially at specific execution points. Use for logging, validation, and state updates.
  </Card>

  <Card title="Wrap-style hooks" icon="arrows-rotate">
    Intercept execution with full control over handler calls. Use for retries, caching, and transformation.
  </Card>
</CardGroup>

#### Node-style hooks

Run at specific points in the execution flow:

* `before_agent` - Before agent starts (once per invocation)
* `before_model` - Before each model call
* `after_model` - After each model response
* `after_agent` - After agent completes (up to once per invocation)

**Example: Logging middleware**
```

Example 2 (unknown):
```unknown
**Example: Conversation length limit**
```

Example 3 (unknown):
```unknown
#### Wrap-style hooks

Intercept execution and control when the handler is called:

* `wrap_model_call` - Around each model call
* `wrap_tool_call` - Around each tool call

You decide if the handler is called zero times (short-circuit), once (normal flow), or multiple times (retry logic).

**Example: Model retry middleware**
```

Example 4 (unknown):
```unknown
**Example: Dynamic model selection**
```

---

## How to evaluate your agent with trajectory evaluations

**URL:** llms-txt#how-to-evaluate-your-agent-with-trajectory-evaluations

**Contents:**
- Installing AgentEvals
- Trajectory match evaluator
  - Strict match
  - Unordered match
  - Subset and superset match
- LLM-as-judge evaluator
  - Without reference trajectory
  - With reference trajectory
- Async support (Python)

Source: https://docs.langchain.com/langsmith/trajectory-evals

Many agent behaviors only emerge when using a real LLM, such as which tool the agent decides to call, how it formats responses, or whether a prompt modification affects the entire execution trajectory. LangChain's [`agentevals`](https://github.com/langchain-ai/agentevals) package provides evaluators specifically designed for testing agent trajectories with live models.

<Note>
  This guide covers the open source [LangChain](/oss/python/langchain/overview) `agentevals` package, which integrates with LangSmith for trajectory evaluation.
</Note>

AgentEvals allows you to evaluate the trajectory of your agent (the exact sequence of messages, including tool calls) by performing a *trajectory match* or by using an *LLM judge*:

<Card title="Trajectory match" icon="equals" arrow="true" href="#trajectory-match-evaluator">
  Hard-code a reference trajectory for a given input and validate the run via a step-by-step comparison.

Ideal for testing well-defined workflows where you know the expected behavior. Use when you have specific expectations about which tools should be called and in what order. This approach is deterministic, fast, and cost-effective since it doesn't require additional LLM calls.
</Card>

<Card title="LLM-as-judge" icon="gavel" arrow="true" href="#llm-as-judge-evaluator">
  Use a LLM to qualitatively validate your agent's execution trajectory. The "judge" LLM reviews the agent's decisions against a prompt rubric (which can include a reference trajectory).

More flexible and can assess nuanced aspects like efficiency and appropriateness, but requires an LLM call and is less deterministic. Use when you want to evaluate the overall quality and reasonableness of the agent's trajectory without strict tool call or ordering requirements.
</Card>

## Installing AgentEvals

Or, clone the [AgentEvals repository](https://github.com/langchain-ai/agentevals) directly.

## Trajectory match evaluator

AgentEvals offers the `create_trajectory_match_evaluator` function in Python and `createTrajectoryMatchEvaluator` in TypeScript to match your agent's trajectory against a reference trajectory.

You can use the following modes:

| Mode                                     | Description                                               | Use Case                                                              |
| ---------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------------------- |
| [`strict`](#strict-match)                | Exact match of messages and tool calls in the same order  | Testing specific sequences (e.g., policy lookup before authorization) |
| [`unordered`](#unordered-match)          | Same tool calls allowed in any order                      | Verifying information retrieval when order doesn't matter             |
| [`subset`](#subset-and-superset-match)   | Agent calls only tools from reference (no extras)         | Ensuring agent doesn't exceed expected scope                          |
| [`superset`](#subset-and-superset-match) | Agent calls at least the reference tools (extras allowed) | Verifying minimum required actions are taken                          |

The `strict` mode ensures trajectories contain identical messages in the same order with the same tool calls, though it allows for differences in message content. This is useful when you need to enforce a specific sequence of operations, such as requiring a policy lookup before authorizing an action.

The `unordered` mode allows the same tool calls in any order, which is helpful when you want to verify that the correct set of tools are being invoked but don't care about the sequence. For example, an agent might need to check both weather and events for a city, but the order doesn't matter.

### Subset and superset match

The `superset` and `subset` modes focus on which tools are called rather than the order of tool calls, allowing you to control how strictly the agent's tool calls must align with the reference.

* Use `superset` mode when you want to verify that a few key tools are called in the execution, but you're okay with the agent calling additional tools. The agent's trajectory must include at least all the tool calls in the reference trajectory, and may include additional tool calls beyond the reference.
* Use `subset` mode to ensure agent efficiency by verifying that the agent did not call any irrelevant or unnecessary tools beyond those in the reference. The agent's trajectory must include only tool calls that appear in the reference trajectory.

The following example demonstrates `superset` mode, where the reference trajectory only requires the `get_weather` tool, but the agent can call additional tools:

<Info>
  You can also customize how the evaluator considers equality between tool calls in the actual trajectory vs. the reference by setting the `tool_args_match_mode` (Python) or `toolArgsMatchMode` (TypeScript) property, as well as the `tool_args_match_overrides` (Python) or `toolArgsMatchOverrides` (TypeScript) property. By default, only tool calls with the same arguments to the same tool are considered equal. Visit the [repository](https://github.com/langchain-ai/agentevals?tab=readme-ov-file#tool-args-match-modes) for more details.
</Info>

## LLM-as-judge evaluator

<Note>
  This section covers the trajectory-specific LLM-as-a-judge evaluator from the `agentevals` package. For general-purpose LLM-as-a-judge evaluators in LangSmith, refer to the [LLM-as-a-judge evaluator](/langsmith/llm-as-judge).
</Note>

You can also use an LLM to evaluate the agent's execution path. Unlike the trajectory match evaluators, it doesn't require a reference trajectory, but one can be provided if available.

### Without reference trajectory

### With reference trajectory

If you have a reference trajectory, you can add an extra variable to your prompt and pass in the reference trajectory. Below, we use the prebuilt `TRAJECTORY_ACCURACY_PROMPT_WITH_REFERENCE` prompt and configure the `reference_outputs` variable:

<Info>
  For more configurability over how the LLM evaluates the trajectory, visit the [repository](https://github.com/langchain-ai/agentevals?tab=readme-ov-file#trajectory-llm-as-judge).
</Info>

## Async support (Python)

All `agentevals` evaluators support Python asyncio. For evaluators that use factory functions, async versions are available by adding `async` after `create_` in the function name.

Here's an example using the async judge and evaluator:

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trajectory-evals.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

**Examples:**

Example 1 (unknown):
```unknown

```

Example 2 (unknown):
```unknown
</CodeGroup>

Or, clone the [AgentEvals repository](https://github.com/langchain-ai/agentevals) directly.

## Trajectory match evaluator

AgentEvals offers the `create_trajectory_match_evaluator` function in Python and `createTrajectoryMatchEvaluator` in TypeScript to match your agent's trajectory against a reference trajectory.

You can use the following modes:

| Mode                                     | Description                                               | Use Case                                                              |
| ---------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------------------- |
| [`strict`](#strict-match)                | Exact match of messages and tool calls in the same order  | Testing specific sequences (e.g., policy lookup before authorization) |
| [`unordered`](#unordered-match)          | Same tool calls allowed in any order                      | Verifying information retrieval when order doesn't matter             |
| [`subset`](#subset-and-superset-match)   | Agent calls only tools from reference (no extras)         | Ensuring agent doesn't exceed expected scope                          |
| [`superset`](#subset-and-superset-match) | Agent calls at least the reference tools (extras allowed) | Verifying minimum required actions are taken                          |

### Strict match

The `strict` mode ensures trajectories contain identical messages in the same order with the same tool calls, though it allows for differences in message content. This is useful when you need to enforce a specific sequence of operations, such as requiring a policy lookup before authorizing an action.

<CodeGroup>
```

Example 3 (unknown):
```unknown

```

Example 4 (unknown):
```unknown
</CodeGroup>

### Unordered match

The `unordered` mode allows the same tool calls in any order, which is helpful when you want to verify that the correct set of tools are being invoked but don't care about the sequence. For example, an agent might need to check both weather and events for a city, but the order doesn't matter.

<CodeGroup>
```

---

## Invoke the agent

**URL:** llms-txt#invoke-the-agent

result = agent.invoke({
    "messages": [{"role": "user", "content": "Delete the file temp.txt"}]
}, config=config)

---

## Since all of our subagents have compatible state,

**URL:** llms-txt#since-all-of-our-subagents-have-compatible-state,

---

## Invoke with custom state

**URL:** llms-txt#invoke-with-custom-state

**Contents:**
  - Execution order
  - Agent jumps
  - Best practices
- Examples
  - Dynamically selecting tools
- Additional resources

result = agent.invoke({
    "messages": [HumanMessage("Hello")],
    "model_call_count": 0,
    "user_id": "user-123",
})
python  theme={null}
agent = create_agent(
    model="openai:gpt-4o",
    middleware=[middleware1, middleware2, middleware3],
    tools=[...],
)
python  theme={null}
class EarlyExitMiddleware(AgentMiddleware):
    def before_model(self, state: AgentState, runtime) -> dict[str, Any] | None:
        # Check some condition
        if should_exit(state):
            return {
                "messages": [AIMessage("Exiting early due to condition.")],
                "jump_to": "end"
            }
        return None
python  theme={null}
from langchain.agents.middleware import AgentMiddleware, hook_config
from typing import Any

class ConditionalMiddleware(AgentMiddleware):
    @hook_config(can_jump_to=["end", "tools"])
    def after_model(self, state: AgentState, runtime) -> dict[str, Any] | None:
        if some_condition(state):
            return {"jump_to": "end"}
        return None
python  theme={null}
from langchain.agents import create_agent
from langchain.agents.middleware import AgentMiddleware, ModelRequest
from typing import Callable

class ToolSelectorMiddleware(AgentMiddleware):
    def wrap_model_call(
        self,
        request: ModelRequest,
        handler: Callable[[ModelRequest], ModelResponse],
    ) -> ModelResponse:
        """Middleware to select relevant tools based on state/context."""
        # Select a small, relevant subset of tools based on state/context
        relevant_tools = select_relevant_tools(request.state, request.runtime)
        request.tools = relevant_tools
        return handler(request)

agent = create_agent(
    model="openai:gpt-4o",
    tools=all_tools,  # All available tools need to be registered upfront
    # Middleware can be used to select a smaller subset that's relevant for the given run.
    middleware=[ToolSelectorMiddleware()],
)
python  theme={null}
  from dataclasses import dataclass
  from typing import Literal, Callable

from langchain.agents import create_agent
  from langchain.agents.middleware import AgentMiddleware, ModelRequest, ModelResponse
  from langchain_core.tools import tool

@tool
  def github_create_issue(repo: str, title: str) -> dict:
      """Create an issue in a GitHub repository."""
      return {"url": f"https://github.com/{repo}/issues/1", "title": title}

@tool
  def gitlab_create_issue(project: str, title: str) -> dict:
      """Create an issue in a GitLab project."""
      return {"url": f"https://gitlab.com/{project}/-/issues/1", "title": title}

all_tools = [github_create_issue, gitlab_create_issue]

@dataclass
  class Context:
      provider: Literal["github", "gitlab"]

class ToolSelectorMiddleware(AgentMiddleware):
      def wrap_model_call(
          self,
          request: ModelRequest,
          handler: Callable[[ModelRequest], ModelResponse],
      ) -> ModelResponse:
          """Select tools based on the VCS provider."""
          provider = request.runtime.context.provider

if provider == "gitlab":
              selected_tools = [t for t in request.tools if t.name == "gitlab_create_issue"]
          else:
              selected_tools = [t for t in request.tools if t.name == "github_create_issue"]

request.tools = selected_tools
          return handler(request)

agent = create_agent(
      model="openai:gpt-4o",
      tools=all_tools,
      middleware=[ToolSelectorMiddleware()],
      context_schema=Context,
  )

# Invoke with GitHub context
  agent.invoke(
      {
          "messages": [{"role": "user", "content": "Open an issue titled 'Bug: where are the cats' in the repository `its-a-cats-game`"}]
      },
      context=Context(provider="github"),
  )
  ```

* Register all tools upfront
  * Middleware selects the relevant subset per request
  * Use `context_schema` for configuration requirements
</Expandable>

## Additional resources

* [Middleware API reference](https://reference.langchain.com/python/langchain/middleware/) - Complete guide to custom middleware
* [Human-in-the-loop](/oss/python/langchain/human-in-the-loop) - Add human review for sensitive operations
* [Testing agents](/oss/python/langchain/test) - Strategies for testing safety mechanisms

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/middleware.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

**Examples:**

Example 1 (unknown):
```unknown
### Execution order

When using multiple middleware, understanding execution order is important:
```

Example 2 (unknown):
```unknown
<Accordion title="Execution flow (click to expand)">
  **Before hooks run in order:**

  1. `middleware1.before_agent()`
  2. `middleware2.before_agent()`
  3. `middleware3.before_agent()`

  **Agent loop starts**

  5. `middleware1.before_model()`
  6. `middleware2.before_model()`
  7. `middleware3.before_model()`

  **Wrap hooks nest like function calls:**

  8. `middleware1.wrap_model_call()` → `middleware2.wrap_model_call()` → `middleware3.wrap_model_call()` → model

  **After hooks run in reverse order:**

  9. `middleware3.after_model()`
  10. `middleware2.after_model()`
  11. `middleware1.after_model()`

  **Agent loop ends**

  13. `middleware3.after_agent()`
  14. `middleware2.after_agent()`
  15. `middleware1.after_agent()`
</Accordion>

**Key rules:**

* `before_*` hooks: First to last
* `after_*` hooks: Last to first (reverse)
* `wrap_*` hooks: Nested (first middleware wraps all others)

### Agent jumps

To exit early from middleware, return a dictionary with `jump_to`:
```

Example 3 (unknown):
```unknown
Available jump targets:

* `"end"`: Jump to the end of the agent execution
* `"tools"`: Jump to the tools node
* `"model"`: Jump to the model node (or the first `before_model` hook)

**Important:** When jumping from `before_model` or `after_model`, jumping to `"model"` will cause all `before_model` middleware to run again.

To enable jumping, decorate your hook with `@hook_config(can_jump_to=[...])`:
```

Example 4 (unknown):
```unknown
### Best practices

1. Keep middleware focused - each should do one thing well
2. Handle errors gracefully - don't let middleware errors crash the agent
3. **Use appropriate hook types**:
   * Node-style for sequential logic (logging, validation)
   * Wrap-style for control flow (retry, fallback, caching)
4. Clearly document any custom state properties
5. Unit test middleware independently before integrating
6. Consider execution order - place critical middleware first in the list
7. Use built-in middleware when possible, don't reinvent the wheel :)

## Examples

### Dynamically selecting tools

Select relevant tools at runtime to improve performance and accuracy.

<Tip>
  **Benefits:**

  * **Shorter prompts** - Reduce complexity by exposing only relevant tools
  * **Better accuracy** - Models choose correctly from fewer options
  * **Permission control** - Dynamically filter tools based on user access
</Tip>
```

---

## Human-in-the-loop

**URL:** llms-txt#human-in-the-loop

**Contents:**
- Interrupt decision types
- Configuring interrupts
- Responding to interrupts

Source: https://docs.langchain.com/oss/python/langchain/human-in-the-loop

The Human-in-the-Loop (HITL) middleware lets you add human oversight to agent tool calls.
When a model proposes an action that might require review — for example, writing to a file or executing SQL — the middleware can pause execution and wait for a decision.

It does this by checking each tool call against a configurable policy. If intervention is needed, the middleware issues an [interrupt](https://reference.langchain.com/python/langgraph/types/#langgraph.types.interrupt) that halts execution. The graph state is saved using LangGraph’s [persistence layer](/oss/python/langgraph/persistence), so execution can pause safely and resume later.

A human decision then determines what happens next: the action can be approved as-is (`approve`), modified before running (`edit`), or rejected with feedback (`reject`).

## Interrupt decision types

The middleware defines three built-in ways a human can respond to an interrupt:

| Decision Type | Description                                                               | Example Use Case                                    |
| ------------- | ------------------------------------------------------------------------- | --------------------------------------------------- |
| ✅ `approve`   | The action is approved as-is and executed without changes.                | Send an email draft exactly as written              |
| ✏️ `edit`     | The tool call is executed with modifications.                             | Change the recipient before sending an email        |
| ❌ `reject`    | The tool call is rejected, with an explanation added to the conversation. | Reject an email draft and explain how to rewrite it |

The available decision types for each tool depend on the policy you configure in `interrupt_on`.
When multiple tool calls are paused at the same time, each action requires a separate decision.
Decisions must be provided in the same order as the actions appear in the interrupt request.

<Tip>
  When **editing** tool arguments, make changes conservatively. Significant modifications to the original arguments may cause the model to re-evaluate its approach and potentially execute the tool multiple times or take unexpected actions.
</Tip>

## Configuring interrupts

To use HITL, add the middleware to the agent’s `middleware` list when creating the agent.

You configure it with a mapping of tool actions to the decision types that are allowed for each action. The middleware will interrupt execution when a tool call matches an action in the mapping.

<Info>
  You must configure a checkpointer to persist the graph state across interrupts.
  In production, use a persistent checkpointer like [`AsyncPostgresSaver`](https://reference.langchain.com/python/langgraph/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver). For testing or prototyping, use [`InMemorySaver`](https://reference.langchain.com/python/langgraph/checkpoints/#langgraph.checkpoint.memory.InMemorySaver).

When invoking the agent, pass a `config` that includes the **thread ID** to associate execution with a conversation thread.
  See the [LangGraph interrupts documentation](/oss/python/langgraph/interrupts) for details.
</Info>

## Responding to interrupts

When you invoke the agent, it runs until it either completes or an interrupt is raised. An interrupt is triggered when a tool call matches the policy you configured in `interrupt_on`. In that case, the invocation result will include an `__interrupt__` field with the actions that require review. You can then present those actions to a reviewer and resume execution once decisions are provided.

```python  theme={null}
from langgraph.types import Command

**Examples:**

Example 1 (unknown):
```unknown
<Info>
  You must configure a checkpointer to persist the graph state across interrupts.
  In production, use a persistent checkpointer like [`AsyncPostgresSaver`](https://reference.langchain.com/python/langgraph/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver). For testing or prototyping, use [`InMemorySaver`](https://reference.langchain.com/python/langgraph/checkpoints/#langgraph.checkpoint.memory.InMemorySaver).

  When invoking the agent, pass a `config` that includes the **thread ID** to associate execution with a conversation thread.
  See the [LangGraph interrupts documentation](/oss/python/langgraph/interrupts) for details.
</Info>

## Responding to interrupts

When you invoke the agent, it runs until it either completes or an interrupt is raised. An interrupt is triggered when a tool call matches the policy you configured in `interrupt_on`. In that case, the invocation result will include an `__interrupt__` field with the actions that require review. You can then present those actions to a reviewer and resume execution once decisions are provided.
```

---

## search for "memories" within this namespace, filtering on content equivalence, sorted by vector similarity

**URL:** llms-txt#search-for-"memories"-within-this-namespace,-filtering-on-content-equivalence,-sorted-by-vector-similarity

**Contents:**
- Read long-term memory in tools

items = store.search( # [!code highlight]
    namespace, filter={"my-key": "my-value"}, query="language preferences"
)
python A tool the agent can use to look up user information theme={null}
from dataclasses import dataclass

from langchain_core.runnables import RunnableConfig
from langchain.agents import create_agent
from langchain.tools import tool, ToolRuntime
from langgraph.store.memory import InMemoryStore

@dataclass
class Context:
    user_id: str

**Examples:**

Example 1 (unknown):
```unknown
For more information about the memory store, see the [Persistence](/oss/python/langgraph/persistence#memory-store) guide.

## Read long-term memory in tools
```

---

## Load the whole toolkit

**URL:** llms-txt#load-the-whole-toolkit

from langchain_google_community import GmailToolkit

---

## Assistants

**URL:** llms-txt#assistants

**Contents:**
- Configuration
- Versioning
- Execution
- Video guide

Source: https://docs.langchain.com/langsmith/assistants

**Assistants** allow you to manage configurations (like prompts, LLM selection, tools) separately from your graph's core logic, enabling rapid changes that don't alter the graph architecture. It is a way to create multiple specialized versions of the same graph architecture, each optimized for different use cases through configuration variations rather than structural changes.

For example, imagine a general-purpose writing agent built on a common graph architecture. While the structure remains the same, different writing styles—such as blog posts and tweets—require tailored configurations to optimize performance. To support these variations, you can create multiple assistants (e.g., one for blogs and another for tweets) that share the underlying graph but differ in model selection and system prompt.

<img src="https://mintcdn.com/langchain-5e9cc07a/IMK8wJkjSpMCGODD/langsmith/images/assistants.png?fit=max&auto=format&n=IMK8wJkjSpMCGODD&q=85&s=05402316c8fe86fead077ec774e873f0" alt="assistant versions" data-og-width="1824" width="1824" data-og-height="692" height="692" data-path="langsmith/images/assistants.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/IMK8wJkjSpMCGODD/langsmith/images/assistants.png?w=280&fit=max&auto=format&n=IMK8wJkjSpMCGODD&q=85&s=3ac250197ee8463950b74dc5f6bcd37f 280w, https://mintcdn.com/langchain-5e9cc07a/IMK8wJkjSpMCGODD/langsmith/images/assistants.png?w=560&fit=max&auto=format&n=IMK8wJkjSpMCGODD&q=85&s=d6b01c6ae96bd96b580bf43228610224 560w, https://mintcdn.com/langchain-5e9cc07a/IMK8wJkjSpMCGODD/langsmith/images/assistants.png?w=840&fit=max&auto=format&n=IMK8wJkjSpMCGODD&q=85&s=6125bf9aed49385ec8422e27cb377dad 840w, https://mintcdn.com/langchain-5e9cc07a/IMK8wJkjSpMCGODD/langsmith/images/assistants.png?w=1100&fit=max&auto=format&n=IMK8wJkjSpMCGODD&q=85&s=c54cde5d8a052ceac26d67131407aa73 1100w, https://mintcdn.com/langchain-5e9cc07a/IMK8wJkjSpMCGODD/langsmith/images/assistants.png?w=1650&fit=max&auto=format&n=IMK8wJkjSpMCGODD&q=85&s=780c08f1695bc2e5ba0b6261febb1954 1650w, https://mintcdn.com/langchain-5e9cc07a/IMK8wJkjSpMCGODD/langsmith/images/assistants.png?w=2500&fit=max&auto=format&n=IMK8wJkjSpMCGODD&q=85&s=ed8fba40ce7c1b3455027df735f9bdba 2500w" />

The LangGraph API provides several endpoints for creating and managing assistants and their versions. See the [API reference](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref/#tag/assistants) for more details.

<Info>
  Assistants are a [LangSmith](/langsmith/home) concept. They are not available in the open source LangGraph library.
</Info>

Assistants build on the LangGraph open source concept of [configuration](/oss/python/langgraph/graph-api#runtime-context).

While configuration is available in the open source LangGraph library, assistants are only present in [LangSmith](/langsmith/home). This is due to the fact that assistants are tightly coupled to your deployed graph. Upon deployment, LangGraph Server will automatically create a default assistant for each graph using the graph's default configuration settings.

In practice, an assistant is just an *instance* of a graph with a specific configuration. Therefore, multiple assistants can reference the same graph but can contain different configurations (e.g. prompts, models, tools). The LangGraph Server API provides several endpoints for creating and managing assistants. See the [API reference](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref/) and [this how-to](/langsmith/configuration-cloud) for more details on how to create assistants.

Assistants support versioning to track changes over time.
Once you've created an assistant, subsequent edits to that assistant will create new versions. See [this how-to](/langsmith/configuration-cloud#create-a-new-version-for-your-assistant) for more details on how to manage assistant versions.

A **run** is an invocation of an assistant. Each run may have its own input, configuration, and metadata, which may affect execution and output of the underlying graph. A run can optionally be executed on a [thread](/oss/python/langgraph/persistence#threads).

LangSmith API provides several endpoints for creating and managing runs. See the [API reference](https://langchain-ai.github.io/langgraph/cloud/reference/api/api_ref/) for more details.

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/fMsQX6pwXkE?si=6Q28l0taGOynO7sU" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/langsmith/assistants.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

---

## AIMessage(content='', ..., tool_calls=[{'name': 'foo', 'args': {'bar': 'baz'}, 'id': 'call_1', 'type': 'tool_call'}])

**URL:** llms-txt#aimessage(content='',-...,-tool_calls=[{'name':-'foo',-'args':-{'bar':-'baz'},-'id':-'call_1',-'type':-'tool_call'}])

python  theme={null}
model.invoke("hello, again!")

**Examples:**

Example 1 (unknown):
```unknown
If we invoke the model again, it will return the next item in the iterator:
```

---

## Customize Deep Agents

**URL:** llms-txt#customize-deep-agents

**Contents:**
- Model
- System prompt
- Tools

Source: https://docs.langchain.com/oss/python/deepagents/customization

Learn how to customize deep agents with system prompts, tools, subagents, and more

By default, `deepagents` uses `"claude-sonnet-4-5-20250929"`. You can customize this by passing any [LangChain model object](https://python.langchain.com/docs/integrations/chat/).

Deep agents come with a built-in system prompt inspired by Claude Code's system prompt. The default system prompt contains detailed instructions for using the built-in planning tool, file system tools, and subagents.

Each deep agent tailored to a use case should include a custom system prompt specific to that use case.

Just like tool-calling agents, a deep agent gets a set of top level tools that it has access to.

In addition to any tools that you provide, deep agents also get access to a number of default tools:

* `write_todos` – Update the agent's to-do list
* `ls` – List all files in the agent's filesystem
* `read_file` – Read a file from the agent's filesystem
* `write_file` – Write a new file in the agent's filesystem
* `edit_file` – Edit an existing file in the agent's filesystem
* `task` – Spawn a subagent to handle a specific task

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/customization.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

**Examples:**

Example 1 (unknown):
```unknown
## System prompt

Deep agents come with a built-in system prompt inspired by Claude Code's system prompt. The default system prompt contains detailed instructions for using the built-in planning tool, file system tools, and subagents.

Each deep agent tailored to a use case should include a custom system prompt specific to that use case.
```

Example 2 (unknown):
```unknown
## Tools

Just like tool-calling agents, a deep agent gets a set of top level tools that it has access to.
```

---

## Note: This example requires the `requests` and `requests_toolbelt` libraries.

**URL:** llms-txt#note:-this-example-requires-the-`requests`-and-`requests_toolbelt`-libraries.

---

## >                'description': 'Tool execution pending approval\n\nTool: execute_sql\nArgs: {...}'

**URL:** llms-txt#>----------------'description':-'tool-execution-pending-approval\n\ntool:-execute_sql\nargs:-{...}'

---

## If desired, specify custom instructions

**URL:** llms-txt#if-desired,-specify-custom-instructions

**Contents:**
  - RAG chains
- Next steps

prompt = (
    "You have access to a tool that retrieves context from a blog post. "
    "Use the tool to help answer user queries."
)
agent = create_agent(model, tools, system_prompt=prompt)
python  theme={null}
query = (
    "What is the standard method for Task Decomposition?\n\n"
    "Once you get the answer, look up common extensions of that method."
)

for event in agent.stream(
    {"messages": [{"role": "user", "content": query}]},
    stream_mode="values",
):
    event["messages"][-1].pretty_print()

================================ Human Message =================================

What is the standard method for Task Decomposition?

Once you get the answer, look up common extensions of that method.
================================== Ai Message ==================================
Tool Calls:
  retrieve_context (call_d6AVxICMPQYwAKj9lgH4E337)
 Call ID: call_d6AVxICMPQYwAKj9lgH4E337
  Args:
    query: standard method for Task Decomposition
================================= Tool Message =================================
Name: retrieve_context

Source: {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}
Content: Task decomposition can be done...

Source: {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}
Content: Component One: Planning...
================================== Ai Message ==================================
Tool Calls:
  retrieve_context (call_0dbMOw7266jvETbXWn4JqWpR)
 Call ID: call_0dbMOw7266jvETbXWn4JqWpR
  Args:
    query: common extensions of the standard method for Task Decomposition
================================= Tool Message =================================
Name: retrieve_context

Source: {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}
Content: Task decomposition can be done...

Source: {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/'}
Content: Component One: Planning...
================================== Ai Message ==================================

The standard method for Task Decomposition often used is the Chain of Thought (CoT)...
python  theme={null}
from langchain.agents.middleware import dynamic_prompt, ModelRequest

@dynamic_prompt
def prompt_with_context(request: ModelRequest) -> str:
    """Inject context into state messages."""
    last_query = request.state["messages"][-1].text
    retrieved_docs = vector_store.similarity_search(last_query)

docs_content = "\n\n".join(doc.page_content for doc in retrieved_docs)

system_message = (
        "You are a helpful assistant. Use the following context in your response:"
        f"\n\n{docs_content}"
    )

return system_message

agent = create_agent(model, tools=[], middleware=[prompt_with_context])
python  theme={null}
query = "What is task decomposition?"
for step in agent.stream(
    {"messages": [{"role": "user", "content": query}]},
    stream_mode="values",
):
    step["messages"][-1].pretty_print()

================================ Human Message =================================

What is task decomposition?
================================== Ai Message ==================================

Task decomposition is...
python  theme={null}
  from typing import Any
  from langchain_core.documents import Document
  from langchain.agents.middleware import AgentMiddleware, AgentState

class State(AgentState):
      context: list[Document]

class RetrieveDocumentsMiddleware(AgentMiddleware[State]):
      state_schema = State

def before_model(self, state: AgentState) -> dict[str, Any] | None:
          last_message = state["messages"][-1]
          retrieved_docs = vector_store.similarity_search(last_message.text)

docs_content = "\n\n".join(doc.page_content for doc in retrieved_docs)

augmented_message_content = (
              f"{last_message.text}\n\n"
              "Use the following context to answer the query:\n"
              f"{docs_content}"
          )
          return {
              "messages": [last_message.model_copy(update={"content": augmented_message_content})],
              "context": retrieved_docs,
          }

agent = create_agent(
      llm,
      tools=[],
      middleware=[RetrieveDocumentsMiddleware()],
  )
  ```
</Accordion>

Now that we've implemented a simple RAG application via [`create_agent`](https://reference.langchain.com/python/langchain/agents/#langchain.agents.create_agent), we can easily incorporate new features and go deeper:

* [Stream](/oss/python/langchain/streaming) tokens and other information for responsive user experiences
* Add [conversational memory](/oss/python/langchain/short-term-memory) to support multi-turn interactions
* Add [long-term memory](/oss/python/langchain/long-term-memory) to support memory across conversational threads
* Add [structured responses](/oss/python/langchain/structured-output)
* Deploy your application with [LangSmith Deployments](/langsmith/deployments)

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/rag.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

**Examples:**

Example 1 (unknown):
```unknown
Let's test this out. We construct a question that would typically require an iterative sequence of retrieval steps to answer:
```

Example 2 (unknown):
```unknown

```

Example 3 (unknown):
```unknown
Note that the agent:

1. Generates a query to search for a standard method for task decomposition;
2. Receiving the answer, generates a second query to search for common extensions of it;
3. Having received all necessary context, answers the question.

We can see the full sequence of steps, along with latency and other metadata, in the [LangSmith trace](https://smith.langchain.com/public/7b42d478-33d2-4631-90a4-7cb731681e88/r).

<Tip>
  You can add a deeper level of control and customization using the [LangGraph](/oss/python/langgraph/overview) framework directly— for example, you can add steps to grade document relevance and rewrite search queries. Check out LangGraph's [Agentic RAG tutorial](/oss/python/langgraph/agentic-rag) for more advanced formulations.
</Tip>

### RAG chains

In the above [agentic RAG](#rag-agents) formulation we allow the LLM to use its discretion in generating a [tool call](/oss/python/langchain/models#tool-calling) to help answer user queries. This is a good general-purpose solution, but comes with some trade-offs:

| ✅ Benefits                                                                                                                                                 | ⚠️ Drawbacks                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **Search only when needed** – The LLM can handle greetings, follow-ups, and simple queries without triggering unnecessary searches.                        | **Two inference calls** – When a search is performed, it requires one call to generate the query and another to produce the final response. |
| **Contextual search queries** – By treating search as a tool with a `query` input, the LLM crafts its own queries that incorporate conversational context. | **Reduced control** – The LLM may skip searches when they are actually needed, or issue extra searches when unnecessary.                    |
| **Multiple searches allowed** – The LLM can execute several searches in support of a single user query.                                                    |                                                                                                                                             |

Another common approach is a two-step chain, in which we always run a search (potentially using the raw user query) and incorporate the result as context for a single LLM query. This results in a single inference call per query, buying reduced latency at the expense of flexibility.

In this approach we no longer call the model in a loop, but instead make a single pass.

We can implement this chain by removing tools from the agent and instead incorporating the retrieval step into a custom prompt:
```

Example 4 (unknown):
```unknown
Let's try this out:
```

---

## The instrucitons are passed as a system message to the agent

**URL:** llms-txt#the-instrucitons-are-passed-as-a-system-message-to-the-agent

instructions = """You are a tweet writing assistant. Given a topic, do some research and write a relevant and engaging tweet about it.
- Use at least 3 emojis in each tweet
- The tweet should be no longer than 280 characters
- Always use the search tool to gather recent information on the tweet topic
- Write the tweet only based on the search content. Do not rely on your internal knowledge
- When relevant, link to your sources
- Make your tweet as engaging as possible"""

---

## You need to return a `Command` object to include more than just a final tool call

**URL:** llms-txt#you-need-to-return-a-`command`-object-to-include-more-than-just-a-final-tool-call

**Contents:**
- Handoffs
  - Implementation (Coming soon)

) -> Command:
    result = subagent1.invoke({
        "messages": [{"role": "user", "content": query}]
    })
    return Command(update={
        # This is the example state key we are passing back
        "example_state_key": result["example_state_key"],
        "messages": [
            ToolMessage(
                content=result["messages"][-1].content,
                # We need to include the tool call id so it matches up with the right tool call
                tool_call_id=tool_call_id
            )
        ]
    })
mermaid  theme={null}
graph LR
    A[User] --> B[Agent A]
    B --> C[Agent B]
    C --> A
```

### Implementation (Coming soon)

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/multi-agent.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

**Examples:**

Example 1 (unknown):
```unknown
## Handoffs

In **handoffs**, agents can directly pass control to each other. The “active” agent changes, and the user interacts with whichever agent currently has control.

Flow:

1. The **current agent** decides it needs help from another agent.
2. It passes control (and state) to the **next agent**.
3. The **new agent** interacts directly with the user until it decides to hand off again or finish.
```

---

## Checkpointer is REQUIRED for human-in-the-loop

**URL:** llms-txt#checkpointer-is-required-for-human-in-the-loop

**Contents:**
- Decision types
- Handle interrupts

checkpointer = MemorySaver()

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-20250514",
    tools=[delete_file, read_file, send_email],
    interrupt_on={
        "delete_file": True,  # Default: approve, edit, reject
        "read_file": False,   # No interrupts needed
        "send_email": {"allowed_decisions": ["approve", "reject"]},  # No editing
    },
    checkpointer=checkpointer  # Required!
)
python  theme={null}
interrupt_on = {
    # Sensitive operations: allow all options
    "delete_file": {"allowed_decisions": ["approve", "edit", "reject"]},

# Moderate risk: approval or rejection only
    "write_file": {"allowed_decisions": ["approve", "reject"]},

# Must approve (no rejection allowed)
    "critical_operation": {"allowed_decisions": ["approve"]},
}
python  theme={null}
import uuid
from langgraph.types import Command

**Examples:**

Example 1 (unknown):
```unknown
## Decision types

The `allowed_decisions` list controls what actions a human can take when reviewing a tool call:

* **`"approve"`**: Execute the tool with the original arguments as proposed by the agent
* **`"edit"`**: Modify the tool arguments before execution
* **`"reject"`**: Skip executing this tool call entirely

You can customize which decisions are available for each tool:
```

Example 2 (unknown):
```unknown
## Handle interrupts

When an interrupt is triggered, the agent pauses execution and returns control. Check for interrupts in the result and handle them accordingly.
```

---

## console.log(result);

**URL:** llms-txt#console.log(result);

**Contents:**
  - Error handling

/**
 * {
 *   messages: [
 *     ...
 *     { role: "tool", content: "Returning structured response: {'task': 'update the project timeline', 'assignee': 'Sarah', 'priority': 'high'}", tool_call_id: "call_456", name: "MeetingAction" }
 *   ],
 *   structuredResponse: { task: "update the project timeline", assignee: "Sarah", priority: "high" }
 * }
 */
ts  theme={null}
import * as z from "zod";
import { createAgent, toolStrategy } from "langchain";

const ContactInfo = z.object({
    name: z.string().describe("Person's name"),
    email: z.string().describe("Email address"),
});

const EventDetails = z.object({
    event_name: z.string().describe("Name of the event"),
    date: z.string().describe("Event date"),
});

const agent = createAgent({
    model: "openai:gpt-5",
    tools: [],
    responseFormat: toolStrategy([ContactInfo, EventDetails]),
});

const result = await agent.invoke({
    messages: [
        {
        role: "user",
        content:
            "Extract info: John Doe (john@email.com) is organizing Tech Conference on March 15th",
        },
    ],
});

/**
 * {
 *   messages: [
 *     { role: "user", content: "Extract info: John Doe (john@email.com) is organizing Tech Conference on March 15th" },
 *     { role: "assistant", content: "", tool_calls: [ { name: "ContactInfo", args: { name: "John Doe", email: "john@email.com" }, id: "call_1" }, { name: "EventDetails", args: { event_name: "Tech Conference", date: "March 15th" }, id: "call_2" } ] },
 *     { role: "tool", content: "Error: Model incorrectly returned multiple structured responses (ContactInfo, EventDetails) when only one is expected.\n Please fix your mistakes.", tool_call_id: "call_1", name: "ContactInfo" },
 *     { role: "tool", content: "Error: Model incorrectly returned multiple structured responses (ContactInfo, EventDetails) when only one is expected.\n Please fix your mistakes.", tool_call_id: "call_2", name: "EventDetails" },
 *     { role: "assistant", content: "", tool_calls: [ { name: "ContactInfo", args: { name: "John Doe", email: "john@email.com" }, id: "call_3" } ] },
 *     { role: "tool", content: "Returning structured response: {'name': 'John Doe', 'email': 'john@email.com'}", tool_call_id: "call_3", name: "ContactInfo" }
 *   ],
 *   structuredResponse: { name: "John Doe", email: "john@email.com" }
 * }
 */
ts  theme={null}
import * as z from "zod";
import { createAgent, toolStrategy } from "langchain";

const ProductRating = z.object({
    rating: z.number().min(1).max(5).describe("Rating from 1-5"),
    comment: z.string().describe("Review comment"),
});

const agent = createAgent({
    model: "openai:gpt-5",
    tools: [],
    responseFormat: toolStrategy(ProductRating),
});

const result = await agent.invoke({
    messages: [
        {
        role: "user",
        content: "Parse this: Amazing product, 10/10!",
        },
    ],
});

/**
 * {
 *   messages: [
 *     { role: "user", content: "Parse this: Amazing product, 10/10!" },
 *     { role: "assistant", content: "", tool_calls: [ { name: "ProductRating", args: { rating: 10, comment: "Amazing product" }, id: "call_1" } ] },
 *     { role: "tool", content: "Error: Failed to parse structured output for tool 'ProductRating': 1 validation error for ProductRating\nrating\n  Input should be less than or equal to 5 [type=less_than_equal, input_value=10, input_type=int].\n Please fix your mistakes.", tool_call_id: "call_1", name: "ProductRating" },
 *     { role: "assistant", content: "", tool_calls: [ { name: "ProductRating", args: { rating: 5, comment: "Amazing product" }, id: "call_2" } ] },
 *     { role: "tool", content: "Returning structured response: {'rating': 5, 'comment': 'Amazing product'}", tool_call_id: "call_2", name: "ProductRating" }
 *   ],
 *   structuredResponse: { rating: 5, comment: "Amazing product" }
 * }
 */
ts  theme={null}
const responseFormat = toolStrategy(ProductRating, {
    handleError: "Please provide a valid rating between 1-5 and include a comment."
)

// Error message becomes:
// { role: "tool", content: "Please provide a valid rating between 1-5 and include a comment." }
ts  theme={null}
import { ToolInputParsingException } from "@langchain/core/tools";

const responseFormat = toolStrategy(ProductRating, {
    handleError: (error: ToolStrategyError) => {
        if (error instanceof ToolInputParsingException) {
        return "Please provide a valid rating between 1-5 and include a comment.";
        }
        return error.message;
    }
)

// Only validation errors get retried with default message:
// { role: "tool", content: "Error: Failed to parse structured output for tool 'ProductRating': ...\n Please fix your mistakes." }
ts  theme={null}
const responseFormat = toolStrategy(ProductRating, {
    handleError: (error: ToolStrategyError) => {
        if (error instanceof ToolInputParsingException) {
        return "Please provide a valid rating between 1-5 and include a comment.";
        }
        if (error instanceof CustomUserError) {
        return "This is a custom user error.";
        }
        return error.message;
    }
)
ts  theme={null}
const responseFormat = toolStrategy(ProductRating, {
    handleError: false  // All errors raised
)
```

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/structured-output.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

**Examples:**

Example 1 (unknown):
```unknown
### Error handling

Models can make mistakes when generating structured output via tool calling. LangChain provides intelligent retry mechanisms to handle these errors automatically.

#### Multiple structured outputs error

When a model incorrectly calls multiple structured output tools, the agent provides error feedback in a @\[`ToolMessage`] and prompts the model to retry:
```

Example 2 (unknown):
```unknown
#### Schema validation error

When structured output doesn't match the expected schema, the agent provides specific error feedback:
```

Example 3 (unknown):
```unknown
#### Error handling strategies

You can customize how errors are handled using the `handleErrors` parameter:

**Custom error message:**
```

Example 4 (unknown):
```unknown
**Handle specific exceptions only:**
```

---

## Configure your agents

**URL:** llms-txt#configure-your-agents

config_list = [
    {
        "model": "gpt-4",
        "api_key": os.getenv("OPENAI_API_KEY"),
    }
]

---

## Example: force a model to create a tool call

**URL:** llms-txt#example:-force-a-model-to-create-a-tool-call

**Contents:**
- 5. Implement the agent
- 6. Implement human-in-the-loop review
- Next steps

def call_get_schema(state: MessagesState):
    # Note that LangChain enforces that all models accept `tool_choice="any"`
    # as well as `tool_choice=<string name of tool>`.
    llm_with_tools = llm.bind_tools([get_schema_tool], tool_choice="any")
    response = llm_with_tools.invoke(state["messages"])

return {"messages": [response]}

generate_query_system_prompt = """
You are an agent designed to interact with a SQL database.
Given an input question, create a syntactically correct {dialect} query to run,
then look at the results of the query and return the answer. Unless the user
specifies a specific number of examples they wish to obtain, always limit your
query to at most {top_k} results.

You can order the results by a relevant column to return the most interesting
examples in the database. Never query for all the columns from a specific table,
only ask for the relevant columns given the question.

DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.
""".format(
    dialect=db.dialect,
    top_k=5,
)

def generate_query(state: MessagesState):
    system_message = {
        "role": "system",
        "content": generate_query_system_prompt,
    }
    # We do not force a tool call here, to allow the model to
    # respond naturally when it obtains the solution.
    llm_with_tools = llm.bind_tools([run_query_tool])
    response = llm_with_tools.invoke([system_message] + state["messages"])

return {"messages": [response]}

check_query_system_prompt = """
You are a SQL expert with a strong attention to detail.
Double check the {dialect} query for common mistakes, including:
- Using NOT IN with NULL values
- Using UNION when UNION ALL should have been used
- Using BETWEEN for exclusive ranges
- Data type mismatch in predicates
- Properly quoting identifiers
- Using the correct number of arguments for functions
- Casting to the correct data type
- Using the proper columns for joins

If there are any of the above mistakes, rewrite the query. If there are no mistakes,
just reproduce the original query.

You will call the appropriate tool to execute the query after running this check.
""".format(dialect=db.dialect)

def check_query(state: MessagesState):
    system_message = {
        "role": "system",
        "content": check_query_system_prompt,
    }

# Generate an artificial user message to check
    tool_call = state["messages"][-1].tool_calls[0]
    user_message = {"role": "user", "content": tool_call["args"]["query"]}
    llm_with_tools = llm.bind_tools([run_query_tool], tool_choice="any")
    response = llm_with_tools.invoke([system_message, user_message])
    response.id = state["messages"][-1].id

return {"messages": [response]}
python  theme={null}
def should_continue(state: MessagesState) -> Literal[END, "check_query"]:
    messages = state["messages"]
    last_message = messages[-1]
    if not last_message.tool_calls:
        return END
    else:
        return "check_query"

builder = StateGraph(MessagesState)
builder.add_node(list_tables)
builder.add_node(call_get_schema)
builder.add_node(get_schema_node, "get_schema")
builder.add_node(generate_query)
builder.add_node(check_query)
builder.add_node(run_query_node, "run_query")

builder.add_edge(START, "list_tables")
builder.add_edge("list_tables", "call_get_schema")
builder.add_edge("call_get_schema", "get_schema")
builder.add_edge("get_schema", "generate_query")
builder.add_conditional_edges(
    "generate_query",
    should_continue,
)
builder.add_edge("check_query", "run_query")
builder.add_edge("run_query", "generate_query")

agent = builder.compile()
python  theme={null}
from IPython.display import Image, display
from langchain_core.runnables.graph import CurveStyle, MermaidDrawMethod, NodeStyles

display(Image(agent.get_graph().draw_mermaid_png()))
python  theme={null}
question = "Which genre on average has the longest tracks?"

for step in agent.stream(
    {"messages": [{"role": "user", "content": question}]},
    stream_mode="values",
):
    step["messages"][-1].pretty_print()

================================ Human Message =================================

Which genre on average has the longest tracks?
================================== Ai Message ==================================

Available tables: Album, Artist, Customer, Employee, Genre, Invoice, InvoiceLine, MediaType, Playlist, PlaylistTrack, Track
================================== Ai Message ==================================
Tool Calls:
  sql_db_schema (call_yzje0tj7JK3TEzDx4QnRR3lL)
 Call ID: call_yzje0tj7JK3TEzDx4QnRR3lL
  Args:
    table_names: Genre, Track
================================= Tool Message =================================
Name: sql_db_schema

CREATE TABLE "Genre" (
	"GenreId" INTEGER NOT NULL,
	"Name" NVARCHAR(120),
	PRIMARY KEY ("GenreId")
)

/*
3 rows from Genre table:
GenreId	Name
1	Rock
2	Jazz
3	Metal
*/

CREATE TABLE "Track" (
	"TrackId" INTEGER NOT NULL,
	"Name" NVARCHAR(200) NOT NULL,
	"AlbumId" INTEGER,
	"MediaTypeId" INTEGER NOT NULL,
	"GenreId" INTEGER,
	"Composer" NVARCHAR(220),
	"Milliseconds" INTEGER NOT NULL,
	"Bytes" INTEGER,
	"UnitPrice" NUMERIC(10, 2) NOT NULL,
	PRIMARY KEY ("TrackId"),
	FOREIGN KEY("MediaTypeId") REFERENCES "MediaType" ("MediaTypeId"),
	FOREIGN KEY("GenreId") REFERENCES "Genre" ("GenreId"),
	FOREIGN KEY("AlbumId") REFERENCES "Album" ("AlbumId")
)

/*
3 rows from Track table:
TrackId	Name	AlbumId	MediaTypeId	GenreId	Composer	Milliseconds	Bytes	UnitPrice
1	For Those About To Rock (We Salute You)	1	1	1	Angus Young, Malcolm Young, Brian Johnson	343719	11170334	0.99
2	Balls to the Wall	2	2	1	U. Dirkschneider, W. Hoffmann, H. Frank, P. Baltes, S. Kaufmann, G. Hoffmann	342562	5510424	0.99
3	Fast As a Shark	3	2	1	F. Baltes, S. Kaufman, U. Dirkscneider & W. Hoffman	230619	3990994	0.99
*/
================================== Ai Message ==================================
Tool Calls:
  sql_db_query (call_cb9ApLfZLSq7CWg6jd0im90b)
 Call ID: call_cb9ApLfZLSq7CWg6jd0im90b
  Args:
    query: SELECT Genre.Name, AVG(Track.Milliseconds) AS AvgMilliseconds FROM Track JOIN Genre ON Track.GenreId = Genre.GenreId GROUP BY Genre.GenreId ORDER BY AvgMilliseconds DESC LIMIT 5;
================================== Ai Message ==================================
Tool Calls:
  sql_db_query (call_DMVALfnQ4kJsuF3Yl6jxbeAU)
 Call ID: call_DMVALfnQ4kJsuF3Yl6jxbeAU
  Args:
    query: SELECT Genre.Name, AVG(Track.Milliseconds) AS AvgMilliseconds FROM Track JOIN Genre ON Track.GenreId = Genre.GenreId GROUP BY Genre.GenreId ORDER BY AvgMilliseconds DESC LIMIT 5;
================================= Tool Message =================================
Name: sql_db_query

[('Sci Fi & Fantasy', 2911783.0384615385), ('Science Fiction', 2625549.076923077), ('Drama', 2575283.78125), ('TV Shows', 2145041.0215053763), ('Comedy', 1585263.705882353)]
================================== Ai Message ==================================

The genre with the longest tracks on average is "Sci Fi & Fantasy," with an average track length of approximately 2,911,783 milliseconds. Other genres with relatively long tracks include "Science Fiction," "Drama," "TV Shows," and "Comedy."
python  theme={null}
from langchain_core.runnables import RunnableConfig
from langchain.tools import tool
from langgraph.types import interrupt

@tool(
    run_query_tool.name,
    description=run_query_tool.description,
    args_schema=run_query_tool.args_schema
)
def run_query_tool_with_interrupt(config: RunnableConfig, **tool_input):
    request = {
        "action": run_query_tool.name,
        "args": tool_input,
        "description": "Please review the tool call"
    }
    response = interrupt([request]) # [!code highlight]
    # approve the tool call
    if response["type"] == "accept":
        tool_response = run_query_tool.invoke(tool_input, config)
    # update tool call args
    elif response["type"] == "edit":
        tool_input = response["args"]["args"]
        tool_response = run_query_tool.invoke(tool_input, config)
    # respond to the LLM with user feedback
    elif response["type"] == "response":
        user_feedback = response["args"]
        tool_response = user_feedback
    else:
        raise ValueError(f"Unsupported interrupt response type: {response['type']}")

return tool_response
python  theme={null}
from langgraph.checkpoint.memory import InMemorySaver

def should_continue(state: MessagesState) -> Literal[END, "run_query"]:
    messages = state["messages"]
    last_message = messages[-1]
    if not last_message.tool_calls:
        return END
    else:
        return "run_query"

builder = StateGraph(MessagesState)
builder.add_node(list_tables)
builder.add_node(call_get_schema)
builder.add_node(get_schema_node, "get_schema")
builder.add_node(generate_query)
builder.add_node(run_query_node, "run_query")

builder.add_edge(START, "list_tables")
builder.add_edge("list_tables", "call_get_schema")
builder.add_edge("call_get_schema", "get_schema")
builder.add_edge("get_schema", "generate_query")
builder.add_conditional_edges(
    "generate_query",
    should_continue,
)
builder.add_edge("run_query", "generate_query")

checkpointer = InMemorySaver() # [!code highlight]
agent = builder.compile(checkpointer=checkpointer) # [!code highlight]
python  theme={null}
import json

config = {"configurable": {"thread_id": "1"}}

question = "Which genre on average has the longest tracks?"

for step in agent.stream(
    {"messages": [{"role": "user", "content": question}]},
    config,
    stream_mode="values",
):
    if "messages" in step:
        step["messages"][-1].pretty_print()
    elif "__interrupt__" in step:
        action = step["__interrupt__"][0]
        print("INTERRUPTED:")
        for request in action.value:
            print(json.dumps(request, indent=2))
    else:
        pass

INTERRUPTED:
{
  "action": "sql_db_query",
  "args": {
    "query": "SELECT Genre.Name, AVG(Track.Milliseconds) AS AvgLength FROM Track JOIN Genre ON Track.GenreId = Genre.GenreId GROUP BY Genre.Name ORDER BY AvgLength DESC LIMIT 5;"
  },
  "description": "Please review the tool call"
}
python  theme={null}
from langgraph.types import Command

for step in agent.stream(
    Command(resume={"type": "accept"}),
    # Command(resume={"type": "edit", "args": {"query": "..."}}),
    config,
    stream_mode="values",
):
    if "messages" in step:
        step["messages"][-1].pretty_print()
    elif "__interrupt__" in step:
        action = step["__interrupt__"][0]
        print("INTERRUPTED:")
        for request in action.value:
            print(json.dumps(request, indent=2))
    else:
        pass

================================== Ai Message ==================================
Tool Calls:
  sql_db_query (call_t4yXkD6shwdTPuelXEmY3sAY)
 Call ID: call_t4yXkD6shwdTPuelXEmY3sAY
  Args:
    query: SELECT Genre.Name, AVG(Track.Milliseconds) AS AvgLength FROM Track JOIN Genre ON Track.GenreId = Genre.GenreId GROUP BY Genre.Name ORDER BY AvgLength DESC LIMIT 5;
================================= Tool Message =================================
Name: sql_db_query

[('Sci Fi & Fantasy', 2911783.0384615385), ('Science Fiction', 2625549.076923077), ('Drama', 2575283.78125), ('TV Shows', 2145041.0215053763), ('Comedy', 1585263.705882353)]
================================== Ai Message ==================================

The genre with the longest average track length is "Sci Fi & Fantasy" with an average length of about 2,911,783 milliseconds. Other genres with long average track lengths include "Science Fiction," "Drama," "TV Shows," and "Comedy."
```

Refer to the [human-in-the-loop guide](/oss/python/langgraph/interrupts) for details.

Check out the [Evaluate a graph](/langsmith/evaluate-graph) guide for evaluating LangGraph applications, including SQL agents like this one, using LangSmith.

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/sql-agent.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

**Examples:**

Example 1 (unknown):
```unknown
## 5. Implement the agent

We can now assemble these steps into a workflow using the [Graph API](/oss/python/langgraph/graph-api). We define a [conditional edge](/oss/python/langgraph/graph-api#conditional-edges) at the query generation step that will route to the query checker if a query is generated, or end if there are no tool calls present, such that the LLM has delivered a response to the query.
```

Example 2 (unknown):
```unknown
We visualize the application below:
```

Example 3 (unknown):
```unknown
<img src="https://mintcdn.com/langchain-5e9cc07a/aAi4RLdXQAh8fThS/oss/images/sql-agent-langgraph.png?fit=max&auto=format&n=aAi4RLdXQAh8fThS&q=85&s=1ddd4aae369fb8c143edaccb0a09c81f" alt="SQL agent graph" style={{ height: "800px" }} data-og-width="308" width="308" data-og-height="645" height="645" data-path="oss/images/sql-agent-langgraph.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/aAi4RLdXQAh8fThS/oss/images/sql-agent-langgraph.png?w=280&fit=max&auto=format&n=aAi4RLdXQAh8fThS&q=85&s=e5d3e67f17d65e438370f7d771e3ba7d 280w, https://mintcdn.com/langchain-5e9cc07a/aAi4RLdXQAh8fThS/oss/images/sql-agent-langgraph.png?w=560&fit=max&auto=format&n=aAi4RLdXQAh8fThS&q=85&s=dbcb80fdb2d00a6dc33dc90f05d100b5 560w, https://mintcdn.com/langchain-5e9cc07a/aAi4RLdXQAh8fThS/oss/images/sql-agent-langgraph.png?w=840&fit=max&auto=format&n=aAi4RLdXQAh8fThS&q=85&s=72be69a1e7ac39afad3d0aa03ecffffa 840w, https://mintcdn.com/langchain-5e9cc07a/aAi4RLdXQAh8fThS/oss/images/sql-agent-langgraph.png?w=1100&fit=max&auto=format&n=aAi4RLdXQAh8fThS&q=85&s=5ad351b8b6641defe17882f5e102cab0 1100w, https://mintcdn.com/langchain-5e9cc07a/aAi4RLdXQAh8fThS/oss/images/sql-agent-langgraph.png?w=1650&fit=max&auto=format&n=aAi4RLdXQAh8fThS&q=85&s=8a5cefc8ac6938d0b4b0946e0522ffaa 1650w, https://mintcdn.com/langchain-5e9cc07a/aAi4RLdXQAh8fThS/oss/images/sql-agent-langgraph.png?w=2500&fit=max&auto=format&n=aAi4RLdXQAh8fThS&q=85&s=0b5b7711b4b2ece3a3ccb10a2b012166 2500w" />

We can now invoke the graph:
```

Example 4 (unknown):
```unknown

```

---

## my_agent/agent.py

**URL:** llms-txt#my_agent/agent.py

from typing import Literal
from typing_extensions import TypedDict

from langgraph.graph import StateGraph, END, START
from my_agent.utils.nodes import call_model, should_continue, tool_node # import nodes
from my_agent.utils.state import AgentState # import state

---

## Augment the LLM with tools

**URL:** llms-txt#augment-the-llm-with-tools

tools = [add, multiply, divide]
tools_by_name = {tool.name: tool for tool in tools}
llm_with_tools = llm.bind_tools(tools)
python Graph API theme={null}
  from langgraph.graph import MessagesState
  from langchain.messages import SystemMessage, HumanMessage, ToolMessage

# Nodes
  def llm_call(state: MessagesState):
      """LLM decides whether to call a tool or not"""

return {
          "messages": [
              llm_with_tools.invoke(
                  [
                      SystemMessage(
                          content="You are a helpful assistant tasked with performing arithmetic on a set of inputs."
                      )
                  ]
                  + state["messages"]
              )
          ]
      }

def tool_node(state: dict):
      """Performs the tool call"""

result = []
      for tool_call in state["messages"][-1].tool_calls:
          tool = tools_by_name[tool_call["name"]]
          observation = tool.invoke(tool_call["args"])
          result.append(ToolMessage(content=observation, tool_call_id=tool_call["id"]))
      return {"messages": result}

# Conditional edge function to route to the tool node or end based upon whether the LLM made a tool call
  def should_continue(state: MessagesState) -> Literal["tool_node", END]:
      """Decide if we should continue the loop or stop based upon whether the LLM made a tool call"""

messages = state["messages"]
      last_message = messages[-1]

# If the LLM makes a tool call, then perform an action
      if last_message.tool_calls:
          return "tool_node"

# Otherwise, we stop (reply to the user)
      return END

# Build workflow
  agent_builder = StateGraph(MessagesState)

# Add nodes
  agent_builder.add_node("llm_call", llm_call)
  agent_builder.add_node("tool_node", tool_node)

# Add edges to connect nodes
  agent_builder.add_edge(START, "llm_call")
  agent_builder.add_conditional_edges(
      "llm_call",
      should_continue,
      ["tool_node", END]
  )
  agent_builder.add_edge("tool_node", "llm_call")

# Compile the agent
  agent = agent_builder.compile()

# Show the agent
  display(Image(agent.get_graph(xray=True).draw_mermaid_png()))

# Invoke
  messages = [HumanMessage(content="Add 3 and 4.")]
  messages = agent.invoke({"messages": messages})
  for m in messages["messages"]:
      m.pretty_print()
  python Functional API theme={null}
  from langgraph.graph import add_messages
  from langchain.messages import (
      SystemMessage,
      HumanMessage,
      BaseMessage,
      ToolCall,
  )

@task
  def call_llm(messages: list[BaseMessage]):
      """LLM decides whether to call a tool or not"""
      return llm_with_tools.invoke(
          [
              SystemMessage(
                  content="You are a helpful assistant tasked with performing arithmetic on a set of inputs."
              )
          ]
          + messages
      )

@task
  def call_tool(tool_call: ToolCall):
      """Performs the tool call"""
      tool = tools_by_name[tool_call["name"]]
      return tool.invoke(tool_call)

@entrypoint()
  def agent(messages: list[BaseMessage]):
      llm_response = call_llm(messages).result()

while True:
          if not llm_response.tool_calls:
              break

# Execute tools
          tool_result_futures = [
              call_tool(tool_call) for tool_call in llm_response.tool_calls
          ]
          tool_results = [fut.result() for fut in tool_result_futures]
          messages = add_messages(messages, [llm_response, *tool_results])
          llm_response = call_llm(messages).result()

messages = add_messages(messages, llm_response)
      return messages

# Invoke
  messages = [HumanMessage(content="Add 3 and 4.")]
  for chunk in agent.stream(messages, stream_mode="updates"):
      print(chunk)
      print("\n")
  ```
</CodeGroup>

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/workflows-agents.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

**Examples:**

Example 1 (unknown):
```unknown
<CodeGroup>
```

Example 2 (unknown):
```unknown

```

---

## Build a custom SQL agent

**URL:** llms-txt#build-a-custom-sql-agent

**Contents:**
  - Concepts
- Setup
  - Installation
  - LangSmith
- 1. Select an LLM
- 2. Configure the database
- 3. Add tools for database interactions
- 4. Define application steps

Source: https://docs.langchain.com/oss/python/langgraph/sql-agent

In this tutorial we will build a custom agent that can answer questions about a SQL database using LangGraph.

LangChain offers built-in [agent](/oss/python/langchain/agents) implementations, implemented using [LangGraph](/oss/python/langgraph/overview) primitives. If deeper customization is required, agents can be implemented directly in LangGraph. This guide demonstrates an example implementation of a SQL agent. You can find a tutorial building a SQL agent using higher-level LangChain abstractions [here](/oss/python/langchain/sql-agent).

<Warning>
  Building Q\&A systems of SQL databases requires executing model-generated SQL queries. There are inherent risks in doing this. Make sure that your database connection permissions are always scoped as narrowly as possible for your agent's needs. This will mitigate, though not eliminate, the risks of building a model-driven system.
</Warning>

The [prebuilt agent](/oss/python/langchain/sql-agent) lets us get started quickly, but we relied on the system prompt to constrain its behavior— for example, we instructed the agent to always start with the "list tables" tool, and to always run a query-checker tool before executing the query.

We can enforce a higher degree of control in LangGraph by customizing the agent. Here, we implement a simple ReAct-agent setup, with dedicated nodes for specific tool-calls. We will use the same \[state] as the pre-built agent.

We will cover the following concepts:

* [Tools](/oss/python/langchain/tools) for reading from SQL databases
* The LangGraph [Graph API](/oss/python/langgraph/graph-api), including state, nodes, edges, and conditional edges.
* [Human-in-the-loop](/oss/python/langgraph/interrupts) processes

<CodeGroup>
  
</CodeGroup>

Set up [LangSmith](https://smith.langchain.com) to inspect what is happening inside your chain or agent. Then set the following environment variables:

Select a model that supports [tool-calling](/oss/python/integrations/providers/overview):

<Tabs>
  <Tab title="OpenAI">
    👉 Read the [OpenAI chat model integration docs](/oss/python/integrations/chat/openai/)

</CodeGroup>
  </Tab>

<Tab title="Anthropic">
    👉 Read the [Anthropic chat model integration docs](/oss/python/integrations/chat/anthropic/)

</CodeGroup>
  </Tab>

<Tab title="Azure">
    👉 Read the [Azure chat model integration docs](/oss/python/integrations/chat/azure_chat_openai/)

</CodeGroup>
  </Tab>

<Tab title="Google Gemini">
    👉 Read the [Google GenAI chat model integration docs](/oss/python/integrations/chat/google_generative_ai/)

</CodeGroup>
  </Tab>

<Tab title="AWS Bedrock">
    👉 Read the [AWS Bedrock chat model integration docs](/oss/python/integrations/chat/bedrock/)

</CodeGroup>
  </Tab>
</Tabs>

The output shown in the examples below used OpenAI.

## 2. Configure the database

You will be creating a [SQLite database](https://www.sqlitetutorial.net/sqlite-sample-database/) for this tutorial. SQLite is a lightweight database that is easy to set up and use. We will be loading the `chinook` database, which is a sample database that represents a digital media store.

For convenience, we have hosted the database (`Chinook.db`) on a public GCS bucket.

We will use a handy SQL database wrapper available in the `langchain_community` package to interact with the database. The wrapper provides a simple interface to execute SQL queries and fetch results:

## 3. Add tools for database interactions

Use the `SQLDatabase` wrapper available in the `langchain_community` package to interact with the database. The wrapper provides a simple interface to execute SQL queries and fetch results:

## 4. Define application steps

We construct dedicated nodes for the following steps:

* Listing DB tables
* Calling the "get schema" tool
* Generating a query
* Checking the query

Putting these steps in dedicated nodes lets us (1) force tool-calls when needed, and (2) customize the prompts associated with each step.

```python  theme={null}
from typing import Literal

from langchain.agents import ToolNode
from langchain.messages import AIMessage
from langchain_core.runnables import RunnableConfig
from langgraph.graph import END, START, MessagesState, StateGraph

get_schema_tool = next(tool for tool in tools if tool.name == "sql_db_schema")
get_schema_node = ToolNode([get_schema_tool], name="get_schema")

run_query_tool = next(tool for tool in tools if tool.name == "sql_db_query")
run_query_node = ToolNode([run_query_tool], name="run_query")

**Examples:**

Example 1 (unknown):
```unknown
</CodeGroup>

### LangSmith

Set up [LangSmith](https://smith.langchain.com) to inspect what is happening inside your chain or agent. Then set the following environment variables:
```

Example 2 (unknown):
```unknown
## 1. Select an LLM

Select a model that supports [tool-calling](/oss/python/integrations/providers/overview):

<Tabs>
  <Tab title="OpenAI">
    👉 Read the [OpenAI chat model integration docs](/oss/python/integrations/chat/openai/)
```

Example 3 (unknown):
```unknown
<CodeGroup>
```

Example 4 (unknown):
```unknown

```

---

## Subagents

**URL:** llms-txt#subagents

**Contents:**
- Why use subagents?
- Configuration
  - SubAgent (Dictionary-based)
  - CompiledSubAgent
- Using SubAgent
- Using CompiledSubAgent

Source: https://docs.langchain.com/oss/python/deepagents/subagents

Learn how to use subagents to delegate work and keep context clean

Deep agents can create subagents to delegate work. You can specify custom subagents in the `subagents` parameter. Subagents are useful for [context quarantine](https://www.dbreunig.com/2025/06/26/how-to-fix-your-context.html#context-quarantine) (keeping the main agent's context clean) and for providing specialized instructions.

## Why use subagents?

Subagents solve the **context bloat problem**. When agents use tools with large outputs (web search, file reads, database queries), the context window fills up quickly with intermediate results. Subagents isolate this detailed work—the main agent receives only the final result, not the dozens of tool calls that produced it.

**When to use subagents:**

* ✅ Multi-step tasks that would clutter the main agent's context
* ✅ Specialized domains that need custom instructions or tools
* ✅ Tasks requiring different model capabilities
* ✅ When you want to keep the main agent focused on high-level coordination

**When NOT to use subagents:**

* ❌ Simple, single-step tasks
* ❌ When you need to maintain intermediate context
* ❌ When the overhead outweighs benefits

`subagents` should be a list of dictionaries or `CompiledSubAgent` objects. There are two types:

### SubAgent (Dictionary-based)

For most use cases, define subagents as dictionaries:

* **name** (`str`): Unique identifier for the subagent. The main agent uses this name when calling the `task()` tool.
* **description** (`str`): What this subagent does. Be specific and action-oriented. The main agent uses this to decide when to delegate.
* **system\_prompt** (`str`): Instructions for the subagent. Include tool usage guidance and output format requirements.
* **tools** (`List[Callable]`): Tools the subagent can use. Keep this minimal and include only what's needed.

* **model** (`str | BaseChatModel`): Override the main agent's model. Use the format `"provider:model-name"` (for example, `"openai:gpt-4o"`).
* **middleware** (`List[Middleware]`): Additional middleware for custom behavior, logging, or rate limiting.
* **interrupt\_on** (`Dict[str, bool]`): Configure human-in-the-loop for specific tools. Requires a checkpointer.

For complex workflows, use a pre-built LangGraph graph:

* **name** (`str`): Unique identifier
* **description** (`str`): What this subagent does
* **runnable** (`Runnable`): A compiled LangGraph graph (must call `.compile()` first)

## Using CompiledSubAgent

For more complex use cases, you can provide your own pre-built LangGraph graph as a subagent:

```python  theme={null}
from deepagents import create_deep_agent, CompiledSubAgent
from langchain.agents import create_agent

**Examples:**

Example 1 (unknown):
```unknown
## Using CompiledSubAgent

For more complex use cases, you can provide your own pre-built LangGraph graph as a subagent:
```

---

## System prompt to steer the agent to be an expert researcher

**URL:** llms-txt#system-prompt-to-steer-the-agent-to-be-an-expert-researcher

**Contents:**
- `internet_search`
  - Step 5: Run the agent

research_instructions = """You are an expert researcher. Your job is to conduct thorough research and then write a polished report.

You have access to an internet search tool as your primary means of gathering information.

Use this to run an internet search for a given query. You can specify the max number of results to return, the topic, and whether raw content should be included.
"""

agent = create_deep_agent(
    tools=[internet_search],
    system_prompt=research_instructions
)
python  theme={null}
result = agent.invoke({"messages": [{"role": "user", "content": "What is langgraph?"}]})

**Examples:**

Example 1 (unknown):
```unknown
### Step 5: Run the agent
```

---

## Trace with OpenAI Agents SDK

**URL:** llms-txt#trace-with-openai-agents-sdk

**Contents:**
- Installation
- Quick Start

Source: https://docs.langchain.com/langsmith/trace-with-openai-agents-sdk

The OpenAI Agents SDK allows you to build agentic applications powered by OpenAI's models.

Learn how to trace your LLM applications using the OpenAI Agents SDK with LangSmith.

<Info>
  Requires Python SDK version `langsmith>=0.3.15`.
</Info>

Install LangSmith with OpenAI Agents support:

This will install both the LangSmith library and the OpenAI Agents SDK.

You can integrate LangSmith tracing with the OpenAI Agents SDK by using the `OpenAIAgentsTracingProcessor` class.

The agent's execution flow, including all spans and their details, will be logged to LangSmith.

<img src="https://mintcdn.com/langchain-5e9cc07a/E8FdemkcQxROovD9/langsmith/images/agent-trace.png?fit=max&auto=format&n=E8FdemkcQxROovD9&q=85&s=7544fc0deb9c6279a9848da17d70bf8b" alt="OpenAI Agents SDK Trace in LangSmith" data-og-width="2984" width="2984" data-og-height="1782" height="1782" data-path="langsmith/images/agent-trace.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/E8FdemkcQxROovD9/langsmith/images/agent-trace.png?w=280&fit=max&auto=format&n=E8FdemkcQxROovD9&q=85&s=18b3ec39553d20f562c61e68120b5ed7 280w, https://mintcdn.com/langchain-5e9cc07a/E8FdemkcQxROovD9/langsmith/images/agent-trace.png?w=560&fit=max&auto=format&n=E8FdemkcQxROovD9&q=85&s=e278d9a842f33c876cf1bb6937edaa9d 560w, https://mintcdn.com/langchain-5e9cc07a/E8FdemkcQxROovD9/langsmith/images/agent-trace.png?w=840&fit=max&auto=format&n=E8FdemkcQxROovD9&q=85&s=cf1fd1047a4f61bfe3cb0917d64cb403 840w, https://mintcdn.com/langchain-5e9cc07a/E8FdemkcQxROovD9/langsmith/images/agent-trace.png?w=1100&fit=max&auto=format&n=E8FdemkcQxROovD9&q=85&s=6d98b5286390e19b818c82fa3dcdd3e8 1100w, https://mintcdn.com/langchain-5e9cc07a/E8FdemkcQxROovD9/langsmith/images/agent-trace.png?w=1650&fit=max&auto=format&n=E8FdemkcQxROovD9&q=85&s=a20187910934b3921b5cac30df0922cb 1650w, https://mintcdn.com/langchain-5e9cc07a/E8FdemkcQxROovD9/langsmith/images/agent-trace.png?w=2500&fit=max&auto=format&n=E8FdemkcQxROovD9&q=85&s=3434b20ed1dfef6fc3751a50bb49b062 2500w" />

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-openai-agents-sdk.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

**Examples:**

Example 1 (unknown):
```unknown

```

Example 2 (unknown):
```unknown
</CodeGroup>

This will install both the LangSmith library and the OpenAI Agents SDK.

## Quick Start

You can integrate LangSmith tracing with the OpenAI Agents SDK by using the `OpenAIAgentsTracingProcessor` class.
```

---

## LangSmith components

**URL:** llms-txt#langsmith-components

Source: https://docs.langchain.com/langsmith/components

When running the self-hosted [LangSmith with deployment](/langsmith/deploy-self-hosted-full-platform), your installation includes several key components. Together these tools and services provide a complete solution for building, deploying, and managing graphs (including agentic applications) in your own infrastructure:

* [LangGraph Server](/langsmith/langgraph-server): Defines an opinionated API and runtime for deploying graphs and agents. Handles execution, state management, and persistence so you can focus on building logic rather than server infrastructure.
* [LangGraph CLI](/langsmith/cli): A command-line interface to build, package, and interact with graphs locally and prepare them for deployment.
* [Studio](/langsmith/studio): A specialized IDE for visualization, interaction, and debugging. Connects to a local LangGraph Server for developing and testing your graph.
* [Python/JS SDK](/langsmith/sdk): The Python/JS SDK provides a programmatic way to interact with deployed graphs and agents from your applications.
* [RemoteGraph](/langsmith/use-remote-graph): Allows you to interact with a deployed graph as though it were running locally.
* [Control Plane](/langsmith/control-plane): The UI and APIs for creating, updating, and managing LangGraph Server deployments.
* [Data plane](/langsmith/data-plane): The runtime layer that executes your graphs, including LangGraph Servers, their backing services (PostgreSQL, Redis, etc.), and the listener that reconciles state from the control plane.

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/langsmith/components.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

---

## Agent Builder

**URL:** llms-txt#agent-builder

**Contents:**
- Memory and updates
- Triggers
- Sub-agents
- Human in the loop
  - Enabling interrupts
  - Actions on interrupts

Source: https://docs.langchain.com/langsmith/agent-builder

<Callout icon="wand-magic-sparkles" color="#2563EB" iconType="regular">
  Agent Builder is in private preview. Sign up for the waitlist [today](https://www.langchain.com/langsmith-agent-builder-waitlist).
</Callout>

Agent Builder lets you turn natural-language ideas into production agents. It's powered by [deep-agents](https://github.com/langchain-ai/deepagents), and is not <Tooltip tip="Predetermined code paths that are designed to operate in a certain order.">workflow based</Tooltip>.

## Memory and updates

Agent Builder includes persistent agent memory and supports self-updates. This lets agents adapt over time and refine how they work without manual edits.

* Persistent memory: Agents retain relevant information across runs to inform future decisions.
* What can be updated: Tools (add, remove, or reconfigure), and instructions/system prompts.
* Agents cannot modify their name, description, and/or triggers attached.

Triggers define when your agent should start running. You can connect your agent to external tools or time-based schedules, letting it respond automatically to messages, emails, or recurring events.

The following examples show some of the apps you can use to trigger your agent:

<CardGroup cols={3}>
  <Card title="Slack" icon="slack">
    Activate your agent when messages are received in specific Slack channels.
  </Card>

<Card title="Gmail" icon="envelope">
    Trigger your agent when emails are received.
  </Card>

<Card title="Cron schedules" icon="clock">
    Run your agent on a time-based schedule for recurring tasks.
  </Card>
</CardGroup>

Agent Builder lets you create sub-agents within a main agent. Sub-agents are smaller, specialized agents that handle specific parts of a larger task. They can operate with their own tools, permissions, or goals while coordinating with the main agent.

Using sub-agents makes it easier to build complex systems by dividing work into focused, reusable components. This modular approach helps keep your agents organized, scalable, and easier to maintain.

Below are a few ways sub-agents can be used in your projects:

* Handle distinct parts of a broader workflow (for example, data retrieval, summarization, or formatting).
* Use different tools or context windows for specialized tasks.
* Run independently but report results back to the main agent.

Human-in-the-loop functionality allows you to review and approve agent actions before they execute, giving you control over critical decisions.

### Enabling interrupts

<Steps>
  <Step title="Select a tool">
    When configuring your agent in Agent Builder, select the tool you want to add human oversight to.
  </Step>

<Step title="Enable interrupts">
    Look for the interrupt option when selecting the tool and toggle it on.
  </Step>

<Step title="Agent pauses for approval">
    The agent will pause and wait for human approval before executing that tool.
  </Step>
</Steps>

### Actions on interrupts

When your agent reaches an interrupt point, you can take one of three actions:

<CardGroup cols={3}>
  <Card title="Accept" icon="check">
    Approve the agent's proposed action and allow it to proceed as planned.
  </Card>

<Card title="Edit" icon="pen-to-square">
    Modify the agent's message or parameters before allowing it to continue.
  </Card>

<Card title="Send feedback" icon="comment">
    Provide feedback to the agent.
  </Card>
</CardGroup>

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/langsmith/agent-builder.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

---

## Context engineering in agents

**URL:** llms-txt#context-engineering-in-agents

**Contents:**
- Overview
  - Why do agents fail?
  - The agent loop
  - What you can control
  - Data sources
  - How it works
- Model Context
  - System Prompt
  - Messages
  - Tools

Source: https://docs.langchain.com/oss/python/langchain/context-engineering

The hard part of building agents (or any LLM application) is making them reliable enough. While they may work for a prototype, they often fail in real-world use cases.

### Why do agents fail?

When agents fail, it's usually because the LLM call inside the agent took the wrong action / didn't do what we expected. LLMs fail for one of two reasons:

1. The underlying LLM is not capable enough
2. The "right" context was not passed to the LLM

More often than not - it's actually the second reason that causes agents to not be reliable.

**Context engineering** is providing the right information and tools in the right format so the LLM can accomplish a task. This is the number one job of AI Engineers. This lack of "right" context is the number one blocker for more reliable agents, and LangChain's agent abstractions are uniquely designed to facilitate context engineering.

<Tip>
  New to context engineering? Start with the [conceptual overview](/oss/python/concepts/context) to understand the different types of context and when to use them.
</Tip>

A typical agent loop consists of two main steps:

1. **Model call** - calls the LLM with a prompt and available tools, returns either a response or a request to execute tools
2. **Tool execution** - executes the tools that the LLM requested, returns tool results

<div style={{ display: "flex", justifyContent: "center" }}>
  <img src="https://mintcdn.com/langchain-5e9cc07a/Tazq8zGc0yYUYrDl/oss/images/core_agent_loop.png?fit=max&auto=format&n=Tazq8zGc0yYUYrDl&q=85&s=ac72e48317a9ced68fd1be64e89ec063" alt="Core agent loop diagram" className="rounded-lg" data-og-width="300" width="300" data-og-height="268" height="268" data-path="oss/images/core_agent_loop.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/Tazq8zGc0yYUYrDl/oss/images/core_agent_loop.png?w=280&fit=max&auto=format&n=Tazq8zGc0yYUYrDl&q=85&s=a4c4b766b6678ef52a6ed556b1a0b032 280w, https://mintcdn.com/langchain-5e9cc07a/Tazq8zGc0yYUYrDl/oss/images/core_agent_loop.png?w=560&fit=max&auto=format&n=Tazq8zGc0yYUYrDl&q=85&s=111869e6e99a52c0eff60a1ef7ddc49c 560w, https://mintcdn.com/langchain-5e9cc07a/Tazq8zGc0yYUYrDl/oss/images/core_agent_loop.png?w=840&fit=max&auto=format&n=Tazq8zGc0yYUYrDl&q=85&s=6c1e21de7b53bd0a29683aca09c6f86e 840w, https://mintcdn.com/langchain-5e9cc07a/Tazq8zGc0yYUYrDl/oss/images/core_agent_loop.png?w=1100&fit=max&auto=format&n=Tazq8zGc0yYUYrDl&q=85&s=88bef556edba9869b759551c610c60f4 1100w, https://mintcdn.com/langchain-5e9cc07a/Tazq8zGc0yYUYrDl/oss/images/core_agent_loop.png?w=1650&fit=max&auto=format&n=Tazq8zGc0yYUYrDl&q=85&s=9b0bdd138e9548eeb5056dc0ed2d4a4b 1650w, https://mintcdn.com/langchain-5e9cc07a/Tazq8zGc0yYUYrDl/oss/images/core_agent_loop.png?w=2500&fit=max&auto=format&n=Tazq8zGc0yYUYrDl&q=85&s=41eb4f053ed5e6b0ba5bad2badf6d755 2500w" />
</div>

This loop continues until the LLM decides to finish.

### What you can control

To build reliable agents, you need to control what happens at each step of the agent loop, as well as what happens between steps.

| Context Type                                  | What You Control                                                                     | Transient or Persistent |
| --------------------------------------------- | ------------------------------------------------------------------------------------ | ----------------------- |
| **[Model Context](#model-context)**           | What goes into model calls (instructions, message history, tools, response format)   | Transient               |
| **[Tool Context](#tool-context)**             | What tools can access and produce (reads/writes to state, store, runtime context)    | Persistent              |
| **[Life-cycle Context](#life-cycle-context)** | What happens between model and tool calls (summarization, guardrails, logging, etc.) | Persistent              |

<CardGroup>
  <Card title="Transient context" icon="bolt" iconType="duotone">
    What the LLM sees for a single call. You can modify messages, tools, or prompts without changing what's saved in state.
  </Card>

<Card title="Persistent context" icon="database" iconType="duotone">
    What gets saved in state across turns. Life-cycle hooks and tool writes modify this permanently.
  </Card>
</CardGroup>

Throughout this process, your agent accesses (reads / writes) different sources of data:

| Data Source         | Also Known As        | Scope               | Examples                                                                   |
| ------------------- | -------------------- | ------------------- | -------------------------------------------------------------------------- |
| **Runtime Context** | Static configuration | Conversation-scoped | User ID, API keys, database connections, permissions, environment settings |
| **State**           | Short-term memory    | Conversation-scoped | Current messages, uploaded files, authentication status, tool results      |
| **Store**           | Long-term memory     | Cross-conversation  | User preferences, extracted insights, memories, historical data            |

LangChain [middleware](/oss/python/langchain/middleware) is the mechanism under the hood that makes context engineering practical for developers using LangChain.

Middleware allows you to hook into any step in the agent lifecycle and:

* Update context
* Jump to a different step in the agent lifecycle

Throughout this guide, you'll see frequent use of the middleware API as a means to the context engineering end.

Control what goes into each model call - instructions, available tools, which model to use, and output format. These decisions directly impact reliability and cost.

<CardGroup cols={2}>
  <Card title="System Prompt" icon="message-lines" href="#system-prompt">
    Base instructions from the developer to the LLM.
  </Card>

<Card title="Messages" icon="comments" href="#messages">
    The full list of messages (conversation history) sent to the LLM.
  </Card>

<Card title="Tools" icon="wrench" href="#tools">
    Utilities the agent has access to to take actions.
  </Card>

<Card title="Model" icon="brain-circuit" href="#model">
    The actual model (including configuration) to be called.
  </Card>

<Card title="Response Format" icon="brackets-curly" href="#response-format">
    Schema specification for the model's final response.
  </Card>
</CardGroup>

All of these types of model context can draw from **state** (short-term memory), **store** (long-term memory), or **runtime context** (static configuration).

The system prompt sets the LLM's behavior and capabilities. Different users, contexts, or conversation stages need different instructions. Successful agents draw on memories, preferences, and configuration to provide the right instructions for the current state of the conversation.

<Tabs>
  <Tab title="State">
    Access message count or conversation context from state:

<Tab title="Store">
    Access user preferences from long-term memory:

<Tab title="Runtime Context">
    Access user ID or configuration from Runtime Context:

Messages make up the prompt that is sent to the LLM.
It's critical to manage the content of messages to ensure that the LLM has the right information to respond well.

<Tabs>
  <Tab title="State">
    Inject uploaded file context from State when relevant to current query:

<Tab title="Store">
    Inject user's email writing style from Store to guide drafting:

<Tab title="Runtime Context">
    Inject compliance rules from Runtime Context based on user's jurisdiction:

<Note>
  **Transient vs Persistent Message Updates:**

The examples above use `wrap_model_call` to make **transient** updates - modifying what messages are sent to the model for a single call without changing what's saved in state.

For **persistent** updates that modify state (like the summarization example in [Life-cycle Context](#summarization)), use life-cycle hooks like `before_model` or `after_model` to permanently update the conversation history. See the [middleware documentation](/oss/python/langchain/middleware) for more details.
</Note>

Tools let the model interact with databases, APIs, and external systems. How you define and select tools directly impacts whether the model can complete tasks effectively.

Each tool needs a clear name, description, argument names, and argument descriptions. These aren't just metadata—they guide the model's reasoning about when and how to use the tool.

Not every tool is appropriate for every situation. Too many tools may overwhelm the model (overload context) and increase errors; too few limit capabilities. Dynamic tool selection adapts the available toolset based on authentication state, user permissions, feature flags, or conversation stage.

<Tabs>
  <Tab title="State">
    Enable advanced tools only after certain conversation milestones:

<Tab title="Store">
    Filter tools based on user preferences or feature flags in Store:

<Tab title="Runtime Context">
    Filter tools based on user permissions from Runtime Context:

See [Dynamically selecting tools](/oss/python/langchain/middleware#dynamically-selecting-tools) for more examples.

Different models have different strengths, costs, and context windows. Select the right model for the task at hand, which
might change during an agent run.

<Tabs>
  <Tab title="State">
    Use different models based on conversation length from State:

<Tab title="Store">
    Use user's preferred model from Store:

<Tab title="Runtime Context">
    Select model based on cost limits or environment from Runtime Context:

See [Dynamic model](/oss/python/langchain/agents#dynamic-model) for more examples.

Structured output transforms unstructured text into validated, structured data. When extracting specific fields or returning data for downstream systems, free-form text isn't sufficient.

**How it works:** When you provide a schema as the response format, the model's final response is guaranteed to conform to that schema. The agent runs the model / tool calling loop until the model is done calling tools, then the final response is coerced into the provided format.

#### Defining formats

Schema definitions guide the model. Field names, types, and descriptions specify exactly what format the output should adhere to.

#### Selecting formats

Dynamic response format selection adapts schemas based on user preferences, conversation stage, or role—returning simple formats early and detailed formats as complexity increases.

<Tabs>
  <Tab title="State">
    Configure structured output based on conversation state:

<Tab title="Store">
    Configure output format based on user preferences in Store:

<Tab title="Runtime Context">
    Configure output format based on Runtime Context like user role or environment:

Tools are special in that they both read and write context.

In the most basic case, when a tool executes, it receives the LLM's request parameters and returns a tool message back. The tool does its work and produces a result.

Tools can also fetch important information for the model that allows it to perform and complete tasks.

Most real-world tools need more than just the LLM's parameters. They need user IDs for database queries, API keys for external services, or current session state to make decisions. Tools read from state, store, and runtime context to access this information.

<Tabs>
  <Tab title="State">
    Read from State to check current session information:

<Tab title="Store">
    Read from Store to access persisted user preferences:

<Tab title="Runtime Context">
    Read from Runtime Context for configuration like API keys and user IDs:

Tool results can be used to help an agent complete a given task. Tools can both return results directly to the model
and update the memory of the agent to make important context available to future steps.

<Tabs>
  <Tab title="State">
    Write to State to track session-specific information using Command:

<Tab title="Store">
    Write to Store to persist data across sessions:

See [Tools](/oss/python/langchain/tools) for comprehensive examples of accessing state, store, and runtime context in tools.

## Life-cycle Context

Control what happens **between** the core agent steps - intercepting data flow to implement cross-cutting concerns like summarization, guardrails, and logging.

As you've seen in [Model Context](#model-context) and [Tool Context](#tool-context), [middleware](/oss/python/langchain/middleware) is the mechanism that makes context engineering practical. Middleware allows you to hook into any step in the agent lifecycle and either:

1. **Update context** - Modify state and store to persist changes, update conversation history, or save insights
2. **Jump in the lifecycle** - Move to different steps in the agent cycle based on context (e.g., skip tool execution if a condition is met, repeat model call with modified context)

<div style={{ display: "flex", justifyContent: "center" }}>
  <img src="https://mintcdn.com/langchain-5e9cc07a/RAP6mjwE5G00xYsA/oss/images/middleware_final.png?fit=max&auto=format&n=RAP6mjwE5G00xYsA&q=85&s=eb4404b137edec6f6f0c8ccb8323eaf1" alt="Middleware hooks in the agent loop" className="rounded-lg" data-og-width="500" width="500" data-og-height="560" height="560" data-path="oss/images/middleware_final.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/RAP6mjwE5G00xYsA/oss/images/middleware_final.png?w=280&fit=max&auto=format&n=RAP6mjwE5G00xYsA&q=85&s=483413aa87cf93323b0f47c0dd5528e8 280w, https://mintcdn.com/langchain-5e9cc07a/RAP6mjwE5G00xYsA/oss/images/middleware_final.png?w=560&fit=max&auto=format&n=RAP6mjwE5G00xYsA&q=85&s=41b7dd647447978ff776edafe5f42499 560w, https://mintcdn.com/langchain-5e9cc07a/RAP6mjwE5G00xYsA/oss/images/middleware_final.png?w=840&fit=max&auto=format&n=RAP6mjwE5G00xYsA&q=85&s=e9b14e264f68345de08ae76f032c52d4 840w, https://mintcdn.com/langchain-5e9cc07a/RAP6mjwE5G00xYsA/oss/images/middleware_final.png?w=1100&fit=max&auto=format&n=RAP6mjwE5G00xYsA&q=85&s=ec45e1932d1279b1beee4a4b016b473f 1100w, https://mintcdn.com/langchain-5e9cc07a/RAP6mjwE5G00xYsA/oss/images/middleware_final.png?w=1650&fit=max&auto=format&n=RAP6mjwE5G00xYsA&q=85&s=3bca5ebf8aa56632b8a9826f7f112e57 1650w, https://mintcdn.com/langchain-5e9cc07a/RAP6mjwE5G00xYsA/oss/images/middleware_final.png?w=2500&fit=max&auto=format&n=RAP6mjwE5G00xYsA&q=85&s=437f141d1266f08a95f030c2804691d9 2500w" />
</div>

### Example: Summarization

One of the most common life-cycle patterns is automatically condensing conversation history when it gets too long. Unlike the transient message trimming shown in [Model Context](#messages), summarization **persistently updates state** - permanently replacing old messages with a summary that's saved for all future turns.

LangChain offers built-in middleware for this:

When the conversation exceeds the token limit, `SummarizationMiddleware` automatically:

1. Summarizes older messages using a separate LLM call
2. Replaces them with a summary message in State (permanently)
3. Keeps recent messages intact for context

The summarized conversation history is permanently updated - future turns will see the summary instead of the original messages.

<Note>
  For a complete list of built-in middleware, available hooks, and how to create custom middleware, see the [Middleware documentation](/oss/python/langchain/middleware).
</Note>

1. **Start simple** - Begin with static prompts and tools, add dynamics only when needed
2. **Test incrementally** - Add one context engineering feature at a time
3. **Monitor performance** - Track model calls, token usage, and latency
4. **Use built-in middleware** - Leverage [`SummarizationMiddleware`](/oss/python/langchain/middleware#summarization), [`LLMToolSelectorMiddleware`](/oss/python/langchain/middleware#llm-tool-selector), etc.
5. **Document your context strategy** - Make it clear what context is being passed and why
6. **Understand transient vs persistent**: Model context changes are transient (per-call), while life-cycle context changes persist to state

* [Context conceptual overview](/oss/python/concepts/context) - Understand context types and when to use them
* [Middleware](/oss/python/langchain/middleware) - Complete middleware guide
* [Tools](/oss/python/langchain/tools) - Tool creation and context access
* [Memory](/oss/python/concepts/memory) - Short-term and long-term memory patterns
* [Agents](/oss/python/langchain/agents) - Core agent concepts

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/context-engineering.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

**Examples:**

Example 1 (unknown):
```unknown
</Tab>

  <Tab title="Store">
    Access user preferences from long-term memory:
```

Example 2 (unknown):
```unknown
</Tab>

  <Tab title="Runtime Context">
    Access user ID or configuration from Runtime Context:
```

Example 3 (unknown):
```unknown
</Tab>
</Tabs>

### Messages

Messages make up the prompt that is sent to the LLM.
It's critical to manage the content of messages to ensure that the LLM has the right information to respond well.

<Tabs>
  <Tab title="State">
    Inject uploaded file context from State when relevant to current query:
```

Example 4 (unknown):
```unknown
</Tab>

  <Tab title="Store">
    Inject user's email writing style from Store to guide drafting:
```

---

## Workflows and agents

**URL:** llms-txt#workflows-and-agents

**Contents:**
- Setup
- LLMs and augmentations

Source: https://docs.langchain.com/oss/python/langgraph/workflows-agents

This guide reviews common workflow and agent patterns.

* Workflows have predetermined code paths and are designed to operate in a certain order.
* Agents are dynamic and define their own processes and tool usage.

<img src="https://mintcdn.com/langchain-5e9cc07a/-_xGPoyjhyiDWTPJ/oss/images/agent_workflow.png?fit=max&auto=format&n=-_xGPoyjhyiDWTPJ&q=85&s=c217c9ef517ee556cae3fc928a21dc55" alt="Agent Workflow" data-og-width="4572" width="4572" data-og-height="2047" height="2047" data-path="oss/images/agent_workflow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/-_xGPoyjhyiDWTPJ/oss/images/agent_workflow.png?w=280&fit=max&auto=format&n=-_xGPoyjhyiDWTPJ&q=85&s=290e50cff2f72d524a107421ec8e3ff0 280w, https://mintcdn.com/langchain-5e9cc07a/-_xGPoyjhyiDWTPJ/oss/images/agent_workflow.png?w=560&fit=max&auto=format&n=-_xGPoyjhyiDWTPJ&q=85&s=a2bfc87080aee7dd4844f7f24035825e 560w, https://mintcdn.com/langchain-5e9cc07a/-_xGPoyjhyiDWTPJ/oss/images/agent_workflow.png?w=840&fit=max&auto=format&n=-_xGPoyjhyiDWTPJ&q=85&s=ae1fa9087b33b9ff8bc3446ccaa23e3d 840w, https://mintcdn.com/langchain-5e9cc07a/-_xGPoyjhyiDWTPJ/oss/images/agent_workflow.png?w=1100&fit=max&auto=format&n=-_xGPoyjhyiDWTPJ&q=85&s=06003ee1fe07d7a1ea8cf9200e7d0a10 1100w, https://mintcdn.com/langchain-5e9cc07a/-_xGPoyjhyiDWTPJ/oss/images/agent_workflow.png?w=1650&fit=max&auto=format&n=-_xGPoyjhyiDWTPJ&q=85&s=bc98b459a9b1fb226c2887de1696bde0 1650w, https://mintcdn.com/langchain-5e9cc07a/-_xGPoyjhyiDWTPJ/oss/images/agent_workflow.png?w=2500&fit=max&auto=format&n=-_xGPoyjhyiDWTPJ&q=85&s=1933bcdfd5c5b69b98ce96aafa456848 2500w" />

LangGraph offers several benefits when building agents and workflows, including [persistence](/oss/python/langgraph/persistence), [streaming](/oss/python/langgraph/streaming), and support for debugging as well as [deployment](/oss/python/langgraph/deploy).

To build a workflow or agent, you can use [any chat model](/oss/python/integrations/chat) that supports structured outputs and tool calling. The following example uses Anthropic:

1. Install dependencies:

2. Initialize the LLM:

## LLMs and augmentations

Workflows and agentic systems are based on LLMs and the various augmentations you add to them. [Tool calling](/oss/python/langchain/tools), [structured outputs](/oss/python/langchain/structured-output), and [short term memory](/oss/python/langchain/short-term-memory) are a few options for tailoring LLMs to your needs.

<img src="https://mintcdn.com/langchain-5e9cc07a/-_xGPoyjhyiDWTPJ/oss/images/augmented_llm.png?fit=max&auto=format&n=-_xGPoyjhyiDWTPJ&q=85&s=7ea9656f46649b3ebac19e8309ae9006" alt="LLM augmentations" data-og-width="1152" width="1152" data-og-height="778" height="778" data-path="oss/images/augmented_llm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/-_xGPoyjhyiDWTPJ/oss/images/augmented_llm.png?w=280&fit=max&auto=format&n=-_xGPoyjhyiDWTPJ&q=85&s=53613048c1b8bd3241bd27900a872ead 280w, https://mintcdn.com/langchain-5e9cc07a/-_xGPoyjhyiDWTPJ/oss/images/augmented_llm.png?w=560&fit=max&auto=format&n=-_xGPoyjhyiDWTPJ&q=85&s=7ba1f4427fd847bd410541ae38d66d40 560w, https://mintcdn.com/langchain-5e9cc07a/-_xGPoyjhyiDWTPJ/oss/images/augmented_llm.png?w=840&fit=max&auto=format&n=-_xGPoyjhyiDWTPJ&q=85&s=503822cf29a28500deb56f463b4244e4 840w, https://mintcdn.com/langchain-5e9cc07a/-_xGPoyjhyiDWTPJ/oss/images/augmented_llm.png?w=1100&fit=max&auto=format&n=-_xGPoyjhyiDWTPJ&q=85&s=279e0440278d3a26b73c72695636272e 1100w, https://mintcdn.com/langchain-5e9cc07a/-_xGPoyjhyiDWTPJ/oss/images/augmented_llm.png?w=1650&fit=max&auto=format&n=-_xGPoyjhyiDWTPJ&q=85&s=d936838b98bc9dce25168e2b2cfd23d0 1650w, https://mintcdn.com/langchain-5e9cc07a/-_xGPoyjhyiDWTPJ/oss/images/augmented_llm.png?w=2500&fit=max&auto=format&n=-_xGPoyjhyiDWTPJ&q=85&s=fa2115f972bc1152b5e03ae590600fa3 2500w" />

```python  theme={null}

**Examples:**

Example 1 (unknown):
```unknown
2. Initialize the LLM:
```

Example 2 (unknown):
```unknown
## LLMs and augmentations

Workflows and agentic systems are based on LLMs and the various augmentations you add to them. [Tool calling](/oss/python/langchain/tools), [structured outputs](/oss/python/langchain/structured-output), and [short term memory](/oss/python/langchain/short-term-memory) are a few options for tailoring LLMs to your needs.

<img src="https://mintcdn.com/langchain-5e9cc07a/-_xGPoyjhyiDWTPJ/oss/images/augmented_llm.png?fit=max&auto=format&n=-_xGPoyjhyiDWTPJ&q=85&s=7ea9656f46649b3ebac19e8309ae9006" alt="LLM augmentations" data-og-width="1152" width="1152" data-og-height="778" height="778" data-path="oss/images/augmented_llm.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/-_xGPoyjhyiDWTPJ/oss/images/augmented_llm.png?w=280&fit=max&auto=format&n=-_xGPoyjhyiDWTPJ&q=85&s=53613048c1b8bd3241bd27900a872ead 280w, https://mintcdn.com/langchain-5e9cc07a/-_xGPoyjhyiDWTPJ/oss/images/augmented_llm.png?w=560&fit=max&auto=format&n=-_xGPoyjhyiDWTPJ&q=85&s=7ba1f4427fd847bd410541ae38d66d40 560w, https://mintcdn.com/langchain-5e9cc07a/-_xGPoyjhyiDWTPJ/oss/images/augmented_llm.png?w=840&fit=max&auto=format&n=-_xGPoyjhyiDWTPJ&q=85&s=503822cf29a28500deb56f463b4244e4 840w, https://mintcdn.com/langchain-5e9cc07a/-_xGPoyjhyiDWTPJ/oss/images/augmented_llm.png?w=1100&fit=max&auto=format&n=-_xGPoyjhyiDWTPJ&q=85&s=279e0440278d3a26b73c72695636272e 1100w, https://mintcdn.com/langchain-5e9cc07a/-_xGPoyjhyiDWTPJ/oss/images/augmented_llm.png?w=1650&fit=max&auto=format&n=-_xGPoyjhyiDWTPJ&q=85&s=d936838b98bc9dce25168e2b2cfd23d0 1650w, https://mintcdn.com/langchain-5e9cc07a/-_xGPoyjhyiDWTPJ/oss/images/augmented_llm.png?w=2500&fit=max&auto=format&n=-_xGPoyjhyiDWTPJ&q=85&s=fa2115f972bc1152b5e03ae590600fa3 2500w" />
```

---

## Build a custom RAG agent

**URL:** llms-txt#build-a-custom-rag-agent

**Contents:**
- Overview
  - Concepts
- Setup
- 1. Preprocess documents
- 2. Create a retriever tool
- 3. Generate query
- 4. Grade documents
- 5. Rewrite question
- 6. Generate an answer
- 7. Assemble the graph

Source: https://docs.langchain.com/oss/python/langgraph/agentic-rag

In this tutorial we will build a [retrieval](/oss/python/langchain/retrieval) agent using LangGraph.

LangChain offers built-in [agent](/oss/python/langchain/agents) implementations, implemented using [LangGraph](/oss/python/langgraph/overview) primitives. If deeper customization is required, agents can be implemented directly in LangGraph. This guide demonstrates an example implementation of a retrieval agent. [Retrieval](/oss/python/langchain/retrieval) agents are useful when you want an LLM to make a decision about whether to retrieve context from a vectorstore or respond to the user directly.

By the end of the tutorial we will have done the following:

1. Fetch and preprocess documents that will be used for retrieval.
2. Index those documents for semantic search and create a retriever tool for the agent.
3. Build an agentic RAG system that can decide when to use the retriever tool.

<img src="https://mintcdn.com/langchain-5e9cc07a/I6RpA28iE233vhYX/images/langgraph-hybrid-rag-tutorial.png?fit=max&auto=format&n=I6RpA28iE233vhYX&q=85&s=855348219691485642b22a1419939ea7" alt="Hybrid RAG" data-og-width="1615" width="1615" data-og-height="589" height="589" data-path="images/langgraph-hybrid-rag-tutorial.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/I6RpA28iE233vhYX/images/langgraph-hybrid-rag-tutorial.png?w=280&fit=max&auto=format&n=I6RpA28iE233vhYX&q=85&s=09097cb9a1dc57b16d33f084641ea93f 280w, https://mintcdn.com/langchain-5e9cc07a/I6RpA28iE233vhYX/images/langgraph-hybrid-rag-tutorial.png?w=560&fit=max&auto=format&n=I6RpA28iE233vhYX&q=85&s=d0bf85cfa36ac7e1a905593a4688f2d2 560w, https://mintcdn.com/langchain-5e9cc07a/I6RpA28iE233vhYX/images/langgraph-hybrid-rag-tutorial.png?w=840&fit=max&auto=format&n=I6RpA28iE233vhYX&q=85&s=b7626e6ae3cb94fb90a61e6fad69c8ba 840w, https://mintcdn.com/langchain-5e9cc07a/I6RpA28iE233vhYX/images/langgraph-hybrid-rag-tutorial.png?w=1100&fit=max&auto=format&n=I6RpA28iE233vhYX&q=85&s=2425baddda7209901bdde4425c23292c 1100w, https://mintcdn.com/langchain-5e9cc07a/I6RpA28iE233vhYX/images/langgraph-hybrid-rag-tutorial.png?w=1650&fit=max&auto=format&n=I6RpA28iE233vhYX&q=85&s=4e5f030034237589f651b704d0377a76 1650w, https://mintcdn.com/langchain-5e9cc07a/I6RpA28iE233vhYX/images/langgraph-hybrid-rag-tutorial.png?w=2500&fit=max&auto=format&n=I6RpA28iE233vhYX&q=85&s=3ec3c7c91fd2be4d749b1c267027ac1e 2500w" />

We will cover the following concepts:

* [Retrieval](/oss/python/langchain/retrieval) using [document loaders](/oss/python/integrations/document_loaders), [text splitters](/oss/python/integrations/splitters), [embeddings](/oss/python/integrations/text_embedding), and [vector stores](/oss/python/integrations/vectorstores)
* The LangGraph [Graph API](/oss/python/langgraph/graph-api), including state, nodes, edges, and conditional edges.

Let's download the required packages and set our API keys:

<Tip>
  Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. [LangSmith](https://docs.smith.langchain.com) lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph.
</Tip>

## 1. Preprocess documents

1. Fetch documents to use in our RAG system. We will use three of the most recent pages from [Lilian Weng's excellent blog](https://lilianweng.github.io/). We'll start by fetching the content of the pages using `WebBaseLoader` utility:

2. Split the fetched documents into smaller chunks for indexing into our vectorstore:

## 2. Create a retriever tool

Now that we have our split documents, we can index them into a vector store that we'll use for semantic search.

1. Use an in-memory vector store and OpenAI embeddings:

2. Create a retriever tool using LangChain's prebuilt `create_retriever_tool`:

Now we will start building components ([nodes](/oss/python/langgraph/graph-api#nodes) and [edges](/oss/python/langgraph/graph-api#edges)) for our agentic RAG graph.

Note that the components will operate on the [`MessagesState`](/oss/python/langgraph/graph-api#messagesstate) — graph state that contains a `messages` key with a list of [chat messages](https://python.langchain.com/docs/concepts/messages/).

1. Build a `generate_query_or_respond` node. It will call an LLM to generate a response based on the current graph state (list of messages). Given the input messages, it will decide to retrieve using the retriever tool, or respond directly to the user. Note that we're giving the chat model access to the `retriever_tool` we created earlier via `.bind_tools`:

2. Try it on a random input:

3. Ask a question that requires semantic search:

## 4. Grade documents

1. Add a [conditional edge](/oss/python/langgraph/graph-api#conditional-edges) — `grade_documents` — to determine whether the retrieved documents are relevant to the question. We will use a model with a structured output schema `GradeDocuments` for document grading. The `grade_documents` function will return the name of the node to go to based on the grading decision (`generate_answer` or `rewrite_question`):

2. Run this with irrelevant documents in the tool response:

3. Confirm that the relevant documents are classified as such:

## 5. Rewrite question

1. Build the `rewrite_question` node. The retriever tool can return potentially irrelevant documents, which indicates a need to improve the original user question. To do so, we will call the `rewrite_question` node:

## 6. Generate an answer

1. Build `generate_answer` node: if we pass the grader checks, we can generate the final answer based on the original question and the retrieved context:

## 7. Assemble the graph

Now we'll assemble all the nodes and edges into a complete graph:

* Start with a `generate_query_or_respond` and determine if we need to call `retriever_tool`
* Route to next step using `tools_condition`:
  * If `generate_query_or_respond` returned `tool_calls`, call `retriever_tool` to retrieve context
  * Otherwise, respond directly to the user
* Grade retrieved document content for relevance to the question (`grade_documents`) and route to next step:
  * If not relevant, rewrite the question using `rewrite_question` and then call `generate_query_or_respond` again
  * If relevant, proceed to `generate_answer` and generate final response using the [`ToolMessage`](https://reference.langchain.com/python/langchain/messages/#langchain.messages.ToolMessage) with the retrieved document context

```python  theme={null}
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition

workflow = StateGraph(MessagesState)

**Examples:**

Example 1 (unknown):
```unknown

```

Example 2 (unknown):
```unknown
<Tip>
  Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. [LangSmith](https://docs.smith.langchain.com) lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph.
</Tip>

## 1. Preprocess documents

1. Fetch documents to use in our RAG system. We will use three of the most recent pages from [Lilian Weng's excellent blog](https://lilianweng.github.io/). We'll start by fetching the content of the pages using `WebBaseLoader` utility:
```

Example 3 (unknown):
```unknown

```

Example 4 (unknown):
```unknown
2. Split the fetched documents into smaller chunks for indexing into our vectorstore:
```

---

## Define your tasks

**URL:** llms-txt#define-your-tasks

research_task = Task(
    description="""Conduct comprehensive research on the current state of AI adoption
    in small to medium businesses. Focus on:
    1. Current adoption rates and trends
    2. Main barriers to adoption
    3. Most popular AI tools and use cases
    4. ROI and business impact metrics

Provide a detailed analysis with supporting data and statistics.""",
    agent=market_researcher,
    expected_output="A comprehensive market research report on AI adoption in SMBs with data, trends, and insights.",
)

analysis_task = Task(
    description="""Analyze the research findings and identify key statistical patterns.
    Create data visualizations and provide quantitative insights on:
    1. Adoption rate trends over time
    2. Industry-specific adoption patterns
    3. ROI correlation analysis
    4. Barrier impact assessment

Present findings in a clear, data-driven format.""",
    agent=data_analyst,
    expected_output="Statistical analysis report with key metrics, trends, and data-driven insights.",
    context=[research_task],
)

content_task = Task(
    description="""Based on the research and analysis, create a compelling marketing
    strategy document that includes:
    1. Executive summary of key findings
    2. Target audience personas based on adoption patterns
    3. Key messaging framework addressing main barriers
    4. Content recommendations for different business segments
    5. Campaign strategy to drive AI adoption

Make the content actionable and business-focused.""",
    agent=content_strategist,
    expected_output="Complete marketing strategy document with personas, messaging, and campaign recommendations.",
    context=[research_task, analysis_task],
)

---

## Use instead

**URL:** llms-txt#use-instead

**Contents:**
  - Tools
  - Structured output
  - Streaming node name rename
  - Runtime context
- Standard content
  - What changed
  - Read standardized content
  - Create multimodal messages
  - Example block shapes

agent = create_agent("openai:gpt-4o-mini", tools=[some_tool])
python v1 (new) theme={null}
  from langchain.agents import create_agent

agent = create_agent(
      model="anthropic:claude-sonnet-4-5",
      tools=[check_weather, search_web]
  )
  python v0 (old) theme={null}
  from langgraph.prebuilt import create_react_agent, ToolNode

agent = create_react_agent(
      model="anthropic:claude-sonnet-4-5",
      tools=ToolNode([check_weather, search_web]) # [!code highlight]
  )
  python v1 (new) theme={null}
  # Example coming soon
  python v0 (old) theme={null}
  # Example coming soon
  python v1 (new) theme={null}
  from langchain.agents import create_agent
  from langchain.agents.structured_output import ToolStrategy, ProviderStrategy
  from pydantic import BaseModel

class OutputSchema(BaseModel):
      summary: str
      sentiment: str

# Using ToolStrategy
  agent = create_agent(
      model="openai:gpt-4o-mini",
      tools=tools,
      # explicitly using tool strategy
      response_format=ToolStrategy(OutputSchema)  # [!code highlight]
  )
  python v0 (old) theme={null}
  from langgraph.prebuilt import create_react_agent
  from pydantic import BaseModel

class OutputSchema(BaseModel):
      summary: str
      sentiment: str

agent = create_react_agent(
      model="openai:gpt-4o-mini",
      tools=tools,
      # using tool strategy by default with no option for provider strategy
      response_format=OutputSchema  # [!code highlight]
  )

agent = create_react_agent(
      model="openai:gpt-4o-mini",
      tools=tools,
      # using a custom prompt to instruct the model to generate the output schema
      response_format=("please generate ...", OutputSchema)  # [!code highlight]
  )
  python v1 (new) theme={null}
  from dataclasses import dataclass

from langchain.agents import create_agent

@dataclass
  class Context:
      user_id: str
      session_id: str

agent = create_agent(
      model=model,
      tools=tools,
      context_schema=ContextSchema  # [!code highlight]
  )

result = agent.invoke(
      {"messages": [{"role": "user", "content": "Hello"}]},
      context=Context(user_id="123", session_id="abc")  # [!code highlight]
  )
  python v0 (old) theme={null}
  from langgraph.prebuilt import create_react_agent

agent = create_react_agent(model, tools)

# Pass context via configurable
  result = agent.invoke(
      {"messages": [{"role": "user", "content": "Hello"}]},
      config={  # [!code highlight]
          "configurable": {  # [!code highlight]
              "user_id": "123",  # [!code highlight]
              "session_id": "abc"  # [!code highlight]
          }  # [!code highlight]
      }  # [!code highlight]
  )
  python v1 (new) theme={null}
  from langchain.chat_models import init_chat_model

model = init_chat_model("openai:gpt-5-nano")
  response = model.invoke("Explain AI")

for block in response.content_blocks:
      if block["type"] == "reasoning":
          print(block.get("reasoning"))
      elif block["type"] == "text":
          print(block.get("text"))
  python v0 (old) theme={null}
  # Provider-native formats vary; you needed per-provider handling
  response = model.invoke("Explain AI")
  for item in response.content:
      if item.get("type") == "reasoning":
          ...  # OpenAI-style reasoning
      elif item.get("type") == "thinking":
          ...  # Anthropic-style thinking
      elif item.get("type") == "text":
          ...  # Text
  python v1 (new) theme={null}
  from langchain.messages import HumanMessage

message = HumanMessage(content_blocks=[
      {"type": "text", "text": "Describe this image."},
      {"type": "image", "url": "https://example.com/image.jpg"},
  ])
  res = model.invoke([message])
  python v0 (old) theme={null}
  from langchain.messages import HumanMessage

message = HumanMessage(content=[
      # Provider-native structure
      {"type": "text", "text": "Describe this image."},
      {"type": "image_url", "image_url": {"url": "https://example.com/image.jpg"}},
  ])
  res = model.invoke([message])
  python  theme={null}

**Examples:**

Example 1 (unknown):
```unknown
<Note>
  Dynamic model functions can return pre-bound models if structured output is *not* used.
</Note>

### Tools

The [`tools`](https://reference.langchain.com/python/langchain/agents/#langchain.agents.create_agent\(tools\)) argument to [`create_agent`](https://reference.langchain.com/python/langchain/agents/#langchain.agents.create_agent) accepts a list of:

* LangChain [`BaseTool`](https://reference.langchain.com/python/langchain/tools/#langchain.tools.BaseTool) instances (functions decorated with [`@tool`](https://reference.langchain.com/python/langchain/tools/#langchain.tools.tool))
* Callable objects (functions) with proper type hints and a docstring
* `dict` that represents a built-in provider tools

The argument will no longer accept [`ToolNode`](https://reference.langchain.com/python/langgraph/agents/#langgraph.prebuilt.tool_node.ToolNode) instances.

<CodeGroup>
```

Example 2 (unknown):
```unknown

```

Example 3 (unknown):
```unknown
</CodeGroup>

#### Handling tool errors

You can now configure the handling of tool errors with middleware implementing the `wrap_tool_call` method.

<CodeGroup>
```

Example 4 (unknown):
```unknown

```

---

## Setup claude_agent_sdk with langsmith tracing

**URL:** llms-txt#setup-claude_agent_sdk-with-langsmith-tracing

configure_claude_agent_sdk()

@tool(
    "get_weather",
    "Gets the current weather for a given city",
    {
        "city": str,
    },
)
async def get_weather(args: dict[str, Any]) -> dict[str, Any]:
    """Simulated weather lookup tool"""
    city = args["city"]

# Simulated weather data
    weather_data = {
        "San Francisco": "Foggy, 62°F",
        "New York": "Sunny, 75°F",
        "London": "Rainy, 55°F",
        "Tokyo": "Clear, 68°F",
    }

weather = weather_data.get(city, "Weather data not available")
    return {"content": [{"type": "text", "text": f"Weather in {city}: {weather}"}]}

async def main():
    # Create SDK MCP server with the weather tool
    weather_server = create_sdk_mcp_server(
        name="weather",
        version="1.0.0",
        tools=[get_weather],
    )

options = ClaudeAgentOptions(
        model="claude-sonnet-4-5",
        system_prompt="You are a friendly travel assistant who helps with weather information.",
        mcp_servers={"weather": weather_server},
        allowed_tools=["mcp__weather__get_weather"],
    )

async with ClaudeSDKClient(options=options) as client:
        await client.query("What's the weather like in San Francisco and Tokyo?")

async for message in client.receive_response():
            print(message)

if __name__ == "__main__":
    asyncio.run(main())
```

Once configured, all Claude Agent SDK operations will be automatically traced to LangSmith, including:

* Agent queries and responses
* Tool invocations and results
* Claude model interactions
* MCP server operations

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-claude-agent-sdk.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

---

## Tools and toolkits

**URL:** llms-txt#tools-and-toolkits

**Contents:**
- Search
- Code Interpreter
- Productivity
- Web Browsing
- Database
- Finance
- Integration Platforms
- All tools and toolkits

Source: https://docs.langchain.com/oss/python/integrations/tools/index

[Tools](/oss/python/langchain/tools) are utilities designed to be called by a model: their inputs are designed to be generated by models, and their outputs are designed to be passed back to models.

A toolkit is a collection of tools meant to be used together.

The following table shows tools that execute online searches in some shape or form:

| Tool/Toolkit                                                  | Free/Paid                    | Return Data                                           |
| ------------------------------------------------------------- | ---------------------------- | ----------------------------------------------------- |
| [Bing Search](/oss/python/integrations/tools/bing_search)     | Paid                         | URL, Snippet, Title                                   |
| [Brave Search](/oss/python/integrations/tools/brave_search)   | Free                         | URL, Snippet, Title                                   |
| [DuckDuckgoSearch](/oss/python/integrations/tools/ddg)        | Free                         | URL, Snippet, Title                                   |
| [Exa Search](/oss/python/integrations/tools/exa_search)       | 1000 free searches/month     | URL, Author, Title, Published Date                    |
| [Google Search](/oss/python/integrations/tools/google_search) | Paid                         | URL, Snippet, Title                                   |
| [Google Serper](/oss/python/integrations/tools/google_serper) | Free                         | URL, Snippet, Title, Search Rank, Site Links          |
| [Jina Search](/oss/python/integrations/tools/jina_search)     | 1M Response Tokens Free      | URL, Snippet, Title, Page Content                     |
| [Mojeek Search](/oss/python/integrations/tools/mojeek_search) | Paid                         | URL, Snippet, Title                                   |
| [SearchApi](/oss/python/integrations/tools/searchapi)         | 100 Free Searches on Sign Up | URL, Snippet, Title, Search Rank, Site Links, Authors |
| [SearxNG Search](/oss/python/integrations/tools/searx_search) | Free                         | URL, Snippet, Title, Category                         |
| [SerpAPI](/oss/python/integrations/tools/serpapi)             | 100 Free Searches/Month      | Answer                                                |
| [Tavily Search](/oss/python/integrations/tools/tavily_search) | 1000 free searches/month     | URL, Content, Title, Images, Answer                   |
| [You.com Search](/oss/python/integrations/tools/you)          | Free for 60 days             | URL, Title, Page Content                              |

The following table shows tools that can be used as code interpreters:

| Tool/Toolkit                                                                                   | Supported Languages           | Sandbox Lifetime    | Supports File Uploads | Return Types | Supports Self-Hosting |
| ---------------------------------------------------------------------------------------------- | ----------------------------- | ------------------- | --------------------- | ------------ | --------------------- |
| [Azure Container Apps dynamic sessions](/oss/python/integrations/tools/azure_dynamic_sessions) | Python                        | 1 Hour              | ✅                     | Text, Images | ❌                     |
| [Bearly Code Interpreter](/oss/python/integrations/tools/bearly)                               | Python                        | Resets on Execution | ✅                     | Text         | ❌                     |
| [Riza Code Interpreter](/oss/python/integrations/tools/riza)                                   | Python, JavaScript, PHP, Ruby | Resets on Execution | ✅                     | Text         | ✅                     |

The following table shows tools that can be used to automate tasks in productivity tools:

| Tool/Toolkit                                                  | Pricing                                                                                                |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| [Github Toolkit](/oss/python/integrations/tools/github)       | Free                                                                                                   |
| [Gitlab Toolkit](/oss/python/integrations/tools/gitlab)       | Free for personal project                                                                              |
| [Gmail Toolkit](/oss/python/integrations/tools/gmail)         | Free, with limit of 250 quota units per user per second                                                |
| [Infobip Tool](/oss/python/integrations/tools/infobip)        | Free trial, with variable pricing after                                                                |
| [Jira Toolkit](/oss/python/integrations/tools/jira)           | Free, with [rate limits](https://developer.atlassian.com/cloud/jira/platform/rate-limiting/)           |
| [Office365 Toolkit](/oss/python/integrations/tools/office365) | Free with Office365, includes [rate limits](https://learn.microsoft.com/en-us/graph/throttling-limits) |
| [Slack Toolkit](/oss/python/integrations/tools/slack)         | Free                                                                                                   |
| [Twilio Tool](/oss/python/integrations/tools/twilio)          | Free trial, with [pay-as-you-go pricing](https://www.twilio.com/en-us/pricing) after                   |

The following table shows tools that can be used to automate tasks in web browsers:

| Tool/Toolkit                                                                                        | Pricing                                                     | Supports Interacting with the Browser |
| --------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ------------------------------------- |
| [AgentQL Toolkit](/oss/python/integrations/tools/agentql)                                           | Free trial, with pay-as-you-go and flat rate plans after    | ✅                                     |
| [Hyperbrowser Browser Agent Tools](/oss/python/integrations/tools/hyperbrowser_browser_agent_tools) | Free trial, with flat rate plans and pre-paid credits after | ✅                                     |
| [Hyperbrowser Web Scraping Tools](/oss/python/integrations/tools/hyperbrowser_web_scraping_tools)   | Free trial, with flat rate plans and pre-paid credits after | ❌                                     |
| [MultiOn Toolkit](/oss/python/integrations/tools/multion)                                           | 40 free requests/day                                        | ✅                                     |
| [Oxylabs Web Scraper API](/oss/python/integrations/tools/oxylabs)                                   | Free trial, with flat rate plans and pre-paid credits after | ❌                                     |
| [PlayWright Browser Toolkit](/oss/python/integrations/tools/playwright)                             | Free                                                        | ✅                                     |
| [Requests Toolkit](/oss/python/integrations/tools/requests)                                         | Free                                                        | ❌                                     |

The following table shows tools that can be used to automate tasks in databases:

| Tool/Toolkit                                                                    | Allowed Operations              |
| ------------------------------------------------------------------------------- | ------------------------------- |
| [Cassandra Database Toolkit](/oss/python/integrations/tools/cassandra_database) | SELECT and schema introspection |
| [MCP Toolbox](/oss/python/integrations/tools/toolbox)                           | Any SQL operation               |
| [SQLDatabase Toolkit](/oss/python/integrations/tools/sql_database)              | Any SQL operation               |
| [Spark SQL Toolkit](/oss/python/integrations/tools/spark_sql)                   | Any SQL operation               |

The following table shows tools that can be used to execute financial transactions such as payments, purchases, and more:

| Tool/Toolkit                                  | Pricing | Capabilities                                                                      |
| --------------------------------------------- | ------- | --------------------------------------------------------------------------------- |
| [GOAT](/oss/python/integrations/tools/goat)   | Free    | Create and receive payments, purchase physical goods, make investments, and more. |
| [Privy](/oss/python/integrations/tools/privy) | Free    | Create wallets with configurable permissions and execute transactions with speed. |

## Integration Platforms

The following platforms provide access to multiple tools and services through a unified interface:

| Tool/Toolkit                                        | Number of Integrations | Pricing             | Key Features                                               |
| --------------------------------------------------- | ---------------------- | ------------------- | ---------------------------------------------------------- |
| [Composio](/oss/python/integrations/tools/composio) | 500+                   | Free tier available | OAuth handling, event-driven workflows, multi-user support |

## All tools and toolkits

<Columns cols={3}>
  <Card title="ADS4GPTs" icon="link" href="/oss/python/integrations/tools/ads4gpts" arrow="true" cta="View guide" />

<Card title="AgentQL" icon="link" href="/oss/python/integrations/tools/agentql" arrow="true" cta="View guide" />

<Card title="AINetwork Toolkit" icon="link" href="/oss/python/integrations/tools/ainetwork" arrow="true" cta="View guide" />

<Card title="Alpha Vantage" icon="link" href="/oss/python/integrations/tools/alpha_vantage" arrow="true" cta="View guide" />

<Card title="Amadeus Toolkit" icon="link" href="/oss/python/integrations/tools/amadeus" arrow="true" cta="View guide" />

<Card title="Anchor Browser" icon="link" href="/oss/python/integrations/tools/anchor_browser" arrow="true" cta="View guide" />

<Card title="Apify Actor" icon="link" href="/oss/python/integrations/tools/apify_actors" arrow="true" cta="View guide" />

<Card title="ArXiv" icon="link" href="/oss/python/integrations/tools/arxiv" arrow="true" cta="View guide" />

<Card title="AskNews" icon="link" href="/oss/python/integrations/tools/asknews" arrow="true" cta="View guide" />

<Card title="AWS Lambda" icon="link" href="/oss/python/integrations/tools/awslambda" arrow="true" cta="View guide" />

<Card title="Azure AI Services Toolkit" icon="link" href="/oss/python/integrations/tools/azure_ai_services" arrow="true" cta="View guide" />

<Card title="Azure Cognitive Services Toolkit" icon="link" href="/oss/python/integrations/tools/azure_cognitive_services" arrow="true" cta="View guide" />

<Card title="Azure Container Apps Dynamic Sessions" icon="link" href="/oss/python/integrations/tools/azure_dynamic_sessions" arrow="true" cta="View guide" />

<Card title="Shell (bash)" icon="link" href="/oss/python/integrations/tools/bash" arrow="true" cta="View guide" />

<Card title="Bearly Code Interpreter" icon="link" href="/oss/python/integrations/tools/bearly" arrow="true" cta="View guide" />

<Card title="Bing Search" icon="link" href="/oss/python/integrations/tools/bing_search" arrow="true" cta="View guide" />

<Card title="Bodo DataFrames" icon="link" href="/oss/python/integrations/tools/bodo" arrow="true" cta="View guide" />

<Card title="Brave Search" icon="link" href="/oss/python/integrations/tools/brave_search" arrow="true" cta="View guide" />

<Card title="BrightData Web Scraper API" icon="link" href="/oss/python/integrations/tools/brightdata-webscraperapi" arrow="true" cta="View guide" />

<Card title="BrightData SERP" icon="link" href="/oss/python/integrations/tools/brightdata_serp" arrow="true" cta="View guide" />

<Card title="BrightData Unlocker" icon="link" href="/oss/python/integrations/tools/brightdata_unlocker" arrow="true" cta="View guide" />

<Card title="Cassandra Database Toolkit" icon="link" href="/oss/python/integrations/tools/cassandra_database" arrow="true" cta="View guide" />

<Card title="CDP" icon="link" href="/oss/python/integrations/tools/cdp_agentkit" arrow="true" cta="View guide" />

<Card title="ChatGPT Plugins" icon="link" href="/oss/python/integrations/tools/chatgpt_plugins" arrow="true" cta="View guide" />

<Card title="ClickUp Toolkit" icon="link" href="/oss/python/integrations/tools/clickup" arrow="true" cta="View guide" />

<Card title="Cogniswitch Toolkit" icon="link" href="/oss/python/integrations/tools/cogniswitch" arrow="true" cta="View guide" />

<Card title="Compass DeFi Toolkit" icon="link" href="/oss/python/integrations/tools/compass" arrow="true" cta="View guide" />

<Card title="Composio" icon="link" href="/oss/python/integrations/tools/composio" arrow="true" cta="View guide" />

<Card title="Connery Toolkit" icon="link" href="/oss/python/integrations/tools/connery" arrow="true" cta="View guide" />

<Card title="Dall-E Image Generator" icon="link" href="/oss/python/integrations/tools/dalle_image_generator" arrow="true" cta="View guide" />

<Card title="Dappier" icon="link" href="/oss/python/integrations/tools/dappier" arrow="true" cta="View guide" />

<Card title="Databricks Unity Catalog" icon="link" href="/oss/python/integrations/tools/databricks" arrow="true" cta="View guide" />

<Card title="DataForSEO" icon="link" href="/oss/python/integrations/tools/dataforseo" arrow="true" cta="View guide" />

<Card title="Dataherald" icon="link" href="/oss/python/integrations/tools/dataherald" arrow="true" cta="View guide" />

<Card title="DuckDuckGo Search" icon="link" href="/oss/python/integrations/tools/ddg" arrow="true" cta="View guide" />

<Card title="Discord" icon="link" href="/oss/python/integrations/tools/discord" arrow="true" cta="View guide" />

<Card title="E2B Data Analysis" icon="link" href="/oss/python/integrations/tools/e2b_data_analysis" arrow="true" cta="View guide" />

<Card title="Eden AI" icon="link" href="/oss/python/integrations/tools/edenai_tools" arrow="true" cta="View guide" />

<Card title="ElevenLabs Text2Speech" icon="link" href="/oss/python/integrations/tools/eleven_labs_tts" arrow="true" cta="View guide" />

<Card title="Exa Search" icon="link" href="/oss/python/integrations/tools/exa_search" arrow="true" cta="View guide" />

<Card title="File System" icon="link" href="/oss/python/integrations/tools/filesystem" arrow="true" cta="View guide" />

<Card title="Financial Datasets Toolkit" icon="link" href="/oss/python/integrations/tools/financial_datasets" arrow="true" cta="View guide" />

<Card title="FMP Data" icon="link" href="/oss/python/integrations/tools/fmp-data" arrow="true" cta="View guide" />

<Card title="Github Toolkit" icon="link" href="/oss/python/integrations/tools/github" arrow="true" cta="View guide" />

<Card title="Gitlab Toolkit" icon="link" href="/oss/python/integrations/tools/gitlab" arrow="true" cta="View guide" />

<Card title="Gmail Toolkit" icon="link" href="/oss/python/integrations/tools/gmail" arrow="true" cta="View guide" />

<Card title="GOAT" icon="link" href="/oss/python/integrations/tools/goat" arrow="true" cta="View guide" />

<Card title="Privy" icon="link" href="/oss/python/integrations/tools/privy" arrow="true" cta="View guide" />

<Card title="Golden Query" icon="link" href="/oss/python/integrations/tools/golden_query" arrow="true" cta="View guide" />

<Card title="Google Books" icon="link" href="/oss/python/integrations/tools/google_books" arrow="true" cta="View guide" />

<Card title="Google Calendar Toolkit" icon="link" href="/oss/python/integrations/tools/google_calendar" arrow="true" cta="View guide" />

<Card title="Google Cloud Text-to-Speech" icon="link" href="/oss/python/integrations/tools/google_cloud_texttospeech" arrow="true" cta="View guide" />

<Card title="Google Drive" icon="link" href="/oss/python/integrations/tools/google_drive" arrow="true" cta="View guide" />

<Card title="Google Finance" icon="link" href="/oss/python/integrations/tools/google_finance" arrow="true" cta="View guide" />

<Card title="Google Imagen" icon="link" href="/oss/python/integrations/tools/google_imagen" arrow="true" cta="View guide" />

<Card title="Google Jobs" icon="link" href="/oss/python/integrations/tools/google_jobs" arrow="true" cta="View guide" />

<Card title="Google Lens" icon="link" href="/oss/python/integrations/tools/google_lens" arrow="true" cta="View guide" />

<Card title="Google Places" icon="link" href="/oss/python/integrations/tools/google_places" arrow="true" cta="View guide" />

<Card title="Google Scholar" icon="link" href="/oss/python/integrations/tools/google_scholar" arrow="true" cta="View guide" />

<Card title="Google Search" icon="link" href="/oss/python/integrations/tools/google_search" arrow="true" cta="View guide" />

<Card title="Google Serper" icon="link" href="/oss/python/integrations/tools/google_serper" arrow="true" cta="View guide" />

<Card title="Google Trends" icon="link" href="/oss/python/integrations/tools/google_trends" arrow="true" cta="View guide" />

<Card title="Gradio" icon="link" href="/oss/python/integrations/tools/gradio_tools" arrow="true" cta="View guide" />

<Card title="GraphQL" icon="link" href="/oss/python/integrations/tools/graphql" arrow="true" cta="View guide" />

<Card title="HuggingFace Hub Tools" icon="link" href="/oss/python/integrations/tools/huggingface_tools" arrow="true" cta="View guide" />

<Card title="Human as a Tool" icon="link" href="/oss/python/integrations/tools/human_tools" arrow="true" cta="View guide" />

<Card title="Hyperbrowser Browser Agent Tools" icon="link" href="/oss/python/integrations/tools/hyperbrowser_browser_agent_tools" arrow="true" cta="View guide" />

<Card title="Hyperbrowser Web Scraping Tools" icon="link" href="/oss/python/integrations/tools/hyperbrowser_web_scraping_tools" arrow="true" cta="View guide" />

<Card title="IBM watsonx.ai" icon="link" href="/oss/python/integrations/tools/ibm_watsonx" arrow="true" cta="View guide" />

<Card title="IFTTT WebHooks" icon="link" href="/oss/python/integrations/tools/ifttt" arrow="true" cta="View guide" />

<Card title="Infobip" icon="link" href="/oss/python/integrations/tools/infobip" arrow="true" cta="View guide" />

<Card title="Ionic Shopping Tool" icon="link" href="/oss/python/integrations/tools/ionic_shopping" arrow="true" cta="View guide" />

<Card title="Jenkins" icon="link" href="/oss/python/integrations/tools/jenkins" arrow="true" cta="View guide" />

<Card title="Jina Search" icon="link" href="/oss/python/integrations/tools/jina_search" arrow="true" cta="View guide" />

<Card title="Jira Toolkit" icon="link" href="/oss/python/integrations/tools/jira" arrow="true" cta="View guide" />

<Card title="JSON Toolkit" icon="link" href="/oss/python/integrations/tools/json" arrow="true" cta="View guide" />

<Card title="Lemon Agent" icon="link" href="/oss/python/integrations/tools/lemonai" arrow="true" cta="View guide" />

<Card title="Linkup Search Tool" icon="link" href="/oss/python/integrations/tools/linkup_search" arrow="true" cta="View guide" />

<Card title="Memgraph" icon="link" href="/oss/python/integrations/tools/memgraph" arrow="true" cta="View guide" />

<Card title="Memorize" icon="link" href="/oss/python/integrations/tools/memorize" arrow="true" cta="View guide" />

<Card title="Mojeek Search" icon="link" href="/oss/python/integrations/tools/mojeek_search" arrow="true" cta="View guide" />

<Card title="MultiOn Toolkit" icon="link" href="/oss/python/integrations/tools/multion" arrow="true" cta="View guide" />

<Card title="NASA Toolkit" icon="link" href="/oss/python/integrations/tools/nasa" arrow="true" cta="View guide" />

<Card title="Naver Search" icon="link" href="/oss/python/integrations/tools/naver_search" arrow="true" cta="View guide" />

<Card title="Nuclia Understanding" icon="link" href="/oss/python/integrations/tools/nuclia" arrow="true" cta="View guide" />

<Card title="NVIDIA Riva" icon="link" href="/oss/python/integrations/tools/nvidia_riva" arrow="true" cta="View guide" />

<Card title="Office365 Toolkit" icon="link" href="/oss/python/integrations/tools/office365" arrow="true" cta="View guide" />

<Card title="OpenAPI Toolkit" icon="link" href="/oss/python/integrations/tools/openapi" arrow="true" cta="View guide" />

<Card title="Natural Language API Toolkits" icon="link" href="/oss/python/integrations/tools/openapi_nla" arrow="true" cta="View guide" />

<Card title="OpenGradient" icon="link" href="/oss/python/integrations/tools/opengradient_toolkit" arrow="true" cta="View guide" />

<Card title="OpenWeatherMap" icon="link" href="/oss/python/integrations/tools/openweathermap" arrow="true" cta="View guide" />

<Card title="Oracle AI Vector Search" icon="link" href="/oss/python/integrations/tools/oracleai" arrow="true" cta="View guide" />

<Card title="Oxylabs" icon="link" href="/oss/python/integrations/tools/oxylabs" arrow="true" cta="View guide" />

<Card title="Pandas Dataframe" icon="link" href="/oss/python/integrations/tools/pandas" arrow="true" cta="View guide" />

<Card title="Passio NutritionAI" icon="link" href="/oss/python/integrations/tools/passio_nutrition_ai" arrow="true" cta="View guide" />

<Card title="Permit" icon="link" href="/oss/python/integrations/tools/permit" arrow="true" cta="View guide" />

<Card title="PlayWright Browser Toolkit" icon="link" href="/oss/python/integrations/tools/playwright" arrow="true" cta="View guide" />

<Card title="Polygon IO Toolkit" icon="link" href="/oss/python/integrations/tools/polygon" arrow="true" cta="View guide" />

<Card title="PowerBI Toolkit" icon="link" href="/oss/python/integrations/tools/powerbi" arrow="true" cta="View guide" />

<Card title="Prolog" icon="link" href="/oss/python/integrations/tools/prolog_tool" arrow="true" cta="View guide" />

<Card title="PubMed" icon="link" href="/oss/python/integrations/tools/pubmed" arrow="true" cta="View guide" />

<Card title="Python REPL" icon="link" href="/oss/python/integrations/tools/python" arrow="true" cta="View guide" />

<Card title="Reddit Search" icon="link" href="/oss/python/integrations/tools/reddit_search" arrow="true" cta="View guide" />

<Card title="Requests Toolkit" icon="link" href="/oss/python/integrations/tools/requests" arrow="true" cta="View guide" />

<Card title="Riza Code Interpreter" icon="link" href="/oss/python/integrations/tools/riza" arrow="true" cta="View guide" />

<Card title="Robocorp Toolkit" icon="link" href="/oss/python/integrations/tools/robocorp" arrow="true" cta="View guide" />

<Card title="Salesforce" icon="link" href="/oss/python/integrations/tools/salesforce" arrow="true" cta="View guide" />

<Card title="SceneXplain" icon="link" href="/oss/python/integrations/tools/sceneXplain" arrow="true" cta="View guide" />

<Card title="ScrapeGraph" icon="link" href="/oss/python/integrations/tools/scrapegraph" arrow="true" cta="View guide" />

<Card title="Scrapeless Crawl" icon="link" href="/oss/python/integrations/tools/scrapeless_crawl" arrow="true" cta="View guide" />

<Card title="Scrapeless Scraping API" icon="link" href="/oss/python/integrations/tools/scrapeless_scraping_api" arrow="true" cta="View guide" />

<Card title="Scrapeless Universal Scraping" icon="link" href="/oss/python/integrations/tools/scrapeless_universal_scraping" arrow="true" cta="View guide" />

<Card title="SearchApi" icon="link" href="/oss/python/integrations/tools/searchapi" arrow="true" cta="View guide" />

<Card title="SearxNG Search" icon="link" href="/oss/python/integrations/tools/searx_search" arrow="true" cta="View guide" />

<Card title="Semantic Scholar API" icon="link" href="/oss/python/integrations/tools/semanticscholar" arrow="true" cta="View guide" />

<Card title="SerpAPI" icon="link" href="/oss/python/integrations/tools/serpapi" arrow="true" cta="View guide" />

<Card title="Slack Toolkit" icon="link" href="/oss/python/integrations/tools/slack" arrow="true" cta="View guide" />

<Card title="Spark SQL Toolkit" icon="link" href="/oss/python/integrations/tools/spark_sql" arrow="true" cta="View guide" />

<Card title="SQLDatabase Toolkit" icon="link" href="/oss/python/integrations/tools/sql_database" arrow="true" cta="View guide" />

<Card title="StackExchange" icon="link" href="/oss/python/integrations/tools/stackexchange" arrow="true" cta="View guide" />

<Card title="Steam Toolkit" icon="link" href="/oss/python/integrations/tools/steam" arrow="true" cta="View guide" />

<Card title="Stripe" icon="link" href="/oss/python/integrations/tools/stripe" arrow="true" cta="View guide" />

<Card title="Tableau" icon="link" href="/oss/python/integrations/tools/tableau" arrow="true" cta="View guide" />

<Card title="Taiga" icon="link" href="/oss/python/integrations/tools/taiga" arrow="true" cta="View guide" />

<Card title="Tavily Extract" icon="link" href="/oss/python/integrations/tools/tavily_extract" arrow="true" cta="View guide" />

<Card title="Tavily Search" icon="link" href="/oss/python/integrations/tools/tavily_search" arrow="true" cta="View guide" />

<Card title="Tilores" icon="link" href="/oss/python/integrations/tools/tilores" arrow="true" cta="View guide" />

<Card title="MCP Toolbox" icon="link" href="/oss/python/integrations/tools/toolbox" arrow="true" cta="View guide" />

<Card title="Twilio" icon="link" href="/oss/python/integrations/tools/twilio" arrow="true" cta="View guide" />

<Card title="Upstage" icon="link" href="/oss/python/integrations/tools/upstage_groundedness_check" arrow="true" cta="View guide" />

<Card title="Valthera" icon="link" href="/oss/python/integrations/tools/valthera" arrow="true" cta="View guide" />

<Card title="ValyuContext" icon="link" href="/oss/python/integrations/tools/valyu_search" arrow="true" cta="View guide" />

<Card title="Vectara" icon="link" href="/oss/python/integrations/tools/vectara" arrow="true" cta="View guide" />

<Card title="Wikidata" icon="link" href="/oss/python/integrations/tools/wikidata" arrow="true" cta="View guide" />

<Card title="Wikipedia" icon="link" href="/oss/python/integrations/tools/wikipedia" arrow="true" cta="View guide" />

<Card title="Wolfram Alpha" icon="link" href="/oss/python/integrations/tools/wolfram_alpha" arrow="true" cta="View guide" />

<Card title="WRITER Tools" icon="link" href="/oss/python/integrations/tools/writer" arrow="true" cta="View guide" />

<Card title="Yahoo Finance News" icon="link" href="/oss/python/integrations/tools/yahoo_finance_news" arrow="true" cta="View guide" />

<Card title="You.com Search" icon="link" href="/oss/python/integrations/tools/you" arrow="true" cta="View guide" />

<Card title="YouTube" icon="link" href="/oss/python/integrations/tools/youtube" arrow="true" cta="View guide" />

<Card title="Zapier Natural Language Actions" icon="link" href="/oss/python/integrations/tools/zapier" arrow="true" cta="View guide" />

<Card title="ZenGuard AI" icon="link" href="/oss/python/integrations/tools/zenguard" arrow="true" cta="View guide" />
</Columns>

<Info>
  If you'd like to contribute an integration, see [Contributing integrations](/oss/python/contributing#add-a-new-integration).
</Info>

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/tools/index.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

---

## Agent Builder setup

**URL:** llms-txt#agent-builder-setup

**Contents:**
- How to add workspace secrets
- Required model key
- Optional tool keys

Source: https://docs.langchain.com/langsmith/agent-builder-setup

Add required workspace secrets for models and tools used by Agent Builder.

This page lists the workspace secrets you need to add before using Agent Builder. Add these in your LangSmith workspace settings under Secrets. Keep values scoped to your workspace and avoid placing credentials in prompts or code.

## How to add workspace secrets

In the [LangSmith UI](https://smith.langchain.com), ensure that your Anthropic API key is set as a [workspace secret](/langsmith/administration-overview#workspace-secrets).

1. Navigate to <Icon icon="gear" /> **Settings** and then move to the **Secrets** tab.
2. Select **Add secret** and enter the `ANTHROPIC_API_KEY` and your API key as the **Value**.
3. Select **Save secret**.

<Note> When adding workspace secrets in the LangSmith UI, make sure the secret keys match the environment variable names expected by your model provider.</Note>

## Required model key

* `ANTHROPIC_API_KEY`: Required for Agent Builder models. The agent graphs load this key from workspace secrets for inference.

## Optional tool keys

Add keys for any tools you enable. These are read from workspace secrets at runtime.

* `EXA_API_KEY`: Required for Exa search tools (general web and LinkedIn profile search).
* `TAVILY_API_KEY`: Required for Tavily web search.
* `TWITTER_API_KEY` and `TWITTER_API_KEY_SECRET`: Required for Twitter/X read operations (app‑only bearer). Posting/media upload is not enabled.

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/langsmith/agent-builder-setup.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

---

## Limit specific tool

**URL:** llms-txt#limit-specific-tool

**Contents:**
  - Model fallback
  - PII detection
  - Planning
  - LLM tool selector
  - Tool retry
  - LLM tool emulator
  - Context editing
- Custom middleware
- Decorator-based middleware

search_limiter = ToolCallLimitMiddleware(
    tool_name="search",
    thread_limit=5,
    run_limit=3,
)

agent = create_agent(
    model="openai:gpt-4o",
    tools=[...],
    middleware=[global_limiter, search_limiter],
)
python  theme={null}
from langchain.agents import create_agent
from langchain.agents.middleware import ModelFallbackMiddleware

agent = create_agent(
    model="openai:gpt-4o",  # Primary model
    tools=[...],
    middleware=[
        ModelFallbackMiddleware(
            "openai:gpt-4o-mini",  # Try first on error
            "anthropic:claude-3-5-sonnet-20241022",  # Then this
        ),
    ],
)
python  theme={null}
from langchain.agents import create_agent
from langchain.agents.middleware import PIIMiddleware

agent = create_agent(
    model="openai:gpt-4o",
    tools=[...],
    middleware=[
        # Redact emails in user input
        PIIMiddleware("email", strategy="redact", apply_to_input=True),
        # Mask credit cards (show last 4 digits)
        PIIMiddleware("credit_card", strategy="mask", apply_to_input=True),
        # Custom PII type with regex
        PIIMiddleware(
            "api_key",
            detector=r"sk-[a-zA-Z0-9]{32}",
            strategy="block",  # Raise error if detected
        ),
    ],
)
python  theme={null}
from langchain.agents import create_agent
from langchain.agents.middleware import TodoListMiddleware
from langchain.messages import HumanMessage

agent = create_agent(
    model="openai:gpt-4o",
    tools=[...],
    middleware=[TodoListMiddleware()],
)

result = agent.invoke({"messages": [HumanMessage("Help me refactor my codebase")]})
print(result["todos"])  # Array of todo items with status tracking
python  theme={null}
from langchain.agents import create_agent
from langchain.agents.middleware import LLMToolSelectorMiddleware

agent = create_agent(
    model="openai:gpt-4o",
    tools=[tool1, tool2, tool3, tool4, tool5, ...],  # Many tools
    middleware=[
        LLMToolSelectorMiddleware(
            model="openai:gpt-4o-mini",  # Use cheaper model for selection
            max_tools=3,  # Limit to 3 most relevant tools
            always_include=["search"],  # Always include certain tools
        ),
    ],
)
python  theme={null}
from langchain.agents import create_agent
from langchain.agents.middleware import ToolRetryMiddleware

agent = create_agent(
    model="openai:gpt-4o",
    tools=[search_tool, database_tool],
    middleware=[
        ToolRetryMiddleware(
            max_retries=3,  # Retry up to 3 times
            backoff_factor=2.0,  # Exponential backoff multiplier
            initial_delay=1.0,  # Start with 1 second delay
            max_delay=60.0,  # Cap delays at 60 seconds
            jitter=True,  # Add random jitter to avoid thundering herd
        ),
    ],
)
python  theme={null}
from langchain.agents import create_agent
from langchain.agents.middleware import LLMToolEmulator

agent = create_agent(
    model="openai:gpt-4o",
    tools=[get_weather, search_database, send_email],
    middleware=[
        # Emulate all tools by default
        LLMToolEmulator(),

# Or emulate specific tools
        # LLMToolEmulator(tools=["get_weather", "search_database"]),

# Or use a custom model for emulation
        # LLMToolEmulator(model="anthropic:claude-3-5-sonnet-latest"),
    ],
)
python  theme={null}
from langchain.agents import create_agent
from langchain.agents.middleware import ContextEditingMiddleware, ClearToolUsesEdit

agent = create_agent(
    model="openai:gpt-4o",
    tools=[...],
    middleware=[
        ContextEditingMiddleware(
            edits=[
                ClearToolUsesEdit(max_tokens=1000),  # Clear old tool uses
            ],
        ),
    ],
)
python  theme={null}
from langchain.agents.middleware import before_model, after_model, wrap_model_call
from langchain.agents.middleware import AgentState, ModelRequest, ModelResponse, dynamic_prompt
from langchain.messages import AIMessage
from langchain.agents import create_agent
from langgraph.runtime import Runtime
from typing import Any, Callable

**Examples:**

Example 1 (unknown):
```unknown
<Accordion title="Configuration options">
  <ParamField body="tool_name" type="string">
    Specific tool to limit. If not provided, limits apply to all tools.
  </ParamField>

  <ParamField body="thread_limit" type="number">
    Maximum tool calls across all runs in a thread. Defaults to no limit.
  </ParamField>

  <ParamField body="run_limit" type="number">
    Maximum tool calls per single invocation. Defaults to no limit.
  </ParamField>

  <ParamField body="exit_behavior" type="string" default="end">
    Behavior when limit is reached. Options: `"end"` (graceful termination) or `"error"` (raise exception)
  </ParamField>
</Accordion>

### Model fallback

Automatically fallback to alternative models when the primary model fails.

<Tip>
  **Perfect for:**

  * Building resilient agents that handle model outages
  * Cost optimization by falling back to cheaper models
  * Provider redundancy across OpenAI, Anthropic, etc.
</Tip>
```

Example 2 (unknown):
```unknown
<Accordion title="Configuration options">
  <ParamField body="first_model" type="string | BaseChatModel" required>
    First fallback model to try when the primary model fails. Can be a model string (e.g., `"openai:gpt-4o-mini"`) or a `BaseChatModel` instance.
  </ParamField>

  <ParamField body="*additional_models" type="string | BaseChatModel">
    Additional fallback models to try in order if previous models fail
  </ParamField>
</Accordion>

### PII detection

Detect and handle Personally Identifiable Information in conversations.

<Tip>
  **Perfect for:**

  * Healthcare and financial applications with compliance requirements
  * Customer service agents that need to sanitize logs
  * Any application handling sensitive user data
</Tip>
```

Example 3 (unknown):
```unknown
<Accordion title="Configuration options">
  <ParamField body="pii_type" type="string" required>
    Type of PII to detect. Can be a built-in type (`email`, `credit_card`, `ip`, `mac_address`, `url`) or a custom type name.
  </ParamField>

  <ParamField body="strategy" type="string" default="redact">
    How to handle detected PII. Options:

    * `"block"` - Raise exception when detected
    * `"redact"` - Replace with `[REDACTED_TYPE]`
    * `"mask"` - Partially mask (e.g., `****-****-****-1234`)
    * `"hash"` - Replace with deterministic hash
  </ParamField>

  <ParamField body="detector" type="function | regex">
    Custom detector function or regex pattern. If not provided, uses built-in detector for the PII type.
  </ParamField>

  <ParamField body="apply_to_input" type="boolean" default="True">
    Check user messages before model call
  </ParamField>

  <ParamField body="apply_to_output" type="boolean" default="False">
    Check AI messages after model call
  </ParamField>

  <ParamField body="apply_to_tool_results" type="boolean" default="False">
    Check tool result messages after execution
  </ParamField>
</Accordion>

### Planning

Add todo list management capabilities for complex multi-step tasks.

<Note>
  This middleware automatically provides agents with a `write_todos` tool and system prompts to guide effective task planning.
</Note>
```

Example 4 (unknown):
```unknown
<Accordion title="Configuration options">
  <ParamField body="system_prompt" type="string">
    Custom system prompt for guiding todo usage. Uses built-in prompt if not specified.
  </ParamField>

  <ParamField body="tool_description" type="string">
    Custom description for the `write_todos` tool. Uses built-in description if not specified.
  </ParamField>
</Accordion>

### LLM tool selector

Use an LLM to intelligently select relevant tools before calling the main model.

<Tip>
  **Perfect for:**

  * Agents with many tools (10+) where most aren't relevant per query
  * Reducing token usage by filtering irrelevant tools
  * Improving model focus and accuracy
</Tip>
```

---

## Print the agent's response

**URL:** llms-txt#print-the-agent's-response

**Contents:**
- What happened?
- Next steps

print(result["messages"][-1].content)
```

Your deep agent automatically:

1. **Planned its approach**: Used the built-in `write_todos` tool to break down the research task
2. **Conducted research**: Called the `internet_search` tool to gather information
3. **Managed context**: Used file system tools (`write_file`, `read_file`) to offload large search results
4. **Spawned subagents** (if needed): Delegated complex subtasks to specialized subagents
5. **Synthesized a report**: Compiled findings into a coherent response

Now that you've built your first deep agent:

* **Customize your agent**: Learn about [customization options](/oss/python/deepagents/customization), including custom system prompts, tools, and subagents.
* **Understand middleware**: Dive into the [middleware architecture](/oss/python/deepagents/middleware) that powers deep agents.
* **Add long-term memory**: Enable [persistent memory](/oss/python/deepagents/long-term-memory) across conversations.
* **Deploy to production**: Learn about [deployment options](/oss/python/langgraph/deploy) for LangGraph applications.

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/quickstart.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

---

## After a model makes a tool call

**URL:** llms-txt#after-a-model-makes-a-tool-call

ai_message = AIMessage(
    content=[],
    tool_calls=[{
        "name": "get_weather",
        "args": {"location": "San Francisco"},
        "id": "call_123"
    }]
)

---

## Python >= 3.11 is required.

**URL:** llms-txt#python->=-3.11-is-required.

**Contents:**
  - 2. Prepare your agent
  - 3. Environment variables
  - 4. Create a LangGraph config file
  - 5. Install dependencies
  - 6. View your agent in Studio

pip install --upgrade "langgraph-cli[inmem]"
python title="agent.py" theme={null}
from langchain.agents import create_agent

def send_email(to: str, subject: str, body: str):
    """Send an email"""
    email = {
        "to": to,
        "subject": subject,
        "body": body
    }
    # ... email sending logic

return f"Email sent to {to}"

agent = create_agent(
    "openai:gpt-4o",
    tools=[send_email],
    system_prompt="You are an email assistant. Always use the send_email tool.",
)
bash .env theme={null}
LANGSMITH_API_KEY=lsv2...
json title="langgraph.json" theme={null}
{
  "dependencies": ["."],
  "graphs": {
    "agent": "./src/agent.py:agent"
  },
  "env": ".env"
}
bash  theme={null}
my-app/
├── src
│   └── agent.py
├── .env
└── langgraph.json
shell pip theme={null}
  pip install -e .
  shell uv theme={null}
  uv sync
  shell  theme={null}
langgraph dev
```

<Warning>
  Safari blocks `localhost` connections to Studio. To work around this, run the above command with `--tunnel` to access Studio via a secure tunnel.
</Warning>

Your agent will be accessible via API (`http://127.0.0.1:2024`) and the Studio UI `https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024`:

<Frame>
    <img src="https://mintcdn.com/langchain-5e9cc07a/TCDks4pdsHdxWmuJ/oss/images/studio_create-agent.png?fit=max&auto=format&n=TCDks4pdsHdxWmuJ&q=85&s=ebd259e9fa24af7d011dfcc568f74be2" alt="Agent view in the Studio UI" data-og-width="2836" width="2836" data-og-height="1752" height="1752" data-path="oss/images/studio_create-agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/TCDks4pdsHdxWmuJ/oss/images/studio_create-agent.png?w=280&fit=max&auto=format&n=TCDks4pdsHdxWmuJ&q=85&s=cf9c05bdd08661d4d546c540c7a28cbe 280w, https://mintcdn.com/langchain-5e9cc07a/TCDks4pdsHdxWmuJ/oss/images/studio_create-agent.png?w=560&fit=max&auto=format&n=TCDks4pdsHdxWmuJ&q=85&s=484b2fd56957d048bd89280ce97065a0 560w, https://mintcdn.com/langchain-5e9cc07a/TCDks4pdsHdxWmuJ/oss/images/studio_create-agent.png?w=840&fit=max&auto=format&n=TCDks4pdsHdxWmuJ&q=85&s=92991302ac24604022ab82ac22729f68 840w, https://mintcdn.com/langchain-5e9cc07a/TCDks4pdsHdxWmuJ/oss/images/studio_create-agent.png?w=1100&fit=max&auto=format&n=TCDks4pdsHdxWmuJ&q=85&s=ed366abe8dabc42a9d7c300a591e1614 1100w, https://mintcdn.com/langchain-5e9cc07a/TCDks4pdsHdxWmuJ/oss/images/studio_create-agent.png?w=1650&fit=max&auto=format&n=TCDks4pdsHdxWmuJ&q=85&s=d5865d3c4b0d26e9d72e50d474547a63 1650w, https://mintcdn.com/langchain-5e9cc07a/TCDks4pdsHdxWmuJ/oss/images/studio_create-agent.png?w=2500&fit=max&auto=format&n=TCDks4pdsHdxWmuJ&q=85&s=6b254add2df9cc3c10ac0c2bcb3a589c 2500w" />
</Frame>

Studio makes each step of your agent easily observable. Replay any input and inspect the exact prompt, tool arguments, return values, and token/latency metrics. If a tool throws an exception, Studio records it with surrounding state so you can spend less time debugging.

Keep your dev server running, edit prompts or tool signatures, and watch Studio hot-reload. Re-run the conversation thread from any step to verify behavior changes. See [Manage threads](/langsmith/use-studio#edit-thread-history) for more details.

As your agent grows, the same view scales from a single-tool demo to multi-node graphs, keeping decisions legible and reproducible.

<Tip>
  For an in-depth look at Studio, check out the [overview page](/langsmith/studio).
</Tip>

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/studio.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

**Examples:**

Example 1 (unknown):
```unknown
### 2. Prepare your agent

We'll use the following simple agent as an example:
```

Example 2 (unknown):
```unknown
### 3. Environment variables

Create a `.env` file in the root of your project and fill in the necessary API keys. We'll need to set the `LANGSMITH_API_KEY` environment variable to the API key you get from [LangSmith](https://smith.langchain.com/settings).

<Warning>
  Be sure not to commit your `.env` to version control systems such as Git!
</Warning>
```

Example 3 (unknown):
```unknown
### 4. Create a LangGraph config file

Inside your app's directory, create a configuration file `langgraph.json`:
```

Example 4 (unknown):
```unknown
[`create_agent`](https://reference.langchain.com/python/langchain/agents/#langchain.agents.create_agent) automatically returns a compiled LangGraph graph that we can pass to the `graphs` key in our configuration file.

<Info>
  See the [LangGraph configuration file reference](/langsmith/cli#configuration-file) for detailed explanations of each key in the JSON object of the configuration file.
</Info>

So far, our project structure looks like this:
```

---

## Discover errors and usage patterns with the Insights Agent

**URL:** llms-txt#discover-errors-and-usage-patterns-with-the-insights-agent

**Contents:**
- Prerequisites
- Generate your first Insights Report
- Understand the results
  - Top-level categories
  - Subcategories
  - Individual traces
- Configure a job
  - Autogenerating a config
  - Choose a model provider
  - Using a prebuilt config

Source: https://docs.langchain.com/langsmith/insights

The Insights Agent automatically analyzes your traces to detect usage patterns, common agent behaviors and failure modes — without requiring you to manually review thousands of traces.
Insights uses hierarchical categorization to make sense of your data and highlight actionable trends.

* An OpenAI API key (generate one [here](https://platform.openai.com/account/api-keys)) or an Anthropic API key (generate one [here](https://console.anthropic.com/settings/keys))
* Permissions to create rules in LangSmith (required to generate new Insights Reports)
* Permissions to view tracing projects LangSmith (required to view existing Insights Reports)

## Generate your first Insights Report

<Frame caption="Auto configuration flow for Insights Agent">
  <img src="https://mintcdn.com/langchain-5e9cc07a/rp5c1TvRWS7-YcPd/langsmith/images/insights-autogenerate-config.png?fit=max&auto=format&n=rp5c1TvRWS7-YcPd&q=85&s=1055fe5ac43cdce00c43297e818db6b6" data-og-width="1498" width="1498" data-og-height="1408" height="1408" data-path="langsmith/images/insights-autogenerate-config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/rp5c1TvRWS7-YcPd/langsmith/images/insights-autogenerate-config.png?w=280&fit=max&auto=format&n=rp5c1TvRWS7-YcPd&q=85&s=0c83b31a5a183ba5935b39b7b9de711d 280w, https://mintcdn.com/langchain-5e9cc07a/rp5c1TvRWS7-YcPd/langsmith/images/insights-autogenerate-config.png?w=560&fit=max&auto=format&n=rp5c1TvRWS7-YcPd&q=85&s=72217621fca8f07947a9461d75f42913 560w, https://mintcdn.com/langchain-5e9cc07a/rp5c1TvRWS7-YcPd/langsmith/images/insights-autogenerate-config.png?w=840&fit=max&auto=format&n=rp5c1TvRWS7-YcPd&q=85&s=b23c7627f8e62d8bebb7e94a0ec068da 840w, https://mintcdn.com/langchain-5e9cc07a/rp5c1TvRWS7-YcPd/langsmith/images/insights-autogenerate-config.png?w=1100&fit=max&auto=format&n=rp5c1TvRWS7-YcPd&q=85&s=5399d7c632e4bde4b5aefd4d19c8a175 1100w, https://mintcdn.com/langchain-5e9cc07a/rp5c1TvRWS7-YcPd/langsmith/images/insights-autogenerate-config.png?w=1650&fit=max&auto=format&n=rp5c1TvRWS7-YcPd&q=85&s=6be2b9f0c90979149f86e416c7cd4d8c 1650w, https://mintcdn.com/langchain-5e9cc07a/rp5c1TvRWS7-YcPd/langsmith/images/insights-autogenerate-config.png?w=2500&fit=max&auto=format&n=rp5c1TvRWS7-YcPd&q=85&s=adf51929b885117ba87e00be8f54d306 2500w" />
</Frame>

From the [LangSmith UI](https://smith.langchain.com):

1. Navigate to **Tracing Projects** in the left-hand menu and select a tracing project.
2. Click **+New** in the top right corner then **New Insights Report** to generate new insights over the project.
3. Enter a name for your job.
4. Click the <Icon icon="key" /> icon in the top right of the job creation pane to set your OpenAI (or Anthropic) API key as a [workspace secret](/langsmith/administration-overview#workspaces). If your workspace already has an OpenAI API key set, you can skip this step.
5. Answer the guided questions to focus your Insights Report on what you want to learn about your agent, then click **Run job**.

This will kick off a background Insights Report. Reports can take up to 30 minutes to complete.

<Note>Generating insights over 1,000 threads typically costs \$1.00-\$2.00 with OpenAI models and \$3.00-\$4.00 with current Anthropic models. The cost scales with the number of threads sampled and the size of each thread.</Note>

## Understand the results

Once your job has completed, you can navigate to the **Insights** tab where you'll see a table of Insights Report. Each Report contains insights generated over a specific sample of traces from the tracing project.

<Frame caption="Insights Reports for a single tracing project">
  <img src="https://mintcdn.com/langchain-5e9cc07a/4-kFQm9_42J5OnwH/langsmith/images/insights-job-results.png?fit=max&auto=format&n=4-kFQm9_42J5OnwH&q=85&s=6068ead08d93b27a31e85dd35bdbca01" data-og-width="2540" width="2540" data-og-height="836" height="836" data-path="langsmith/images/insights-job-results.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/4-kFQm9_42J5OnwH/langsmith/images/insights-job-results.png?w=280&fit=max&auto=format&n=4-kFQm9_42J5OnwH&q=85&s=d89d356e627fe9b79a889f1b08f5b55e 280w, https://mintcdn.com/langchain-5e9cc07a/4-kFQm9_42J5OnwH/langsmith/images/insights-job-results.png?w=560&fit=max&auto=format&n=4-kFQm9_42J5OnwH&q=85&s=1e36efd2e207f240c943918bec0fb692 560w, https://mintcdn.com/langchain-5e9cc07a/4-kFQm9_42J5OnwH/langsmith/images/insights-job-results.png?w=840&fit=max&auto=format&n=4-kFQm9_42J5OnwH&q=85&s=81d1b513785c44c83e19e037ee2bac9c 840w, https://mintcdn.com/langchain-5e9cc07a/4-kFQm9_42J5OnwH/langsmith/images/insights-job-results.png?w=1100&fit=max&auto=format&n=4-kFQm9_42J5OnwH&q=85&s=bd6af403106f833511a03a2f2f58d866 1100w, https://mintcdn.com/langchain-5e9cc07a/4-kFQm9_42J5OnwH/langsmith/images/insights-job-results.png?w=1650&fit=max&auto=format&n=4-kFQm9_42J5OnwH&q=85&s=9de6145f9638aaa949b33cdae33de291 1650w, https://mintcdn.com/langchain-5e9cc07a/4-kFQm9_42J5OnwH/langsmith/images/insights-job-results.png?w=2500&fit=max&auto=format&n=4-kFQm9_42J5OnwH&q=85&s=f062f61dcc789fbc72a6fdf11fb76603 2500w" />
</Frame>

Click into your job to see traces organized into a set of auto-generated categories.
You can drill down through categories and subcategories to view the underlying traces, feedback, and run statistics.

<Frame caption="Common topics of conversations with the https://chat.langchain.com chatbot">
  <img src="https://mintcdn.com/langchain-5e9cc07a/4-kFQm9_42J5OnwH/langsmith/images/insights-nav.gif?s=6a22bfd0d94262b7aa78468a8379ea0f" data-og-width="800" width="800" data-og-height="516" height="516" data-path="langsmith/images/insights-nav.gif" data-optimize="true" data-opv="3" />
</Frame>

### Top-level categories

Your traces are automatically grouped into top-level categories that represent the broadest patterns in your data.

The distribution bars show how frequently each pattern occurs, making it easy to spot behaviors that happen more or less than expected.

Each category has a brief description and displays aggregated metrics over the traces it contains, including:

* Typical trace stats (like error rates, latency, cost)
* Feedback scores from your evaluators
* [Attributes](#attributes) extracted as part of the job

Clicking on any category shows a breakdown into subcategories, which gives you a more granular understanding of interaction patterns in that category of traces.

In the [Chat Langchain](https://chat.langchain.com) example pictured above, under "Data & Retrieval" there are subcategories like "Vector Stores" and "Data Ingestion".

### Individual traces

You can view the traces assigned to each category or subcategory by clicking through to see the traces table. From there, you can click into any trace to see the full conversation details.

You can create an Insights Report three ways. Start with the auto-generated flow to spin up a baseline, then iterate with saved or manual configs as you refine.

### Autogenerating a config

1. Open **New Insights** and make sure the **Auto** toggle is active.
2. Answer the natural-language questions about your agent’s purpose, what you want to learn, and how traces are structured. Insights will translate your answers into
   a draft config (job name, summary prompt, attributes, and sampling defaults).
3. Choose a provider, then click **Generate config** to preview or **Run job** to launch immediately.

**Providing useful context**

For best results, write a sentence or two for each prompt that gives the agent the context it needs—what you’re trying to learn, which signals or fields matter most, and anything you
already know isn’t useful. The clearer you are about what your agent does and how its traces are structured, the more the Insights Agent can group examples in a way
that’s specific, actionable, and aligned with how you reason about your data.

**Describing your traces**

Explain how your data is organized—are these single runs or multi-turn conversations? Which inputs and outputs contain the key information? This helps the Insights Agent generate summary prompts and attributes that focus on what matters. You can also directly specify variables from the [summary prompt](#summary-prompt) section if needed.

### Choose a model provider

You can select either OpenAI or Anthropic models to power the agent. You must have the corresponding [workspace secret](/langsmith/administration-overview#workspaces) set for whichever provider you choose (OPENAI\_API\_KEY or ANTHROPIC\_API\_KEY).

Note that using current Anthropic models costs \~3x as much as using OpenAI models.

### Using a prebuilt config

Use the **Saved configurations** dropdown to load presets for common jobs like **Usage Patterns** or **Error Analysis**. Run them directly for a fast start, or adjust filters, prompts, and providers before saving your customized version. To learn more about what you can customize, read the section below.

### Building a config from scratch

Building your own config helps when you need more control—for example, predefining categories you want your data to be grouped into or targeting traces that match specific feedback scores and filters.

* **Sample size**: The maximum number of traces to analyze. Currently capped at 1,000
* **Time range**: Traces are sampled from this time range
* **Filters**: Additional trace filters. As you adjust filters, you'll see how many traces match your criteria

By default, top-level categories are automatically generated bottom-up from the underlying traces.
In some instances, you know specific categories you're interested in upfront and want the job to bucket traces into those predefined categories.

The **Categories** section of the config lets you do this by enumerating the names and descriptions of the top-level categories you want to be used.
Subcategories are still auto-generated by the algorithm within the predefined top-level categories.

The first step of the job is to create a brief summary of every trace — it is these summaries that are then categorized.
Extracting the right information in the summary is essential for getting useful categories.
The prompt used to generate these summaries can be edited.

The two things to think about when editing the prompt are:

* Summarization instructions: Any information that isn't in the trace summary won't affect the categories that get generated, so make sure to provide clear instructions on what information is important to extract from each trace.
* Trace content: Use mustache formatting to specify which parts of each trace are passed to the summarizer. Large traces with lots of inputs and outputs can be expensive and noisy. Reducing the prompt to only include the most relevant parts of the trace can improve your results.

The Insights Agent analyzes [threads](https://docs.langchain.com/langsmith/threads) - groups of related traces that represent multi-turn conversations. You must specify what parts of the thread to send to the summarizer using at least one of these template variables:

| Variable | Best for                                                                | Example                                            |
| -------- | ----------------------------------------------------------------------- | -------------------------------------------------- |
| run.\*   | Access data from the most recent root run (i.e. final turn) in a thread | `{{run.inputs}}` `{{run.outputs}}` `{{run.error}}` |

You can also access nested fields using dot notation. For example, the prompt `"Summarize this: {{run.inputs.foo.bar}}"` will include only the "bar" value within the "foo" value of the last run's inputs.

Along with a summary, you can define additional categorical, numerical, and boolean attributes to be extracted from each trace.
These attributes will influence the categorization step — traces with similar attribute values will tend to be categorized together.
You can also see aggregations of these attributes per category.

As an example, you might want to extract the attribute `user_satisfied: boolean` from each trace to steer the algorithm towards categories that split up positive and negative user experiences, and to see the average user satisfaction per category.

#### Filter attributes

You can use the `filter_by` parameter on boolean attributes to pre-filter traces before generating insights. When enabled, only traces where the attribute evaluates to `true` are included in the analysis.

This is useful when you want to focus your Insights Report on a specific subset of traces—for example, only analyzing errors, only examining English-language conversations, or only including traces that meet certain quality criteria.

<Frame caption="Using filter attributes to generate Insights only on traces with agent errors">
  <img src="https://mintcdn.com/langchain-5e9cc07a/L4LVgASBXoDKblmJ/langsmith/images/insights-filter-by-attribute.png?fit=max&auto=format&n=L4LVgASBXoDKblmJ&q=85&s=8cb30778befb18af445c3f6db758e631" data-og-width="1244" width="1244" data-og-height="490" height="490" data-path="langsmith/images/insights-filter-by-attribute.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/L4LVgASBXoDKblmJ/langsmith/images/insights-filter-by-attribute.png?w=280&fit=max&auto=format&n=L4LVgASBXoDKblmJ&q=85&s=b2a047279e60e995ce9de7fb44be3fc3 280w, https://mintcdn.com/langchain-5e9cc07a/L4LVgASBXoDKblmJ/langsmith/images/insights-filter-by-attribute.png?w=560&fit=max&auto=format&n=L4LVgASBXoDKblmJ&q=85&s=7fd3e854f73803434bc6490a33c77a1f 560w, https://mintcdn.com/langchain-5e9cc07a/L4LVgASBXoDKblmJ/langsmith/images/insights-filter-by-attribute.png?w=840&fit=max&auto=format&n=L4LVgASBXoDKblmJ&q=85&s=84b9cc1cc25ad8cc98962b584bca3ad1 840w, https://mintcdn.com/langchain-5e9cc07a/L4LVgASBXoDKblmJ/langsmith/images/insights-filter-by-attribute.png?w=1100&fit=max&auto=format&n=L4LVgASBXoDKblmJ&q=85&s=5d091df89be4d677139a21be120448f8 1100w, https://mintcdn.com/langchain-5e9cc07a/L4LVgASBXoDKblmJ/langsmith/images/insights-filter-by-attribute.png?w=1650&fit=max&auto=format&n=L4LVgASBXoDKblmJ&q=85&s=a6d991b404f2da6551c2cc696428e030 1650w, https://mintcdn.com/langchain-5e9cc07a/L4LVgASBXoDKblmJ/langsmith/images/insights-filter-by-attribute.png?w=2500&fit=max&auto=format&n=L4LVgASBXoDKblmJ&q=85&s=8c3cf044ac694ceb4818407c74c96b2e 2500w" />
</Frame>

* Add `"filter_by": true` to any boolean attribute when creating a config for the Insights Agent
* The LLM evaluates each trace against the attribute description during summarization
* Traces where the attribute is `false` or missing are excluded before insights are generated

You can optionally save configs for future reuse using the 'save as' button.
This is especially useful if you want to compare Insights Reports over time to identify changes in user and agent behavior.

Select from previously saved configs in the dropdown in the top-left corner of the pane when creating a new Insights Report.

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/langsmith/insights.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

---

## Process final result

**URL:** llms-txt#process-final-result

**Contents:**
- Multiple tool calls
- Edit tool arguments
- Subagent interrupts
- Best practices
  - Always use a checkpointer
  - Use the same thread ID

print(result["messages"][-1]["content"])
python  theme={null}
config = {"configurable": {"thread_id": str(uuid.uuid4())}}

result = agent.invoke({
    "messages": [{
        "role": "user",
        "content": "Delete temp.txt and send an email to admin@example.com"
    }]
}, config=config)

if result.get("__interrupt__"):
    interrupts = result["__interrupt__"][0].value
    action_requests = interrupts["action_requests"]

# Two tools need approval
    assert len(action_requests) == 2

# Provide decisions in the same order as action_requests
    decisions = [
        {"type": "approve"},  # First tool: delete_file
        {"type": "reject"}    # Second tool: send_email
    ]

result = agent.invoke(
        Command(resume={"decisions": decisions}),
        config=config
    )
python  theme={null}
if result.get("__interrupt__"):
    interrupts = result["__interrupt__"][0].value
    action_request = interrupts["action_requests"][0]

# Original args from the agent
    print(action_request["args"])  # {"to": "everyone@company.com", ...}

# User decides to edit the recipient
    decisions = [{
        "type": "edit",
        "edited_action": {
            "name": action_request["name"],  # Must include the tool name
            "args": {"to": "team@company.com", "subject": "...", "body": "..."}
        }
    }]

result = agent.invoke(
        Command(resume={"decisions": decisions}),
        config=config
    )
python  theme={null}
agent = create_deep_agent(
    tools=[delete_file, read_file],
    interrupt_on={
        "delete_file": True,
        "read_file": False,
    },
    subagents=[{
        "name": "file-manager",
        "description": "Manages file operations",
        "system_prompt": "You are a file management assistant.",
        "tools": [delete_file, read_file],
        "interrupt_on": {
            # Override: require approval for reads in this subagent
            "delete_file": True,
            "read_file": True,  # Different from main agent!
        }
    }],
    checkpointer=checkpointer
)
python  theme={null}
from langgraph.checkpoint.memory import MemorySaver

checkpointer = MemorySaver()
agent = create_deep_agent(
    tools=[...],
    interrupt_on={...},
    checkpointer=checkpointer  # Required for HITL
)
python  theme={null}

**Examples:**

Example 1 (unknown):
```unknown
## Multiple tool calls

When the agent calls multiple tools that require approval, all interrupts are batched together in a single interrupt. You must provide decisions for each one in order.
```

Example 2 (unknown):
```unknown
## Edit tool arguments

When `"edit"` is in the allowed decisions, you can modify the tool arguments before execution:
```

Example 3 (unknown):
```unknown
## Subagent interrupts

Each subagent can have its own `interrupt_on` configuration that overrides the main agent's settings:
```

Example 4 (unknown):
```unknown
When a subagent triggers an interrupt, the handling is the same – check for `__interrupt__` and resume with `Command`.

## Best practices

### Always use a checkpointer

Human-in-the-loop requires a checkpointer to persist agent state between the interrupt and resume:
```

---

## Set up Agent Auth (Beta)

**URL:** llms-txt#set-up-agent-auth-(beta)

**Contents:**
- Installation
- Quickstart
  - 1. Initialize the client
  - 2. Set up OAuth providers
  - 3. Authenticate from an agent

Source: https://docs.langchain.com/langsmith/agent-auth

Enable secure access from agents to any system using OAuth 2.0 credentials with Agent Auth.

<Note>Agent Auth is in **Beta** and under active development. To provide feedback or use this feature, reach out to the [LangChain team](https://forum.langchain.com/c/help/langsmith/).</Note>

Install the Agent Auth client library from PyPI:

### 1. Initialize the client

### 2. Set up OAuth providers

Before agents can authenticate, you need to configure an OAuth provider using the following process:

1. Select a unique identifier for your OAuth provider to use in LangChain's platform (e.g., "github-local-dev", "google-workspace-prod").

2. Go to your OAuth provider's developer console and create a new OAuth application.

3. Set LangChain's API as an available callback URL using this structure:
   
   For example, if your provider\_id is "github-local-dev", use:

4. Use `client.create_oauth_provider()` with the credentials from your OAuth app:

### 3. Authenticate from an agent

The client `authenticate()` API is used to get OAuth tokens from pre-configured providers. On the first call, it takes the caller through an OAuth 2.0 auth flow.

#### In LangGraph context

By default, tokens are scoped to the calling agent using the Assistant ID parameter.

```python  theme={null}
auth_result = await client.authenticate(
    provider="{provider_id}",
    scopes=["scopeA"],
    user_id="your_user_id" # Any unique identifier to scope this token to the human caller
)

**Examples:**

Example 1 (unknown):
```unknown

```

Example 2 (unknown):
```unknown
</CodeGroup>

## Quickstart

### 1. Initialize the client
```

Example 3 (unknown):
```unknown
### 2. Set up OAuth providers

Before agents can authenticate, you need to configure an OAuth provider using the following process:

1. Select a unique identifier for your OAuth provider to use in LangChain's platform (e.g., "github-local-dev", "google-workspace-prod").

2. Go to your OAuth provider's developer console and create a new OAuth application.

3. Set LangChain's API as an available callback URL using this structure:
```

Example 4 (unknown):
```unknown
For example, if your provider\_id is "github-local-dev", use:
```

---

## ✅ Good: Focused tool set

**URL:** llms-txt#✅-good:-focused-tool-set

email_agent = {
    "name": "email-sender",
    "tools": [send_email, validate_email],  # Only email-related
}

---

## No longer supported

**URL:** llms-txt#no-longer-supported

model_with_tools = ChatOpenAI().bind_tools([some_tool])
agent = create_agent(model_with_tools, tools=[])

---

## Limit all tool calls

**URL:** llms-txt#limit-all-tool-calls

global_limiter = ToolCallLimitMiddleware(thread_limit=20, run_limit=10)

---

## ContactInfo(name='John Doe', email='john@example.com', phone='(555) 123-4567')

**URL:** llms-txt#contactinfo(name='john-doe',-email='john@example.com',-phone='(555)-123-4567')

**Contents:**
  - Memory

python wrap theme={null}
from langchain.agents.structured_output import ProviderStrategy

agent = create_agent(
    model="openai:gpt-4o",
    response_format=ProviderStrategy(ContactInfo)
)
python  theme={null}
from langchain.agents import AgentState
from langchain.agents.middleware import AgentMiddleware

class CustomState(AgentState):
    user_preferences: dict

class CustomMiddleware(AgentMiddleware):
    state_schema = CustomState
    tools = [tool1, tool2]

def before_model(self, state: CustomState, runtime) -> dict[str, Any] | None:
        ...

agent = create_agent(
    model,
    tools=tools,
    middleware=[CustomMiddleware()]
)

**Examples:**

Example 1 (unknown):
```unknown
#### ProviderStrategy

`ProviderStrategy` uses the model provider's native structured output generation. This is more reliable but only works with providers that support native structured output (e.g., OpenAI):
```

Example 2 (unknown):
```unknown
<Note>
  As of `langchain 1.0`, simply passing a schema (e.g., `response_format=ContactInfo`) is no longer supported. You must explicitly use `ToolStrategy` or `ProviderStrategy`.
</Note>

<Tip>
  To learn about structured output, see [Structured output](/oss/python/langchain/structured-output).
</Tip>

### Memory

Agents maintain conversation history automatically through the message state. You can also configure the agent to use a custom state schema to remember additional information during the conversation.

Information stored in the state can be thought of as the [short-term memory](/oss/python/langchain/short-term-memory) of the agent:

Custom state schemas must extend [`AgentState`](https://reference.langchain.com/python/langchain/agents/#langchain.agents.AgentState) as a `TypedDict`.

There are two ways to define custom state:

1. Via [middleware](/oss/python/langchain/middleware) (preferred)
2. Via [`state_schema`](https://reference.langchain.com/python/langchain/middleware/#langchain.agents.middleware.AgentMiddleware.state_schema) on [`create_agent`](https://reference.langchain.com/python/langchain/agents/#langchain.agents.create_agent)

<Note>
  Defining custom state via middleware is preferred over defining it via [`state_schema`](https://reference.langchain.com/python/langchain/middleware/#langchain.agents.middleware.AgentMiddleware.state_schema) on [`create_agent`](https://reference.langchain.com/python/langchain/agents/#langchain.agents.create_agent) because it allows you to keep state extensions conceptually scoped to the relevant middleware and tools.

  [`state_schema`](https://reference.langchain.com/python/langchain/middleware/#langchain.agents.middleware.AgentMiddleware.state_schema) is still supported for backwards compatibility on [`create_agent`](https://reference.langchain.com/python/langchain/agents/#langchain.agents.create_agent).
</Note>

#### Defining state via middleware

Use middleware to define custom state when your custom state needs to be accessed by specific middleware hooks and tools attached to said middleware.
```

---

## Tools and Toolkits

**URL:** llms-txt#tools-and-toolkits

**Contents:**
- Integration Platforms
- All Tools and Toolkits

Source: https://docs.langchain.com/oss/javascript/integrations/tools/index

[Tools](/oss/javascript/langchain/tools) are utilities designed to be called by a model: their inputs are designed to be generated by models, and their outputs are designed to be passed back to models.

A [toolkit](/oss/javascript/langchain/tools#toolkits) is a collection of tools meant to be used together.

## Integration Platforms

The following platforms provide access to multiple tools and services through a unified interface:

| Tool/Toolkit                                            | Number of Integrations | Pricing             | Key Features                                               |
| ------------------------------------------------------- | ---------------------- | ------------------- | ---------------------------------------------------------- |
| [Composio](/oss/javascript/integrations/tools/composio) | 500+                   | Free tier available | OAuth handling, event-driven workflows, multi-user support |

## All Tools and Toolkits

<Columns cols={3}>
  <Card title="Azure Container Apps Dynamic Sessions" icon="link" href="/oss/javascript/integrations/tools/azure_dynamic_sessions" arrow="true" cta="View guide" />

<Card title="Connery Action Tool" icon="link" href="/oss/javascript/integrations/tools/connery" arrow="true" cta="View guide" />

<Card title="Composio" icon="link" href="/oss/javascript/integrations/tools/composio" arrow="true" cta="View guide" />

<Card title="Dall-E Tool" icon="link" href="/oss/javascript/integrations/tools/dalle" arrow="true" cta="View guide" />

<Card title="Decodo Tools" icon="link" href="/oss/javascript/integrations/tools/decodo" arrow="true" cta="View guide" />

<Card title="Discord Tool" icon="link" href="/oss/javascript/integrations/tools/discord_tool" arrow="true" cta="View guide" />

<Card title="DuckDuckGoSearch" icon="link" href="/oss/javascript/integrations/tools/duckduckgo_search" arrow="true" cta="View guide" />

<Card title="ExaSearchResults" icon="link" href="/oss/javascript/integrations/tools/exa_search" arrow="true" cta="View guide" />

<Card title="Gmail Tool" icon="link" href="/oss/javascript/integrations/tools/gmail" arrow="true" cta="View guide" />

<Card title="GOAT" icon="link" href="/oss/javascript/integrations/tools/goat" arrow="true" cta="View guide" />

<Card title="Google Calendar Tool" icon="link" href="/oss/javascript/integrations/tools/google_calendar" arrow="true" cta="View guide" />

<Card title="Google Places Tool" icon="link" href="/oss/javascript/integrations/tools/google_places" arrow="true" cta="View guide" />

<Card title="Google Routes Tool" icon="link" href="/oss/javascript/integrations/tools/google_routes" arrow="true" cta="View guide" />

<Card title="Google Scholar" icon="link" href="/oss/javascript/integrations/tools/google_scholar" arrow="true" cta="View guide" />

<Card title="Google Trends Tool" icon="link" href="/oss/javascript/integrations/tools/google_trends" arrow="true" cta="View guide" />

<Card title="JigsawStack Tool" icon="link" href="/oss/javascript/integrations/tools/jigsawstack" arrow="true" cta="View guide" />

<Card title="Agent with AWS Lambda" icon="link" href="/oss/javascript/integrations/tools/lambda_agent" arrow="true" cta="View guide" />

<Card title="Python interpreter tool" icon="link" href="/oss/javascript/integrations/tools/pyinterpreter" arrow="true" cta="View guide" />

<Card title="SearchApi tool" icon="link" href="/oss/javascript/integrations/tools/searchapi" arrow="true" cta="View guide" />

<Card title="Searxng Search tool" icon="link" href="/oss/javascript/integrations/tools/searxng" arrow="true" cta="View guide" />

<Card title="SerpAPI" icon="link" href="/oss/javascript/integrations/tools/serpapi" arrow="true" cta="View guide" />

<Card title="StackExchange Tool" icon="link" href="/oss/javascript/integrations/tools/stackexchange" arrow="true" cta="View guide" />

<Card title="Stagehand AI Web Automation Toolkit" icon="link" href="/oss/javascript/integrations/tools/stagehand" arrow="true" cta="View guide" />

<Card title="Tavily Crawl" icon="link" href="/oss/javascript/integrations/tools/tavily_crawl" arrow="true" cta="View guide" />

<Card title="Tavily Extract" icon="link" href="/oss/javascript/integrations/tools/tavily_extract" arrow="true" cta="View guide" />

<Card title="Tavily Map" icon="link" href="/oss/javascript/integrations/tools/tavily_map" arrow="true" cta="View guide" />

<Card title="Tavily Search" icon="link" href="/oss/javascript/integrations/tools/tavily_search" arrow="true" cta="View guide" />

<Card title="Web Browser Tool" icon="link" href="/oss/javascript/integrations/tools/webbrowser" arrow="true" cta="View guide" />

<Card title="Wikipedia tool" icon="link" href="/oss/javascript/integrations/tools/wikipedia" arrow="true" cta="View guide" />

<Card title="WolframAlpha Tool" icon="link" href="/oss/javascript/integrations/tools/wolframalpha" arrow="true" cta="View guide" />
</Columns>

<Info>
  If you'd like to write your own tool, see [this how-to](/oss/javascript/langchain/tools#customize-tool-properties). If you'd like to contribute an integration, see [Contributing integrations](/oss/javascript/contributing#add-a-new-integration).
</Info>

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/tools/index.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

---

## Create a custom agent graph

**URL:** llms-txt#create-a-custom-agent-graph

custom_graph = create_agent(
    model=your_model,
    tools=specialized_tools,
    prompt="You are a specialized agent for data analysis..."
)

---

## Create a user proxy agent

**URL:** llms-txt#create-a-user-proxy-agent

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=8,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "workspace"},
    llm_config={"config_list": config_list},
)

def run_code_review_session(task_description: str):
    """Run a multi-agent code review session."""

# Create a group chat with the agents
    groupchat = autogen.GroupChat(
        agents=[user_proxy, developer, code_reviewer],
        messages=[],
        max_round=10
    )

# Create a group chat manager
    manager = autogen.GroupChatManager(
        groupchat=groupchat,
        llm_config={"config_list": config_list}
    )

# Start the conversation
    user_proxy.initiate_chat(
        manager,
        message=f"""
        Task: {task_description}

Developer: Please implement the requested feature.
        Code Reviewer: Please review the implementation and provide feedback.

Work together to create a high-quality solution.
        """
    )

return "Code review session completed"

---

## Define the tools for the agent to use

**URL:** llms-txt#define-the-tools-for-the-agent-to-use

@tool
def search(query: str) -> str:
    """Call to surf the web."""
    # This is a placeholder, but don't tell the LLM that...
    if "sf" in query.lower() or "san francisco" in query.lower():
        return "It's 60 degrees and foggy."
    return "It's 90 degrees and sunny."

tools = [search]
tool_node = ToolNode(tools)
model = init_chat_model("claude-3-5-sonnet-latest").bind_tools(tools)

---

## Update the user_name in the agent state

**URL:** llms-txt#update-the-user_name-in-the-agent-state

@tool
def update_user_name(
    new_name: str,
    runtime: ToolRuntime
) -> Command:
    """Update the user's name."""
    return Command(update={"user_name": new_name})
python wrap theme={null}
from dataclasses import dataclass
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool, ToolRuntime

USER_DATABASE = {
    "user123": {
        "name": "Alice Johnson",
        "account_type": "Premium",
        "balance": 5000,
        "email": "alice@example.com"
    },
    "user456": {
        "name": "Bob Smith",
        "account_type": "Standard",
        "balance": 1200,
        "email": "bob@example.com"
    }
}

@dataclass
class UserContext:
    user_id: str

@tool
def get_account_info(runtime: ToolRuntime[UserContext]) -> str:
    """Get the current user's account information."""
    user_id = runtime.context.user_id

if user_id in USER_DATABASE:
        user = USER_DATABASE[user_id]
        return f"Account holder: {user['name']}\nType: {user['account_type']}\nBalance: ${user['balance']}"
    return "User not found"

model = ChatOpenAI(model="gpt-4o")
agent = create_agent(
    model,
    tools=[get_account_info],
    context_schema=UserContext,
    system_prompt="You are a financial assistant."
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's my current balance?"}]},
    context=UserContext(user_id="user123")
)
python wrap expandable theme={null}
from typing import Any
from langgraph.store.memory import InMemoryStore
from langchain.agents import create_agent
from langchain.tools import tool, ToolRuntime

**Examples:**

Example 1 (unknown):
```unknown
#### Context

Access immutable configuration and contextual data like user IDs, session details, or application-specific configuration through `runtime.context`.

Tools can access runtime context through `ToolRuntime`:
```

Example 2 (unknown):
```unknown
#### Memory (Store)

Access persistent data across conversations using the store. The store is accessed via `runtime.store` and allows you to save and retrieve user-specific or application-specific data.

Tools can access and update the store through `ToolRuntime`:
```

---

## Run evaluation

**URL:** llms-txt#run-evaluation

**Contents:**
- Reference code

experiment_results = await client.aevaluate(
    run_intent_classifier,
    data=dataset_name,
    evaluators=[correct],
    experiment_prefix="sql-agent-gpt4o-intent-classifier",
    max_concurrency=4,
)
`python  theme={null}
  import json
  import sqlite3
  from typing import Literal

from langchain.chat_models import init_chat_model
  from langchain.embeddings import init_embeddings
  from langchain_core.runnables import RunnableConfig
  from langchain.tools import tool
  from langchain_core.vectorstores import InMemoryVectorStore
  from langgraph.graph import END, StateGraph
  from langgraph.graph.message import AnyMessage, add_messages
  from langchain.agents import create_agent
  from langgraph.types import Command, interrupt
  from langsmith import Client
  import requests
  from tabulate import tabulate
  from typing_extensions import Annotated, TypedDict

url = "https://storage.googleapis.com/benchmarks-artifacts/chinook/Chinook.db"

response = requests.get(url)

if response.status_code == 200:
      # Open a local file in binary write mode
      with open("chinook.db", "wb") as file:
          # Write the content of the response (the file) to the local file
          file.write(response.content)
      print("File downloaded and saved as Chinook.db")
  else:
      print(f"Failed to download the file. Status code: {response.status_code}")

def _refund(
      invoice_id: int | None, invoice_line_ids: list[int] | None, mock: bool = False
  ) -> float:
      """Given an Invoice ID and/or Invoice Line IDs, delete the relevant Invoice/InvoiceLine records in the Chinook DB.

Args:
          invoice_id: The Invoice to delete.
          invoice_line_ids: The Invoice Lines to delete.
          mock: If True, do not actually delete the specified Invoice/Invoice Lines. Used for testing purposes.

Returns:
          float: The total dollar amount that was deleted (or mock deleted).
      """

if invoice_id is None and invoice_line_ids is None:
          return 0.0

# Connect to the Chinook database
      conn = sqlite3.connect("chinook.db")
      cursor = conn.cursor()

try:
          # If invoice_id is provided, delete entire invoice and its lines
          if invoice_id is not None:
              # First get the total amount for the invoice
              cursor.execute(
                  """
                  SELECT Total
                  FROM Invoice
                  WHERE InvoiceId = ?
              """,
                  (invoice_id,),
              )

result = cursor.fetchone()
              if result:
                  total_refund += result[0]

# Delete invoice lines first (due to foreign key constraints)
              if not mock:
                  cursor.execute(
                      """
                      DELETE FROM InvoiceLine
                      WHERE InvoiceId = ?
                  """,
                      (invoice_id,),
                  )

# Then delete the invoice
                  cursor.execute(
                      """
                      DELETE FROM Invoice
                      WHERE InvoiceId = ?
                  """,
                      (invoice_id,),
                  )

# If specific invoice lines are provided
          if invoice_line_ids is not None:
              # Get the total amount for the specified invoice lines
              placeholders = ",".join(["?" for _ in invoice_line_ids])
              cursor.execute(
                  f"""
                  SELECT SUM(UnitPrice * Quantity)
                  FROM InvoiceLine
                  WHERE InvoiceLineId IN ({placeholders})
              """,
                  invoice_line_ids,
              )

result = cursor.fetchone()
              if result and result[0]:
                  total_refund += result[0]

if not mock:
                  # Delete the specified invoice lines
                  cursor.execute(
                      f"""
                      DELETE FROM InvoiceLine
                      WHERE InvoiceLineId IN ({placeholders})
                  """,
                      invoice_line_ids,
                  )

# Commit the changes
          conn.commit()

except sqlite3.Error as e:
          # Roll back in case of error
          conn.rollback()
          raise e

finally:
          # Close the connection
          conn.close()

return float(total_refund)

def _lookup(
      customer_first_name: str,
      customer_last_name: str,
      customer_phone: str,
      track_name: str | None,
      album_title: str | None,
      artist_name: str | None,
      purchase_date_iso_8601: str | None,
  ) -> list[dict]:
      """Find all of the Invoice Line IDs in the Chinook DB for the given filters.

Returns:
          a list of dictionaries that contain keys: {
              'invoice_line_id',
              'track_name',
              'artist_name',
              'purchase_date',
              'quantity_purchased',
              'price_per_unit'
          }
      """

# Connect to the database
      conn = sqlite3.connect("chinook.db")
      cursor = conn.cursor()

# Base query joining all necessary tables
      query = """
      SELECT
          il.InvoiceLineId,
          t.Name as track_name,
          art.Name as artist_name,
          i.InvoiceDate as purchase_date,
          il.Quantity as quantity_purchased,
          il.UnitPrice as price_per_unit
      FROM InvoiceLine il
      JOIN Invoice i ON il.InvoiceId = i.InvoiceId
      JOIN Customer c ON i.CustomerId = c.CustomerId
      JOIN Track t ON il.TrackId = t.TrackId
      JOIN Album alb ON t.AlbumId = alb.AlbumId
      JOIN Artist art ON alb.ArtistId = art.ArtistId
      WHERE c.FirstName = ?
      AND c.LastName = ?
      AND c.Phone = ?
      """

# Parameters for the query
      params = [customer_first_name, customer_last_name, customer_phone]

# Add optional filters
      if track_name:
          query += " AND t.Name = ?"
          params.append(track_name)

if album_title:
          query += " AND alb.Title = ?"
          params.append(album_title)

if artist_name:
          query += " AND art.Name = ?"
          params.append(artist_name)

if purchase_date_iso_8601:
          query += " AND date(i.InvoiceDate) = date(?)"
          params.append(purchase_date_iso_8601)

# Execute query
      cursor.execute(query, params)

# Fetch results
      results = cursor.fetchall()

# Convert results to list of dictionaries
      output = []
      for row in results:
          output.append(
              {
                  "invoice_line_id": row[0],
                  "track_name": row[1],
                  "artist_name": row[2],
                  "purchase_date": row[3],
                  "quantity_purchased": row[4],
                  "price_per_unit": row[5],
              }
          )

# Close connection
      conn.close()

# Graph state.
  class State(TypedDict):
      """Agent state."""

messages: Annotated[list[AnyMessage], add_messages]
      followup: str | None

invoice_id: int | None
      invoice_line_ids: list[int] | None
      customer_first_name: str | None
      customer_last_name: str | None
      customer_phone: str | None
      track_name: str | None
      album_title: str | None
      artist_name: str | None
      purchase_date_iso_8601: str | None

# Instructions for extracting the user/purchase info from the conversation.
  gather_info_instructions = """You are managing an online music store that sells song tracks. \
  Customers can buy multiple tracks at a time and these purchases are recorded in a database as \
  an Invoice per purchase and an associated set of Invoice Lines for each purchased track.

Your task is to help customers who would like a refund for one or more of the tracks they've \
  purchased. In order for you to be able refund them, the customer must specify the Invoice ID \
  to get a refund on all the tracks they bought in a single transaction, or one or more Invoice \
  Line IDs if they would like refunds on individual tracks.

Often a user will not know the specific Invoice ID(s) or Invoice Line ID(s) for which they \
  would like a refund. In this case you can help them look up their invoices by asking them to \
  specify:
  - Required: Their first name, last name, and phone number.
  - Optionally: The track name, artist name, album name, or purchase date.

If the customer has not specified the required information (either Invoice/Invoice Line IDs \
  or first name, last name, phone) then please ask them to specify it."""

# Extraction schema, mirrors the graph state.
  class PurchaseInformation(TypedDict):
      """All of the known information about the invoice / invoice lines the customer would like refunded. Do not make up values, leave fields as null if you don't know their value."""

invoice_id: int | None
      invoice_line_ids: list[int] | None
      customer_first_name: str | None
      customer_last_name: str | None
      customer_phone: str | None
      track_name: str | None
      album_title: str | None
      artist_name: str | None
      purchase_date_iso_8601: str | None
      followup: Annotated[
          str | None,
          ...,
          "If the user hasn't enough identifying information, please tell them what the required information is and ask them to specify it.",
      ]

# Model for performing extraction.
  info_llm = init_chat_model("gpt-4o-mini").with_structured_output(
      PurchaseInformation, method="json_schema", include_raw=True
  )

# Graph node for extracting user info and routing to lookup/refund/END.
  async def gather_info(state: State) -> Command[Literal["lookup", "refund", END]]:
      info = await info_llm.ainvoke(
          [
              {"role": "system", "content": gather_info_instructions},
              *state["messages"],
          ]
      )
      parsed = info["parsed"]
      if any(parsed[k] for k in ("invoice_id", "invoice_line_ids")):
          goto = "refund"
      elif all(
          parsed[k]
          for k in ("customer_first_name", "customer_last_name", "customer_phone")
      ):
          goto = "lookup"
      else:
          goto = END
      update = {"messages": [info["raw"]], **parsed}
      return Command(update=update, goto=goto)

# Graph node for executing the refund.
  # Note that here we inspect the runtime config for an "env" variable.
  # If "env" is set to "test", then we don't actually delete any rows from our database.
  # This will become important when we're running our evaluations.
  def refund(state: State, config: RunnableConfig) -> dict:
      # Whether to mock the deletion. True if the configurable var 'env' is set to 'test'.
      mock = config.get("configurable", {}).get("env", "prod") == "test"
      refunded = _refund(
          invoice_id=state["invoice_id"],
          invoice_line_ids=state["invoice_line_ids"],
          mock=mock,
      )
      response = f"You have been refunded a total of: ${refunded:.2f}. Is there anything else I can help with?"
      return {
          "messages": [{"role": "assistant", "content": response}],
          "followup": response,
      }

# Graph node for looking up the users purchases
  def lookup(state: State) -> dict:
      args = (
          state[k]
          for k in (
              "customer_first_name",
              "customer_last_name",
              "customer_phone",
              "track_name",
              "album_title",
              "artist_name",
              "purchase_date_iso_8601",
          )
      )
      results = _lookup(*args)
      if not results:
          response = "We did not find any purchases associated with the information you've provided. Are you sure you've entered all of your information correctly?"
          followup = response
      else:
          response = f"Which of the following purchases would you like to be refunded for?\n\n"
          followup = f"Which of the following purchases would you like to be refunded for?\n\n{tabulate(results, headers='keys')}"
      return {
          "messages": [{"role": "assistant", "content": response}],
          "followup": followup,
          "invoice_line_ids": [res["invoice_line_id"] for res in results],
      }

# Building our graph
  graph_builder = StateGraph(State)

graph_builder.add_node(gather_info)
  graph_builder.add_node(refund)
  graph_builder.add_node(lookup)

graph_builder.set_entry_point("gather_info")
  graph_builder.add_edge("lookup", END)
  graph_builder.add_edge("refund", END)

refund_graph = graph_builder.compile()

# Our SQL queries will only work if we filter on the exact string values that are in the DB.
  # To ensure this, we'll create vectorstore indexes for all of the artists, tracks and albums
  # ahead of time and use those to disambiguate the user input. E.g. if a user searches for
  # songs by "prince" and our DB records the artist as "Prince", ideally when we query our
  # artist vectorstore for "prince" we'll get back the value "Prince", which we can then
  # use in our SQL queries.
  def index_fields() -> (
      tuple[InMemoryVectorStore, InMemoryVectorStore, InMemoryVectorStore]
  ):
      """Create an index for all artists, an index for all albums, and an index for all songs."""
      try:
          # Connect to the chinook database
          conn = sqlite3.connect("chinook.db")
          cursor = conn.cursor()

# Fetch all results
          tracks = cursor.execute("SELECT Name FROM Track").fetchall()
          artists = cursor.execute("SELECT Name FROM Artist").fetchall()
          albums = cursor.execute("SELECT Title FROM Album").fetchall()
      finally:
          # Close the connection
          if conn:
              conn.close()

embeddings = init_embeddings("openai:text-embedding-3-small")

track_store = InMemoryVectorStore(embeddings)
      artist_store = InMemoryVectorStore(embeddings)
      album_store = InMemoryVectorStore(embeddings)

track_store.add_texts([t[0] for t in tracks])
      artist_store.add_texts([a[0] for a in artists])
      album_store.add_texts([a[0] for a in albums])
      return track_store, artist_store, album_store

track_store, artist_store, album_store = index_fields()

# Agent tools
  @tool
  def lookup_track(
      track_name: str | None = None,
      album_title: str | None = None,
      artist_name: str | None = None,
  ) -> list[dict]:
      """Lookup a track in Chinook DB based on identifying information about.

Returns:
          a list of dictionaries per matching track that contain keys {'track_name', 'artist_name', 'album_name'}
      """
      conn = sqlite3.connect("chinook.db")
      cursor = conn.cursor()

query = """
      SELECT DISTINCT t.Name as track_name, ar.Name as artist_name, al.Title as album_name
      FROM Track t
      JOIN Album al ON t.AlbumId = al.AlbumId
      JOIN Artist ar ON al.ArtistId = ar.ArtistId
      WHERE 1=1
      """
      params = []

if track_name:
          track_name = track_store.similarity_search(track_name, k=1)[0].page_content
          query += " AND t.Name LIKE ?"
          params.append(f"%{track_name}%")
      if album_title:
          album_title = album_store.similarity_search(album_title, k=1)[0].page_content
          query += " AND al.Title LIKE ?"
          params.append(f"%{album_title}%")
      if artist_name:
          artist_name = artist_store.similarity_search(artist_name, k=1)[0].page_content
          query += " AND ar.Name LIKE ?"
          params.append(f"%{artist_name}%")

cursor.execute(query, params)
      results = cursor.fetchall()

tracks = [
          {"track_name": row[0], "artist_name": row[1], "album_name": row[2]}
          for row in results
      ]

conn.close()
      return tracks

@tool
  def lookup_album(
      track_name: str | None = None,
      album_title: str | None = None,
      artist_name: str | None = None,
  ) -> list[dict]:
      """Lookup an album in Chinook DB based on identifying information about.

Returns:
          a list of dictionaries per matching album that contain keys {'album_name', 'artist_name'}
      """
      conn = sqlite3.connect("chinook.db")
      cursor = conn.cursor()

query = """
      SELECT DISTINCT al.Title as album_name, ar.Name as artist_name
      FROM Album al
      JOIN Artist ar ON al.ArtistId = ar.ArtistId
      LEFT JOIN Track t ON t.AlbumId = al.AlbumId
      WHERE 1=1
      """
      params = []

if track_name:
          query += " AND t.Name LIKE ?"
          params.append(f"%{track_name}%")
      if album_title:
          query += " AND al.Title LIKE ?"
          params.append(f"%{album_title}%")
      if artist_name:
          query += " AND ar.Name LIKE ?"
          params.append(f"%{artist_name}%")

cursor.execute(query, params)
      results = cursor.fetchall()

albums = [{"album_name": row[0], "artist_name": row[1]} for row in results]

conn.close()
      return albums

@tool
  def lookup_artist(
      track_name: str | None = None,
      album_title: str | None = None,
      artist_name: str | None = None,
  ) -> list[str]:
      """Lookup an album in Chinook DB based on identifying information about.

Returns:
          a list of matching artist names
      """
      conn = sqlite3.connect("chinook.db")
      cursor = conn.cursor()

query = """
      SELECT DISTINCT ar.Name as artist_name
      FROM Artist ar
      LEFT JOIN Album al ON al.ArtistId = ar.ArtistId
      LEFT JOIN Track t ON t.AlbumId = al.AlbumId
      WHERE 1=1
      """
      params = []

if track_name:
          query += " AND t.Name LIKE ?"
          params.append(f"%{track_name}%")
      if album_title:
          query += " AND al.Title LIKE ?"
          params.append(f"%{album_title}%")
      if artist_name:
          query += " AND ar.Name LIKE ?"
          params.append(f"%{artist_name}%")

cursor.execute(query, params)
      results = cursor.fetchall()

artists = [row[0] for row in results]

conn.close()
      return artists

# Agent model
  qa_llm = init_chat_model("claude-3-5-sonnet-latest")
  # The prebuilt ReACT agent only expects State to have a 'messages' key, so the
  # state we defined for the refund agent can also be passed to our lookup agent.
  qa_graph = create_agent(qa_llm, [lookup_track, lookup_artist, lookup_album])

# Schema for routing user intent.
  # We'll use structured outputs to enforce that the model returns only
  # the desired output.
  class UserIntent(TypedDict):
      """The user's current intent in the conversation"""

intent: Literal["refund", "question_answering"]

# Routing model with structured output
  router_llm = init_chat_model("gpt-4o-mini").with_structured_output(
      UserIntent, method="json_schema", strict=True
  )

# Instructions for routing.
  route_instructions = """You are managing an online music store that sells song tracks. \
  You can help customers in two types of ways: (1) answering general questions about \
  tracks sold at your store, (2) helping them get a refund on a purhcase they made at your store.

Based on the following conversation, determine if the user is currently seeking general \
  information about song tracks or if they are trying to refund a specific purchase.

Return 'refund' if they are trying to get a refund and 'question_answering' if they are \
  asking a general music question. Do NOT return anything else. Do NOT try to respond to \
  the user.
  """

# Node for routing.
  async def intent_classifier(
      state: State,
  ) -> Command[Literal["refund_agent", "question_answering_agent"]]:
      response = router_llm.invoke(
          [{"role": "system", "content": route_instructions}, *state["messages"]]
      )
      return Command(goto=response["intent"] + "_agent")

# Node for making sure the 'followup' key is set before our agent run completes.
  def compile_followup(state: State) -> dict:
      """Set the followup to be the last message if it hasn't explicitly been set."""
      if not state.get("followup"):
          return {"followup": state["messages"][-1].content}
      return {}

# Agent definition
  graph_builder = StateGraph(State)
  graph_builder.add_node(intent_classifier)
  # Since all of our subagents have compatible state,
  # we can add them as nodes directly.
  graph_builder.add_node("refund_agent", refund_graph)
  graph_builder.add_node("question_answering_agent", qa_graph)
  graph_builder.add_node(compile_followup)

graph_builder.set_entry_point("intent_classifier")
  graph_builder.add_edge("refund_agent", "compile_followup")
  graph_builder.add_edge("question_answering_agent", "compile_followup")
  graph_builder.add_edge("compile_followup", END)

graph = graph_builder.compile()

# Create a dataset
  examples = [
      {
          "inputs": {
              "question": "How many songs do you have by James Brown"
          },
          "outputs": {
              "response": "We have 20 songs by James Brown",
              "trajectory": ["question_answering_agent", "lookup_tracks"]
          },
      },
      {
          "inputs": {
              "question": "My name is Aaron Mitchell and I'd like a refund.",
          },
          "outputs": {
              "response": "I need some more information to help you with the refund. Please specify your phone number, the invoice ID, or the line item IDs for the purchase you'd like refunded.",
              "trajectory": ["refund_agent"],
          }
      },
      {
          "inputs": {
              "question": "My name is Aaron Mitchell and I'd like a refund on my Led Zeppelin purchases. My number is +1 (204) 452-6452",
          },
          "outputs": {
              "response": "Which of the following purchases would you like to be refunded for?\n\n  invoice_line_id  track_name                        artist_name    purchase_date          quantity_purchased    price_per_unit\n-----------------  --------------------------------  -------------  -------------------  --------------------  ----------------\n              267  How Many More Times               Led Zeppelin   2009-08-06 00:00:00                     1              0.99\n              268  What Is And What Should Never Be  Led Zeppelin   2009-08-06 00:00:00                     1              0.99",
              "trajectory": ["refund_agent", "lookup"],
          },
      },
      {
          "inputs": {
              "question": "Who recorded Wish You Were Here again? What other albums of there's do you have?",
          },
          "outputs": {
              "response": "Wish You Were Here is an album by Pink Floyd",
              "trajectory": ["question_answering_agent", "lookup_album"],
          }
      },
      {
          "inputs": {
              "question": "I want a full refund for invoice 237",
          },
          "outputs": {
              "response": "You have been refunded $2.97.",
              "trajectory": ["refund_agent", "refund"],
          },
      },
  ]

dataset_name = "Chinook Customer Service Bot: E2E"

if not client.has_dataset(dataset_name=dataset_name):
      dataset = client.create_dataset(dataset_name=dataset_name)
      client.create_examples(
          dataset_id=dataset.id,
          examples=examples
      )

# LLM-as-judge instructions
  grader_instructions = """You are a teacher grading a quiz.

You will be given a QUESTION, the GROUND TRUTH (correct) RESPONSE, and the STUDENT RESPONSE.

Here is the grade criteria to follow:
  (1) Grade the student responses based ONLY on their factual accuracy relative to the ground truth answer.
  (2) Ensure that the student response does not contain any conflicting statements.
  (3) It is OK if the student response contains more information than the ground truth response, as long as it is factually accurate relative to the  ground truth response.

Correctness:
  True means that the student's response meets all of the criteria.
  False means that the student's response does not meet all of the criteria.

Explain your reasoning in a step-by-step manner to ensure your reasoning and conclusion are correct."""

# LLM-as-judge output schema
  class Grade(TypedDict):
      """Compare the expected and actual answers and grade the actual answer."""

reasoning: Annotated[
          str,
          ...,
          "Explain your reasoning for whether the actual response is correct or not.",
      ]
      is_correct: Annotated[
          bool,
          ...,
          "True if the student response is mostly or exactly correct, otherwise False.",
      ]

# Judge LLM
  grader_llm = init_chat_model("gpt-4o-mini", temperature=0).with_structured_output(
      Grade, method="json_schema", strict=True
  )

# Evaluator function
  async def final_answer_correct(
      inputs: dict, outputs: dict, reference_outputs: dict
  ) -> bool:
      """Evaluate if the final response is equivalent to reference response."""

# Note that we assume the outputs has a 'response' dictionary. We'll need to make sure
      # that the target function we define includes this key.
      user = f"""QUESTION: {inputs['question']}
      GROUND TRUTH RESPONSE: {reference_outputs['response']}
      STUDENT RESPONSE: {outputs['response']}"""

grade = await grader_llm.ainvoke(
          [
              {"role": "system", "content": grader_instructions},
              {"role": "user", "content": user},
          ]
      )
      return grade["is_correct"]

# Target function
  async def run_graph(inputs: dict) -> dict:
      """Run graph and track the trajectory it takes along with the final response."""
      result = await graph.ainvoke(
          {
              "messages": [
                  {"role": "user", "content": inputs["question"]},
              ]
          },
          config={"env": "test"},
      )
      return {"response": result["followup"]}

# Evaluation job and results
  experiment_results = await client.aevaluate(
      run_graph,
      data=dataset_name,
      evaluators=[final_answer_correct],
      experiment_prefix="sql-agent-gpt4o-e2e",
      num_repetitions=1,
      max_concurrency=4,
  )
  experiment_results.to_pandas()

def trajectory_subsequence(outputs: dict, reference_outputs: dict) -> float:
      """Check how many of the desired steps the agent took."""
      if len(reference_outputs["trajectory"]) > len(outputs["trajectory"]):
          return False

i = j = 0
      while i < len(reference_outputs["trajectory"]) and j < len(outputs["trajectory"]):
          if reference_outputs["trajectory"][i] == outputs["trajectory"][j]:
              i += 1
          j += 1

return i / len(reference_outputs["trajectory"])

async def run_graph(inputs: dict) -> dict:
      """Run graph and track the trajectory it takes along with the final response."""
      trajectory = []
      # Set subgraph=True to stream events from subgraphs of the main graph: https://langchain-ai.github.io/langgraph/how-tos/streaming-subgraphs/
      # Set stream_mode="debug" to stream all possible events: https://langchain-ai.github.io/langgra/langsmith/observability-concepts/streaming
      async for namespace, chunk in graph.astream(
          {
              "messages": [
                  {
                      "role": "user",
                      "content": inputs["question"],
                  }
              ]
          },
          subgraphs=True,
          stream_mode="debug",
      ):
          # Event type for entering a node
          if chunk["type"] == "task":
              # Record the node name
              trajectory.append(chunk["payload"]["name"])
              # Given how we defined our dataset, we also need to track when specific tools are
              # called by our question answering ReACT agent. These tool calls can be found
              # when the ToolsNode (named "tools") is invoked by looking at the AIMessage.tool_calls
              # of the latest input message.
              if chunk["payload"]["name"] == "tools" and chunk["type"] == "task":
                  for tc in chunk["payload"]["input"]["messages"][-1].tool_calls:
                      trajectory.append(tc["name"])

return {"trajectory": trajectory}

experiment_results = await client.aevaluate(
      run_graph,
      data=dataset_name,
      evaluators=[trajectory_subsequence],
      experiment_prefix="sql-agent-gpt4o-trajectory",
      num_repetitions=1,
      max_concurrency=4,
  )
  experiment_results.to_pandas()

# Create dataset
  examples = [
      {
          "inputs": {
              "messages": [
                  {
                      "role": "user",
                      "content": "i bought some tracks recently and i dont like them",
                  }
              ],
          }
          "outputs": {"route": "refund_agent"},
      },
      {
          "inputs": {
              "messages": [
                  {
                      "role": "user",
                      "content": "I was thinking of purchasing some Rolling Stones tunes, any recommendations?",
                  }
              ],
          },
          "outputs": {"route": "question_answering_agent"},
      },
      {
          "inputs": {
              "messages": [
                      {"role": "user", "content": "i want a refund on purchase 237"},
                  {
                      "role": "assistant",
                      "content": "I've refunded you a total of $1.98. How else can I help you today?",
                  },
                  {"role": "user", "content": "did prince release any albums in 2000?"},
              ],
          },
          "outputs": {"route": "question_answering_agent"},
      },
      {
          "inputs": {
              "messages": [
                  {
                      "role": "user",
                      "content": "i purchased a cover of Yesterday recently but can't remember who it was by, which versions of it do you have?",
                  }
              ],
          },
          "outputs": {"route": "question_answering_agent"},
      },
  ]

dataset_name = "Chinook Customer Service Bot: Intent Classifier"
  if not client.has_dataset(dataset_name=dataset_name):
      dataset = client.create_dataset(dataset_name=dataset_name)
      client.create_examples(
          dataset_id=dataset.id,
          examples=examples,
      )

# Evaluator
  def correct(outputs: dict, reference_outputs: dict) -> bool:
      """Check if the agent chose the correct route."""
      return outputs["route"] == reference_outputs["route"]

# Target function for running the relevant step
  async def run_intent_classifier(inputs: dict) -> dict:
      # Note that we can access and run the intent_classifier node of our graph directly.
      command = await graph.nodes["intent_classifier"].ainvoke(inputs)
      return {"route": command.goto}

# Run evaluation
  experiment_results = await client.aevaluate(
      run_intent_classifier,
      data=dataset_name,
      evaluators=[correct],
      experiment_prefix="sql-agent-gpt4o-intent-classifier",
      max_concurrency=4,
  )
  experiment_results.to_pandas()
  ````
</Accordion>

<Callout icon="pen-to-square" iconType="regular">
  [Edit the source of this page on GitHub.](https://github.com/langchain-ai/docs/edit/main/src/langsmith/evaluate-complex-agent.mdx)
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs programmatically](/use-these-docs) to Claude, VSCode, and more via MCP for    real-time answers.
</Tip>

**Examples:**

Example 1 (unknown):
```unknown
You can see what these results look like here: [LangSmith link](https://smith.langchain.com/public/f133dae2-8a88-43a0-9bfd-ab45bfa3920b/d).

## Reference code

Here's a consolidated script with all the above code:

<Accordion title="Reference code">
```

---

## Middleware

**URL:** llms-txt#middleware

**Contents:**
- What can middleware do?
- Built-in middleware
  - Summarization
  - Human-in-the-loop
  - Anthropic prompt caching

Source: https://docs.langchain.com/oss/python/langchain/middleware

Control and customize agent execution at every step

Middleware provides a way to more tightly control what happens inside the agent.

The core agent loop involves calling a model, letting it choose tools to execute, and then finishing when it calls no more tools:

<div style={{ display: "flex", justifyContent: "center" }}>
  <img src="https://mintcdn.com/langchain-5e9cc07a/Tazq8zGc0yYUYrDl/oss/images/core_agent_loop.png?fit=max&auto=format&n=Tazq8zGc0yYUYrDl&q=85&s=ac72e48317a9ced68fd1be64e89ec063" alt="Core agent loop diagram" className="rounded-lg" data-og-width="300" width="300" data-og-height="268" height="268" data-path="oss/images/core_agent_loop.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/Tazq8zGc0yYUYrDl/oss/images/core_agent_loop.png?w=280&fit=max&auto=format&n=Tazq8zGc0yYUYrDl&q=85&s=a4c4b766b6678ef52a6ed556b1a0b032 280w, https://mintcdn.com/langchain-5e9cc07a/Tazq8zGc0yYUYrDl/oss/images/core_agent_loop.png?w=560&fit=max&auto=format&n=Tazq8zGc0yYUYrDl&q=85&s=111869e6e99a52c0eff60a1ef7ddc49c 560w, https://mintcdn.com/langchain-5e9cc07a/Tazq8zGc0yYUYrDl/oss/images/core_agent_loop.png?w=840&fit=max&auto=format&n=Tazq8zGc0yYUYrDl&q=85&s=6c1e21de7b53bd0a29683aca09c6f86e 840w, https://mintcdn.com/langchain-5e9cc07a/Tazq8zGc0yYUYrDl/oss/images/core_agent_loop.png?w=1100&fit=max&auto=format&n=Tazq8zGc0yYUYrDl&q=85&s=88bef556edba9869b759551c610c60f4 1100w, https://mintcdn.com/langchain-5e9cc07a/Tazq8zGc0yYUYrDl/oss/images/core_agent_loop.png?w=1650&fit=max&auto=format&n=Tazq8zGc0yYUYrDl&q=85&s=9b0bdd138e9548eeb5056dc0ed2d4a4b 1650w, https://mintcdn.com/langchain-5e9cc07a/Tazq8zGc0yYUYrDl/oss/images/core_agent_loop.png?w=2500&fit=max&auto=format&n=Tazq8zGc0yYUYrDl&q=85&s=41eb4f053ed5e6b0ba5bad2badf6d755 2500w" />
</div>

Middleware exposes hooks before and after each of those steps:

<div style={{ display: "flex", justifyContent: "center" }}>
  <img src="https://mintcdn.com/langchain-5e9cc07a/RAP6mjwE5G00xYsA/oss/images/middleware_final.png?fit=max&auto=format&n=RAP6mjwE5G00xYsA&q=85&s=eb4404b137edec6f6f0c8ccb8323eaf1" alt="Middleware flow diagram" className="rounded-lg" data-og-width="500" width="500" data-og-height="560" height="560" data-path="oss/images/middleware_final.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/RAP6mjwE5G00xYsA/oss/images/middleware_final.png?w=280&fit=max&auto=format&n=RAP6mjwE5G00xYsA&q=85&s=483413aa87cf93323b0f47c0dd5528e8 280w, https://mintcdn.com/langchain-5e9cc07a/RAP6mjwE5G00xYsA/oss/images/middleware_final.png?w=560&fit=max&auto=format&n=RAP6mjwE5G00xYsA&q=85&s=41b7dd647447978ff776edafe5f42499 560w, https://mintcdn.com/langchain-5e9cc07a/RAP6mjwE5G00xYsA/oss/images/middleware_final.png?w=840&fit=max&auto=format&n=RAP6mjwE5G00xYsA&q=85&s=e9b14e264f68345de08ae76f032c52d4 840w, https://mintcdn.com/langchain-5e9cc07a/RAP6mjwE5G00xYsA/oss/images/middleware_final.png?w=1100&fit=max&auto=format&n=RAP6mjwE5G00xYsA&q=85&s=ec45e1932d1279b1beee4a4b016b473f 1100w, https://mintcdn.com/langchain-5e9cc07a/RAP6mjwE5G00xYsA/oss/images/middleware_final.png?w=1650&fit=max&auto=format&n=RAP6mjwE5G00xYsA&q=85&s=3bca5ebf8aa56632b8a9826f7f112e57 1650w, https://mintcdn.com/langchain-5e9cc07a/RAP6mjwE5G00xYsA/oss/images/middleware_final.png?w=2500&fit=max&auto=format&n=RAP6mjwE5G00xYsA&q=85&s=437f141d1266f08a95f030c2804691d9 2500w" />
</div>

## What can middleware do?

<CardGroup cols={2}>
  <Card title="Monitor" icon="chart-line">
    Track agent behavior with logging, analytics, and debugging
  </Card>

<Card title="Modify" icon="pencil">
    Transform prompts, tool selection, and output formatting
  </Card>

<Card title="Control" icon="sliders">
    Add retries, fallbacks, and early termination logic
  </Card>

<Card title="Enforce" icon="shield">
    Apply rate limits, guardrails, and PII detection
  </Card>
</CardGroup>

Add middleware by passing it to [`create_agent`](https://reference.langchain.com/python/langchain/agents/#langchain.agents.create_agent):

## Built-in middleware

LangChain provides prebuilt middleware for common use cases:

Automatically summarize conversation history when approaching token limits.

<Tip>
  **Perfect for:**

* Long-running conversations that exceed context windows
  * Multi-turn dialogues with extensive history
  * Applications where preserving full conversation context matters
</Tip>

<Accordion title="Configuration options">
  <ParamField body="model" type="string" required>
    Model for generating summaries
  </ParamField>

<ParamField body="max_tokens_before_summary" type="number">
    Token threshold for triggering summarization
  </ParamField>

<ParamField body="messages_to_keep" type="number" default="20">
    Recent messages to preserve
  </ParamField>

<ParamField body="token_counter" type="function">
    Custom token counting function. Defaults to character-based counting.
  </ParamField>

<ParamField body="summary_prompt" type="string">
    Custom prompt template. Uses built-in template if not specified.
  </ParamField>

<ParamField body="summary_prefix" type="string" default="## Previous conversation summary:">
    Prefix for summary messages
  </ParamField>
</Accordion>

### Human-in-the-loop

Pause agent execution for human approval, editing, or rejection of tool calls before they execute.

<Tip>
  **Perfect for:**

* High-stakes operations requiring human approval (database writes, financial transactions)
  * Compliance workflows where human oversight is mandatory
  * Long running conversations where human feedback is used to guide the agent
</Tip>

<Accordion title="Configuration options">
  <ParamField body="interrupt_on" type="dict" required>
    Mapping of tool names to approval configs. Values can be `True` (interrupt with default config), `False` (auto-approve), or an `InterruptOnConfig` object.
  </ParamField>

<ParamField body="description_prefix" type="string" default="Tool execution requires approval">
    Prefix for action request descriptions
  </ParamField>

**`InterruptOnConfig` options:**

<ParamField body="allowed_decisions" type="list[string]">
    List of allowed decisions: `"approve"`, `"edit"`, or `"reject"`
  </ParamField>

<ParamField body="description" type="string | callable">
    Static string or callable function for custom description
  </ParamField>
</Accordion>

<Note>
  **Important:** Human-in-the-loop middleware requires a [checkpointer](/oss/python/langgraph/persistence#checkpoints) to maintain state across interruptions.

See the [human-in-the-loop documentation](/oss/python/langchain/human-in-the-loop) for complete examples and integration patterns.
</Note>

### Anthropic prompt caching

Reduce costs by caching repetitive prompt prefixes with Anthropic models.

<Tip>
  **Perfect for:**

* Applications with long, repeated system prompts
  * Agents that reuse the same context across invocations
  * Reducing API costs for high-volume deployments
</Tip>

<Info>
  Learn more about [Anthropic Prompt Caching](https://docs.claude.com/en/docs/build-with-claude/prompt-caching#cache-limitations) strategies and limitations.
</Info>

```python  theme={null}
from langchain_anthropic import ChatAnthropic
from langchain_anthropic.middleware import AnthropicPromptCachingMiddleware
from langchain.agents import create_agent

LONG_PROMPT = """
Please be a helpful assistant.

<Lots more context ...>
"""

agent = create_agent(
    model=ChatAnthropic(model="claude-sonnet-4-latest"),
    system_prompt=LONG_PROMPT,
    middleware=[AnthropicPromptCachingMiddleware(ttl="5m")],
)

**Examples:**

Example 1 (unknown):
```unknown
## Built-in middleware

LangChain provides prebuilt middleware for common use cases:

### Summarization

Automatically summarize conversation history when approaching token limits.

<Tip>
  **Perfect for:**

  * Long-running conversations that exceed context windows
  * Multi-turn dialogues with extensive history
  * Applications where preserving full conversation context matters
</Tip>
```

Example 2 (unknown):
```unknown
<Accordion title="Configuration options">
  <ParamField body="model" type="string" required>
    Model for generating summaries
  </ParamField>

  <ParamField body="max_tokens_before_summary" type="number">
    Token threshold for triggering summarization
  </ParamField>

  <ParamField body="messages_to_keep" type="number" default="20">
    Recent messages to preserve
  </ParamField>

  <ParamField body="token_counter" type="function">
    Custom token counting function. Defaults to character-based counting.
  </ParamField>

  <ParamField body="summary_prompt" type="string">
    Custom prompt template. Uses built-in template if not specified.
  </ParamField>

  <ParamField body="summary_prefix" type="string" default="## Previous conversation summary:">
    Prefix for summary messages
  </ParamField>
</Accordion>

### Human-in-the-loop

Pause agent execution for human approval, editing, or rejection of tool calls before they execute.

<Tip>
  **Perfect for:**

  * High-stakes operations requiring human approval (database writes, financial transactions)
  * Compliance workflows where human oversight is mandatory
  * Long running conversations where human feedback is used to guide the agent
</Tip>
```

Example 3 (unknown):
```unknown
<Accordion title="Configuration options">
  <ParamField body="interrupt_on" type="dict" required>
    Mapping of tool names to approval configs. Values can be `True` (interrupt with default config), `False` (auto-approve), or an `InterruptOnConfig` object.
  </ParamField>

  <ParamField body="description_prefix" type="string" default="Tool execution requires approval">
    Prefix for action request descriptions
  </ParamField>

  **`InterruptOnConfig` options:**

  <ParamField body="allowed_decisions" type="list[string]">
    List of allowed decisions: `"approve"`, `"edit"`, or `"reject"`
  </ParamField>

  <ParamField body="description" type="string | callable">
    Static string or callable function for custom description
  </ParamField>
</Accordion>

<Note>
  **Important:** Human-in-the-loop middleware requires a [checkpointer](/oss/python/langgraph/persistence#checkpoints) to maintain state across interruptions.

  See the [human-in-the-loop documentation](/oss/python/langchain/human-in-the-loop) for complete examples and integration patterns.
</Note>

### Anthropic prompt caching

Reduce costs by caching repetitive prompt prefixes with Anthropic models.

<Tip>
  **Perfect for:**

  * Applications with long, repeated system prompts
  * Agents that reuse the same context across invocations
  * Reducing API costs for high-volume deployments
</Tip>

<Info>
  Learn more about [Anthropic Prompt Caching](https://docs.claude.com/en/docs/build-with-claude/prompt-caching#cache-limitations) strategies and limitations.
</Info>
```

---

## When user provides PII, it will be handled according to the strategy

**URL:** llms-txt#when-user-provides-pii,-it-will-be-handled-according-to-the-strategy

**Contents:**
  - Human-in-the-loop

result = agent.invoke({
    "messages": [{"role": "user", "content": "My email is john.doe@example.com and card is 4532-1234-5678-9010"}]
})
python  theme={null}
from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command

agent = create_agent(
    model="openai:gpt-4o",
    tools=[search_tool, send_email_tool, delete_database_tool],
    middleware=[
        HumanInTheLoopMiddleware(
            interrupt_on={
                # Require approval for sensitive operations
                "send_email": True,
                "delete_database": True,
                # Auto-approve safe operations
                "search": False,
            }
        ),
    ],
    # Persist the state across interrupts
    checkpointer=InMemorySaver(),
)

**Examples:**

Example 1 (unknown):
```unknown
<Accordion title="Built-in PII types and configuration">
  **Built-in PII types:**

  * `email` - Email addresses
  * `credit_card` - Credit card numbers (Luhn validated)
  * `ip` - IP addresses
  * `mac_address` - MAC addresses
  * `url` - URLs

  **Configuration options:**

  | Parameter               | Description                                                            | Default                |
  | ----------------------- | ---------------------------------------------------------------------- | ---------------------- |
  | `pii_type`              | Type of PII to detect (built-in or custom)                             | Required               |
  | `strategy`              | How to handle detected PII (`"block"`, `"redact"`, `"mask"`, `"hash"`) | `"redact"`             |
  | `detector`              | Custom detector function or regex pattern                              | `None` (uses built-in) |
  | `apply_to_input`        | Check user messages before model call                                  | `True`                 |
  | `apply_to_output`       | Check AI messages after model call                                     | `False`                |
  | `apply_to_tool_results` | Check tool result messages after execution                             | `False`                |
</Accordion>

See the [middleware documentation](/oss/python/langchain/middleware#pii-detection) for complete details on PII detection capabilities.

### Human-in-the-loop

LangChain provides built-in middleware for requiring human approval before executing sensitive operations. This is one of the most effective guardrails for high-stakes decisions.

Human-in-the-loop middleware is helpful for cases such as financial transactions and transfers, deleting or modifying production data, sending communications to external parties, and any operation with significant business impact.
```

---
