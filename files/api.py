from fastapi import FastAPI
from pydantic import BaseModel
from controller import ControllerCadastro, ControllerLogin

app = FastAPI()


class UserRegister(BaseModel):
    name: str
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


@app.post('/register')
def register(user: UserRegister):
    register_status = ControllerCadastro.register_user(user.name, user.email, user.password)
    if register_status == 1:
        return {"message": "user successfully registered"}
    elif register_status == 2:
        return{"error": "the name must contain less than 50 characters"}
    elif register_status == 3:
        return{"error": "register a valid email"}
    elif register_status == 4:
        return{"error": "the password it is not strong enough"}
    else:
        return{"error": "unknown error"}
    

@app.post('/login')
def login(user: UserLogin):
    print(user.email)
    login = ControllerLogin.login(user.email, user.password)
    if login:
        return {"message": f"user {login} have successfully logged in"}
    else:
        return {"message": "email or password is incorrect"}