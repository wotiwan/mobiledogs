from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import UserBase
from hash_password import hash_pass
from ..database import get_db


router = APIRouter()


@router.post("/create_user")  # post - запрос отправки данных
def create_user(user: UserBase, db: Session = Depends(get_db)):  # функция получает аргумент 'user', он должен соответствовать схеме UserBase
    hashed_password = hash_pass(user.password)  # Хэшируем пароль из
    user["password"] = hashed_password
    db.add(user)
    db.commit()
    db.refresh(user)

