from sqlalchemy.orm import Session
from repositories.text import TextRepository 
from schemas.text import TextCreate 
from  core.logging import logging

def create_text(db: Session, text_data: TextCreate):
    try:
        text_repo = TextRepository(db)
        new_text = text_repo.create(**text_data.model_dump())

        db.commit()
        db.refresh(new_text)

        return new_text
    except Exception as e:
        logging.error(f"Failed to create text: {text_data.title}. Error: {str(e)}")
        db.rollback()
        raise