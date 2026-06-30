# Configuration for EcoVision Backend

import os
from dotenv import load_dotenv

load_dotenv()

# -----------------------------
# Database Configuration
# -----------------------------
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./ecovision.db")

# -----------------------------
# API Configuration
# Render provides PORT automatically
# -----------------------------
API_HOST = "0.0.0.0"
API_PORT = int(os.getenv("PORT", 10000))

# -----------------------------
# CORS Configuration
# -----------------------------
ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://carbon-footprint-plum-five.vercel.app"
]

# -----------------------------
# Carbon Emission Factors
# -----------------------------
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