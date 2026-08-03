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
def get_books(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return books

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


@router.delete('/books/{book_id}')
def delete_books(book_id: int, db: Session = Depends(get_db)):
    delete_books = db.query(Book).filter(Book.id == book_id).first()

    db.delete(delete_books)
    db.commit()
    return {'message': 'book deleted'}


