from pydantic import BaseModel, Field


class CollarBase(BaseModel):
    reg_number: int = Field(gt=0)
    nickname: str


class CollarUpdate(BaseModel):
    reg_number: int = Field(gt=0)


class CoordinateBase(BaseModel):
    collar_id: int
    latitude: float
    longitude: float
    timestamp: str


class GetCoordinate(BaseModel):
    collar_id: int
    start_time: str
    end_time: str
