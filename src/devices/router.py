from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .models import Collar
from .schemas import CollarBase
from database import get_db

device_router = APIRouter()


@device_router.post("/add_collar")
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
