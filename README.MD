# 🐟 FishMate – Smart IoT Aquaculture Monitoring System (Backend)

![Status](https://img.shields.io/badge/Status-Active_Development-brightgreen)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95%2B-009688)
![Database](https://img.shields.io/badge/PostgreSQL-TimescaleDB-336791)

**FishMate** is a smart IoT-based aquaculture monitoring platform that combines **real-time sensor ingestion**, **time-series data storage**, and **machine learning–driven water quality prediction** to prevent fish mortality and optimize yield.

This repository contains the **production-grade backend**, acting as the system’s brain — ingesting ESP32 sensor data, validating it, running ML inference, storing it efficiently, and serving it via APIs.

🔗 **Frontend UI (Figma)**  
https://real-bask-81965835.figma.site/

---

## 🚀 Core Capabilities

### 📡 Real-Time IoT Data Ingestion
- Handles **high-frequency ESP32 sensor writes**
- Fully validated using **Pydantic**
- Designed for horizontal scaling

**Tracked Parameters**
- 💧 Dissolved Oxygen (DO)
- 🌡️ Temperature
- 🧪 pH
- 🌫️ TDS / Turbidity
- ☠️ Ammonia (NH₃)
- 🔋 Device voltage & health

---

### 🧠 ML-Powered Water Quality Prediction
- **Random Forest Classifier**
- Real-time inference on every reading
- Stored alongside raw sensor data

**Prediction Classes**
- 🟢 `EXCELLENT`
- 🟡 `GOOD`
- 🔴 `BAD`

**Extras**
- Confidence probability
- Rule-based + ML hybrid validation

---

### 💾 Time-Series Optimized Storage
- **PostgreSQL + TimescaleDB**
- Sensor data stored as hypertables
- Optimized for:
  - High write throughput
  - Fast historical queries
  - Long-term storage

---

### 🔔 Intelligent Alert Readiness
- Threshold-based checks
- ML-based predictive flags
- Debouncing-ready service layer

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| API Framework | FastAPI |
| Language | Python 3.10+ |
| Database | PostgreSQL + TimescaleDB |
| ORM | SQLAlchemy |
| Validation | Pydantic |
| ML | Scikit-learn |
| Data Processing | Pandas |
| Deployment Ready | Uvicorn |

---

## 🧩 System Architecture (From Actual Codebase)

### 🔁 End-to-End Data Flow
ESP32 Sensors
↓ (HTTP JSON)
FastAPI Router
↓
Service Layer
↓
Quality Checks + ML Inference
↓
TimescaleDB (Hypertables)
↓
REST API → Dashboard / Mobile App


---

## 📂 Backend Architecture (Verified)

```bash
fishmate-backend/
├── app/
│   ├── main.py                  # FastAPI app entry point
│
│   ├── api/
│   │   └── v1/
│   │       ├── router.py        # API version router
│   │       └── sensor.py        # Sensor endpoints
│
│   ├── core/
│   │   ├── config.py            # Environment & settings
│   │   └── security.py          # Security utilities
│
│   ├── models/
│   │   ├── sensor.py            # SQLAlchemy DB models
│   │   └── fishmate_rf_latest_v1.pkl  # Trained ML model
│
│   ├── services/
│   │   ├── ingestion.py         # Sensor ingestion logic
│   │   ├── quality_check.py     # Rule-based validation
│   │   └── reading.py           # Read/query operations
│
│   ├── ml/
│   │   ├── model.py             # ML model loader
│   │   └── predict.py           # Prediction logic
│
│   └── db/
│       └── session.py           # DB session management
│
├── ml_training/
│   ├── train_model.py           # Offline model training
│   └── data/                    # CSV datasets
│
├── .env                         # Environment variables
├── run.sh                       # Startup script
├── requirments.txt              # Python dependencies
└── README.md
## ⚡ API Endpoints
###1️⃣ Sensor Data Ingestion

POST /api/v1/sensor-data

{
  "device_id": "FM-001",
  "timestamp": "2026-01-11T10:30:00Z",
  "dissolved_oxygen": 5.2,
  "tds": 480,
  "ph": 7.1,
  "ammonia": 0.04,
  "temperature": 29.5,
  "voltage": 3.7
}


✔ Validated
✔ Stored
✔ Classified
✔ Scored

###2️⃣ Latest Device Reading

GET /api/v1/sensor-data/latest/{device_id}

Returns:

Latest sensor values

ML classification

Confidence score

###3️⃣ Historical Time-Series Data

GET /api/v1/sensor-data/history/{device_id}

Query Params

start_time

end_time

limit

Optimized for charts & analytics.

🔧 Installation & Setup
Prerequisites

Python 3.10+

PostgreSQL 14+


###1️⃣ Clone & Install
git clone https://github.com/yourusername/fishmate-backend.git
cd fishmate-backend
pip install -r requirments.txt

###2️⃣ Environment Configuration

Create .env:

DATABASE_URL=postgresql://user:password@localhost:5432/fishmate_db
SECRET_KEY=super_secret_key

###3️⃣ Run Server
uvicorn app.main:app --reload


###📘 Swagger UI
http://localhost:8000/docs

🔮 Roadmap

 Docker & Docker Compose

 MQTT ingestion (ESP32 native)

 Role-based authentication

 Flutter mobile app

 Automated ML retraining

 Alert notification service (SMS / Push)

### © 2026 FishMate Project
Smart Aquaculture powered by IoT & AI
