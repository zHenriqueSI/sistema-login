
from sqlalchemy import Column, Integer, String
from connection import Base, engine

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    email = Column(String(200))
    senha = Column(String(32))

Base.metadata.create_all(bind=engine)
