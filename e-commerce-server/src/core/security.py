from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import timedelta, datetime, timezone

from user.model import User

pwt_context = CryptContext(schemes='argon2', deprecated='auto')
oauth2_schema = OAuth2PasswordBearer(tokenUrl='auth/login')


def hash_password(password:str) -> str:
    return pwt_context.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    return pwt_context.verify(password, hashed_password)

def gen_access_token(user_id:str) -> str:

    payload = {
        'sub': user_id,
        'exp': datetime.now(timezone.utc) + timedelta(minutes=30),
        'type':'access_token'
    }

    return jwt.encode(payload, 'secrete', algorithm='HS256')

def gen_refresh_token(user_id) -> str:
    payload = {
        'sub': user_id,
        'exp': datetime.now(timezone.utc) + timedelta(days=7),
        'type': 'refresh_token'
    }

    return jwt.encode(payload, 'secret')

def verify_token(token: str = Depends(oauth2_schema)) -> dict:
    try:
        payload = jwt.decode(token=token, key='secrete', algorithms=['HS256'])
        return payload

    except JWTError as e:
        raise Exception
