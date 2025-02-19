from ..models import Genre
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError 
from ..schemas import GenreRequest
from fastapi_pagination.ext.sqlalchemy import paginate
from ..exceptions.catalogs_exceptions import (
    GenreNotFoundException, 
    GenreAlreadyExistException, 
    EmptyFieldsException
)


def get_all_genres(db: Session):
    genres = db.query(Genre)
    return paginate(genres)

def get_genre_by_description(db: Session, description: str):
    genre =  db.query(Genre).filter(Genre.description == description.capitalize()).first()
    if genre is None:
        raise GenreNotFoundException #exception
    return genre


def create_genre(db: Session, genreRequest: GenreRequest):
    # genre = db.query(Genre).filter(Genre.description == genreRequest.description.
    #                                title().strip()).first()
    if genreRequest.description.strip() == "":
        raise EmptyFieldsException("Field empty.")
    try:
        genre = Genre(description = genreRequest.description.
                      capitalize().strip())
        db.add(genre)
        db.commit()
        return genre
    except IntegrityError:
        db.rollback()
        raise GenreAlreadyExistException


def update_genre(db: Session, genreRequest: GenreRequest, id: int):
    genre = db.query(Genre).filter(Genre.id == id).first()
    if genre is None:
        raise GenreNotFoundException
    try:
        genre.description = genreRequest.description.capitalize().strip()
        db.add(genre)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise GenreAlreadyExistException


def delete_genre(db: Session, id: int):
    genre = db.query(Genre).filter(Genre.id == id).first()
    if genre is None:
        raise GenreNotFoundException
    db.query(Genre).filter(Genre.id == id).delete()
    db.commit()
    




