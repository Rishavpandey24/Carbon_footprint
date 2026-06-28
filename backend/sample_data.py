# Sample Data Initialization Script for EcoVision
# This file documents sample data that can be inserted

import sqlite3
import json
from datetime import datetime

# Connect to database
conn = sqlite3.connect('ecovision.db')
cursor = conn.cursor()

# Sample users data (optional - can be added manually)
SAMPLE_USERS = [
    {
        'username': 'eco_warrior',
        'email': 'warrior@ecovision.com',
        'full_name': 'Alex Green',
        'green_score': 500,
        'total_carbon_saved': 150.5,
        'challenges_completed': 5,
        'badge_level': 'Carbon Saver'
    },
    {
        'username': 'nature_lover',
        'email': 'lover@ecovision.com',
        'full_name': 'Sam Nature',
        'green_score': 300,
        'total_carbon_saved': 75.2,
        'challenges_completed': 3,
        'badge_level': 'Eco Beginner'
    },
]

# Sample footprint data
SAMPLE_FOOTPRINTS = {
    'user_1': {
        'car_km_per_month': 500,
        'public_transport_km_per_month': 100,
        'flight_km_per_month': 0,
        'electricity_kwh_per_month': 150,
        'beef_meals_per_week': 2,
        'chicken_meals_per_week': 2,
        'vegetarian_meals_per_week': 2,
        'vegan_meals_per_week': 0,
    }
}

def insert_sample_data():
    """
    Insert sample data into the database.
    NOTE: Run this only after creating tables via main.py
    """
    try:
        # Insert users
        for user in SAMPLE_USERS:
            cursor.execute("""
                INSERT OR IGNORE INTO users 
                (username, email, full_name, green_score, total_carbon_saved, 
                 challenges_completed, badge_level)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                user['username'],
                user['email'],
                user['full_name'],
                user['green_score'],
                user['total_carbon_saved'],
                user['challenges_completed'],
                user['badge_level']
            ))
        
        conn.commit()
        print("✓ Sample data inserted successfully!")
        
    except Exception as e:
        print(f"✗ Error inserting sample data: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    print("Sample Data Initialization")
    print("=" * 50)
    print("This script adds sample users to the database.")
    print("NOTE: Run this after starting the backend at least once.")
    print("=" * 50)
    print()
    
    # Uncomment the line below to insert sample data
    # insert_sample_data()
    
    print("To use sample data:")
    print("1. Start the backend: python main.py")
    print("2. Uncomment insert_sample_data() in this file")
    print("3. Run: python sample_data.py")
