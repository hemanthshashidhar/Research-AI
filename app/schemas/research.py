from pydantic import BaseModel, Field


class ResearchRequest(BaseModel):
    topic: str = Field(
        ...,
        min_length=3,
        description="Technical research topic"
    )


class ResearchResponse(BaseModel):
    topic: str
    execution_plan: list[str]
