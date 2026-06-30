import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./ecovision.db"
)

API_HOST = "0.0.0.0"
API_PORT = int(os.getenv("PORT", 10000))

EMISSION_FACTORS = {
    "car": 0.21,
    "public_transport": 0.05,
    "flight": 0.255,
    "electricity": 0.92,
    "natural_gas": 2.04,
    "water": 0.34,
    "beef": 27,
    "chicken": 6.9,
    "vegetarian": 2,
    "vegan": 0.5,
}