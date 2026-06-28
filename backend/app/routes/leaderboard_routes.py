# Leaderboard routes
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import desc
from database import get_db
from app.models import User

router = APIRouter()

@router.get("/top-users")
def get_top_users(limit: int = 10, db: Session = Depends(get_db)):
    """
    Get top users by green score and carbon saved
    """
    # Get top users by green score
    top_users_by_score = db.query(User).order_by(
        desc(User.green_score)
    ).limit(limit).all()
    
    # Get top users by carbon saved
    top_users_by_savings = db.query(User).order_by(
        desc(User.total_carbon_saved)
    ).limit(limit).all()
    
    return {
        "status": "success",
        "leaderboard": {
            "by_green_score": [
                {
                    "rank": idx + 1,
                    "username": user.username,
                    "full_name": user.full_name or "Anonymous",
                    "green_score": user.green_score,
                    "challenges_completed": user.challenges_completed,
                    "badge_level": user.badge_level
                }
                for idx, user in enumerate(top_users_by_score)
            ],
            "by_carbon_saved": [
                {
                    "rank": idx + 1,
                    "username": user.username,
                    "full_name": user.full_name or "Anonymous",
                    "total_carbon_saved_kg_co2": user.total_carbon_saved,
                    "challenges_completed": user.challenges_completed,
                    "badge_level": user.badge_level
                }
                for idx, user in enumerate(top_users_by_savings)
            ]
        }
    }

@router.get("/badges")
def get_badge_distribution(db: Session = Depends(get_db)):
    """
    Get badge distribution across all users
    """
    badges = {
        "Eco Beginner": db.query(User).filter(User.badge_level == "Eco Beginner").count(),
        "Carbon Saver": db.query(User).filter(User.badge_level == "Carbon Saver").count(),
        "Climate Champion": db.query(User).filter(User.badge_level == "Climate Champion").count()
    }
    
    return {
        "status": "success",
        "badges": badges
    }

@router.get("/stats")
def get_global_stats(db: Session = Depends(get_db)):
    """
    Get global platform statistics
    """
    users = db.query(User).all()
    
    total_users = len(users)
    total_carbon_saved = sum(u.total_carbon_saved for u in users)
    total_challenges_completed = sum(u.challenges_completed for u in users)
    average_carbon_saved = total_carbon_saved / total_users if total_users > 0 else 0
    average_challenges = total_challenges_completed / total_users if total_users > 0 else 0
    
    return {
        "status": "success",
        "stats": {
            "total_users": total_users,
            "total_carbon_saved_kg_co2": round(total_carbon_saved, 2),
            "total_challenges_completed": total_challenges_completed,
            "average_carbon_saved_per_user": round(average_carbon_saved, 2),
            "average_challenges_per_user": round(average_challenges, 2)
        }
    }
