from fastapi import FastAPI
from routes import books
from routes import users
from database import engine
from models import Base
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(books.router)
app.include_router(users.router)
Base.metadata.create_all(bind=engine)

