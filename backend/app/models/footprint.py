# Carbon Footprint model
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Footprint(Base):
    __tablename__ = "footprints"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    # Travel data (monthly)
    car_km_per_month = Column(Float, default=0)
    public_transport_km_per_month = Column(Float, default=0)
    flight_km_per_month = Column(Float, default=0)
    
    # Electricity data (monthly in kWh)
    electricity_kwh_per_month = Column(Float, default=0)
    
    # Food habits (meals per week)
    beef_meals_per_week = Column(Float, default=0)
    chicken_meals_per_week = Column(Float, default=0)
    vegetarian_meals_per_week = Column(Float, default=0)
    vegan_meals_per_week = Column(Float, default=0)
    
    # Calculated totals (kg CO₂)
    travel_footprint_monthly = Column(Float, default=0)
    electricity_footprint_monthly = Column(Float, default=0)
    food_footprint_monthly = Column(Float, default=0)
    lifestyle_footprint_monthly = Column(Float, default=0)
    total_footprint_monthly = Column(Float, default=0)
    total_footprint_yearly = Column(Float, default=0)
    
    # Breakdown data stored as JSON
    breakdown = Column(JSON, default={})
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship
    user = relationship("User", back_populates="footprints")

    class Config:
        from_attributes = True
