from pydantic import BaseModel
from datetime import datetime

class SensorPayload(BaseModel):
    device_id: str
    timestamp: datetime
    do: float
    tds: float
    ph: float
    ammonia: float
    temperature: float
    battery: float
