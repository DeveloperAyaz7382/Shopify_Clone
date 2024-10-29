from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud.user import create_user, authenticate_user
from schemas.user import UserRegister, UserLogin
from config.database import get_db

router = APIRouter()

@router.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):
    db_user = create_user(db, user.name, user.email, user.password)
    if not db_user:
        raise HTTPException(status_code=400, detail="User registration failed")
    return {"message": "User registered successfully"}

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    user_obj = authenticate_user(db, user.email, user.password)
    if not user_obj:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": "Login successful"}
