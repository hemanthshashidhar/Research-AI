from typing import TypedDict


class ResearchState(TypedDict):
    topic: str

    planner_output: list[str]

    search_results: list[str]

    documentation: list[str]

    github_analysis: dict

    review: str

    report: str
