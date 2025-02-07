from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .config import settings

DB_URL = settings.DB_URL

engine = create_engine(DB_URL)
sesionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()