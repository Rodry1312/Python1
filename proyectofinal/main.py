from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import engine, Base, get_db
from models.anime import Anime  # Asegúrate de que el nombre coincida con tu archivo

# Crear tablas con el nuevo modelo de Anime
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mi Colección de Anime con Docker")

@app.get("/")
def read_root():
    return {"message": "¡Catálogo de Anime listo!"}

# 1. Añadir un Anime (POST)
@app.post("/animes/")
def create_anime(title: str, genre: str, episodes: int, db: Session = Depends(get_db)):
    nuevo_anime = Anime(title=title, genre=genre, episodes=episodes)
    db.add(nuevo_anime)
    db.commit()
    db.refresh(nuevo_anime)
    return nuevo_anime

# 2. Listar todos los Animes (GET)
@app.get("/animes/")
def get_animes(db: Session = Depends(get_db)):
    return db.query(Anime).all()

# 3. Actualizar datos de un Anime (PUT)
@app.put("/animes/{anime_id}")
def update_anime(anime_id: int, title: str, genre: str, episodes: int, db: Session = Depends(get_db)):
    anime = db.query(Anime).filter(Anime.id == anime_id).first()
    if not anime:
        raise HTTPException(status_code=404, detail="Anime no encontrado")
    
    anime.title = title
    anime.genre = genre
    anime.episodes = episodes
    
    db.commit()
    db.refresh(anime)
    return anime

# 4. Eliminar de la colección (DELETE)
@app.delete("/animes/{anime_id}")
def delete_anime(anime_id: int, db: Session = Depends(get_db)):
    anime = db.query(Anime).filter(Anime.id == anime_id).first()
    if not anime:
        raise HTTPException(status_code=404, detail="Ese anime no existe")
    
    db.delete(anime)
    db.commit()
    return {"message": f"'{anime.title}' ha sido eliminado de tu lista"}