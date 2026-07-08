from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="ResearchOS AI",
    version="1.0.0",
    description="Enterprise Multi-Agent AI Research Platform"
)

app.include_router(router)
