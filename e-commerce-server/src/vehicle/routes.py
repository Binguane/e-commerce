from fastapi import APIRouter, Depends, HTTPException, status, UploadFile
from pathlib import Path

from core.database import session
from .schema import VehicleCreateSchema
from .repository import create_resource, read_resource
from auth.dependecies import get_current_user


router = APIRouter(prefix='/vehicle', tags=['Vehivles'])

BASE_DIR=Path(__file__).resolve().parent.parent.parent
Target = f'{BASE_DIR}/filesDB'

@router.post('/')
def post_vehicle(vehicle:VehicleCreateSchema, session:session, current_user=Depends(get_current_user)):

    if current_user==None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid Credentials')

    new_resource = create_resource(vehicle, session)
    print(new_resource)
    breakpoint()
    return new_resource

@router.get('/')
def get_vehicle(session:session):
    return read_resource(session)

@router.post('/ilustration')
async def post_pics(file:UploadFile):
    
    file_data = await file.read()

    with open(f'{Target}/{file.filename}', 'wb') as f:
        f.write(file_data)

    return {'filename':file.filename}
