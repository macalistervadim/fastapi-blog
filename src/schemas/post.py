from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    pass

class PostRead(PostBase):
    id: int

    class Config:
        from_attributes = True
