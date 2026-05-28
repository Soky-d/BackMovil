from fastapi import FastAPI
from app.database import engine, Base
from app.routes import router

# Crear tablas automáticamente
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Control de Entradas")

from fastapi import FastAPI

app.include_router(router)






