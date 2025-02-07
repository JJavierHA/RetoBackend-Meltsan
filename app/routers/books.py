from fastapi import APIRouter, Depends, Path, Query
from fastapi_pagination import Page
from starlette import status
from sqlalchemy.orm import Session
from typing import Annotated

from ..database import sesionLocal
from ..schemas import BookRequest, BookRequestGet
from ..services.book_services import (
    get_all_books, 
    get_book_by_id,
    create_book,
    update_book,
    delete_book,
    get_book_by_author_or_title
)

router = APIRouter(
    prefix="/api/books",
    tags=["books"]
)

def get_db():
    db = sesionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@router.get("", status_code=status.HTTP_200_OK, 
            response_model=Page[BookRequestGet])
async def list_books(db: db_dependency):
    return get_all_books(db)


@router.get("/{id}", status_code=status.HTTP_200_OK)
async def book_by_id(db: db_dependency, id: int = Path(gt=0)):
    return get_book_by_id(db, id)


@router.get("/search/", status_code=status.HTTP_200_OK, 
            response_model=Page[BookRequestGet])
async def book_by_author_or_title(
    db: db_dependency, 
    query: str = Query(
        description="Search by auth or title"
    )
):
    return get_book_by_author_or_title(db, query)


@router.post("", response_model=BookRequest, status_code=status.HTTP_201_CREATED)
async def create_new_book(db: db_dependency, bookRequest: BookRequest):
    return create_book(db, bookRequest)


@router.put("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_existing_book(db: db_dependency, bookRequest: BookRequest, 
                               id: int = Path(gt=0)):
    update_book(db, bookRequest, id)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_existing_book(db: db_dependency, id:int = Path(gt=0)):
    delete_book(db, id)