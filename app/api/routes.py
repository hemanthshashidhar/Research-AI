from fastapi import APIRouter

from app.graph.workflow import graph
from app.schemas.research import ResearchRequest

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


@router.post("/research")
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

    # Execute LangGraph workflow
    result = graph.invoke(state)

    return {
    "topic": result["topic"],
    "execution_plan": result["planner_output"],
    "search_summary": result["search_results"],
    "github": result["github_analysis"],
    "review": result["review"],
    "report": result["report"],
            }


