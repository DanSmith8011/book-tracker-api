from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from database import SessionLocal
from schemas import BookCreate
from models import Book
from models import User
from fastapi.security import OAuth2PasswordBearer
from auth import verify_token

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/books')
def get_books(db: Session = Depends(get_db), token:str = Depends(oauth2_scheme)):
    user_id = verify_token(token)
    books = db.query(Book).filter(int(user_id) == Book.user_id).all()
    return books

@router.post('/books')
def create_book(book: BookCreate, db: Session = Depends(get_db), token:str = Depends(oauth2_scheme)):
    user_id = verify_token(token)
    new_book = Book(
        title=book.title,
        author=book.author,
        year=book.year,
        genre=book.genre,
        user_id=user_id
    )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


@router.delete('/books/{book_id}')
def delete_books(book_id: int, db: Session = Depends(get_db), token:str = Depends(oauth2_scheme)):
    user_id = verify_token(token)
    book_to_delete = db.query(Book).filter(Book.id == book_id).first()
    if book_to_delete.user_id == int(user_id):
        db.delete(book_to_delete)
        db.commit()
        return {'message': 'book deleted'}
    else:
        raise HTTPException(status_code=401, detail="Unable to delete book")

    


