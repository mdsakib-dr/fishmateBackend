from fastapi import Header, HTTPException
from app.core.config import DEVICE_API_KEY

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != DEVICE_API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized device")
