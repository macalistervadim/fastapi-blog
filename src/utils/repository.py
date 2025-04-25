from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas.post import PostRead

ModelType = TypeVar("ModelType")


class AbstractRepository(ABC, Generic[ModelType]):
    @abstractmethod
    async def add_one(self, data: dict) -> int:
        raise NotImplementedError

    @abstractmethod
    async def get_all(self) -> list[PostRead]:
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository[ModelType]):
    model: type[ModelType] | None = None

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def add_one(self, data: dict) -> int:
        if self.model is None:
            raise ValueError("Model class must be defined")
        stmt = insert(self.model).values(**data).returning(self.model.id)  # type: ignore
        res = await self.session.execute(stmt)
        await self.session.commit()
        return res.scalar_one()

    async def get_all(self) -> list[PostRead]:
        if self.model is None:
            raise ValueError("Model class must be defined")
        stmt = select(self.model)
        res = await self.session.execute(stmt)
        return [PostRead.model_validate(row[0]) for row in res.all()]
