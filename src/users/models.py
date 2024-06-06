from database import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    nickname = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
