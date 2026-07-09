from typing import TypedDict


class SearchResult(TypedDict):
    title: str
    url: str
    snippet: str


class ResearchState(TypedDict):

    topic: str

    planner_output: list[str]

    search_results: list[SearchResult]

    documentation: list[str]

    github_analysis: dict

    review: str

    report: str
