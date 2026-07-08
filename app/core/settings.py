from functools import lru_cache

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    APP_NAME: str = "ResearchOS AI"
    APP_VERSION: str = "1.0.0"

    GEMINI_API_KEY: str

    GOOGLE_MODEL: str = "gemini-2.5-flash"

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
