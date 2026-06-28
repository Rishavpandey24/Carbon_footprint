# Future emission prediction service
class EmissionPrediction:
    """Service for predicting future carbon emissions"""

    @staticmethod
    def predict_emissions(current_monthly_footprint, months=12, trend="stable"):
        """
        Predict future emissions based on current habits
        
        Args:
            current_monthly_footprint: Current monthly emissions in kg CO₂
            months: Number of months to predict (6 or 12)
            trend: "stable", "increasing", "decreasing"
        
        Returns:
            List of predictions with months and estimated emissions
        """
        predictions = []
        
        # Trend multipliers (slight changes based on user behavior)
        trend_factors = {
            "stable": [1.0] * months,
            "increasing": [1.0 + (i * 0.02) for i in range(months)],  # 2% increase per month
            "decreasing": [1.0 - (i * 0.02) for i in range(months)]   # 2% decrease per month
        }
        
        factors = trend_factors.get(trend, trend_factors["stable"])
        
        month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        
        for i in range(months):
            month_idx = i % 12
            predicted_emissions = round(current_monthly_footprint * factors[i], 2)
            
            predictions.append({
                "month": month_names[month_idx],
                "month_number": i + 1,
                "predicted_emissions_kg_co2": predicted_emissions,
                "yearly_projection": round(predicted_emissions * 12, 2) if i == 11 else None
            })
        
        return predictions

    @staticmethod
    def predict_with_interventions(current_footprint, interventions):
        """
        Predict emissions after implementing suggestions
        
        Args:
            current_footprint: Current monthly emissions
            interventions: List of interventions with estimated savings
        
        Returns:
            Prediction with interventions
        """
        total_savings = 0
        
        for intervention in interventions:
            if "savings" in intervention:
                total_savings += intervention["savings"]
        
        new_footprint = max(0, current_footprint - total_savings)
        
        return {
            "current_monthly": current_footprint,
            "after_interventions_monthly": round(new_footprint, 2),
            "monthly_savings": round(total_savings, 2),
            "yearly_savings": round(total_savings * 12, 2),
            "percentage_reduction": round((total_savings / current_footprint * 100), 1) if current_footprint > 0 else 0
        }

    @staticmethod
    def get_emission_goals(current_footprint):
        """
        Get recommended emission reduction goals
        """
        global_average_monthly = 333  # kg CO₂ per person globally
        sustainable_monthly = 100  # Target for climate goals
        
        return {
            "current": round(current_footprint, 2),
            "global_average": global_average_monthly,
            "sustainable_target": sustainable_monthly,
            "immediate_goal_6months": round(current_footprint * 0.85, 2),
            "long_term_goal_12months": round(current_footprint * 0.7, 2),
            "suggestions": "Focus on reducing your top emission sources for maximum impact."
        }
