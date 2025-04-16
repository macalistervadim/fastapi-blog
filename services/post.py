from schemas.post import PostCreate
from utils.repository import AbstractRepository


class PostServices:
    def __init__(self, repository: AbstractRepository):
        self.repository: AbstractRepository = repository

    async def add_post(self, post: PostCreate) -> int:
        post_dict = post.model_dump()
        task_id = await self.repository.add_one(post_dict)
        return task_id
