import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Card, ProgressBar } from '../components/shared';
import { EmissionBreakdownChart, EmissionTrendChart } from '../components/Charts';

const API_BASE_URL = 'https://ecovision-backend-vhmp.onrender.com/api';

function Dashboard() {
  const [footprint, setFootprint] = useState(null);
  const [predictions, setPredictions] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchDashboardData();
  }, []);

  const fetchDashboardData = async () => {
    setLoading(true);
    try {
      const [footprintRes, predictionRes] = await Promise.all([
        axios.get(`${API_BASE_URL}/footprint/current`),
        axios.get(`${API_BASE_URL}/footprint/prediction`)
      ]);

      if (footprintRes.data.status === 'success') {
        setFootprint(footprintRes.data.data);
      }
      if (predictionRes.data.status === 'success') {
        setPredictions(predictionRes.data);
      }
    } catch (err) {
      setError('Failed to load dashboard data');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div className="loading">Loading your eco dashboard...</div>;
  }

  if (!footprint) {
    return (
      <div className="dashboard empty-state">
        <Card title="Welcome to EcoVision">
          <div className="empty-message">
            <p>👋 Welcome to your sustainability dashboard!</p>
            <p>Start by calculating your carbon footprint to see your environmental impact and get personalized recommendations.</p>
            <a href="/calculator" className="btn btn-primary">Calculate My Footprint</a>
          </div>
        </Card>
      </div>
    );
  }

  return (
    <div className="dashboard">
      {/* Summary Cards */}
      <div className="summary-grid">
        <Card title="Your Monthly Footprint" className="summary-card">
          <div className="metric-large">
            <span className="value">{footprint.total_monthly?.toFixed(1) || 0}</span>
            <span className="unit">kg CO₂</span>
          </div>
          <p className="metric-description">Based on your current lifestyle</p>
        </Card>

        <Card title="Annual Footprint" className="summary-card">
          <div className="metric-large">
            <span className="value">{footprint.total_yearly?.toFixed(1) || 0}</span>
            <span className="unit">kg CO₂/year</span>
          </div>
          <p className="metric-description">Extrapolated from monthly data</p>
        </Card>

        <Card title="Emission Breakdown" className="summary-card">
          {footprint.breakdown ? (
            <div className="breakdown-simple">
              {Object.entries(footprint.breakdown).map(([key, value]) => (
                <div key={key} className="breakdown-item">
                  <span className="category">{key}</span>
                  <span className="percentage">{value}%</span>
                </div>
              ))}
            </div>
          ) : (
            <p>No breakdown data available</p>
          )}
        </Card>
      </div>

      {/* Detailed Charts */}
      <div className="charts-grid">
        <Card title="Emission Sources">
          {footprint.breakdown ? (
            <EmissionBreakdownChart data={footprint.breakdown} />
          ) : (
            <p>No data to display</p>
          )}
        </Card>

        <Card title="Future Emission Prediction (12 Months)">
          {predictions?.predictions ? (
            <EmissionTrendChart data={predictions.predictions} />
          ) : (
            <p>No prediction data available</p>
          )}
        </Card>
      </div>

      {/* Activity Details */}
      <div className="activity-grid">
        <Card title="Your Activity">
          {footprint.travel && (
            <>
              <h4>🚗 Travel (Monthly)</h4>
              <ProgressBar 
                label="Car usage" 
                value={footprint.travel.car_km} 
                max={1000}
              />
              <ProgressBar 
                label="Public transport" 
                value={footprint.travel.public_transport_km}
                max={500}
                color="#3b82f6"
              />
              <ProgressBar 
                label="Flights" 
                value={footprint.travel.flight_km}
                max={500}
                color="#8b5cf6"
              />
            </>
          )}
        </Card>

        <Card title="Quick Stats">
          {footprint.travel && (
            <div className="stats-list">
              <div className="stat">
                <span className="label">💨 Travel emissions:</span>
                <span className="value">{footprint.travel.monthly_kg_co2?.toFixed(1)} kg CO₂</span>
              </div>
              <div className="stat">
                <span className="label">⚡ Electricity emissions:</span>
                <span className="value">{footprint.electricity?.monthly_kg_co2?.toFixed(1)} kg CO₂</span>
              </div>
              <div className="stat">
                <span className="label">🍽️ Food emissions:</span>
                <span className="value">{footprint.food?.monthly_kg_co2?.toFixed(1)} kg CO₂</span>
              </div>
            </div>
          )}
        </Card>
      </div>

      {/* Emission Goals */}
      {predictions?.goals && (
        <Card title="Your Emission Goals">
          <div className="goals-container">
            <div className="goal">
              <span className="goal-label">Current Monthly Average:</span>
              <span className="goal-value">{predictions.goals.current?.toFixed(1)} kg CO₂</span>
            </div>
            <div className="goal target">
              <span className="goal-label">Global Average:</span>
              <span className="goal-value">{predictions.goals.global_average} kg CO₂</span>
            </div>
            <div className="goal target">
              <span className="goal-label">Sustainable Target:</span>
              <span className="goal-value">{predictions.goals.sustainable_target} kg CO₂</span>
            </div>
            <div className="goal upcoming">
              <span className="goal-label">6-Month Goal (85% reduction):</span>
              <span className="goal-value">{predictions.goals.immediate_goal_6months?.toFixed(1)} kg CO₂</span>
            </div>
          </div>
        </Card>
      )}
    </div>
  );
}

export default Dashboard;
