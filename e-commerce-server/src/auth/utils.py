from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import timedelta, datetime, timezone

from user.model import User

# from .erros import ValidationError

pwt_context = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_password(password:str) -> str:
    return pwt_context.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    return pwt_context.verify(password, hashed_password)

def gen_refresh_token(user_id) -> str:
    payload = {
        'sub': user_id,
        'exp': datetime.now(timezone.utc) + timedelta(days=7),
        'type': 'refresh_token'
    }

    return jwt.encode(payload, 'secret')

def gen_access_token(user_id:str) -> str:

    payload = {
        'sub': user_id,
        'exp': datetime.now(timezone.utc) + timedelta(minutes=30),
        'type':'access_token'
    }

    return jwt.encode(payload, 'secrete', algorithm='HS256')

def verify_token(token: str) -> dict:
    try:
        payload = jwt.decode(token=token, key='secrete', algorithms=['HS256'])
        print(payload)
        return payload

    except JWTError as e:
        return e

def get_by_email(email, session):
    return session.query(User).filter(User.email==email).first()

def authenticate_user(payload, session):
    user = get_by_email(payload.email, session)
    
    if not user:
        return None

    if not verify_password(payload.password, user.hashed_password):
        return None

    return user
