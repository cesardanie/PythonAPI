from sqlalchemy.orm import Session
# Cambia esta línea:
from app.models.usuario import Usuario  # Importación directa

def get_usuario(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.Id == usuario_id).first()

def get_usuarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Usuario).offset(skip).limit(limit).all()

def create_usuario(db: Session, usuario_data: dict):
    db_usuario = Usuario(**usuario_data)  # Usa Usuario directamente
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def update_usuario(db: Session, usuario_id: int, usuario_data: dict):
    db_usuario = db.query(Usuario).filter(Usuario.Id == usuario_id).first()
    if db_usuario:
        for key, value in usuario_data.items():
            setattr(db_usuario, key, value)
        db.commit()
        db.refresh(db_usuario)
    return db_usuario

def delete_usuario(db: Session, usuario_id: int):
    db_usuario = db.query(Usuario).filter(Usuario.Id == usuario_id).first()
    if db_usuario:
        db.delete(db_usuario)
        db.commit()
    return db_usuario