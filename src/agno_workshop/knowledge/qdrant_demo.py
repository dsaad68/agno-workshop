import asyncio

from agno.agent import Agent
from agno.knowledge.knowledge import Knowledge
from agno.vectordb.qdrant import Qdrant

COLLECTION_NAME = "pdf-documents"

vector_db = Qdrant(collection=COLLECTION_NAME, url="http://localhost:6333")

# Create a knowledge instance using Qdrant vector storage
knowledge = Knowledge(
    vector_db=vector_db,
)


# Create an agent with the knowledge
agent = Agent(
    knowledge=knowledge,
    search_knowledge=True,
)

if __name__ == "__main__":
    # Asynchronously add the content of the PDF file to the knowledge.
    asyncio.run(
        knowledge.add_content_async(
            path="data/pdf",
        ),
    )

    # Create and use the agent
    asyncio.run(agent.aprint_response("How to make Thai curry?", markdown=True))
