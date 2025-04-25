from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.session import get_db
from src.repositories.post import PostRepository
from src.schemas.post import PostCreate, PostRead
from src.services.post import PostServices

router = APIRouter(prefix="/posts", tags=["posts"])


async def get_post_repo(
    session: AsyncSession = Depends(get_db),
) -> PostRepository:
    return PostRepository(session)


async def get_post_service(
    repo: PostRepository = Depends(get_post_repo),
) -> PostServices:
    return PostServices(repo)


@router.get("/", response_model=list[PostRead])
async def get_posts(
    repo: PostRepository = Depends(get_post_repo),
) -> list[PostRead]:
    return await repo.get_all()


@router.post("/", status_code=201)
async def create_post(
    post: PostCreate,
    service: PostServices = Depends(get_post_service),
) -> dict[str, int]:
    try:
        task_id = await service.add_post(post)
        return {"task_id": task_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
