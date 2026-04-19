from .model import User

def read_resource(user_id, session):
    resource = session.query(User).filter(User.id==user_id).first()

    print(resource.name)

    if not resource:
        return None

    return resource
