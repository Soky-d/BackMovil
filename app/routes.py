from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas import EntradaRequest, EntradaResponse
from app.crud import validar_entrada

from typing import Annotated

router = APIRouter()

# Dependency DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/validar-entrada", response_model=EntradaResponse)
def validar(
    data: EntradaRequest,
    db: Annotated[Session, Depends(get_db)]
):
    
    result = validar_entrada(db, data.dni,data.nombres)
    return result
