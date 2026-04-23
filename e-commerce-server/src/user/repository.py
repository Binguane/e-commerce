from .model import User
from auth.utils import hash_password

def create_user(user, session):
    new_resource = User(
        name=user.username,
        email=user.email,
        hashed_password=hash_password(user.password),
    )

    session.add(new_resource)
    session.commit()

    return new_resource

def read_by_id(user_id, session):
    return session.query(User).filter(User.id==user_id).first()

def read_by_email(user_email, session):
    return session.query(User).filter(User.email==user_email).first()