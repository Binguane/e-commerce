from fastapi import FastAPI

from core.config import settings
from core.database import Base, engine 

from user.routes import router as user_router
from vehicle.routes import router as vehicle_router
from auth.routes import router as auth_router

app = FastAPI(
    title=settings.app_name
)

Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(vehicle_router)
app.include_router(auth_router)

@app.get('/healthcheck')
def health_check():
    return {'status':'ok'}



