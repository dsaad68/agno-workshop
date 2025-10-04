from agno.os import AgentOS

from agno_workshop.team.coordinate import financial_agent_team

agent_os = AgentOS(
    id="my-first-os",
    description="My first AgentOS",
    teams=[financial_agent_team],
)

app = agent_os.get_app()

if __name__ == "__main__":
    agent_os.serve(app="agno_workshop.agentos.app:app", reload=True)
