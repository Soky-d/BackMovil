from sqlalchemy import Column, Integer, String
from app.database import Base

class Venta(Base):
    __tablename__ = "ventas"

    id = Column(Integer, primary_key=True, index=True)
    dni = Column(String, index=True)
    nombres = Column(String)
    ticket = Column(String, default="00")