from app.graph.state import ResearchState
from app.prompts.search import SEARCH_PROMPT
from app.services.llm_service import get_llm
from app.services.search_service import web_search

llm = get_llm()


def search_node(state: ResearchState) -> ResearchState:
    """
    Search Agent

    Performs web research and stores
    a summarized result.
    """

    search_results = web_search(
        state["topic"]
    )

    formatted_results = ""

    for index, item in enumerate(
        search_results,
        start=1,
    ):

        formatted_results += f"""
Result {index}

Title:
{item["title"]}

URL:
{item["url"]}

Snippet:
{item["snippet"]}

"""

    prompt = SEARCH_PROMPT.format(
        topic=state["topic"],
        results=formatted_results,
    )

    response = llm.invoke(prompt)

    state["search_results"] = [
        response.content
    ]

    return state
