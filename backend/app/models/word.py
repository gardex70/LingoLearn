from .base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Float, DateTime, ForeignKey
from datetime import datetime

class Word(BaseModel):
    __tablename__ = "Word"

    original: Mapped[str] = mapped_column(String(255))
    tranlation: Mapped[str] = mapped_column(String(255))
    difficulty: Mapped[int] = mapped_column(Float, default=1.0)
    last_reviewed: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    next_review: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    text_id: Mapped[int] = mapped_column(ForeignKey("Text.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"))

    #Relationship
    text: Mapped["Text"] = relationship(back_populates="words")
    user: Mapped["User"] = relationship(back_populates="words")