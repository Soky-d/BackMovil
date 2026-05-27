from sqlalchemy.orm import Session
from app.models import Venta

def validar_entrada(db: Session, dni: str, nombres: str):

    if not dni:

        venta = db.query(Venta).filter(
            Venta.nombres == nombres
        ).first()

    else:

        venta = db.query(Venta).filter(
            Venta.dni == dni,
            Venta.nombres == nombres
        ).first()
    
    # 1. NO EXISTE
    if not venta:
        return {
            "status": "ERROR",
            "message": "Entrada no válida"
        }

    # 2. YA INGRESÓ
    if venta.ticket.strip() == "11":
        return {
            "status": "DUPLICADO",
            "message": "Ya se registró su ingreso"
        }

    # 3. VALIDAR OK → REGISTRAR INGRESO
    venta.ticket = "11"

    db.commit()

    return {
        "status": "OK",
        "message": "Pase, adelante"
    }