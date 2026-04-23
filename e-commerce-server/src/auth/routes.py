from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer

from .schema import Token, LoginUserSchema, SignupUserSchema
from .utils import gen_access_token, gen_refresh_token, authenticate_user

from user.model import User
from core.database import session
from user.repository import create_user, read_by_email

router = APIRouter(prefix='/auth', tags=['Authentication'])
oauth2_schema=OAuth2PasswordBearer(tokenUrl='auth/login')

# def verify_token(token: str = Depends(oauth2_schema)) -> dict:
#     try:
#         payload = jwt.decode(token=token, key='secrete', algorithms=['HS256'])
#         return payload

#     except JWTError as e:
#         return e

@router.get('/')
def get_user(session:session):
    return session.query(User).all()


@router.post('/signup', response_model=Token)
def Signup(request:SignupUserSchema, session:session):

    if read_by_email(request.email, session):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='email already exists')

    new_user = create_user(request, session)

    if new_user:
        access_token = gen_access_token(new_user.id)
        refresh_token = gen_refresh_token(new_user.id)

        return {
            'access_token':access_token,
            'refresh_token':refresh_token,
        }


@router.post('/login', response_model=Token)
def Login(request:LoginUserSchema, session:session):

    user = authenticate_user(request, session)
    
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Wrong Credentials!')

    access_token = gen_access_token(user.id)
    refresh_token = gen_refresh_token(user.id)

    return {
        'access_token':access_token,
        'refresh_token':refresh_token,
        }

@router.post('/refresh-token')
def get_refresh_token():
    ...    