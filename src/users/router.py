from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .schemas import UserBase
from .hash_password import hash_pass
from .models import User
from database import get_db


router = APIRouter()


@router.post("/create_user")  # post - запрос отправки данных
def create_user(user: UserBase, db: Session = Depends(get_db)):  # функция получает аргумент 'user', он должен соответствовать схеме UserBase
    try:
        db.begin_nested()
        hashed_password = hash_pass(user.password)  # Хэшируем пароль из
        db_user = User(nickname=user.nickname, email=user.email, password=hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return {"user_id": db_user.id}
    except Exception as e:
        db.rollback()
        if "users.nickname" in str(e) and "Duplicate" in str(e):
            raise HTTPException(status_code=400, detail="Nickname already exists")
        elif "users.email" in str(e) and "Duplicate" in str(e):
            raise HTTPException(status_code=400, detail="Email already exists")
        else:
            raise HTTPException(status_code=500, detail="Internal Error")
