from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.user import register_user
from schemas.user import UserCreate, UserResponse
from database.connection import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserResponse, status_code=201)
def register_user_endpoint(
    user: UserCreate,
    db: Session = Depends(get_db)
):  
    return register_user(db, user)
    