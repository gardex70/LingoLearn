from sqlalchemy.orm import Session
from models import Word
from .base_repository import BaseRepository

class WordRepository(BaseRepository[Word]):
    def __init__(self, db: Session):
        super().__init__(Word, db)

    