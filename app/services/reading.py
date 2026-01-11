from app.db.repository import (
    get_latest_sensor_data,
    get_sensor_data_history
)


def fetch_latest_data(device_id: str):
    return get_latest_sensor_data(device_id)


def fetch_history(device_id: str, start_time, end_time, limit: int):
    return get_sensor_data_history(device_id, start_time, end_time, limit)
