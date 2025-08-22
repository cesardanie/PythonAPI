from fastapi import FastAPI
from app.core.database import engine, Base
from app.api import usuarios  # Importar el router de usuarios

# Crear las tablas en la base de datos (solo para desarrollo)
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Incluir los routers
app.include_router(usuarios.router, prefix="/api/usuarios", tags=["usuarios"])

@app.get("/")
def read_root():
    return {"message": "API de Usuarios funcionando"}