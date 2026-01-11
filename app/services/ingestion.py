from app.services.quality_check import validate_sensor_data
from app.db.repository import insert_sensor_data

def ingest_sensor_data(payload):
    validate_sensor_data(payload)
    insert_sensor_data(payload)
