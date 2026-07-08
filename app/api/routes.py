from fastapi import APIRouter

from app.graph.workflow import graph

router = APIRouter()


@router.post("/research")
def research():

    result = graph.invoke(
        {
            "topic": "LangGraph",

            "planner_output": "",

            "search_results": "",

            "documentation": "",

            "github_analysis": "",

            "review": "",

            "report": ""
        }
    )

    return result
