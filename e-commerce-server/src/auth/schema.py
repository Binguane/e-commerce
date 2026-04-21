from pydantic import BaseModel, EmailStr


class Token(BaseModel):
    access_token: str
    refresh_token: str

class SignupUserSchema(BaseModel):
    username:str
    email:EmailStr
    password:str

class LoginUserSchema(BaseModel):
    email: EmailStr
    password: str
