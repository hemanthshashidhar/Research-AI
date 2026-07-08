from typing import TypedDict


class ResearchState(TypedDict):
    topic: str

    planner_output: str

    search_results: str

    documentation: str

    github_analysis: str

    review: str

    report: str
