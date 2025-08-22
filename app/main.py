# app/main.py
from fastapi import FastAPI
from app.core.database import engine, Base

app = FastAPI()

@app.on_event("startup")
def on_startup():
    """
    Importa aquí todos los módulos que definen modelos para que sus clases
    se registren en Base.metadata antes de llamar a create_all.
    """
    # IMPORTANTE: ajusta la ruta si tus modelos están en otra parte.
    # Ejemplo común: app.models o app.api.usuarios.models, etc.
    try:
        import app.models  # <-- Cambia esto por el módulo donde tienes tus clases declarativas
    except Exception:
        # Si no tienes un módulo central de modelos, importa los módulos donde los declares.
        # Ejemplo: from app.api.usuarios import models as usuarios_models
        pass

    # Crear tablas en startup (no al importar el módulo)
    Base.metadata.create_all(bind=engine)


# ahora importa y registra routers (después del evento startup está bien)
from app.api import usuarios  # importa routers aquí
app.include_router(usuarios.router, prefix="/api/usuarios", tags=["usuarios"])


@app.get("/")
def read_root():
    return {"message": "API de Usuarios funcionando"}
