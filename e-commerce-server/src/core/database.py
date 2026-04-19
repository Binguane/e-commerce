from typing import Annotated
from fastapi import Depends
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

from core.config import settings


# DATABASE_URL=settings.DATABASE_URL_PROD
DATABASE_URL = 'sqlite:///../database.db'

engine=create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def get_session():
    try:
        session = SessionLocal()
        yield session
    finally:
        session.close()

session = Annotated[Session, Depends(get_session)]