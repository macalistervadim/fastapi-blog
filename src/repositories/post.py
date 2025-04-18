from src.models.post import Post
from src.utils.repository import SQLAlchemyRepository


class PostRepository(SQLAlchemyRepository):
    model = Post
