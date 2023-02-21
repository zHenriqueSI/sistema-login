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
        try:
            session.query(Users).filter(Users.email==email).one()
            return True
        except Exception:
            return False


    @staticmethod
    def validade_password(password):
        regex = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$'
        return bool(re.match(regex, password))   


    @staticmethod
    def encrypt_password(password):
        return md5(password.encode()).hexdigest()


class ControllerCadastro(ControllerGeneral):
    @classmethod
    def register_user(cls, name, email, password):
        if len(name) > 50:
            return 2
        elif not super().validate_email(email) or super().check_email_existence(email):
            return 3
        elif not super().validade_password(password):
            return 4
        else:
            session = super().return_session()
            user = Users(nome=name, email=email, senha=super().encrypt_password(password))
            session.add(user)
            session.commit()
            return 1
