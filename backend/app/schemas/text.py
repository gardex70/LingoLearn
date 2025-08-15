from pydantic import BaseModel

class TextImport(BaseModel):
    title: str
    author: str
    content: str
    language: str
    user_id: int

class TextResponse(BaseModel):
    id: int
    user_id: int
    title: str
    author: str
    language: str
    total_know_words: int
    total_words: int

class TextListResponse(BaseModel):
    texts: list[TextResponse]
    total: int
    page: int
    per_page: int
    total_pages: int


    
    