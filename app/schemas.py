from pydantic import BaseModel, Field


class GenreRequest(BaseModel):
    description: str = Field(min_length=1)


class GenreRequestGet(BaseModel):
    id: int
    description: str = Field(min_length=1)


class BookRequest(BaseModel):
    title: str = Field(min_length=1, max_length=50)
    author: str = Field(min_length=1, max_length=50)
    ISBN: str = Field(min_length=1, max_length=13)
    published: int
    genre: int = Field(gt=0)
    stock: int = Field(gt=-1)


class BookRequestGet(BaseModel):
    id: int
    title: str = Field(min_length=1, max_length=50)
    author: str = Field(min_length=1, max_length=50)
    ISBN: str = Field(min_length=1, max_length=13)
    published: int
    genre: int = Field(gt=0)
    stock: int = Field(gt=-1)
