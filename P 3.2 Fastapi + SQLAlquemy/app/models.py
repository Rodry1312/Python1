from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .database import Base

class Autor(Base):
    __tablename__ = "autores"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    nacionalidad = Column(String)
    edad = Column(Integer)
    activo = Column(Boolean, default=True)
    
    libros = relationship("Libro", back_populates="autor")

class Libro(Base):
    __tablename__ = "libros"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    genero = Column(String)
    precio = Column(Float)
    paginas = Column(Integer)
    autor_id = Column(Integer, ForeignKey("autores.id"))

    autor = relationship("Autor", back_populates="libros")