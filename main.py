from fastapi import FastAPI
from routes import books
from database import engine
from models import Base

app = FastAPI()
app.include_router(books.router)
Base.metadata.create_all(bind=engine)