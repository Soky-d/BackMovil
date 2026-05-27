from pydantic import BaseModel

class EntradaRequest(BaseModel):
    dni: str
    nombres: str

class EntradaResponse(BaseModel):
    status: str
    message: str