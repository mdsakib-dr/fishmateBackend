from fastapi import APIRouter
from app.api.v1.sensor import router as sensor_router

api_router = APIRouter()
api_router.include_router(sensor_router, tags=["Sensor"])
