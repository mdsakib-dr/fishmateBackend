import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
DEVICE_API_KEY = os.getenv("DEVICE_API_KEY")
