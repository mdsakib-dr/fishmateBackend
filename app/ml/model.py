
import joblib
from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parents[1] / "models" / "fishmate_rf_latest_v1.pkl"

model = joblib.load(MODEL_PATH)

CLASS_MAP = {
    0: "BAD",
    1: "GOOD",
    2: "EXCELLENT"
}
