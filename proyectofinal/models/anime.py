from sqlalchemy import Column, Integer, String
from database.database import Base

class Anime(Base):
    __tablename__ = "animes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    genre = Column(String)
    episodes = Column(Integer)