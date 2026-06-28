# Carbon calculation service
from config import EMISSION_FACTORS

class CarbonCalculator:
    """Service for calculating carbon footprint"""

    @staticmethod
    def calculate_travel_footprint(car_km, public_transport_km, flight_km):
        """
        Calculate travel emissions in kg CO₂
        """
        travel_footprint = (
            car_km * EMISSION_FACTORS["car"] +
            public_transport_km * EMISSION_FACTORS["public_transport"] +
            flight_km * EMISSION_FACTORS["flight"]
        )
        return round(travel_footprint, 2)

    @staticmethod
    def calculate_electricity_footprint(kwh_per_month):
        """
        Calculate electricity emissions in kg CO₂
        """
        electricity_footprint = kwh_per_month * EMISSION_FACTORS["electricity"]
        return round(electricity_footprint, 2)

    @staticmethod
    def calculate_food_footprint(beef_meals, chicken_meals, vegetarian_meals, vegan_meals, per_week=True):
        """
        Calculate food emissions in kg CO₂
        If per_week=True, assumes weekly meals. Multiply by 4.33 for monthly.
        """
        meals_multiplier = 4.33 if per_week else 1
        
        food_footprint = (
            beef_meals * EMISSION_FACTORS["beef"] * meals_multiplier +
            chicken_meals * EMISSION_FACTORS["chicken"] * meals_multiplier +
            vegetarian_meals * EMISSION_FACTORS["vegetarian"] * meals_multiplier +
            vegan_meals * EMISSION_FACTORS["vegan"] * meals_multiplier
        )
        return round(food_footprint, 2)

    @staticmethod
    def calculate_lifestyle_footprint(water_usage_m3=None, shopping_impact=None):
        """
        Calculate lifestyle emissions (water, shopping, etc.)
        water_usage_m3: cubic meters per month
        shopping_impact: estimated kg CO₂ from shopping
        """
        lifestyle_footprint = 0
        if water_usage_m3:
            lifestyle_footprint += water_usage_m3 * EMISSION_FACTORS["water"]
        if shopping_impact:
            lifestyle_footprint += shopping_impact
        
        return round(lifestyle_footprint, 2)

    @staticmethod
    def calculate_total_footprint(travel, electricity, food, lifestyle=0):
        """
        Calculate total monthly and yearly footprint
        """
        monthly = travel + electricity + food + lifestyle
        yearly = monthly * 12
        
        return {
            "monthly": round(monthly, 2),
            "yearly": round(yearly, 2)
        }

    @staticmethod
    def get_breakdown(travel, electricity, food, lifestyle, total):
        """
        Get percentage breakdown of emissions by category
        """
        if total == 0:
            return {
                "travel": 0,
                "electricity": 0,
                "food": 0,
                "lifestyle": 0
            }
        
        return {
            "travel": round((travel / total) * 100, 1),
            "electricity": round((electricity / total) * 100, 1),
            "food": round((food / total) * 100, 1),
            "lifestyle": round((lifestyle / total) * 100, 1)
        }
