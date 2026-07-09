from app.graph.state import ResearchState
from app.prompts.reviewer import REVIEWER_PROMPT
from app.services.llm_service import get_llm

llm = get_llm()


def reviewer_node(state: ResearchState) -> ResearchState:
    """
    Reviewer Agent

    Combines planner output,
    search results,
    and GitHub analysis into
    structured technical notes.
    """

    # Convert search results into readable text
    search_summary = ""

    for item in state["search_results"]:
        search_summary += f"""
Title:
{item["title"]}

URL:
{item["url"]}

Snippet:
{item["snippet"]}

"""

    prompt = REVIEWER_PROMPT.format(
        topic=state["topic"],
        plan="\n".join(state["planner_output"]),
        summary=search_summary,
        github=state["github_analysis"],
    )

    response = llm.invoke(prompt)

    state["review"] = response.content

    return state
