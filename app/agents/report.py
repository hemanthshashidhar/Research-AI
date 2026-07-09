from app.graph.state import ResearchState
from app.prompts.report import REPORT_PROMPT
from app.services.llm_service import get_llm

llm = get_llm()


def report_node(state: ResearchState) -> ResearchState:
    """
    Report Agent

    Generates the final research report.
    """

    prompt = REPORT_PROMPT.format(
        topic=state["topic"],
        review=state["review"],
        github=state["github_analysis"],
    )

    response = llm.invoke(prompt)

    state["report"] = response.content

    return state
