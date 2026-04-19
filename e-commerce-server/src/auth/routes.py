from fastapi import APIRouter
from user.schema import UserCreatSchema
from user.model import User
from core.database import session
from .utils import hash_password

router = APIRouter(prefix='/auth', tags=['Authentication'])

@router.get('/')
def get_user(session:session):
    return session.query(User).all()

@router.post('/')
def post_user(user:UserCreatSchema, session:session):
    new_user = User(
        name=user.name,
        email=user.email,
        hashed_password=hash_password(user.password),
    )

    session.add(new_user)
    session.commit()

    return new_user