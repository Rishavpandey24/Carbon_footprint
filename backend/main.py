from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine, Base
from app.routes import (
    footprint_routes,
    challenge_routes,
    leaderboard_routes
)

from config import API_HOST, API_PORT

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="EcoVision API",
    description="AI-powered Carbon Footprint Tracker",
    version="1.0.0"
)

# -------------------- CORS --------------------
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"https://.*\.vercel\.app",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ----------------------------------------------

# Routes
app.include_router(
    footprint_routes.router,
    prefix="/api/footprint",
    tags=["Footprint"]
)

app.include_router(
    challenge_routes.router,
    prefix="/api/challenges",
    tags=["Challenges"]
)

app.include_router(
    leaderboard_routes.router,
    prefix="/api/leaderboard",
    tags=["Leaderboard"]
)

@app.get("/")
def root():
    return {
        "message": "EcoVision Backend Running",
        "docs": "/docs"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host=API_HOST,
        port=API_PORT,
        reload=False
    )