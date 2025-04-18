from abc import ABC, abstractmethod

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas.post import PostRead


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, data: dict) -> int:
        raise NotImplementedError

    @abstractmethod
    async def get_all(self):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data: dict) -> int:
        smtp = insert(self.model).values(**data).returning(self.model.id)
        res = await self.session.execute(smtp)
        await self.session.commit()
        return res.scalar_one()

    async def get_all(self):
        smtp = select(self.model)
        res = await self.session.execute(smtp)
        return [PostRead.model_validate(row[0]) for row in res.all()]
