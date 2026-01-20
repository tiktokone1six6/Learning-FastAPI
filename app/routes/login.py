from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from ..database import SessionLocal
from .. import crud, schemas, database, models
from ..auth import sessions, security

router = APIRouter(prefix="/login", tags=["login"])

def get_db():
    db = SessionLocal()
    try:
        yield db


    finally:
        db.close()

@router.post("/")
def login(user: schemas.UserLogin, response: Response, db: Session=Depends(get_db)):

    
    user_from_db = db.query(models.User).filter(models.User.email == user.email).first()
    if user_from_db:
        hashed_password = user_from_db.hashed_password

        authenticated = security.verify_password(user.plain_text_password, hashed_password)
    else:
        return {"message": "User not found"}
    if not authenticated:
        raise HTTPException(status_code=401)
    if authenticated:
        session_id = sessions.create_session(user_from_db.id)

    response.set_cookie(
        key="session_id",
        value=session_id,
        httponly=True, 
        max_age=3600
    )
    return {"message": "Loggin in successfully"}
