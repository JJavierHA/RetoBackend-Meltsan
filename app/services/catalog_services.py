from ..models import Genre
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError 
from ..schemas import GenreRequest
from fastapi import HTTPException
from fastapi_pagination.ext.sqlalchemy import paginate
from starlette import status


def get_all_genres(db: Session):
    genres = db.query(Genre)
    return paginate(genres)

def get_genre_by_description(db: Session, description: str):
    genre =  db.query(Genre).filter(Genre.description == description).first()
    if genre is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Genre not found."
        )
    return genre


def create_genre(db: Session, genreRequest: GenreRequest):
    # genre = db.query(Genre).filter(Genre.description == genreRequest.description.
    #                                title().strip()).first()
    if genreRequest.description.strip() == "":
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="The field can not be empty."
        )
    try:
        genre = Genre(description = genreRequest.description.
                      capitalize().strip())
        db.add(genre)
        db.commit()
        return genre
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Genre already exist."
        )


def update_genre(db: Session, genreRequest: GenreRequest, id: int):
    genre = db.query(Genre).filter(Genre.id == id).first()
    if genre is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Genre not found."
        )
    try:
        genre.description = genreRequest.description.capitalize().strip()
        db.add(genre)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Genre already exist."
        )


def delete_genre(db: Session, id: int):
    genre = db.query(Genre).filter(Genre.id == id).first()
    if genre is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Genre not found."
        )
    db.query(Genre).filter(Genre.id == id).delete()
    db.commit()
    




