from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author: str
    year: int
    genre: str

class BookResponse(BaseModel):
    id: int 
    title: str
    author: str
    year: int
    genre: str

    class Config:
        from_attributes = True