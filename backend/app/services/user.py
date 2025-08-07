from core.security import hash_password
from core.exceptions import UserAlreadyExistsError
from repositories.user import UserRepository
from schemas.user import UserCreate, UserResponse
from sqlalchemy.orm import Session

def register_user(db: Session, user_data: UserCreate) -> UserResponse:
    try:
        user_repo = UserRepository(db)

        if user_repo.get_by(email=user_data.email):
            raise UserAlreadyExistsError(email=user_data.email)
        
        user_to_create = {
            "username": user_data.username,
            "email": user_data.email,
            "password": hash_password(user_data.password)
        }
        
        new_user = user_repo.create(**user_to_create)
        
        db.commit()
        db.refresh(new_user)

        user_response = UserResponse(
            id=new_user.id,
            email=new_user.email,
            username=new_user.username
        )
        
        return user_response
    except Exception:
        db.rollback()
        raise
    
