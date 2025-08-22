from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Configuración de conexión a la base de datos
server = 'GWNR71517\\SQLEXPRESS'  # Usa doble backslash para escape
database = 'Prueba'  # Nombre de tu base de datos

SQLALCHEMY_DATABASE_URL = f'mssql+pyodbc://@{server}/{database}?trusted_connection=yes&driver=SQL+Server&Encrypt=no'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()