from pydantic import BaseModel, PositiveFloat

class VehicleCreateSchema(BaseModel):
     brand: str
     model: str
     year: str
     price: PositiveFloat
     mileage: PositiveFloat
     description: str
     location: str
     user_id: str


class VehicleResponseSchema(BaseModel):
     id: str
     brand: str
     model: str
     year: str
     price: PositiveFloat
     mileage: PositiveFloat
     description: str
     location: str
     user_id: str
     created_at: str


class VehicleUpdateSchema(BaseModel):
     brand: str
     model: str
     year: str
     price: PositiveFloat
     mileage: PositiveFloat
     description: str
     location: str


