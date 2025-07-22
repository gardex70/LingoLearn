from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import users, auth
from database.connection import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(auth.router)

@app.get("/")
def home():
    return {"message": "API de Usuários"}