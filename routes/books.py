from fastapi import APIRouter

router = APIRouter()

@router.get('/books')
def get_books():
    return []

@router.post('/books')
def post_books():
    return {'message': 'book created'}