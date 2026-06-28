# AI suggestion engine (rule-based)
class AISuggestions:
    """Service for generating personalized carbon reduction suggestions"""

    @staticmethod
    def generate_suggestions(footprint_data):
        """
        Generate suggestions based on user's footprint data
        Returns list of suggestions with estimated savings
        """
        suggestions = []
        
        # Travel suggestions
        if footprint_data.get("car_km_per_month", 0) > 500:
            suggestions.append({
                "category": "travel",
                "title": "Switch to Public Transport",
                "description": "You drive frequently. Using public transport 3 days/week could save significant emissions.",
                "estimated_savings": {
                    "co2_kg_monthly": round((footprint_data.get("car_km_per_month", 0) * 0.3) * (0.21 - 0.05), 2),
                    "money_saved_monthly": round((footprint_data.get("car_km_per_month", 0) * 0.3) * 0.15, 2)
                },
                "difficulty": "medium",
                "impact": "high"
            })
        
        if footprint_data.get("car_km_per_month", 0) > 200:
            suggestions.append({
                "category": "travel",
                "title": "Carpool or Bike for Short Trips",
                "description": "For trips under 5km, consider cycling or walking. Carpool with colleagues.",
                "estimated_savings": {
                    "co2_kg_monthly": round((footprint_data.get("car_km_per_month", 0) * 0.2) * 0.21, 2),
                    "money_saved_monthly": round((footprint_data.get("car_km_per_month", 0) * 0.2) * 0.20, 2)
                },
                "difficulty": "easy",
                "impact": "medium"
            })
        
        # Electricity suggestions
        if footprint_data.get("electricity_kwh_per_month", 0) > 200:
            suggestions.append({
                "category": "electricity",
                "title": "Use LED Bulbs",
                "description": "Replace traditional bulbs with LEDs. They use 75% less energy.",
                "estimated_savings": {
                    "co2_kg_monthly": round(30 * 0.92, 2),
                    "money_saved_monthly": 15
                },
                "difficulty": "easy",
                "impact": "medium"
            })
        
        if footprint_data.get("electricity_kwh_per_month", 0) > 150:
            suggestions.append({
                "category": "electricity",
                "title": "Reduce AC Usage",
                "description": "Set AC to 25°C instead of 22°C. Use ceiling fans.",
                "estimated_savings": {
                    "co2_kg_monthly": round(50 * 0.92, 2),
                    "money_saved_monthly": 25
                },
                "difficulty": "easy",
                "impact": "high"
            })
        
        if footprint_data.get("electricity_kwh_per_month", 0) > 100:
            suggestions.append({
                "category": "electricity",
                "title": "Install Solar Panels",
                "description": "Consider solar panels for long-term savings and energy independence.",
                "estimated_savings": {
                    "co2_kg_monthly": round(footprint_data.get("electricity_kwh_per_month", 0) * 0.5 * 0.92, 2),
                    "money_saved_monthly": "Varies"
                },
                "difficulty": "hard",
                "impact": "very_high"
            })
        
        # Food suggestions
        beef_meals = footprint_data.get("beef_meals_per_week", 0)
        if beef_meals > 2:
            suggestions.append({
                "category": "food",
                "title": "Reduce Beef Consumption",
                "description": "Beef has the highest carbon footprint. Replace with chicken or vegetarian.",
                "estimated_savings": {
                    "co2_kg_monthly": round((beef_meals - 1) * 27 * 4.33, 2),
                    "money_saved_monthly": round((beef_meals - 1) * 5 * 4.33, 2)
                },
                "difficulty": "medium",
                "impact": "high"
            })
        
        if (beef_meals + footprint_data.get("chicken_meals_per_week", 0)) > 4:
            suggestions.append({
                "category": "food",
                "title": "Try Meat-Free Mondays",
                "description": "Choose vegetarian or vegan meals one day per week.",
                "estimated_savings": {
                    "co2_kg_monthly": round((27 + 6.9) / 2 * 4.33, 2),
                    "money_saved_monthly": 10
                },
                "difficulty": "easy",
                "impact": "medium"
            })
        
        if footprint_data.get("vegan_meals_per_week", 0) < 1:
            suggestions.append({
                "category": "food",
                "title": "Include More Plant-Based Foods",
                "description": "Plant-based meals have 75% lower carbon footprint.",
                "estimated_savings": {
                    "co2_kg_monthly": round(10 * 0.5 * 4.33, 2),
                    "money_saved_monthly": 15
                },
                "difficulty": "easy",
                "impact": "medium"
            })
        
        # General suggestions
        suggestions.append({
            "category": "lifestyle",
            "title": "Participate in Eco-Challenges",
            "description": "Join challenges to track progress and get motivated.",
            "estimated_savings": {
                "co2_kg_monthly": "Variable",
                "money_saved_monthly": "Variable"
            },
            "difficulty": "easy",
            "impact": "high"
        })
        
        return suggestions

    @staticmethod
    def calculate_potential_savings(suggestions):
        """Calculate total potential savings if all suggestions are followed"""
        total_savings = 0
        total_money = 0
        
        for suggestion in suggestions:
            savings = suggestion.get("estimated_savings", {})
            co2 = savings.get("co2_kg_monthly", 0)
            money = savings.get("money_saved_monthly", 0)
            
            if isinstance(co2, (int, float)):
                total_savings += co2
            if isinstance(money, (int, float)):
                total_money += money
        
        return {
            "total_co2_savings_monthly": round(total_savings, 2),
            "total_money_savings_monthly": round(total_money, 2),
            "total_co2_savings_yearly": round(total_savings * 12, 2)
        }
