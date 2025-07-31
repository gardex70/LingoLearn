from pydantic import BaseModel


class TextCreate(BaseModel):
    title: str
    content: str
    language: str
    user_id: int

class TextResponse(BaseModel):
    id: int
    title: str
    content: str
    language: str
    user_id: int

    
    