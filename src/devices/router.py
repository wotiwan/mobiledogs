from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .models import Collar, Coordinate
from users.models import User
from users.schemas import UserUpdate
from .schemas import CollarBase, CoordinateBase, CollarUpdate, GetCoordinate
from database import get_db
from logs.logger import logger

device_router = APIRouter()


@device_router.post("/add_collar")  # Добавить
def add_collar(collar: CollarBase, db: Session = Depends(get_db)):
    try:
        db.begin_nested()
        existing_collar = db.query(Collar).filter(Collar.registration_number == collar.reg_number).first()
        if existing_collar:
            if existing_collar.is_deleted == 1:
                raise HTTPException(status_code=400,
                                    detail="Collar was deleted, please, recover it")
            else:
                raise HTTPException(status_code=400, detail="Collar already registered")
        db_collar = Collar(registration_number=collar.reg_number, nickname=collar.nickname, is_deleted=0)
        db.add(db_collar)
        db.commit()
        db.refresh(db_collar)
        logger.info(f"Collar added: {db_collar.registration_number}")
        return {"reg_number": db_collar.registration_number, "nickname": db_collar.nickname}
    except Exception as e:
        db.rollback()
        logger.error(f"Error adding collar: {e}")
        if "Collar was deleted" in str(e) or "already registered" in str(e):
            raise HTTPException(status_code=400, detail=f"{e}")
        else:
            raise HTTPException(status_code=500, detail="Internal Error")


@device_router.get("/get_collars")
def get_collars(db: Session = Depends(get_db)):
    try:
        collars = db.query(Collar).filter(Collar.is_deleted == 0).all()  # all для всех записей
        if not collars:
            raise HTTPException(status_code=404, detail="No data yet")
        logger.info(f"Existing collars: {len(collars)}")
        return collars
    except Exception as e:
        logger.error(f"Error finding collars: {e}")
        if "No data yet" in str(e):
            raise HTTPException(status_code=404, detail=f"{e}")
        raise HTTPException(status_code=500, detail="Internal Error")


@device_router.post("/delete_collar")
def delete_collar(reg_number: CollarUpdate, db: Session = Depends(get_db)):
    try:
        collar = db.query(Collar).filter(Collar.registration_number == reg_number.reg_number).first()
        if not collar:
            raise HTTPException(status_code=404, detail="Collar is not existing")
        collar.is_deleted = 1
        db.commit()
        logger.info(f"Collar deleted: {reg_number}")
        return {"message": "successfully deleted!"}
    except Exception as e:
        logger.error(f"Error deleting collar: {e}")
        if "Collar is not" in str(e):
            raise HTTPException(status_code=404, detail=f"{e}")
        raise HTTPException(status_code=500, detail="Internal Error")


@device_router.post("/recover_collar")
def recover_collar(reg_number: CollarUpdate, db: Session = Depends(get_db)):
    try:
        collar = db.query(Collar).filter(Collar.registration_number == reg_number.reg_number).first()
        if collar.is_deleted == 0:
            raise HTTPException(status_code=400, detail="Collar is not deleted")
        if not collar:
            raise HTTPException(status_code=404, detail="Collar is not existing")
        collar.is_deleted = 0
        db.commit()
        logger.info(f"Collar recovered: {reg_number}")
        return {"message": "successfully recovered!"}
    except Exception as e:
        logger.error(f"Error recovering collar: {e}")
        if "Collar is not" in str(e):
            raise HTTPException(status_code=404, detail=f"{e}")
        raise HTTPException(status_code=500, detail="Internal Error")


@device_router.post("/link_collar")  # Привязка пёсика к волонтёру
def link_collar(reg_number: CollarUpdate, uid: UserUpdate, db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.id == uid.id).first()  # Необходимо, чтобы убедиться в том что пользователь
        # с таким id существует
        if not user:
            raise HTTPException(status_code=404, detail="User is not existing")
        collar = db.query(Collar).filter(Collar.registration_number == reg_number.reg_number).first()
        if not collar:
            raise HTTPException(status_code=404, detail="Collar is not existing")
        collar.user_id = uid.id
        db.commit()
        logger.info(f"Collar {reg_number.reg_number} linked to user {uid.id}")
        return {"message": "successfully linked!"}
    except Exception as e:
        logger.error(f"Error linking collar: {e}")
        if "User is" in str(e) or "Collar is" in str(e):
            raise HTTPException(status_code=404, detail=f"{e}")
        raise HTTPException(status_code=500, detail="Internal Error")


@device_router.post("/unlink_collar")
def unlink_collar(reg_number: CollarUpdate, uid: UserUpdate, db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.id == uid.id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User is not existing")
        collar = db.query(Collar).filter(
            Collar.registration_number == reg_number.reg_number and Collar.user_id == uid.id).first()
        if not collar:
            raise HTTPException(status_code=404, detail="Collar is not existing")
        collar.user_id = 0
        db.commit()
        logger.info(f"Collar {reg_number.reg_number} unlinked from user {uid.id}")
        return {"message": "successfully unlinked!"}
    except Exception as e:
        logger.error(f"Error unlinking collar: {e}")
        if "User is" in str(e) or "Collar is" in str(e):
            raise HTTPException(status_code=404, detail=f"{e}")
        raise HTTPException(status_code=500, detail="Internal Error")


@device_router.post("/send_coordinates")
def send_coordinates(coordinate: CoordinateBase, db: Session = Depends(get_db)):
    try:
        collar = db.query(Collar).filter(Collar.registration_number == coordinate.collar_id).first()
        if not collar:
            raise HTTPException(status_code=400, detail="Collar is not existing")

        db_coordinate = Coordinate(
            collar_id=coordinate.collar_id,
            latitude=coordinate.latitude,
            longitude=coordinate.longitude,
            timestamp=coordinate.timestamp
        )
        db.add(db_coordinate)
        db.commit()
        db.refresh(db_coordinate)
        logger.info(f"Coordinates sent for collar {coordinate.collar_id}")
        return {"status": "success", "coordinate_id": db_coordinate.id}
    except Exception as e:
        db.rollback()
        logger.error(f"Error sending coordinates: {e}")
        if "Incorrect datetime value" in str(e):
            raise HTTPException(status_code=400, detail="Incorrect DATETIME")
        elif "Collar is" in str(e):
            raise HTTPException(status_code=400, detail=f"{e}")
        raise HTTPException(status_code=500, detail=f"Internal Error")


@device_router.post("/get_track")
def get_track(collar: GetCoordinate, db: Session = Depends(get_db)):
    try:
        collar_db = db.query(Collar).filter(Collar.registration_number == collar.collar_id).first()
        if not collar_db:
            raise HTTPException(status_code=404, detail="Collar is not existing")

        track = db.query(Coordinate).filter(
            Coordinate.collar_id == collar.collar_id,
            Coordinate.timestamp >= collar.start_time,
            Coordinate.timestamp <= collar.end_time
        ).all()
        if not track:
            raise HTTPException(status_code=400, detail="No track info for this time range")
        logger.info(f"Track retrieved for collar {collar.collar_id} from {collar.start_time} to {collar.end_time}")
        return track
    except Exception as e:
        logger.error(f"Error getting track: {e}")
        if "Incorrect DATETIME" in str(e):
            raise HTTPException(status_code=400, detail="Incorrect DATETIME")
        elif "Collar is" in str(e) or "No track" in str(e):
            raise HTTPException(status_code=400, detail=f"{e}")
        else:
            raise HTTPException(status_code=500, detail="Internal Error")
