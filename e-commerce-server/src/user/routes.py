from fastapi import APIRouter, Depends, status, HTTPException

from .schema import UserUpdateSchema, UserResponseSchema, UserLoginSchema
from .repository import read_by_id

from core.database import session
from auth.dependecies import get_current_user
from auth.utils import verify_token
from user.repository import read_by_id

router = APIRouter(prefix='/user', tags=['Users'], dependencies=[])

@router.get('/me', response_model=UserResponseSchema,)
def get_me(session:session, token:str=Depends(get_current_user)):
    user=verify_token(token)
    user_n=read_by_id(user['sub'], session)
    return user_n

@router.put('/')
def update_user(request:UserUpdateSchema, session:session):
    ...

@router.delete('/')
def delete_user(session:session):
    ...
    
