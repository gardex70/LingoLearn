from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from schemas.auth import Token
from database.connection import get_db
from repositories.user import UserRepository
from services.auth import AuthService

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user_repo = UserRepository(db)
    auth_service = AuthService(user_repo)
    
    try:
        token = auth_service.authenticate_user(email=form_data.username, password=form_data.password)
        if not token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciais inválidas",
                headers={"WWW-Authenticate": "Bearer"}
            )
        return token
    except HTTPException:
        raise
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ocorreu um erro interno ao processar seu registro")
