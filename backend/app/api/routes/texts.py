from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.text import create_text
from schemas.text import TextCreate, TextResponse
from database.connection import get_db

router = APIRouter(prefix="/texts", tags=["texts"])

@router.post("/", response_model=TextResponse, status_code=201)
def create_text_endpoint(
    text: TextCreate,
    db: Session = Depends(get_db)
):  
    try:
        return create_text(db, text)
    except ValueError as e:
        print(f'aaa: {str(e)}')
        raise HTTPException(status_code=400, detail="Ocorreu um erro interno")
    except Exception as e:
        print(f'bbb: {str(e)}')
        raise HTTPException(status_code=500, detail="Ocorreu um erro interno ao processar seu registro")