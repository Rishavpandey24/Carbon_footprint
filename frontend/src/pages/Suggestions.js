import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Card } from '../components/shared';
import { SuggestionCard } from '../components/Cards';

const API_BASE_URL = 'https://ecovision-backend-vhmp.onrender.com/api';

function Suggestions() {
  const [suggestions, setSuggestions] = useState([]);
  const [potentialSavings, setPotentialSavings] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [filterDifficulty, setFilterDifficulty] = useState('all');

  useEffect(() => {
    fetchSuggestions();
  }, []);

  const fetchSuggestions = async () => {
    setLoading(true);
    try {
      const response = await axios.get(`${API_BASE_URL}/footprint/suggestions`);
      if (response.data.status === 'success') {
        setSuggestions(response.data.suggestions || []);
        setPotentialSavings(response.data.potential_savings);
      }
    } catch (err) {
      setError('Failed to load suggestions. Please calculate your footprint first.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div className="loading">Loading AI suggestions...</div>;
  }

  const filteredSuggestions = filterDifficulty === 'all' 
    ? suggestions 
    : suggestions.filter(s => s.difficulty === filterDifficulty);

  return (
    <div className="suggestions">
      <Card title="AI-Powered Personalized Suggestions">
        <p className="subtitle">Based on your carbon footprint, here are practical actions you can take</p>
      </Card>

      {error && (
        <Card title="No Data Available" className="warning-card">
          <p>{error}</p>
          <a href="/calculator" className="btn btn-primary">Calculate Footprint First</a>
        </Card>
      )}

      {potentialSavings && (
        <Card title="Potential Impact" className="impact-card">
          <div className="impact-grid">
            <div className="impact-item">
              <span className="icon">📉</span>
              <span className="label">Monthly CO₂ Savings</span>
              <span className="value">{potentialSavings.total_co2_savings_monthly?.toFixed(1)}</span>
              <span className="unit">kg</span>
            </div>
            <div className="impact-item">
              <span className="icon">🌍</span>
              <span className="label">Yearly CO₂ Savings</span>
              <span className="value">{potentialSavings.total_co2_savings_yearly?.toFixed(1)}</span>
              <span className="unit">kg</span>
            </div>
            <div className="impact-item">
              <span className="icon">💰</span>
              <span className="label">Monthly Money Saved</span>
              <span className="value">${potentialSavings.total_money_savings_monthly?.toFixed(2)}</span>
              <span className="unit">USD</span>
            </div>
          </div>
        </Card>
      )}

      {/* Filter */}
      <Card title="Filter Suggestions">
        <div className="filter-group">
          <button 
            className={`filter-btn ${filterDifficulty === 'all' ? 'active' : ''}`}
            onClick={() => setFilterDifficulty('all')}
          >
            All
          </button>
          <button 
            className={`filter-btn ${filterDifficulty === 'easy' ? 'active' : ''}`}
            onClick={() => setFilterDifficulty('easy')}
          >
            Easy
          </button>
          <button 
            className={`filter-btn ${filterDifficulty === 'medium' ? 'active' : ''}`}
            onClick={() => setFilterDifficulty('medium')}
          >
            Medium
          </button>
          <button 
            className={`filter-btn ${filterDifficulty === 'hard' ? 'active' : ''}`}
            onClick={() => setFilterDifficulty('hard')}
          >
            Hard
          </button>
        </div>
      </Card>

      {/* Suggestions List */}
      <div className="suggestions-grid">
        {filteredSuggestions.length > 0 ? (
          filteredSuggestions.map((suggestion, index) => (
            <SuggestionCard key={index} suggestion={suggestion} index={index} />
          ))
        ) : (
          <Card title="No Suggestions">
            <p>No suggestions match your filter. Try selecting a different difficulty level.</p>
          </Card>
        )}
      </div>

      {suggestions.length > 0 && (
        <Card title="Next Steps" className="next-steps">
          <ol>
            <li>Review the suggestions above and identify quick wins (easy difficulty)</li>
            <li>Start with 2-3 changes that fit your lifestyle</li>
            <li>Track your progress on the Challenges page</li>
            <li>Check your improved footprint after 1 month</li>
            <li>Share your impact with friends and join the Leaderboard!</li>
          </ol>
        </Card>
      )}
    </div>
  );
}

export default Suggestions;
