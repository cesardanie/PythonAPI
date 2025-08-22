from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Usuario(Base):
    __tablename__ = "Usuarios"  # Nombre exacto de la tabla en SQL Server

    Id = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(100))
    CC = Column(String(50))  # Asumiendo que CC es una cadena

    # Si necesitas mapear nombres diferentes, puedes usar:
    # __table_args__ = {'extend_existing': True}