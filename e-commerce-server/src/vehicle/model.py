from sqlalchemy import Column, String, Integer, Float, ForeignKey, Date

from datetime import date
from core.database import Base

class Vehicle(Base):
    __tablename__='vehicles'

    id = Column(Integer, primary_key=True)

    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    mileage = Column(Float, nullable=False) 
    description = Column(String, nullable=False)
    location = Column(String, nullable=False)
    user_id = Column(String, ForeignKey('users.id'))
    created_at = Column(Date, default=date.today())
