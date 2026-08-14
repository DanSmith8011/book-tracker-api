from fastapi import APIRouter
from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends
from database import SessionLocal
from schemas import UserCreate
from schemas import UserLogin
from models import User
from auth import create_token
import bcrypt

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/users')
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    hashed = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    new_user = User(
        username=user.username,
        password=hashed.decode('utf-8')
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post('/login')
def user_login(user: UserLogin, db: Session = Depends(get_db)):
    username_check = db.query(User).filter(User.username == user.username).first()
    if username_check == None:
        raise HTTPException(status_code=401, detail="User does not exist")
    else: 
        password_match = bcrypt.checkpw(user.password.encode('utf-8'), username_check.password.encode('utf-8'))
    if not password_match:
        raise HTTPException(status_code=401, detail="Incorrect password")
    else:
        return create_token({'sub': str(username_check.id)})