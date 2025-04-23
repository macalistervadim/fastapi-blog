from typing import cast

from sqlalchemy import String, inspect

from src.models.post import Post


def test_post_model_metadata() -> None:
    assert Post.__tablename__ == "posts"


def test_post_model_columns() -> None:
    mapper = inspect(Post)
    columns = {column.name: column for column in mapper.columns}

    assert "id" in columns
    assert columns["id"].primary_key is True
    assert columns["id"].nullable is False
    assert columns["id"].index is True
    assert str(columns["id"].type).lower().startswith("integer")

    assert "title" in columns
    assert columns["title"].nullable is False

    title_type = cast(String, columns["title"].type)
    assert isinstance(title_type.length, int)
    assert title_type.length == 100
    assert str(title_type).startswith("VARCHAR")

    assert "content" in columns
    assert str(columns["content"].type).lower().startswith("text")
    assert columns["content"].nullable is False
