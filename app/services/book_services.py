from sqlalchemy.orm import Session
from fastapi import HTTPException
from fastapi_pagination.ext.sqlalchemy import paginate
from starlette import status
from sqlalchemy.exc import IntegrityError
from sqlalchemy import or_
from ..schemas import BookRequest
from ..models import Book
from ..exceptions.catalogs_exceptions import GenreNotFoundException 
from ..exceptions.books_exceptions import (
    BookNotFoundException,
    IsbnAlreadyExistException
)

def get_all_books(db: Session):
    books = db.query(Book)
    return paginate(books)


def get_book_by_id(db: Session, id: int):
    book = db.query(Book).filter(Book.id == id).first()
    if book is None:
        raise BookNotFoundException
    return book


def get_book_by_author_or_title(db: Session, query: str):
    book = db.query(Book).filter(or_(Book.title.ilike(f"%{query}%"), 
                                     Book.author.ilike(f"%{query}%")))
    if not book.first():
        raise BookNotFoundException
    return paginate(book)


def create_book(db: Session, bookReques: BookRequest):
    book = db.query(Book).filter(Book.ISBN == bookReques.ISBN.upper()
                                 .strip()).first()
    if book is not None:
        raise IsbnAlreadyExistException
    try:
        book = Book(
            title = bookReques.title.title().strip(),
            author = bookReques.author.title().strip(),
            ISBN = bookReques.ISBN.upper().strip(),
            published = bookReques.published,
            genre = bookReques.genre,
            stock = bookReques.stock
        )
        db.add(book)
        db.commit()
        return book
    except IntegrityError:
        db.rollback()
        raise GenreNotFoundException
        

def update_book(db: Session, bookRequest: BookRequest, id: int):
    book = db.query(Book).filter(Book.id == id).first()
    if book is None:
        raise BookNotFoundException
    try:
        book.title = bookRequest.title.title().strip()
        book.author = bookRequest.author.title().strip()
        book.ISBN = bookRequest.ISBN.upper().strip()
        book.published = bookRequest.published
        book.genre = bookRequest.genre
        book.stock = bookRequest.stock
        db.add(book)
        db.commit()
        return book
    except IntegrityError:
        db.rollback() # discard change
        raise IsbnAlreadyExistException
    

def delete_book(db: Session, id: int):
    if db.query(Book).filter(Book.id == id).first() is None:
        raise BookNotFoundException
    db.query(Book).filter(Book.id == id).delete()
    db.commit()