from models.user import User
from core.security import hash_password
from core.exceptions import UserAlreadyExistsError
from repositories.user import UserRepository
from schemas.user import UserCreate
from sqlalchemy.orm import Session
from core.logging import logging

def register_user(db: Session, user_data: UserCreate) -> User:
    try:
        user_repo = UserRepository(db)

        if user_repo.get_by(email=user_data.email):
            raise UserAlreadyExistsError(email=user_data.email)
        
        user_to_create = {
            "username": user_data.username,
            "email": user_data.email,
            "password": hash_password(user_data.password)
        }
        
        new_user = user_repo.create(user_to_create)
        
        db.commit()
        db.refresh(new_user)

        return new_user
    except Exception as e:
        logging.error(f"Failed to register user: {user_data.email}. Error: {str(e)}")
        db.rollback()
        raise
    
