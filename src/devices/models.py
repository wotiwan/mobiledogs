from sqlalchemy import Column, Integer, String
from database import Base


class Collar(Base):
    __tablename__ = 'collars'
    registration_number = Column(Integer, primary_key=True)
    nickname = Column(String)
