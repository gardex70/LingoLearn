from sqlalchemy import select
from sqlalchemy.orm import Session
from models.user import User
from .base_repository import BaseRepository

class UserRepository(BaseRepository[User]):
    def __init__(self, database: Session):
        super().__init__(User, database)

    def get_user_by_email(self, email: str) -> User:
        stmt = select(User).where(User.email == email)
        return self.database.scalars(stmt).first()
    