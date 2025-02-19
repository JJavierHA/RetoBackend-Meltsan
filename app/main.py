from fastapi import FastAPI
from fastapi_pagination import add_pagination
from .routers import books, catalogs
from . import models
from .database import engine
from .exceptions.handlers import (
    genre_not_found_handler, 
    genre_already_exist_handler, 
    empty_fields_handler,
    book_not_found_handler,
    isbn_aready_exist_handler,
)
from .exceptions.catalogs_exceptions import (
    GenreNotFoundException, 
    GenreAlreadyExistException, 
    EmptyFieldsException,
)
from .exceptions.books_exceptions import (
    BookNotFoundException,
    IsbnAlreadyExistException,
)

app = FastAPI(
    title="Reto Backend",
    description="Micro servicio para la gestion de libros de una biblioteca",
    contact={
        "name": "Jose Javier Herrera Arguello",
        "email": "jose.herrera@meltsan.com",
        "url": "https://github.com/JJavierHA",
    },
)

# add pagination
add_pagination(app)

# exceptions
app.add_exception_handler(GenreNotFoundException, genre_not_found_handler)
app.add_exception_handler(GenreAlreadyExistException, genre_already_exist_handler)
app.add_exception_handler(EmptyFieldsException, empty_fields_handler)
app.add_exception_handler(BookNotFoundException, book_not_found_handler)
app.add_exception_handler(IsbnAlreadyExistException, isbn_aready_exist_handler)

# db
models.Base.metadata.create_all(bind=engine)

app.include_router(catalogs.router)
app.include_router(books.router)