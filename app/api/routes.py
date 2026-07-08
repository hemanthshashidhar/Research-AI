from fastapi import APIRouter

from app.graph.workflow import graph
from app.schemas.research import (
    ResearchRequest,
    ResearchResponse,
)

router = APIRouter()


@router.get("/")
def home():
    return {
        "project": "ResearchOS AI",
        "status": "running",
    }


@router.get("/health")
def health():
    return {
        "status": "healthy",
    }


@router.post(
    "/research",
    response_model=ResearchResponse,
)
def research(request: ResearchRequest):

    state = {
        "topic": request.topic,
        "planner_output": [],
        "search_results": [],
        "documentation": [],
        "github_analysis": {},
        "review": "",
        "report": "",
    }

    result = graph.invoke(state)

    return ResearchResponse(
        topic=result["topic"],
        execution_plan=result["planner_output"],
    )
