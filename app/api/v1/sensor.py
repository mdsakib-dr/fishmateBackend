# from fastapi import APIRouter, Depends, HTTPException, Query
# from datetime import datetime
# from app.models.sensor import SensorPayload
# from app.services.ingestion import ingest_sensor_data
# from app.core.security import verify_api_key
# from app.services.reading import fetch_latest_data, fetch_history
# from app.ml.predict import predict_latest
# from sqlalchemy import text
# from app.db.session import engine


# router = APIRouter()

# @router.post("/sensor-data")
# def receive_data(
#     payload: SensorPayload,
#     api_key: str = Depends(verify_api_key)
# ):
#     ingest_sensor_data(payload)
#     return {"status": "success"}


# @router.post("/sensor-data")
# def ingest_sensor_data(payload: SensorDataIn):

#     save_sensor_data(payload)  # existing logic

#     verdict, confidence = predict_latest(payload.dict())

#     verdict_map = {"BAD": 0, "GOOD": 1, "EXCELLENT": 2}

#     query = """
#     INSERT INTO water_quality_verdict (
#         time, device_id,
#         dissolved_oxygen, ph, ammonia, temperature, tds,
#         verdict, confidence, model_version
#     )
#     VALUES (
#         :time, :device_id,
#         :do, :ph, :ammonia, :temp, :tds,
#         :verdict, :confidence, :version
#     )
#     """

#     with engine.begin() as conn:
#         conn.execute(text(query), {
#             "time": payload.timestamp,
#             "device_id": payload.device_id,
#             "do": payload.do,
#             "ph": payload.ph,
#             "ammonia": payload.ammonia,
#             "temp": payload.temperature,
#             "tds": payload.tds,
#             "verdict": verdict_map[verdict],
#             "confidence": confidence,
#             "version": "rf_v1"
#         })

#     return {
#         "status": "ingested",
#         "verdict": verdict,
#         "confidence": confidence
#     }


# @router.get("/sensor-data/latest/{device_id}", dependencies=[Depends(verify_api_key)])
# def get_latest(device_id: str):
#     data = fetch_latest_data(device_id)

#     if not data:
#         raise HTTPException(status_code=404, detail="No data found for device")

#     return data


# @router.get("/sensor-data/history/{device_id}", dependencies=[Depends(verify_api_key)])
# def get_history(
#     device_id: str,
#     start_time: datetime = Query(..., description="ISO 8601 start time"),
#     end_time: datetime = Query(..., description="ISO 8601 end time"),
#     limit: int = Query(500, ge=1, le=5000)
# ):
#     data = fetch_history(device_id, start_time, end_time, limit)

#     if not data:
#         raise HTTPException(status_code=404, detail="No data found for given range")

#     return data

from fastapi import APIRouter, Depends, HTTPException, Query
from datetime import datetime
from sqlalchemy import text

from app.models.sensor import SensorPayload
from app.services.ingestion import ingest_sensor_data
from app.core.security import verify_api_key
from app.services.reading import fetch_latest_data, fetch_history
from app.ml.predict import predict_latest
from app.db.session import engine

router = APIRouter()


@router.post("/sensor-data")
def receive_data(
    payload: SensorPayload,
    api_key: str = Depends(verify_api_key)
):
    # 1️⃣ Existing ingestion (UNCHANGED)
    ingest_sensor_data(payload)

    # 2️⃣ ML prediction (LATEST DATA ONLY)
    verdict, confidence = predict_latest(payload.dict())

    verdict_map = {"BAD": 0, "GOOD": 1, "EXCELLENT": 2}

    # 3️⃣ Save verdict (NEW, NON-BREAKING)
    query = """
    INSERT INTO water_quality_verdict (
        time, device_id,
        dissolved_oxygen, ph, ammonia, temperature, tds,
        verdict, confidence, model_version
    )
    VALUES (
        :time, :device_id,
        :do, :ph, :ammonia, :temp, :tds,
        :verdict, :confidence, :version
    )
    """

    with engine.begin() as conn:
        conn.execute(text(query), {
            "time": payload.timestamp,
            "device_id": payload.device_id,
            "do": payload.do,
            "ph": payload.ph,
            "ammonia": payload.ammonia,
            "temp": payload.temperature,
            "tds": payload.tds,
            "verdict": verdict_map[verdict],
            "confidence": confidence,
            "version": "rf_v1"
        })

    # 4️⃣ Response (BACKWARD SAFE)
    return {
        "status": "success",
        "verdict": verdict,
        "confidence": confidence
    }


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
