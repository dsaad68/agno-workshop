import asyncio

from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.qdrant import Qdrant

COLLECTION_NAME = "thai-recipes"

# Initialize Qdrant with local instance
vector_db = Qdrant(
    collection=COLLECTION_NAME,
    url="http://localhost:6333",
)

# Create knowledge base
knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=vector_db,
)

knowledge_agent = Agent(
    name="Knowledge Agent",
    role="Search the knowledge base for information",
    knowledge=knowledge_base,
    show_tool_calls=True,
    markdown=True,
)

if __name__ == "__main__":
    # Load knowledge base asynchronously
    asyncio.run(knowledge_base.aload(recreate=True))  # Comment out after first run

    # Create and use the agent asynchronously
    asyncio.run(knowledge_agent.aprint_response("What are the 3 categories of Thai SELECT is given to restaurants overseas?", markdown=True))
