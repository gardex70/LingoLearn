from pydantic import EmailStr
from schemas.auth import Token
from core.security import verify_password
from repositories.user import UserRepository
from core.security import create_access_token

class AuthService:
    def __init__(self, user_repository: UserRepository):
        self.user_repo = user_repository

    def authenticate_user(self, email: EmailStr, password: str) -> Token | None:
        user = self.user_repo.get_user_by_email(email)
        
        if not user or not verify_password(password, user.password):
            return None

        token_data = {"sub": user.email}
        access_token = create_access_token(token_data)

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }