from app.graph.state import ResearchState
from app.services.github_service import search_repository


def github_node(state: ResearchState) -> ResearchState:
    """
    GitHub Agent

    Searches GitHub for the most relevant repository
    related to the research topic.
    """

    repository = search_repository(state["topic"])

    state["github_analysis"] = repository

    return state
