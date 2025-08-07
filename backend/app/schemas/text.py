from pydantic import BaseModel

class TextImport(BaseModel):
    title: str
    autor: str
    content: str
    language: str
    user_id: int

class TextResponse(BaseModel):
    id: int
    user_id: int
    title: str
    autor: str
    language: str

    
    