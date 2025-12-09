from sqlalchemy import Column, Integer, String
from model.dao import Base

class Usuario(Base): # Modelo de usuário
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100))
    email = Column(String(100))
    senha = Column(String(200))
