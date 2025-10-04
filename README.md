# agno-workshop

> 🆕 **Update:** This repository now reflects the latest features and improvements introduced in `Agno V2.0`.

This the sample codes and demo suite for `Introduction to LLM Workshop 2.0` with [Agno](https://docs.agno.com) — a lightweight, model-agnostic framework for reasoning agents, multimodal agents, and agentic workflows.

## 📦 Installation & Environment Setup

#### 0. Installing `uv`

on mac and Linux:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

on windows:
```shell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
or with pip:
```bash
pip install uv
```

#### 1. Clone this repo

```bash
git clone https://github.com/dsaad68/agno-workshop.git
cd agno-workshop
```

#### 2. Install dependencies 

```bash
uv sync --frozen
```

#### 3. Set up API keys

- For OpenAI: `export OPENAI_API_KEY=sk-...`
- For Raindrop Agent: `export RAINDROP_ACCESS_TOKEN=...`

---

## ▶️ Running the Demos

This repo includes several demo agents to showcase Agno's capabilities:

### 1. Barebone Agent
A minimal agent using OpenAI GPT-4.1. Answers general questions.
```bash
uv run src/agno_workshop/simple/agent.py
```

### 2. Simple Tool Agent
Agent with YFinance tools for financial data, company info, and news.
```bash
uv run src/agno_workshop/with_tool/internal_tool.py
```

### 3. Raindrop Agent
Agent with a custom toolkit for querying Raindrop bookmarks by date and tag. More about [Raindrop.io](https://raindrop.io/).
Requires `RAINDROP_ACCESS_TOKEN`. Visit [Raindrop.io](https://raindrop.io/settings/applications) to get your token.
```bash
uv run src/agno_workshop/with_tool/raindrop_agent/agent.py
```

### 4. Knowledge Agent
Agent that create a simple RAG over PDFs.

#### Qdrant Database
Requires `Qdrant` Vector Database.

1. Setup the Vector Database:
```bash
docker run -p 6333:6333 -p 6334:6334 \
  -v $(pwd)/qdrant_storage:/qdrant/storage:z \
  qdrant/qdrant
```

2. Run the agent:
```bash
uv run src/agno_workshop/knowledge/qdrant_demo.py
```

#### SurrealDB Database
Requires `SurrealDB` Vector Database.

1. Setup the Vector Database:
```bash
docker run --rm --pull always -p 8000:8000 \
  surrealdb/surrealdb:latest start \
  --user root --pass root
```
2. Run the agent:
```bash
uv run src/agno_workshop/knowledge/surrealdb_demo.py
```

### 5. Agent with Reasoning Tool
Agent that uses a reasoning tool to answer questions.
```bash
uv run src/agno_workshop/reasoning/reasoning_tool.py
```

### 6. Agent with Reasoning LLM
Agent that uses a reasoning LLM to answer questions.
```bash
uv run src/agno_workshop/reasoning/reasoning_with_llm.py
```

### 7. Agent with Memory
Agent that uses a memory to answer questions.
```bash
uv run src/agno_workshop/memory/simple.py
```

### 8. Agent Team
Agent Team that contains two agents:
- Web Agent: Search the web for information
- Finance Agent: Get financial data

They are working together to do a research on a given topic.

```bash
uv run src/agno_workshop/team/coordinate.py
```

---

## 🖥️ Agno AgentOS (FastAPI App)

You can launch a playground UI to interact with all agents:

```bash
uv run src/agno_workshop/agentos/app.py
```

This starts a FastAPI app with a chat interface for all demo agents.

---

## 💬 Agent UI (Next.js Frontend)

A modern chat UI for Agno agents is included in `agent-ui/`.
The Agent UI doesn't support Agent Team & Agent Workflow.

### Quick Start

```bash
npx create-agent-ui@latest
cd agent-ui
npm run dev
```

- Open [http://localhost:3000](http://localhost:3000) to chat with your agents.
- By default, connects to `http://localhost:7777` (configurable in the UI).
- See [agent-ui/README.md](agent-ui/README.md) for more.
