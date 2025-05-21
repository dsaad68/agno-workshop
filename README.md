# agno-workshop

A practical workshop and demo suite for building advanced AI agents with [Agno](https://docs.agno.com) — a lightweight, model-agnostic framework for reasoning agents, multimodal agents, and agentic workflows.

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

#### 1. Clone this repo

```bash
git clone https://github.com/your-org/agno-workshop.git
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
uv run demo/simple/agent.py
```

### 2. Simple Tool Agent
Agent with YFinance tools for financial data, company info, and news.
```bash
uv run demo/with_tool/tool.py
```

### 3. Raindrop Agent
Agent with a custom toolkit for querying Raindrop bookmarks by date and tag.
Requires `RAINDROP_ACCESS_TOKEN`.
```bash
uv run demo/with_tool/raindrop_agent/agent.py
```

### 4. Knowledge Agent
Agent that create a simple RAG over PDFs.
Requires `Qdrant` Vector Database.

1. Setup the Vector Database:
```bash
docker run -p 6333:6333 -p 6334:6334 \
  -v $(pwd)/qdrant_storage:/qdrant/storage:z \
  qdrant/qdrant
```

2. Run the agent:
```bash
uv run demo/knowledge/qdrant-demo.py
```

### 5. Agent Team
Agent Team that contains two agents:
- Web Agent: Search the web for information
- Finance Agent: Get financial data

They are working together to do a research on a given topic.

```bash
uv run demo/team/coordinate.py
```

---

## 🖥️ Agent Playground (FastAPI App)

You can launch a playground UI to interact with all agents:

```bash
uv run main.py
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

---

## 📚 Documentation & Community

- [Agno Docs](https://docs.agno.com)
- [Getting Started Cookbook](https://docs.agno.com/cookbook)
- [Community Forum](https://community.agno.com)
- [Discord Chat](https://discord.gg/agno)



