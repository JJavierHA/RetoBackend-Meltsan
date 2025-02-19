from fastapi import HTTPException
from starlette import status

class BookNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, 
                         detail="Book not found.")


class IsbnAlreadyExistException(HTTPException): 
    def __init__(self):
        super().__init__(status_code=status.HTTP_409_CONFLICT,
                         detail="ISBN already exist.")