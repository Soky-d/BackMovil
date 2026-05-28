from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Annotated

# 1. Importas get_db directamente desde tu archivo centralizado de base de datos
from app.database import get_db 
from app.schemas import EntradaRequest, EntradaResponse
from app.crud import validar_entrada

router = APIRouter()

@router.post("/validar-entrada", response_model=EntradaResponse)
def validar(
    data: EntradaRequest,
    db: Annotated[Session, Depends(get_db)] # 2. Ahora usa la dependencia centralizada
):
    try:
        # 3. Ejecutas la validación en tu archivo CRUD
        result = validar_entrada(db, data.dni, data.nombres)
        
        # 4. Si el resultado es nulo o inválido, manejas el error HTTP adecuadamente
        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Entrada no válida o usuario no encontrado"
            )
            
        return result
        
    except Exception as e:
        # 5. Evitas que el servidor colapse ante fallos inesperados de la BD
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error interno en el servidor: {str(e)}"
        )