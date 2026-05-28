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
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)