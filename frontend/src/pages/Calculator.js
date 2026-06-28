import React, { useState } from 'react';
import axios from 'axios';
import { Card } from '../components/shared';

const API_BASE_URL = 'http://localhost:8000/api';

function Calculator() {
  const [formData, setFormData] = useState({
    car_km_per_month: 0,
    public_transport_km_per_month: 0,
    flight_km_per_month: 0,
    electricity_kwh_per_month: 0,
    beef_meals_per_week: 0,
    chicken_meals_per_week: 0,
    vegetarian_meals_per_week: 0,
    vegan_meals_per_week: 0,
  });

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: parseFloat(value) || 0
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    try {
      const response = await axios.post(`${API_BASE_URL}/footprint/calculate`, formData);
      if (response.data.status === 'success') {
        setResult(response.data.data);
      }
    } catch (err) {
      setError('Failed to calculate footprint. Please try again.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="calculator">
      <Card title="Carbon Footprint Calculator">
        <p className="subtitle">Enter your lifestyle data to calculate your monthly carbon footprint</p>
        
        <form onSubmit={handleSubmit} className="calculator-form">
          {/* Travel Section */}
          <fieldset className="form-section">
            <legend>🚗 Travel Habits (Monthly)</legend>
            <div className="form-grid">
              <div className="form-group">
                <label htmlFor="car_km">Car kilometers per month</label>
                <input
                  type="number"
                  id="car_km"
                  name="car_km_per_month"
                  value={formData.car_km_per_month}
                  onChange={handleChange}
                  placeholder="e.g., 500"
                  min="0"
                  step="10"
                />
                <small>km • Emission factor: 0.21 kg CO₂/km</small>
              </div>

              <div className="form-group">
                <label htmlFor="public_transport">Public transport kilometers per month</label>
                <input
                  type="number"
                  id="public_transport"
                  name="public_transport_km_per_month"
                  value={formData.public_transport_km_per_month}
                  onChange={handleChange}
                  placeholder="e.g., 200"
                  min="0"
                  step="10"
                />
                <small>km • Emission factor: 0.05 kg CO₂/km</small>
              </div>

              <div className="form-group">
                <label htmlFor="flight">Flight kilometers per month</label>
                <input
                  type="number"
                  id="flight"
                  name="flight_km_per_month"
                  value={formData.flight_km_per_month}
                  onChange={handleChange}
                  placeholder="e.g., 0"
                  min="0"
                  step="100"
                />
                <small>km • Emission factor: 0.255 kg CO₂/km</small>
              </div>
            </div>
          </fieldset>

          {/* Electricity Section */}
          <fieldset className="form-section">
            <legend>⚡ Energy Usage (Monthly)</legend>
            <div className="form-group">
              <label htmlFor="electricity">Electricity consumption</label>
              <input
                type="number"
                id="electricity"
                name="electricity_kwh_per_month"
                value={formData.electricity_kwh_per_month}
                onChange={handleChange}
                placeholder="e.g., 150"
                min="0"
                step="10"
              />
              <small>kWh • Emission factor: 0.92 kg CO₂/kWh (average)</small>
            </div>
          </fieldset>

          {/* Food Section */}
          <fieldset className="form-section">
            <legend>🍽️ Food Habits (Per Week)</legend>
            <div className="form-grid">
              <div className="form-group">
                <label htmlFor="beef">Beef meals per week</label>
                <input
                  type="number"
                  id="beef"
                  name="beef_meals_per_week"
                  value={formData.beef_meals_per_week}
                  onChange={handleChange}
                  placeholder="e.g., 2"
                  min="0"
                  step="0.5"
                />
                <small>meals • Emission factor: 27 kg CO₂/kg</small>
              </div>

              <div className="form-group">
                <label htmlFor="chicken">Chicken meals per week</label>
                <input
                  type="number"
                  id="chicken"
                  name="chicken_meals_per_week"
                  value={formData.chicken_meals_per_week}
                  onChange={handleChange}
                  placeholder="e.g., 2"
                  min="0"
                  step="0.5"
                />
                <small>meals • Emission factor: 6.9 kg CO₂/kg</small>
              </div>

              <div className="form-group">
                <label htmlFor="vegetarian">Vegetarian meals per week</label>
                <input
                  type="number"
                  id="vegetarian"
                  name="vegetarian_meals_per_week"
                  value={formData.vegetarian_meals_per_week}
                  onChange={handleChange}
                  placeholder="e.g., 2"
                  min="0"
                  step="0.5"
                />
                <small>meals • Emission factor: 2 kg CO₂/meal</small>
              </div>

              <div className="form-group">
                <label htmlFor="vegan">Vegan meals per week</label>
                <input
                  type="number"
                  id="vegan"
                  name="vegan_meals_per_week"
                  value={formData.vegan_meals_per_week}
                  onChange={handleChange}
                  placeholder="e.g., 1"
                  min="0"
                  step="0.5"
                />
                <small>meals • Emission factor: 0.5 kg CO₂/meal</small>
              </div>
            </div>
          </fieldset>

          {error && <div className="error-message">{error}</div>}

          <button type="submit" className="btn btn-primary btn-large" disabled={loading}>
            {loading ? 'Calculating...' : 'Calculate My Footprint'}
          </button>
        </form>
      </Card>

      {/* Results */}
      {result && (
        <div className="results-container">
          <Card title="Your Carbon Footprint Results" className="results-card">
            <div className="results-grid">
              <div className="result-item highlight">
                <span className="label">Monthly Footprint</span>
                <span className="value">{result.total_kg_co2_monthly?.toFixed(1)}</span>
                <span className="unit">kg CO₂</span>
              </div>

              <div className="result-item">
                <span className="label">Annual Footprint</span>
                <span className="value">{result.total_kg_co2_yearly?.toFixed(1)}</span>
                <span className="unit">kg CO₂</span>
              </div>
            </div>

            <div className="breakdown">
              <h3>Emission Sources</h3>
              <div className="breakdown-details">
                <div className="breakdown-item">
                  <span className="source">🚗 Travel</span>
                  <span className="amount">{result.travel_kg_co2_monthly?.toFixed(1)} kg CO₂</span>
                  <span className="percentage">{result.breakdown?.travel || 0}%</span>
                </div>
                <div className="breakdown-item">
                  <span className="source">⚡ Electricity</span>
                  <span className="amount">{result.electricity_kg_co2_monthly?.toFixed(1)} kg CO₂</span>
                  <span className="percentage">{result.breakdown?.electricity || 0}%</span>
                </div>
                <div className="breakdown-item">
                  <span className="source">🍽️ Food</span>
                  <span className="amount">{result.food_kg_co2_monthly?.toFixed(1)} kg CO₂</span>
                  <span className="percentage">{result.breakdown?.food || 0}%</span>
                </div>
              </div>
            </div>

            <p className="info-text">
              💡 Tip: Navigate to "AI Suggestions" to get personalized recommendations on how to reduce your footprint!
            </p>
          </Card>
        </div>
      )}
    </div>
  );
}

export default Calculator;
