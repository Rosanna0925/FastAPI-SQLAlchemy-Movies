# models.py
from sqlalchemy import Column, Integer, String
from database import Base

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    intro = Column(String, index=True)
    rating = Column(Integer, index=True)
