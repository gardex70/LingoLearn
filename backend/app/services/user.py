from models.user import User
from core.security import hash_password
from repositories.user import UserRepository
from schemas.user import UserCreate
import logging

logger = logging.getLogger(__name__)


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def register_user(self, user_data: UserCreate) -> User:
        try:
            if self.user_repo.get_user_by_email(user_data.email):
                logger.warning(f"Email já registrado: {user_data.email}")
                raise ValueError("Email já registrado")
            
            user_to_create = {
                "username": user_data.username,
                "email": user_data.email,
                "password": hash_password(user_data.password)
            }
            
            new_user = self.user_repo.create(user_to_create, commit=True)
            
            return new_user
                
        except ValueError as ve:
            logger.warning(f"Validação falhou: {str(ve)}")
            
        except Exception as e:
            logger.error(f"Erro no registro: {str(e)}", exc_info=True)
            raise ValueError("Falha ao registrar usuário") from e