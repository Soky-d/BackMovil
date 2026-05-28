from sqlalchemy import func
from sqlalchemy.orm import Session
from app.models import Venta

def validar_entrada(db: Session, dni: str, nombres: str):

    dni_limpio = dni.strip()
    nombres_limpios = nombres.strip()

    # --- SÚPER TEST DE DEPURACIÓN ---
    # Esto traerá los primeros 3 usuarios de tu base de datos reales en Render
    test_usuarios = db.query(models.Usuario).limit(3).all()
    print("--- DEPURACIÓN DE DATOS REALES EN RENDER ---")
    for u in test_usuarios:
        print(f"DNI en BD: '{u.dni}' (Tipo: {type(u.dni)}) | Nombre en BD: '{u.nombres}'")
    print(f"Buscando DNI enviado: '{dni_limpio}' | Nombre enviado: '{nombres_limpios}'")
    # ---------------------------------

    # Tu consulta (Búsqueda flexible usando func.trim)

    if not dni:

        venta = db.query(Venta).filter(
            Venta.nombres.ilike(f"%{nombres_limpios}%")
        ).first()

    else:

        venta = db.query(Venta).filter(
            func.trim(Venta.dni) == dni_limpio,
            Venta.nombres.ilike(f"%{nombres_limpios}%")
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