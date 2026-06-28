# Footprint routes
from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from database import get_db
from app.models import User, Footprint
from app.services import CarbonCalculator, AISuggestions, EmissionPrediction
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

# Pydantic schemas
class FootprintInput(BaseModel):
    car_km_per_month: float = 0
    public_transport_km_per_month: float = 0
    flight_km_per_month: float = 0
    electricity_kwh_per_month: float = 0
    beef_meals_per_week: float = 0
    chicken_meals_per_week: float = 0
    vegetarian_meals_per_week: float = 0
    vegan_meals_per_week: float = 0

class FootprintResponse(BaseModel):
    id: int
    total_footprint_monthly: float
    total_footprint_yearly: float
    breakdown: dict
    created_at: str
    
    class Config:
        from_attributes = True

# Mock user ID (in production, use authentication)
MOCK_USER_ID = 1

@router.post("/calculate")
def calculate_footprint(data: FootprintInput, db: Session = Depends(get_db)):
    """
    Calculate carbon footprint based on user input
    """
    try:
        # Calculate emissions for each category
        travel = CarbonCalculator.calculate_travel_footprint(
            data.car_km_per_month,
            data.public_transport_km_per_month,
            data.flight_km_per_month
        )
        
        electricity = CarbonCalculator.calculate_electricity_footprint(
            data.electricity_kwh_per_month
        )
        
        food = CarbonCalculator.calculate_food_footprint(
            data.beef_meals_per_week,
            data.chicken_meals_per_week,
            data.vegetarian_meals_per_week,
            data.vegan_meals_per_week
        )
        
        totals = CarbonCalculator.calculate_total_footprint(travel, electricity, food)
        breakdown = CarbonCalculator.get_breakdown(travel, electricity, food, 0, totals["monthly"])
        
        # Get or create user (mock for now)
        user = db.query(User).filter(User.id == MOCK_USER_ID).first()
        if not user:
            user = User(id=MOCK_USER_ID, username="demo_user", email="demo@ecovision.com")
            db.add(user)
            db.commit()
        
        # Create or update footprint record
        footprint = db.query(Footprint).filter(Footprint.user_id == MOCK_USER_ID).first()
        if not footprint:
            footprint = Footprint(user_id=MOCK_USER_ID)
        
        # Update footprint data
        footprint.car_km_per_month = data.car_km_per_month
        footprint.public_transport_km_per_month = data.public_transport_km_per_month
        footprint.flight_km_per_month = data.flight_km_per_month
        footprint.electricity_kwh_per_month = data.electricity_kwh_per_month
        footprint.beef_meals_per_week = data.beef_meals_per_week
        footprint.chicken_meals_per_week = data.chicken_meals_per_week
        footprint.vegetarian_meals_per_week = data.vegetarian_meals_per_week
        footprint.vegan_meals_per_week = data.vegan_meals_per_week
        
        footprint.travel_footprint_monthly = travel
        footprint.electricity_footprint_monthly = electricity
        footprint.food_footprint_monthly = food
        footprint.total_footprint_monthly = totals["monthly"]
        footprint.total_footprint_yearly = totals["yearly"]
        footprint.breakdown = breakdown
        
        db.add(footprint)
        db.commit()
        db.refresh(footprint)
        
        return {
            "status": "success",
            "data": {
                "travel_kg_co2_monthly": travel,
                "electricity_kg_co2_monthly": electricity,
                "food_kg_co2_monthly": food,
                "total_kg_co2_monthly": totals["monthly"],
                "total_kg_co2_yearly": totals["yearly"],
                "breakdown": breakdown
            }
        }
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/current")
def get_current_footprint(db: Session = Depends(get_db)):
    """
    Get current user's footprint data
    """
    footprint = db.query(Footprint).filter(Footprint.user_id == MOCK_USER_ID).first()
    
    if not footprint:
        return {
            "status": "no_data",
            "message": "No footprint data found. Please calculate your footprint first."
        }
    
    return {
        "status": "success",
        "data": {
            "total_monthly": footprint.total_footprint_monthly,
            "total_yearly": footprint.total_footprint_yearly,
            "travel": {
                "car_km": footprint.car_km_per_month,
                "public_transport_km": footprint.public_transport_km_per_month,
                "flight_km": footprint.flight_km_per_month,
                "monthly_kg_co2": footprint.travel_footprint_monthly
            },
            "electricity": {
                "kwh_per_month": footprint.electricity_kwh_per_month,
                "monthly_kg_co2": footprint.electricity_footprint_monthly
            },
            "food": {
                "beef_meals_per_week": footprint.beef_meals_per_week,
                "chicken_meals_per_week": footprint.chicken_meals_per_week,
                "vegetarian_meals_per_week": footprint.vegetarian_meals_per_week,
                "vegan_meals_per_week": footprint.vegan_meals_per_week,
                "monthly_kg_co2": footprint.food_footprint_monthly
            },
            "breakdown": footprint.breakdown
        }
    }

@router.get("/suggestions")
def get_suggestions(db: Session = Depends(get_db)):
    """
    Get AI-powered suggestions to reduce carbon footprint
    """
    footprint = db.query(Footprint).filter(Footprint.user_id == MOCK_USER_ID).first()
    
    if not footprint:
        return {
            "status": "no_data",
            "message": "Please calculate your footprint first to get suggestions."
        }
    
    footprint_data = {
        "car_km_per_month": footprint.car_km_per_month,
        "public_transport_km_per_month": footprint.public_transport_km_per_month,
        "flight_km_per_month": footprint.flight_km_per_month,
        "electricity_kwh_per_month": footprint.electricity_kwh_per_month,
        "beef_meals_per_week": footprint.beef_meals_per_week,
        "chicken_meals_per_week": footprint.chicken_meals_per_week,
        "vegetarian_meals_per_week": footprint.vegetarian_meals_per_week,
        "vegan_meals_per_week": footprint.vegan_meals_per_week,
    }
    
    suggestions = AISuggestions.generate_suggestions(footprint_data)
    potential_savings = AISuggestions.calculate_potential_savings(suggestions)
    
    return {
        "status": "success",
        "suggestions": suggestions,
        "potential_savings": potential_savings
    }

@router.get("/prediction")
def get_emission_prediction(db: Session = Depends(get_db)):
    """
    Get future emission predictions and goals
    """
    footprint = db.query(Footprint).filter(Footprint.user_id == MOCK_USER_ID).first()
    
    if not footprint:
        return {
            "status": "no_data",
            "message": "Please calculate your footprint first to get predictions."
        }
    
    # Generate predictions for 12 months
    predictions = EmissionPrediction.predict_emissions(
        footprint.total_footprint_monthly,
        months=12,
        trend="stable"
    )
    
    # Get goals
    goals = EmissionPrediction.get_emission_goals(footprint.total_footprint_monthly)
    
    return {
        "status": "success",
        "predictions": predictions,
        "goals": goals
    }
