from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    nickname: str
    email: EmailStr
    password: str
