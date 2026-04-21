from user.model import User
from .utils import hash_password

def create_user(user, session):
    new_resource = User(
        name=user.name,
        email=user.email,
        hashed_password=hash_password(user.password),
    )

    session.add(new_resource)
    session.commit()

    return new_resource

def get_by_email(user_payload, session):
    return session.query(User).filter(User.email==user_payload.email).first()
