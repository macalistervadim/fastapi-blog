from typing import Self

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.post import PostRepository
from src.schemas.post import PostRead
from utils.repository import AbstractRepository


class TestPostRepository:
    @pytest.fixture
    async def repository(
        self: Self,
        async_session: AsyncSession,
    ) -> PostRepository:
        return PostRepository(async_session)

    async def test_add_one(self: Self, repository: AbstractRepository) -> None:
        test_data = {"title": "Test Post", "content": "Test Content"}
        post_id = await repository.add_one(test_data)
        assert isinstance(post_id, int)
        assert post_id > 0

    async def test_get_all(self, repository: AbstractRepository) -> None:
        test_data = [
            {"title": "Post 1", "content": "Content 1"},
            {"title": "Post 2", "content": "Content 2"},
        ]

        for data in test_data:
            await repository.add_one(data)

        posts = await repository.get_all()
        assert len(posts) == 2
        assert all(isinstance(post, PostRead) for post in posts)
