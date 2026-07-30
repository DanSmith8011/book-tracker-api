from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from database import SessionLocal
from schemas import BookCreate
from models import Book

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/books')
def get_books():
    return []

@router.post('/books')
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    new_book = Book(
        title=book.title,
        author=book.author,
        year=book.year,
        genre=book.genre
    )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book





