from models.post import Post
from utils.repository import SQLAlchemyRepository


class PostRepository(SQLAlchemyRepository):
    model = Post
