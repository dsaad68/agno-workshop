from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.team import Team

spanish_agent = Agent(
    name="Spanish Agent",
    role="Search the web for information",
    model=OpenAIChat(id="gpt-4o"),
    instructions="Translate given text into Spanish",
    markdown=True,
)

chinese_agent = Agent(
    name="Chinese Agent",
    role="You are a Chinese translator.",
    model=OpenAIChat(id="gpt-4o"),
    instructions="Translate given text into Chinese",
    markdown=True,
)

japanese_agent = Agent(
    name="Japanese Agent",
    role="You are a Japanese translator.",
    model=OpenAIChat(id="gpt-4o"),
    instructions="Translate given text into Japanese",
    markdown=True,
)

agent_team = Team(
    name="Translator Agent Team",
    # Mode is here is router mode
    determine_input_for_members=True,
    respond_directly=True,
    members=[spanish_agent, chinese_agent, japanese_agent],
    model=OpenAIChat(id="gpt-4o"),
    instructions=dedent("""
                    Your role is to route the request to the appropriate agent.
                    When a translation request is received, determine which language are required (Spanish, Chinese, or Japanese) and route the request to the appropriate agent.
                    Ensure that each agent only receives the text relevant to their language.
                    """),
    markdown=True,
)

if __name__ == "__main__":
    agent_team.print_response("Translate 'I love pizza with pineapple.' into Spanish", stream=True)
