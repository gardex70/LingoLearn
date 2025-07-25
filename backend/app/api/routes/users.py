from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.user import UserService
from repositories.user import UserRepository
from schemas.user import UserCreate, UserResponse
from database.connection import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserResponse, status_code=201)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    user_repo = UserRepository(db)
    user_service = UserService(user_repo)
    
    try:
        return user_service.register_user(user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Ocorreu um erro interno ao processar seu registro")