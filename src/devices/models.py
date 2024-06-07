from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base


class Collar(Base):
    __tablename__ = 'collars'
    registration_number = Column(Integer, primary_key=True)
    nickname = Column(String)
    is_deleted = Column(Integer)
    user_id = Column(Integer)


class Coordinate(Base):
    __tablename__ = 'coordinates'
    id = Column(Integer, primary_key=True, index=True)
    collar_id = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)
    timestamp = Column(DateTime, default='now()')
