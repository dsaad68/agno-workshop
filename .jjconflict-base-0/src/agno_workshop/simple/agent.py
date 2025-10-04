from agno.agent import Agent
from agno.models.openai import OpenAIChat

barebone_agent = Agent(
    name="Barebone Agent",
    model=OpenAIChat(id="gpt-4.1"),
    instructions="You are a helpful assistant that can answer users questions.",
    markdown=True,
    )

if __name__ == "__main__":
    barebone_agent.print_response("What is what, when is now?")
