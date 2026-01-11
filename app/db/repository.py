from sqlalchemy import text
from app.db.session import engine

def insert_sensor_data(payload):
    query = text("""
        INSERT INTO sensor_data
        (time, device_id, dissolved_oxygen, tds, ph, ammonia, temperature, battery)
        VALUES (
            :time,
            :device_id,
            :dissolved_oxygen,
            :tds,
            :ph,
            :ammonia,
            :temperature,
            :battery
        )
    """)

    with engine.begin() as conn:
        conn.execute(
            query,
            {
                "time": payload.timestamp,
                "device_id": payload.device_id,
                "dissolved_oxygen": payload.do,
                "tds": payload.tds,
                "ph": payload.ph,
                "ammonia": payload.ammonia,
                "temperature": payload.temperature,
                "battery": payload.battery
            }
        )
def get_latest_sensor_data(device_id: str):
    query = text("""
        SELECT
            time,
            device_id,
            dissolved_oxygen,
            tds,
            ph,
            ammonia,
            temperature,
            battery
        FROM sensor_data
        WHERE device_id = :device_id
        ORDER BY time DESC
        LIMIT 1
    """)

    with engine.connect() as conn:
        result = conn.execute(query, {"device_id": device_id}).mappings().first()
        return result


def get_sensor_data_history(device_id: str, start_time, end_time, limit: int):
    query = text("""
        SELECT
            time,
            device_id,
            dissolved_oxygen,
            tds,
            ph,
            ammonia,
            temperature,
            battery
        FROM sensor_data
        WHERE device_id = :device_id
          AND time BETWEEN :start_time AND :end_time
        ORDER BY time ASC
        LIMIT :limit
    """)

    with engine.connect() as conn:
        result = conn.execute(
            query,
            {
                "device_id": device_id,
                "start_time": start_time,
                "end_time": end_time,
                "limit": limit
            }
        ).mappings().all()

        return result
