from pydantic import BaseModel, EmailStr

class UserCreatSchema(BaseModel):
    name: str
    email: EmailStr
    password: str