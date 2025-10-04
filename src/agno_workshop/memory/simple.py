from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.openai import OpenAIChat
from rich.pretty import pprint

# UserId for the memories
user_id = "ava"
# Database file for memory and storage
db_file = "tmp/agno.db"

# Initialize storage
db = SqliteDb(db_file=db_file)
db.clear_memories()

# Initialize Agent
memory_agent = Agent(
    name="Agent with Memory",
    model=OpenAIChat(id="gpt-4o"),
    # Store memories in a database
    db=db,
    # Give the Agent the ability to update memories
    enable_agentic_memory=True,
    # OR - Run the MemoryManager after each response
    enable_user_memories=True,
    # Number of history runs
    num_history_runs=3,
    markdown=True,
)

if __name__ == "__main__":

    memory_agent.print_response(
    "My name is Ava and I like to ski.",
    user_id=user_id,
    stream=True,
    stream_intermediate_steps=True,
    )
    pprint("Memories about Ava:")
    pprint(memory_agent.get_user_memories(user_id=user_id))

    memory_agent.print_response(
        "I live in san francisco, where should i move within a 4 hour drive?",
        user_id=user_id,
        stream=True,
        stream_intermediate_steps=True,
    )
    pprint("Memories about Ava:")
    pprint(memory_agent.get_user_memories(user_id=user_id))
