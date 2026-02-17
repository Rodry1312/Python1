from pydantic import BaseModel
from typing import List, Optional

# Esquemas para LIBROS (Deben ir primero)
class LibroBase(BaseModel):
    titulo: str
    genero: str
    precio: float
    paginas: int
    autor_id: int

class LibroCreate(LibroBase):
    pass

class LibroResponse(LibroBase):
    id: int
    class Config:
        from_attributes = True

# Esquemas para AUTORES
class AutorBase(BaseModel):
    nombre: str
    nacionalidad: str
    edad: int
    activo: bool

class AutorCreate(AutorBase):
    pass

class AutorResponse(AutorBase):
    id: int
    libros: List[LibroResponse] = [] # Ahora ya sabe qué es LibroResponse
    class Config:
        from_attributes = True