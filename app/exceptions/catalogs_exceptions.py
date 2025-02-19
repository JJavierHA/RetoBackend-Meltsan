from fastapi import HTTPException
from starlette import status

class GenreNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail="Genre not found.")


class GenreAlreadyExistException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail="Genre already exist.")


class EmptyFieldsException(HTTPException):
    def __init__(self, e: str):
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail=e)