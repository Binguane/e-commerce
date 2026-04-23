from pydantic import BaseModel, EmailStr, field_validator

class Token(BaseModel):
    access_token: str
    refresh_token: str

class SignupUserSchema(BaseModel):
    username:str
    email:EmailStr
    password:str
    
    @field_validator("email")
    @classmethod
    def lower_case_email(cls, value: EmailStr):
        return value.lower()

class LoginUserSchema(BaseModel):
    email: EmailStr
    password: str
    
    @field_validator("email")
    @classmethod
    def lower_case_email(cls, value: EmailStr):
        return value.lower()
