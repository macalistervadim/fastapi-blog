import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str = "database"
    POSTGRES_PORT: int = 5432

    class Config:
        env_file = os.environ.get("ENV_FILE", ".env.local")
        extra = "ignore"


settings = Settings()  # type: ignore
