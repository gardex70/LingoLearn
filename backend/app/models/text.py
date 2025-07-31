
from __future__ import annotations
from .base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Text  

class Text(BaseModel):
    __tablename__ = "Text"

    title: Mapped[str] = mapped_column(String(255))
    content: Mapped[str] = mapped_column(Text)
    language: Mapped[str] = mapped_column(String(10))
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"))

    #Relationships
    user: Mapped["User"] = relationship(back_populates="texts")
    words: Mapped[list["Word"]] = relationship(back_populates="text")