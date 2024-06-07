from pydantic import BaseModel, Field


class CollarBase(BaseModel):
    reg_number: int = Field(gt=0)
    nickname: str


class CoordinateBase(BaseModel):
    collar_id: int
    latitude: float
    longitude: float
    timestamp: str
