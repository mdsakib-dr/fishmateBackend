from app.ml.model import model, CLASS_MAP

def predict_latest(sensor_data: dict):
    X = [[
        sensor_data["dissolved_oxygen"],
        sensor_data["ph"],
        sensor_data["ammonia"],
        sensor_data["temperature"],
        sensor_data["tds"]
    ]]

    prediction = model.predict(X)[0]
    confidence = float(model.predict_proba(X)[0].max())

    return CLASS_MAP[prediction], confidence
