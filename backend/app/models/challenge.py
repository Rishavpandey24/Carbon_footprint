# Challenge model
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from database import Base

class ChallengeType(str, enum.Enum):
    ELECTRICITY = "save_electricity"
    CAR_USAGE = "reduce_car_usage"
    PLASTIC = "avoid_plastic"
    VEGETARIAN = "vegetarian_meals"
    WATER = "water_conservation"

class Challenge(Base):
    __tablename__ = "challenges"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    description = Column(String(500))
    challenge_type = Column(Enum(ChallengeType))
    target = Column(Float)  # Target value (e.g., save 10 kWh)
    reward_points = Column(Integer, default=100)
    difficulty = Column(String(20), default="medium")  # easy, medium, hard
    duration_days = Column(Integer, default=7)
    carbon_saved_potential = Column(Float)  # kg CO₂ saved if completed
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    user_challenges = relationship("UserChallenge", back_populates="challenge")

    class Config:
        from_attributes = True

class UserChallenge(Base):
    __tablename__ = "user_challenges"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    challenge_id = Column(Integer, ForeignKey("challenges.id"))
    status = Column(String(20), default="active")  # active, completed, failed
    progress = Column(Float, default=0)  # Progress towards target (0-100%)
    started_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)
    
    # Relationships
    user = relationship("User", back_populates="challenges")
    challenge = relationship("Challenge", back_populates="user_challenges")

    class Config:
        from_attributes = True
