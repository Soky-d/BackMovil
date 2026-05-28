# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
#
#DATABASE_URL = "postgresql://ruvay_user:WL2WrZihzcWnVt4H8O9K2m0G2yXZEtzU@dpg-d5e2356uk2gs739an4j0-a.virginia-postgres.render.com/ruvay"
#
#
#engine = create_engine(DATABASE_URL)
#
#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
#Base = declarative_base()

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Intenta leer la URL desde Render. Si estás en tu PC (local), usará el plan B.
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://ruvay_user:WL2WrZihzcWnVt4H8O9K2m0G2yXZEtzU@dpg-d5e2356uk2gs739an4j0-a.virginia-postgres.render.com/ruvay"
)

# ⚠️ NOTA CRÍTICA PARA RELEVANTE EN RENDER:
# SQLAlchemy requiere que el prefijo sea 'postgresql://'. 
# Si Render te da una URL que inicia con 'postgres://', este código lo corrige automáticamente:
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://usuario_local:postgresql@localhost:08126172/bdlocal"
)

# 2. Corrección crítica de protocolo para SQLAlchemy en Render
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# 3. Crear el motor de conexión
engine = create_engine(DATABASE_URL)

# 4. Crear la fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 5. Base para heredar en tus modelos de tablas
Base = declarative_base()

# 6. Función de dependencia para abrir y cerrar la BD automáticamente
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()