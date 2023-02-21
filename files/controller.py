from sqlalchemy.orm import sessionmaker
from connection import engine
from hashlib import md5
from models import Users
import re


class ControllerGeneral:
    @staticmethod
    def return_session():
        Session = sessionmaker(bind=engine)
        return Session()


    @staticmethod
    def validate_email(email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        return bool(re.match(regex, email))


    @classmethod
    def check_email_existence(cls, email):
        session = cls.return_session()
        email_exists = bool(session.query(Users).filter(email=email).one())

    @staticmethod
    def validade_password(password):
        regex = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$'
        return bool(re.match(regex, password))   


    @staticmethod
    def encrypt_password(password):
        return md5(password.encode()).hexdigest()
