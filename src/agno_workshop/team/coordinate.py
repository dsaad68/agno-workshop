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
    instructions="Always include sources",
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools()],
    instructions="Use tables to display data",
    markdown=True,
)

financial_agent_team = Team(
    name="Financial Agent Team",
    # Mode is here is coordinate mode
    determine_input_for_members=True,
    members=[web_agent, finance_agent],
    model=OpenAIChat(id="gpt-4o"),
    instructions=dedent("""
                    You are the coordinator of a team of expert agents collaborating to produce a comprehensive, data-driven financial news report.
                    Guide the discussion, encourage collaboration, and ensure all relevant perspectives are considered.
                    The final report should be well-structured, with clear sections, actionable insights, and data presented in tables where appropriate.
                    Always cite credible sources for all information and data.
                    Instruct team members to leverage their unique expertise and share relevant findings to enhance the overall quality and coherence of the report.
                    """),
    markdown=True,
)

if __name__ == "__main__":

    financial_agent_team.print_response("What's the market outlook and financial performance of AI semiconductor companies?", stream=True)
