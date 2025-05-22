import asyncio
import os

from agno.agent import Agent

from .tools.raindrop import RaindropTools

RAINDROP_ACCESS_TOKEN = os.getenv("RAINDROP_ACCESS_TOKEN")

raindrop_toolkit = RaindropTools(
    access_token=RAINDROP_ACCESS_TOKEN,
)

# Create an agent with the toolkit
raindrop_agent = Agent(
    name="Raindrop Agent",
    tools=[raindrop_toolkit],
    show_tool_calls=True,
    instructions="You are a helpful assistant that can help me with my raindrops. Add as summary the raindrops that you find.",
    markdown=True,
    )

if __name__ == "__main__":
    asyncio.run(raindrop_agent.aprint_response("get raindrops from 2025-01-01 to 2025-04-30 with tag 'python'"))
