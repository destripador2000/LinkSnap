from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlmodel import SQLModel
from config.db import engine
from models.url_model import Link  # Si no se importa esto, no se crea la tabla

# El ciclo de vida de la app
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Iniciando proyecto")
    # Crea las tablas definidas en los modelos importados
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    yield
    print("Apagando proyecto")

# Instancia de la app
app = FastAPI(
    title="LinkSnap API",
    version="1.0.0",
    lifespan=lifespan
)

@app.get("/")
async def home():
    return {"message": "Servidor encendido"}