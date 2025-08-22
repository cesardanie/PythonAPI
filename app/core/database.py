# app/core/database.py
import urllib.parse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Ajusta estos valores a los tuyos
server = r'GWNR71517\SQLEXPRESS'  # raw string para que el backslash no haga problemas
database = 'Prueba'

# Cadena ODBC recomendada (usa ODBC Driver 18)
odbc_str = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    f"SERVER={server};"
    f"DATABASE={database};"
    "Trusted_Connection=Yes;"       # si usas autenticación integrada de Windows
    "Encrypt=no;"                  # en local; en Azure usar Encrypt=yes
    "TrustServerCertificate=yes;"
)

params = urllib.parse.quote_plus(odbc_str)
SQLALCHEMY_DATABASE_URL = f"mssql+pyodbc:///?odbc_connect={params}"

# Crea el engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,
    # no habilites fast_executemany por ahora si tienes problemas; se puede activar luego
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
