from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from pydantic import BaseModel


class JokeTopics(BaseModel):
    """A list of joke topics."""
    topics: list[str]


class Joke(BaseModel):
    """A joke."""
    joke: str


class BestJoke(BaseModel):
    """Best Selected joke."""
    joke: str
    topic: str
    reason: str


joke_topic_generator_agent = Agent(
    name="Joke Topic Generator Agent",
    model=OpenAIChat(id="gpt-4o"),
    instructions=dedent("""
        You are a helpful assistant that can generate joke topics.
        When asked to generate N jokes, you will generate N joke topics.
        Return ONLY valid JSON object with a 'topics' array: {"topics": ["string"]}. No prose.
        Example: {"topics": ["A robot trying to understand human emotions"]}
        """),
    output_schema=JokeTopics,
    )

joke_teller_agent = Agent(
    name="Joke Agent",
    model=OpenAIChat(id="gpt-4o"),
    instructions=dedent("""
        You are a helpful assistant that can tell jokes. Tell a joke for the given topic.
        Example:
            Topic: A robot trying to understand human emotions
            Joke: "Why did the robot fail its human emotions test? It only felt "battery-low" and "404-error".
        """),
    output_schema=Joke,
    )

joke_selector_agent = Agent(
    name="Joke Judge Agent",
    model=OpenAIChat(id="gpt-4o"),
    instructions=dedent("""
        You are a helpful assistant that can judge jokes. Select the best joke from given list of jokes.
        Also provide a reason for your selection.
        Example:
            Topic: A robot trying to understand human emotions
            Joke: "Why did the robot fail its human emotions test? It only felt "battery-low" and "404-error".
            Reason: The joke is funny and it makes a good point about how robots don't understand human emotions.
        """),
    output_schema=BestJoke,
    )
