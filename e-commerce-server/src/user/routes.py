from fastapi import APIRouter, Depends, status
from core.database import session
from .schema import UserCreateSchema, UserResponseSchema
from .model import User
from auth.dependecies import get_current_user

router = APIRouter(prefix='/user', tags=['Users'])

@router.get('/me', response_model=UserResponseSchema,)
def get_user(token:str=Depends(get_current_user)):
    return token
    