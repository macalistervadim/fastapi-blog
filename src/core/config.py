import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str

    @property
    def db_url(self):
        return self.DATABASE_URL

    class Config:
        env_file = os.environ.get("ENV_FILE", ".env.local")


settings = Settings()
