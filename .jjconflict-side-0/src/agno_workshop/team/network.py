from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    instructions=dedent("""
        Always include sources
        """),
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools()],
    instructions=dedent("""
        Use tables to display data
        Be extremely detail-oriented in your reporting.
        """),
    markdown=True,
)

agent_team = Team(
    name="Financial Agent Team",
    delegate_task_to_all_members=True,
    members=[web_agent, finance_agent],
    model=OpenAIChat(id="gpt-4o"),
    instructions=dedent("""
                    You are the facilitator of a team of expert agents working together to create a thorough, data-driven financial report.
                    Your responsibilities:
                    - Actively guide the discussion, ensuring all agents share their unique insights and expertise.
                    - Foster collaboration and make sure every relevant perspective is considered.
                    - Encourage agents to reference and build upon each other's findings using the shared memory.
                    - Conclude the discussion only when the team has reached a clear consensus and the report is complete.

                    The final report must:
                    - Be well-organized, with clear sections and actionable insights.
                    - Present data in tables where appropriate.
                    - Always cite credible sources for all information and data.

                    Discussion rules:
                    - Each member should contribute at least 2 turns to the discussion.
                    - The discussion should not exceed 3 turns per member.
                    - Ensure the conversation remains focused and productive.

                    Your goal is to facilitate a collaborative process that results in a high-quality, consensus-driven financial report.
                    """),
    show_members_responses=True,
    markdown=True,
)

if __name__ == "__main__":

    agent_team.print_response("What's the market outlook and financial performance of AI semiconductor companies?", stream=True)
