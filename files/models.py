
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from connection import Base, engine
import datetime

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    email = Column(String(200))
    senha = Column(String(32))

class Tokens(Base):
    __tablename__ = "users_tokens"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    token = Column(String(100))
    dt_valid = Column(DateTime, default=datetime.datetime.utcnow())

if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
