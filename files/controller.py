from sqlalchemy.orm import sessionmaker
from connection import engine
from hashlib import md5
from models import Users, Tokens
from secrets import token_hex
import datetime
import re

class ControllerGeneral:
    @staticmethod
    def return_session():
        Session = sessionmaker(bind=engine)
        return Session()

    @staticmethod
    def validate_email(email):
        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        return bool(re.match(regex, email))

    @classmethod
    def check_email_existence(cls, email):
        session = cls.return_session()
        try:
            session.query(Users).filter(Users.email == email).one()
            return True
        except Exception:
            return False

    @staticmethod
    def validade_password(password):
        regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$'
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


class ControllerLogin(ControllerGeneral):
    @classmethod
    def login(cls, email, senha):
        session = super().return_session()
        senha_encrypted = super().encrypt_password(senha)

        try:
            login_success = session.query(Users).filter_by(email=email, senha=senha_encrypted).one()
            cls.update_token(login_success.id, session)
            return login_success.nome
        except Exception:
            return False
        

    @classmethod
    def update_token(cls, user_id, session):
        token = token_hex(50)
        try:
            user_token = session.query(Tokens).filter_by(user_id=user_id).one()
            user_token.token = token
            user_token.login_dt = datetime.datetime.now()
            
        except Exception:
            new_token = Tokens(user_id=user_id, token=token, login_dt=datetime.datetime.now())
            session.add(new_token)
        finally:
            session.commit()
