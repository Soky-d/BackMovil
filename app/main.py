from fastapi import FastAPI
from app.database import engine, Base
from app.routes import router

# Crear tablas automáticamente
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Control de Entradas")

app.include_router(router)