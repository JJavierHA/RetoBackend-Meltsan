from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base


class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(50), unique=True)


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    author = Column(String(50))
    ISBN = Column(String(13), unique=True)
    published = Column(Integer)
    genre = Column(Integer, ForeignKey("genres.id"))
    stock = Column(Integer)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(50), unique=True)
    hashed_password = Column(String(100))
    email = Column(String(50), unique=True)