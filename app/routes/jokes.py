from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import SessionLocal
from .. import crud, schemas

router = APIRouter(prefix="/jokes", tags=["jokes"])

def get_db():
    db = SessionLocal()
    try:
        yield db


    finally:
        db.close()

@router.get("/")
def read_jokes(db: Session = Depends(get_db)):
    return crud.get_jokes(db)

@router.get("/{joke_id}", response_model=schemas.Joke)
def read_joke(joke_id: int, db: Session = Depends(get_db)):
    return crud.get_joke(db, joke_id)


@router.post("/", response_model=schemas.Joke)
def ceate_new_joke(joke: schemas.JokeCreate, db: Session = Depends(get_db)):
    return crud.create_joke(db, joke)


@router.delete("/{joke_id}", response_model=schemas.Joke)
def delete_joke(joke_id:int, db: Session = Depends(get_db)):
    return crud.delete_joke(db, joke_id)

