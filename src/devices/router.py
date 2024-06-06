from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .models import Collar
from users.models import User
from .schemas import CollarBase
from database import get_db

device_router = APIRouter()


@device_router.post("/add_collar")  # Добавить
def add_collar(collar: CollarBase, db: Session = Depends(get_db)):
    try:
        db.begin_nested()
        db_collar = Collar(registration_number=collar.reg_number, nickname=collar.nickname)
        db.add(db_collar)
        db.commit()
        db.refresh(db_collar)
        return {"reg_number": db_collar.registration_number, "nickname": db_collar.nickname}
    except Exception as e:
        db.rollback()
        if "collars.PRIMARY" in str(e) and "Duplicate" in str(e):
            raise HTTPException(status_code=400, detail="Collar already registered")
        else:
            raise HTTPException(status_code=500, detail="Internal Error")


@device_router.get("/get_collars")
def get_collars(db: Session = Depends(get_db)):
    try:
        collars = db.query(Collar).filter(Collar.is_deleted == 0).all()  # all для всех записей
        return collars
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Error")


@device_router.post("/delete_collar")
def delete_collar(reg_number: int, db: Session = Depends(get_db)):
    try:
        collar = db.query(Collar).filter(Collar.registration_number == reg_number).first()
        collar.is_deleted = 1
        db.commit()
        return {"message": "successfully deleted!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Error")  # Добавить исключение отсутствия ошейника


@device_router.post("/recover_collar")
def recover_collar(reg_number: int, db: Session = Depends(get_db)):
    try:
        collar = db.query(Collar).filter(Collar.registration_number == reg_number).first()
        collar.is_deleted = 0
        db.commit()
        return {"message": "successfully recovered!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Error")  # Добавить исключение отсутствия ошейника


@device_router.post("/link_collar")  # Привязка пёсика к волонтёру
def link_collar(reg_number: int, uid: int, db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.id == uid).first()  # Необходимо, чтобы убедиться в том что пользователь
        # с таким id существует
        collar = db.query(Collar).filter(Collar.registration_number == reg_number).first()
        collar.user_id = uid
        db.commit()
        return {"message": "successfully linked!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Error")


@device_router.post("/unlink_collar")
def unlink_collar(reg_number: int, uid: int, db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.id == uid).first()
        collar = db.query(Collar).filter(Collar.registration_number == reg_number and Collar.user_id == uid).first()
        collar.user_id = 0
        db.commit()
        return {"message": "successfully unlinked!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Error")
