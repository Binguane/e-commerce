from jose import jwt
from passlib.context import CryptContext

def gen_access_token(payload):
    return jwt.encode(payload, 'secrete')

pwt_context = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_password(password) -> str:
    return pwt_context.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    return pwt_context.verify(password, hashed_password)
