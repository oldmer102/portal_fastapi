from pydantic import UUID4, BaseModel, EmailStr, Field, validator


class PostModel(BaseModel):
    title: str
    content: str
    values: str


class PostDetailsModel(BaseModel):
    title: str
    content: str
    values: str