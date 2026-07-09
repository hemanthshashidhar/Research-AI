from app.graph.state import ResearchState

from app.services.github_service import (
    extract_repo_from_search_results,
    get_repository,
    search_repository,
)


def github_node(state: ResearchState) -> ResearchState:
    """
    GitHub Agent

    1. Look for GitHub repositories in the
       search results.

    2. If found, analyze that repository.

    3. Otherwise perform a GitHub search.
    """

    repo = extract_repo_from_search_results(
        state["search_results"]
    )

    if repo:

        state["github_analysis"] = get_repository(repo)

    else:

        state["github_analysis"] = search_repository(
            state["topic"]
        )

    return state
