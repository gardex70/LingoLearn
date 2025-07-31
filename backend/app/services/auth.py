from pydantic import EmailStr
from schemas.auth import Token
from core.security import verify_password
from repositories.user import UserRepository
from core.security import create_access_token
from sqlalchemy.orm import Session
from core.logging import logging

def authenticate_user(db: Session, email: EmailStr, password: str) -> Token | bool:
    user = UserRepository(db).get_by(email=email)
    
    if not user or not verify_password(password, user.password):
        logging.warning(f"Failed authentication attempt for email: {email}")
        return False

    token_data = {"sub": user.email}
    access_token = create_access_token(token_data)

    return {
        "access_token": access_token,
        "token_type": "bearer"
        }