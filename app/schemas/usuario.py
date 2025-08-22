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
        orm_mode = True
        from_attributes = True  # Para SQLAlchemy 2.0