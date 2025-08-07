from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.text import import_text
from schemas.text import TextImport, TextResponse
from database.connection import get_db

router = APIRouter(prefix="/texts", tags=["texts"])

@router.post("/", response_model=TextResponse, status_code=201)
def create_text_endpoint(
    text: TextImport,
    db: Session = Depends(get_db)
):  
    return import_text(db, text)
   