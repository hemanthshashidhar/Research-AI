from langchain_google_genai import ChatGoogleGenerativeAI

from app.core.settings import settings

_llm = ChatGoogleGenerativeAI(
    model=settings.GOOGLE_MODEL,
    google_api_key=settings.GEMINI_API_KEY,
    temperature=0.2,
)


def get_llm() -> ChatGoogleGenerativeAI:
    """
    Returns a singleton Gemini model.

    Every agent should call this function
    instead of creating a new LLM instance.
    """

    return _llm
