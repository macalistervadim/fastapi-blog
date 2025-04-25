from unittest.mock import AsyncMock

import pytest

from src.schemas.post import PostCreate
from src.services.post import PostServices


@pytest.mark.asyncio
async def test_add_post() -> None:
    mock_repo = AsyncMock()
    mock_repo.add_one.return_value = 1

    service = PostServices(mock_repo)

    post = PostCreate(title="Test title", content="Test content")

    result = await service.add_post(post)

    assert result == 1

    mock_repo.add_one.assert_called_once_with(
        {
            "title": "Test title",
            "content": "Test content",
        },
    )
