from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
from os import environ

Base = declarative_base()
load_dotenv()

CONN = environ.get('SQL_CONN')
engine = create_engine(CONN, echo=True)
