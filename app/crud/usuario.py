from sqlalchemy.orm import Session
from app.models import usuario

def get_usuario(db: Session, usuario_id: int):
    return db.query(usuario.Usuario).filter(usuario.Usuario.Id == usuario_id).first()

def get_usuarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(usuario.Usuario).offset(skip).limit(limit).all()

def create_usuario(db: Session, usuario_data: dict):
    db_usuario = usuario.Usuario(**usuario_data)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def update_usuario(db: Session, usuario_id: int, usuario_data: dict):
    db_usuario = db.query(usuario.Usuario).filter(usuario.Usuario.Id == usuario_id).first()
    if db_usuario:
        for key, value in usuario_data.items():
            setattr(db_usuario, key, value)
        db.commit()
        db.refresh(db_usuario)
    return db_usuario

def delete_usuario(db: Session, usuario_id: int):
    db_usuario = db.query(usuario.Usuario).filter(usuario.Usuario.Id == usuario_id).first()
    if db_usuario:
        db.delete(db_usuario)
        db.commit()
    return db_usuario