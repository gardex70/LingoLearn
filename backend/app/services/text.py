from sqlalchemy.orm import Session
from repositories import TextRepository, PageRepository, TextWordRepository
from schemas.text import TextImport, TextResponse
from core.utils import parse_text_into_pages, parse_text_into_words, get_text_total_words

def import_text(db: Session, text_data: TextImport) -> TextResponse:
    try:
        text_repo = TextRepository(db)
        text_to_create = {
            "user_id": text_data.user_id,
            "title": text_data.title,
            "autor": text_data.author,
            "language": text_data.language,
            "total_words": get_text_total_words(text_data.content)
        }
        new_text = text_repo.create(**text_to_create)
        db.flush()
        db.refresh(new_text)

        page_repo = PageRepository(db)
        pages = parse_text_into_pages(text=text_data.content, words_per_page=300)
        for i, page in enumerate(pages):
            page_to_create = {
                "text_id": new_text.id,
                "number": i+1,
                "content": page 
            }
            page_repo.create(**page_to_create)

        word_repo = TextWordRepository(db)
        words = parse_text_into_words(text_data.content)
        for word, count in words:
            word_to_create = {
                "text_id": new_text.id,
                "normalized": word,
                "appearance_count": count
            }
            word_repo.create(**word_to_create)

        db.commit()

        text_response = TextResponse(
            id=new_text.id,
            user_id=new_text.user_id,
            title=new_text.title,
            author=new_text.autor,
            language=new_text.language
        )

        return text_response
    except Exception:
        db.rollback()
        raise
