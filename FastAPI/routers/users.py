from .auth import get_current_user, get_user_exception, verify_password, get_password_hash
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, APIRouter
from database import SessionLocal, engine
import models
from typing import Optional
import sys
sys.path.append("..")


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}}
)


models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
        

class UserVerification(BaseModel):
    username: str
    password: str
    new_password: str


class User(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    hashed_password: str
    is_active: bool


@router.get("/")
async def read_all(db: Session = Depends(get_db)):
    return db.query(models.Users).all()


@router.get("/user/{user_id}")
async def user_by_path(user_id: int,
                       db: Session = Depends(get_db)):
    user_model = db.query(models.Users)\
        .filter(models.Users.id == user_id)\
        .first()
    if user_model is not None:
        return user_model
    raise http_exception()


@router.get("/user/")
async def user_by_query(user_id: int,
                        db: Session = Depends(get_db)):
    user_model = db.query(models.Users)\
        .filter(models.Users.id == user_id)\
        .first()
    if user_model is not None:
        return user_model
    raise http_exception()


@router.put("/user/password")
async def user_password_change(user_verification: UserVerification,
                               user: dict = Depends(get_current_user),
                               db: Session = Depends(get_db)): 
    if user is None:
        raise get_user_exception()
    
    user_model: User = db.query(models.Users)\
        .filter(models.Users.id == user.get("id"))\
        .first()
        
    if user_model is not None:
        if user_verification.username == user_model.username and verify_password(user_verification.password, 
                                                                                 user_model.hashed_password):
            user_model.hashed_password = get_password_hash(user_verification.new_password)
            db.add(user_model)
            db.commit()
            return successful_response(200)
    return "Invalid user or request"


@router.delete("/user")
async def delete_user(user: dict = Depends(get_current_user),
                      db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()
    
    user_model = db.query(models.Users)\
        .filter(models.Users.id == user.get("id"))\
        .first()
        
    if user_model is None:
        return http_exception
    
    db.query(models.Users)\
        .filter(models.Users.id == user.get("id"))\
        .delete()

    db.commit()
    
    return successful_response(200)

# exception

def http_exception():
    return HTTPException(status_code=404, detail="User not found")


def successful_response(status_code: int):
    return {
        "status": status_code,
        "transaction": "Successful"
    }
