import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load dataset
df = pd.read_csv("fishmate_training_data.csv")

X = df[
    ["dissolved_oxygen", "ph", "ammonia", "temperature", "tds"]
]
y = df["label"]

# Train-test split (optional but recommended)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    random_state=42
)

model.fit(X_train, y_train)

# Save model
joblib.dump(model, "fishmate_rf_latest_v1.pkl")

print("Model trained and saved successfully")
