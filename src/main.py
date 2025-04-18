from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.api.v1 import posts
from src.db.create_tables import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(posts.router, prefix="/v1")
