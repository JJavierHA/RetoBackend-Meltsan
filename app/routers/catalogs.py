from fastapi import APIRouter, Depends, Path
from fastapi_pagination import Page
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status

from ..schemas import GenreRequest, GenreRequestGet
from ..database import sesionLocal
from ..services.catalog_services import (
    get_all_genres, 
    create_genre, 
    get_genre_by_description, 
    update_genre,
    delete_genre
)

router = APIRouter(
    prefix="/api/catalogs/genre",
    tags=["catalogs"]
)

# dependency
# interact with the database
def get_db():
    db = sesionLocal()
    try:
        yield db
    finally:
        db.close()

# dependency injection
db_dependency = Annotated[Session, Depends(get_db)]

@router.get("", status_code=status.HTTP_200_OK, 
            response_model=Page[GenreRequestGet])
async def list_all_genres(db: db_dependency):
    return get_all_genres(db)


@router.get("/")
async def genre_by_description(db: db_dependency, description: str):
    return get_genre_by_description(db, description)


@router.post("", response_model=GenreRequest, status_code=status.HTTP_201_CREATED)
async def creat_new_genre(db: db_dependency, genreRequest: GenreRequest):
    genre = create_genre(db, genreRequest)
    return genre
    

@router.put("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_existing_genre(db: db_dependency, genreRequest: GenreRequest, 
                       id: int = Path(gt=0)):
    update_genre(db, genreRequest, id)
    
    
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delet_existing_genre(db: db_dependency, id: int = Path(gt=0)):
    delete_genre(db, id)
        