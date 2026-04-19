from fastapi import APIRouter
from core.database import session
from .schema import UserCreatSchema
from .model import User

router = APIRouter(prefix='/user', tags=['Users'])

