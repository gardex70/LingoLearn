from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from .base_model import BaseModel

class User(BaseModel):
    __tablename__ = "user"
    
    username: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, unique=True)
    password: Mapped[str] = mapped_column(String)