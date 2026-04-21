from pydantic import BaseModel, EmailStr, field_validator

class UserCreateSchema(BaseModel):
    name: str
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
