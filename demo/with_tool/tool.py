from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools

tool_agent = Agent(
    name="Simple Tool",
    model=OpenAIChat(id="gpt-4.1"),
    tools=[YFinanceTools(stock_price=True,
                        analyst_recommendations=True,
                        company_info=True,
                        company_news=True)],
    instructions="Use tables to display data.",
    show_tool_calls=True,
    markdown=True,
)

if __name__ == "__main__":
    tool_agent.print_response("Write a report comparing NVDA to TSLA", stream=True)
