from pydantic import BaseModel
from typing import Optional

class UsuarioBase(BaseModel):
    Nombre: str
    CC: str

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioUpdate(BaseModel):
    Nombre: Optional[str] = None
    CC: Optional[str] = None

class Usuario(UsuarioBase):
    Id: int

    class Config:
        from_attributes = True  # Cambiado de orm_mode