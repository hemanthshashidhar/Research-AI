from app.graph.state import ResearchState
from app.prompts.planner import PLANNER_PROMPT
from app.services.llm_service import get_llm


llm = get_llm()


def planner_node(state: ResearchState) -> ResearchState:
    """
    Planner Agent

    Receives the research topic and generates
    an execution plan.
    """

    prompt = PLANNER_PROMPT.format(
        topic=state["topic"]
    )

    response = llm.invoke(prompt)

    plan = []

    for line in response.content.split("\n"):

        line = line.strip()

        if not line:
            continue

        if line[0].isdigit():

            line = line.split(".", 1)[-1].strip()

        plan.append(line)

    state["planner_output"] = plan

    return state
