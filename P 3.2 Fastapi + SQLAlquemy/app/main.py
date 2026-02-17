from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routes import autores, libros

# Crea las tablas físicamente en el archivo biblioteca.db
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Biblioteca Digital")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluimos los routers
app.include_router(autores.router)
app.include_router(libros.router)

@app.get("/")
def home():
    return {"message": "API Funcionando Correctamente"}