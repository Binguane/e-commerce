from fastapi import APIRouter

from core.database import session
from .schema import VehicleCreateSchema
from .repository import create_resource, read_resource


router = APIRouter(prefix='/vehicle', tags=['Vehivles'])

@router.post('/')
def post_vehicle(vehicle:VehicleCreateSchema, session:session):
    new_resource = create_resource(vehicle, session)

    return new_resource

@router.get('/')
def get_vehicle(session:session):
    return read_resource(session)