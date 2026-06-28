# EcoVision Backend - Main FastAPI Application
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base, get_db
from app.models import User, Footprint, Challenge, UserChallenge
from app.routes import footprint_routes, challenge_routes, leaderboard_routes
from config import ALLOWED_ORIGINS

# Create all database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="EcoVision API",
    description="AI-powered carbon footprint tracker and sustainability platform",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(footprint_routes.router, prefix="/api/footprint", tags=["Footprint"])
app.include_router(challenge_routes.router, prefix="/api/challenges", tags=["Challenges"])
app.include_router(leaderboard_routes.router, prefix="/api/leaderboard", tags=["Leaderboard"])

@app.get("/")
def read_root():
    """Welcome endpoint"""
    return {
        "message": "Welcome to EcoVision API",
        "version": "1.0.0",
        "documentation": "/docs"
    }

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "EcoVision Backend"}

if __name__ == "__main__": 
    import uvicorn
    from config import API_HOST, API_PORT
    
    uvicorn.run(app, host=API_HOST, port=API_PORT)
