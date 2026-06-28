# User model
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    password_hash = Column(String(255))
    full_name = Column(String(100))
    green_score = Column(Float, default=0)
    total_carbon_saved = Column(Float, default=0)
    challenges_completed = Column(Integer, default=0)
    badge_level = Column(String(50), default="Eco Beginner")  # Eco Beginner, Carbon Saver, Climate Champion
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    footprints = relationship("Footprint", back_populates="user")
    challenges = relationship("UserChallenge", back_populates="user")

    class Config:
        from_attributes = True
