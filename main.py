from agno.playground import Playground, serve_playground_app

from demo.knowledge.qdrant_demo import knowledge_agent
from demo.simple.agent import barebone_agent
from demo.team.coordinate import finance_agent, web_agent
from demo.with_tool.raindrop_agent.agent import raindrop_agent
from demo.with_tool.tool import tool_agent

app = Playground(agents=[tool_agent, raindrop_agent, barebone_agent, knowledge_agent, web_agent, finance_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("main:app", reload=True)
