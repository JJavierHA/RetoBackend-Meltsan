from fastapi import FastAPI
from fastapi_pagination import add_pagination
from .routers import books, catalogs
from . import models
from .database import engine

app = FastAPI()

# add pagination
add_pagination(app)

models.Base.metadata.create_all(bind=engine)

app.include_router(catalogs.router)
app.include_router(books.router)