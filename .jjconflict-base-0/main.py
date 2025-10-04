from agno.playground import Playground, serve_playground_app

from demo.knowledge.qdrant_demo import knowledge_agent
from demo.memory.simple import memory_agent
from demo.reasoning.reasoning_tool import reasoning_agent
from demo.reasoning.reasoning_with_llm import reason_llm_agent
from demo.simple.agent import barebone_agent
from demo.team.coordinate import finance_agent, web_agent
from demo.with_tool.raindrop_agent.agent import raindrop_agent
from demo.with_tool.tool import tool_agent

app = Playground(agents=[tool_agent,
                        raindrop_agent,
                        barebone_agent,
                        knowledge_agent,
                        web_agent,
                        finance_agent,
                        memory_agent,
                        reasoning_agent,
                        reason_llm_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("main:app", reload=True)
