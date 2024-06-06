from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship  # А зочем


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    nickname = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
