from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Usuario(Base):
    __tablename__ = "Usuarios"

    Id = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(100))
    CC = Column(String(50))