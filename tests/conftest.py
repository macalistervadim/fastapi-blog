from collections.abc import AsyncGenerator

import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.models.post import Base

DATABASE_URL = "sqlite+aiosqlite:///:memory:"


@pytest.fixture(scope="session")
def engine() -> AsyncEngine:
    return create_async_engine(DATABASE_URL, echo=False)


@pytest.fixture(scope="session", autouse=True)
async def init_db(engine: AsyncEngine) -> AsyncGenerator:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


@pytest.fixture(autouse=True)
async def clean_tables(engine: AsyncEngine) -> None:
    async with engine.begin() as conn:
        await conn.execute(text("DELETE FROM posts"))


@pytest.fixture()
async def async_session(engine: AsyncEngine) -> AsyncGenerator[AsyncSession]:
    async_session_maker = async_sessionmaker(
        engine,
        expire_on_commit=False,
        class_=AsyncSession,
    )
    async with async_session_maker() as session:
        yield session
        await session.rollback()
