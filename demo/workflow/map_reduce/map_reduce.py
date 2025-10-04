from agents import JokeTopics, joke_selector_agent, joke_teller_agent, joke_topic_generator_agent
from agno.workflow import Parallel, Step, StepInput, StepOutput, Workflow


def dynamic_map_parallel(step_input: StepInput) -> StepOutput:
    """Dynamic map parallel function for telling jokes based on topics.

    Args:
        step_input (StepInput): Step input containing topics from previous step.

    Returns:
        StepOutput: Step output with jokes from all topics.
    """
    # Read the joke topics from the previous step's content
    raw = step_input.previous_step_content or step_input.input or "[]"

    topics = raw.topics if isinstance(raw, JokeTopics) else []

    if not topics:
        return StepOutput(step_name="Dynamic Map", content="No topics found to execute in parallel.")

    # Build a Parallel of function steps, one per topic
    def make_joke_teller_step(topic: str, index: int) -> Step:
        def run_joke_teller(_: StepInput) -> StepOutput:
            # Run the joke teller agent as a one-off step to ensure proper StepOutput
            tell_joke_step = Step(name=f"joke_teller_{index}", agent=joke_teller_agent, max_retries=1)
            # Create a fresh StepInput so the agent receives the topic as its message
            return tell_joke_step.execute(StepInput(input=f"Tell a joke for this topic: {topic}"), session_state={})
        return Step(name=f"Joke Teller {index}", executor=run_joke_teller)

    parallel = Parallel(
        *[make_joke_teller_step(topic, index) for index, topic in enumerate(topics)],  # pyright: ignore[reportArgumentType]
        name="Map: Joke Teller Topics",
    )

    # Execute the dynamic Parallel with the same StepInput context
    return parallel.execute(step_input)


workflow = Workflow(
    name="Parallel Joke Teller Pipeline",
    steps=[
        Step(name="Joke Topic Generation", agent=joke_topic_generator_agent),
        Step(name="Map (Dynamic Parallel)", executor=dynamic_map_parallel),
        Step(name="Joke Selection", agent=joke_selector_agent),
    ],
    stream_intermediate_steps=True,
)

if __name__ == "__main__":
    workflow.print_response("Tell me 3 jokes", markdown=True)
