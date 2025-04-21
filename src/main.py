from fastapi import FastAPI

from src.api.v1 import posts

app = FastAPI()

app.include_router(posts.router, prefix="/v1")
