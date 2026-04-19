from sqlalchemy import String, Column

from uuid import uuid4
from core.database import Base

class User(Base):
    __tablename__='users'
    
    id = Column(String, primary_key=True, default=lambda:str(uuid4()))
    name = Column(String)
    email = Column(String, unique=True)
    hashed_password = Column(String)
