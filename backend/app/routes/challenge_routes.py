# Challenge routes
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from app.models import Challenge, UserChallenge, ChallengeType, User
from pydantic import BaseModel
from datetime import datetime
from typing import List

router = APIRouter()

# Mock user ID
MOCK_USER_ID = 1

class ChallengeData(BaseModel):
    title: str
    description: str
    challenge_type: str
    target: float
    reward_points: int = 100
    difficulty: str = "medium"
    carbon_saved_potential: float = 0

class ChallengeResponse(BaseModel):
    id: int
    title: str
    description: str
    reward_points: int
    difficulty: str
    carbon_saved_potential: float
    
    class Config:
        from_attributes = True

@router.get("/available")
def get_available_challenges(db: Session = Depends(get_db)):
    """
    Get list of available challenges
    """
    challenges = db.query(Challenge).all()
    
    if not challenges:
        # Create default challenges if none exist
        default_challenges = [
            Challenge(
                title="Save 50 kWh Electricity",
                description="Reduce your electricity usage by 50 kWh this week",
                challenge_type=ChallengeType.ELECTRICITY,
                target=50,
                reward_points=100,
                difficulty="medium",
                carbon_saved_potential=46
            ),
            Challenge(
                title="Car-Free Week",
                description="Use public transport or cycling instead of driving",
                challenge_type=ChallengeType.CAR_USAGE,
                target=7,
                reward_points=150,
                difficulty="hard",
                carbon_saved_potential=147
            ),
            Challenge(
                title="Plastic-Free Shopping",
                description="Shop without using plastic bags (use cloth bags)",
                challenge_type=ChallengeType.PLASTIC,
                target=5,
                reward_points=80,
                difficulty="easy",
                carbon_saved_potential=5
            ),
            Challenge(
                title="Vegetarian Week",
                description="Eat vegetarian meals only for 7 days",
                challenge_type=ChallengeType.VEGETARIAN,
                target=7,
                reward_points=120,
                difficulty="medium",
                carbon_saved_potential=75
            ),
            Challenge(
                title="Water Conservation",
                description="Reduce water usage by 20% this week",
                challenge_type=ChallengeType.WATER,
                target=20,
                reward_points=90,
                difficulty="easy",
                carbon_saved_potential=15
            ),
        ]
        
        for challenge in default_challenges:
            db.add(challenge)
        db.commit()
        challenges = default_challenges
    
    return {
        "status": "success",
        "challenges": [
            {
                "id": c.id,
                "title": c.title,
                "description": c.description,
                "type": c.challenge_type,
                "target": c.target,
                "reward_points": c.reward_points,
                "difficulty": c.difficulty,
                "carbon_saved_potential": c.carbon_saved_potential
            }
            for c in challenges
        ]
    }

@router.get("/active")
def get_active_challenges(db: Session = Depends(get_db)):
    """
    Get user's active challenges
    """
    # Get or create user
    user = db.query(User).filter(User.id == MOCK_USER_ID).first()
    if not user:
        user = User(id=MOCK_USER_ID, username="demo_user", email="demo@ecovision.com")
        db.add(user)
        db.commit()
    
    # Get active challenges for user
    user_challenges = db.query(UserChallenge).filter(
        UserChallenge.user_id == MOCK_USER_ID,
        UserChallenge.status == "active"
    ).all()
    
    return {
        "status": "success",
        "challenges": [
            {
                "id": uc.id,
                "challenge_id": uc.challenge_id,
                "title": uc.challenge.title,
                "description": uc.challenge.description,
                "progress": uc.progress,
                "status": uc.status,
                "reward_points": uc.challenge.reward_points,
                "started_at": uc.started_at.isoformat()
            }
            for uc in user_challenges
        ]
    }

@router.post("/join/{challenge_id}")
def join_challenge(challenge_id: int, db: Session = Depends(get_db)):
    """
    Join a challenge
    """
    # Get or create user
    user = db.query(User).filter(User.id == MOCK_USER_ID).first()
    if not user:
        user = User(id=MOCK_USER_ID, username="demo_user", email="demo@ecovision.com")
        db.add(user)
        db.commit()
    
    # Check if already joined
    existing = db.query(UserChallenge).filter(
        UserChallenge.user_id == MOCK_USER_ID,
        UserChallenge.challenge_id == challenge_id,
        UserChallenge.status == "active"
    ).first()
    
    if existing:
        return {"status": "already_joined", "message": "You are already participating in this challenge"}
    
    # Create new user challenge
    user_challenge = UserChallenge(
        user_id=MOCK_USER_ID,
        challenge_id=challenge_id,
        status="active",
        progress=0
    )
    
    db.add(user_challenge)
    db.commit()
    db.refresh(user_challenge)
    
    return {
        "status": "success",
        "message": "Successfully joined challenge",
        "data": {
            "id": user_challenge.id,
            "challenge_id": user_challenge.challenge_id,
            "status": user_challenge.status
        }
    }

@router.post("/update-progress/{user_challenge_id}")
def update_progress(user_challenge_id: int, progress: float = 0, db: Session = Depends(get_db)):
    """
    Update challenge progress
    """
    user_challenge = db.query(UserChallenge).filter(
        UserChallenge.id == user_challenge_id,
        UserChallenge.user_id == MOCK_USER_ID
    ).first()
    
    if not user_challenge:
        raise HTTPException(status_code=404, detail="Challenge not found")
    
    # Update progress
    user_challenge.progress = min(progress, 100)
    
    # Check if completed
    if user_challenge.progress >= 100:
        user_challenge.status = "completed"
        user_challenge.completed_at = datetime.utcnow()
        
        # Update user stats
        user = db.query(User).filter(User.id == MOCK_USER_ID).first()
        if user:
            user.challenges_completed += 1
            user.green_score += user_challenge.challenge.reward_points
            user.total_carbon_saved += user_challenge.challenge.carbon_saved_potential
            
            # Update badge level
            if user.challenges_completed >= 20:
                user.badge_level = "Climate Champion"
            elif user.challenges_completed >= 10:
                user.badge_level = "Carbon Saver"
            else:
                user.badge_level = "Eco Beginner"
    
    db.add(user_challenge)
    db.commit()
    db.refresh(user_challenge)
    
    return {
        "status": "success",
        "progress": user_challenge.progress,
        "status": user_challenge.status,
        "message": "Progress updated successfully"
    }
