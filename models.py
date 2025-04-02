from sqlalchemy import Column, Integer, Float, String
from db_config import Base

class FareHistory(Base):
    __tablename__ = "fare_history"

    id = Column(Integer, primary_key=True, index=True)
    origin = Column(String, nullable=True)
    destination = Column(String, nullable=True)
    distance = Column(Float)
    unit = Column(String)
    fare = Column(Float)
    currency = Column(String, default="NGN")
