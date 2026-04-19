from .model import Vehicle
from user.repository import read_resource as read_user


def create_resource(vehicle, session):
    user = read_user(vehicle.user_id, session)

    if not user:
        return None

    resource = Vehicle(**vehicle.model_dump())
    session.add(resource)
    session.commit()

    print(resource.id)
    return resource

def read_resource(session):
    vehicles = session.query(Vehicle).all()
    return vehicles
