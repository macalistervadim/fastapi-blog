import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str

    @property
    def db_url(self):
        return os.getenv("DATABASE_URL")

    class Config:
        env_file = os.environ.get("ENV_FILE", ".env.local")


settings = Settings()
