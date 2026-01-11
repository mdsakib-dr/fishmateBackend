def validate_sensor_data(p):
    if not (0 <= p.do <= 20):
        raise ValueError("Invalid DO value")
    if not (0 <= p.ph <= 14):
        raise ValueError("Invalid pH value")
    if p.ammonia < 0:
        raise ValueError("Invalid Ammonia value")
    if not (0 <= p.temperature <= 50):
        raise ValueError("Invalid Temperature value")
