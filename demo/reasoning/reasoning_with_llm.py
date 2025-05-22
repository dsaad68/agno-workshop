from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools

reason_llm_agent = Agent(
    name="Reasoning Agent",
    model=OpenAIChat(id="o3-mini"),
    tools=[YFinanceTools(stock_price=True,
                        analyst_recommendations=True,
                        company_info=True,
                        company_news=True)],
    instructions="Use tables to display data.",
    show_tool_calls=True,
    markdown=True,
)

if __name__ == "__main__":
    reason_llm_agent.print_response("Write a report comparing NVDA to TSLA",
                            stream=True,
                            show_full_reasoning=True,
                            stream_intermediate_steps=True,
                            show_reasoning=True,
                            )
