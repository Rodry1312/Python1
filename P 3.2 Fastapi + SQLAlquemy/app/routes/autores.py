from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/autores", tags=["Autores"])

# OBTENER TODOS LOS AUTORES
@router.get("/", response_model=List[schemas.AutorResponse])
def leer_autores(db: Session = Depends(get_db)):
    return db.query(models.Autor).all()

# CREAR UN AUTOR
@router.post("/", response_model=schemas.AutorResponse, status_code=status.HTTP_201_CREATED)
def crear_autor(autor: schemas.AutorCreate, db: Session = Depends(get_db)):
    nuevo_autor = models.Autor(**autor.model_dump())
    db.add(nuevo_autor)
    db.commit()
    db.refresh(nuevo_autor)
    return nuevo_autor

# OBTENER UN AUTOR POR ID
@router.get("/{autor_id}", response_model=schemas.AutorResponse)
def obtener_autor(autor_id: int, db: Session = Depends(get_db)):
    db_autor = db.query(models.Autor).filter(models.Autor.id == autor_id).first()
    if not db_autor:
        raise HTTPException(status_code=404, detail="Autor no encontrado")
    return db_autor

# ACTUALIZAR UN AUTOR
@router.put("/{autor_id}", response_model=schemas.AutorResponse)
def actualizar_autor(autor_id: int, autor_actualizado: schemas.AutorCreate, db: Session = Depends(get_db)):
    query = db.query(models.Autor).filter(models.Autor.id == autor_id)
    db_autor = query.first()
    
    if not db_autor:
        raise HTTPException(status_code=404, detail="Autor no encontrado para actualizar")
    
    query.update(autor_actualizado.model_dump(), synchronize_session=False)
    db.commit()
    return query.first()

# ELIMINAR UN AUTOR
@router.delete("/{autor_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_autor(autor_id: int, db: Session = Depends(get_db)):
    db_autor = db.query(models.Autor).filter(models.Autor.id == autor_id).first()
    
    if not db_autor:
        raise HTTPException(status_code=404, detail="Autor no encontrado")
    
    db.delete(db_autor)
    db.commit()
    return None