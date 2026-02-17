from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/libros", tags=["Libros"])

# OBTENER TODOS LOS LIBROS
@router.get("/", response_model=List[schemas.LibroResponse])
def leer_libros(db: Session = Depends(get_db)):
    return db.query(models.Libro).all()

# OBTENER UN LIBRO POR ID
@router.get("/{libro_id}", response_model=schemas.LibroResponse)
def obtener_libro(libro_id: int, db: Session = Depends(get_db)):
    db_libro = db.query(models.Libro).filter(models.Libro.id == libro_id).first()
    if not db_libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return db_libro

# CREAR UN NUEVO LIBRO
@router.post("/", response_model=schemas.LibroResponse, status_code=status.HTTP_201_CREATED)
def crear_libro(libro: schemas.LibroCreate, db: Session = Depends(get_db)):
    # Verificamos si el autor existe antes de crear el libro para evitar errores de FK
    autor_existe = db.query(models.Autor).filter(models.Autor.id == libro.autor_id).first()
    if not autor_existe:
        raise HTTPException(status_code=400, detail="El autor especificado no existe")
    
    nuevo_libro = models.Libro(**libro.model_dump())
    db.add(nuevo_libro)
    db.commit()
    db.refresh(nuevo_libro)
    return nuevo_libro

# ACTUALIZAR UN LIBRO
@router.put("/{libro_id}", response_model=schemas.LibroResponse)
def actualizar_libro(libro_id: int, libro_actualizado: schemas.LibroCreate, db: Session = Depends(get_db)):
    query_libro = db.query(models.Libro).filter(models.Libro.id == libro_id)
    db_libro = query_libro.first()
    
    if not db_libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    
    query_libro.update(libro_actualizado.model_dump(), synchronize_session=False)
    db.commit()
    return query_libro.first()

# ELIMINAR UN LIBRO
@router.delete("/{libro_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_libro(libro_id: int, db: Session = Depends(get_db)):
    db_libro = db.query(models.Libro).filter(models.Libro.id == libro_id).first()
    
    if not db_libro:
        raise HTTPException(status_code=404, detail="El libro no existe")
    
    db.delete(db_libro)
    db.commit()
    return None