from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    nickname: str
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    id: int = Field(gt=0)
