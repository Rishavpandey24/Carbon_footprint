# Configuration for EcoVision Backend
import os
from dotenv import load_dotenv

load_dotenv()

# Database Configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./ecovision.db")

# API Configuration
API_HOST = os.getenv("API_HOST", "127.0.0.1")
API_PORT = int(os.getenv("API_PORT", 8000))

# CORS Configuration
ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:3001",
    "http://127.0.0.1:3001",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

# Carbon Emission Factors (kg CO₂ per unit)
EMISSION_FACTORS = {
    "car": 0.21,  # kg CO₂ per km
    "public_transport": 0.05,  # kg CO₂ per km
    "flight": 0.255,  # kg CO₂ per km
    "electricity": 0.92,  # kg CO₂ per kWh (average)
    "natural_gas": 2.04,  # kg CO₂ per m³
    "water": 0.34,  # kg CO₂ per cubic meter
    "beef": 27,  # kg CO₂ per kg
    "chicken": 6.9,  # kg CO₂ per kg
    "vegetarian": 2,  # kg CO₂ per meal
    "vegan": 0.5,  # kg CO₂ per meal
}
