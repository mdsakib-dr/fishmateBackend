from fastapi import APIRouter, Depends, HTTPException, Query
from datetime import datetime
from app.models.sensor import SensorPayload
from app.services.ingestion import ingest_sensor_data
from app.core.security import verify_api_key
from app.services.reading import fetch_latest_data, fetch_history

router = APIRouter()

@router.post("/sensor-data")
def receive_data(
    payload: SensorPayload,
    api_key: str = Depends(verify_api_key)
):
    ingest_sensor_data(payload)
    return {"status": "success"}
@router.get("/sensor-data/latest/{device_id}", dependencies=[Depends(verify_api_key)])
def get_latest(device_id: str):
    data = fetch_latest_data(device_id)

    if not data:
        raise HTTPException(status_code=404, detail="No data found for device")

    return data


@router.get("/sensor-data/history/{device_id}", dependencies=[Depends(verify_api_key)])
def get_history(
    device_id: str,
    start_time: datetime = Query(..., description="ISO 8601 start time"),
    end_time: datetime = Query(..., description="ISO 8601 end time"),
    limit: int = Query(500, ge=1, le=5000)
):
    data = fetch_history(device_id, start_time, end_time, limit)

    if not data:
        raise HTTPException(status_code=404, detail="No data found for given range")

    return data
