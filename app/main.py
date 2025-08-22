from fastapi import FastAPI
from app.api import user  # importamos las rutas

app = FastAPI(title="Mi API en FastAPI")

# incluir las rutas
app.include_router(user.router, prefix="/users", tags=["Users"])

@app.get("/")
def root():
    return {"message": "Bienvenido a la API con FastAPI 🚀"}
