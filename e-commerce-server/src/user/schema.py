from pydantic import BaseModel, EmailStr, field_validator

class UserSignupSchema(BaseModel):
    name: str
    email: EmailStr
    password: str

    @field_validator("email")
    @classmethod
    def lower_case_email(cls, value: EmailStr):
        return value.lower()


class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str
    
    @field_validator("email")
    @classmethod
    def lower_case_email(cls, value: EmailStr):
        return value.lower()


class UserResponseSchema(BaseModel):
    id:str
    name:str
    email:str


class UserUpdateSchema(BaseModel):
    name:str
    email:EmailStr

    @field_validator("email")
    @classmethod
    def lower_case_email(cls, value: EmailStr):
        return value.lower()