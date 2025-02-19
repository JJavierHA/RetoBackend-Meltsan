from fastapi import Request
from fastapi.responses import JSONResponse
from .catalogs_exceptions import (
    GenreNotFoundException, 
    GenreAlreadyExistException, 
    EmptyFieldsException,
)
from .books_exceptions import (
    BookNotFoundException, 
    IsbnAlreadyExistException,
)

async def genre_not_found_handler(request: Request, 
                                  exc: GenreNotFoundException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail, 
            "message":"The requested genre does not exist."
        }
    )


async def genre_already_exist_handler(request: Request, 
                                      exc: GenreAlreadyExistException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail, 
            "message":"The entered genre already exist."
        }
    )


async def empty_fields_handler(request: Request, 
                               exc: EmptyFieldsException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail, 
            "message":"Fields cannot be empty."
        }
    )


async def book_not_found_handler(request: Request, 
                                 exc: BookNotFoundException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail, 
            "message":"The book entered does not exist."
        }
    )


async def isbn_aready_exist_handler(request: Request, 
                                    exc: IsbnAlreadyExistException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail, 
            "message":"The ISBN you want to enter already exists."
        }
    )