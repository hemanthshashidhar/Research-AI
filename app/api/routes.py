from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def home():
    return {
        "project": "ResearchOS AI",
        "status": "Running"
    }


@router.get("/health")
def health():
    return {
        "status": "healthy"
    }
