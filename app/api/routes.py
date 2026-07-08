from fastapi import APIRouter

from app.graph.workflow import graph
from app.schemas.research import ResearchRequest

router = APIRouter()


@router.post("/research")
def research(request: ResearchRequest):

    result = graph.invoke(
        {
            "topic": request.topic,
            "planner_output": [],
            "search_results": [],
            "documentation": [],
            "github_analysis": {},
            "review": "",
            "report": ""
        }
    )

    return result
