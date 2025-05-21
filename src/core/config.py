import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = os.environ.get("ENV_FILE", ".env.local")
        extra = "ignore"


settings = Settings()  # type: ignore
