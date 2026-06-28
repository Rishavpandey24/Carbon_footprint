import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Card } from '../components/shared';
import { LeaderboardEntry } from '../components/Cards';

const API_BASE_URL = 'http://localhost:8000/api';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState(null);
  const [globalStats, setGlobalStats] = useState(null);
  const [badgeStats, setBadgeStats] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedTab, setSelectedTab] = useState('score');

  useEffect(() => {
    fetchLeaderboardData();
  }, []);

  const fetchLeaderboardData = async () => {
    setLoading(true);
    try {
      const [leaderboardRes, statsRes, badgesRes] = await Promise.all([
        axios.get(`${API_BASE_URL}/leaderboard/top-users?limit=20`),
        axios.get(`${API_BASE_URL}/leaderboard/stats`),
        axios.get(`${API_BASE_URL}/leaderboard/badges`)
      ]);

      if (leaderboardRes.data.status === 'success') {
        setLeaderboard(leaderboardRes.data.leaderboard);
      }
      if (statsRes.data.status === 'success') {
        setGlobalStats(statsRes.data.stats);
      }
      if (badgesRes.data.status === 'success') {
        setBadgeStats(badgesRes.data.badges);
      }
    } catch (err) {
      setError('Failed to load leaderboard data');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div className="loading">Loading leaderboard...</div>;
  }

  return (
    <div className="leaderboard">
      {/* Global Stats */}
      {globalStats && (
        <Card title="Global Impact" className="stats-card">
          <div className="stats-grid">
            <div className="stat-box">
              <span className="stat-value">{globalStats.total_users}</span>
              <span className="stat-label">Active Users</span>
            </div>
            <div className="stat-box">
              <span className="stat-value">{globalStats.total_carbon_saved_kg_co2.toFixed(0)}</span>
              <span className="stat-label">kg CO₂ Saved</span>
            </div>
            <div className="stat-box">
              <span className="stat-value">{globalStats.total_challenges_completed}</span>
              <span className="stat-label">Challenges Completed</span>
            </div>
            <div className="stat-box">
              <span className="stat-value">{globalStats.average_carbon_saved_per_user.toFixed(1)}</span>
              <span className="stat-label">Avg CO₂/User</span>
            </div>
          </div>
        </Card>
      )}

      {/* Badge Distribution */}
      {badgeStats && (
        <Card title="Badge Distribution" className="badges-card">
          <div className="badges-grid">
            <div className="badge-stat">
              <span className="badge-emoji">🌱</span>
              <span className="badge-name">Eco Beginner</span>
              <span className="badge-count">{badgeStats['Eco Beginner']} users</span>
            </div>
            <div className="badge-stat">
              <span className="badge-emoji">🌿</span>
              <span className="badge-name">Carbon Saver</span>
              <span className="badge-count">{badgeStats['Carbon Saver']} users</span>
            </div>
            <div className="badge-stat">
              <span className="badge-emoji">🌳</span>
              <span className="badge-name">Climate Champion</span>
              <span className="badge-count">{badgeStats['Climate Champion']} users</span>
            </div>
          </div>
        </Card>
      )}

      {/* Leaderboard Tabs */}
      {leaderboard && (
        <>
          <Card title="Top Performers" className="leaderboard-card">
            <div className="leaderboard-tabs">
              <button 
                className={`tab-btn ${selectedTab === 'score' ? 'active' : ''}`}
                onClick={() => setSelectedTab('score')}
              >
                By Green Score
              </button>
              <button 
                className={`tab-btn ${selectedTab === 'savings' ? 'active' : ''}`}
                onClick={() => setSelectedTab('savings')}
              >
                By Carbon Saved
              </button>
            </div>

            <div className="leaderboard-list">
              {selectedTab === 'score' ? (
                leaderboard.by_green_score && leaderboard.by_green_score.length > 0 ? (
                  leaderboard.by_green_score.map((user, idx) => (
                    <LeaderboardEntry 
                      key={idx}
                      rank={idx + 1}
                      user={user}
                      scoreType="green_score"
                    />
                  ))
                ) : (
                  <p>No users yet. Be the first!</p>
                )
              ) : (
                leaderboard.by_carbon_saved && leaderboard.by_carbon_saved.length > 0 ? (
                  leaderboard.by_carbon_saved.map((user, idx) => (
                    <LeaderboardEntry 
                      key={idx}
                      rank={idx + 1}
                      user={user}
                      scoreType="carbon_saved"
                    />
                  ))
                ) : (
                  <p>No data yet. Start saving carbon!</p>
                )
              )}
            </div>
          </Card>
        </>
      )}

      {error && (
        <Card title="Error" className="error-card">
          <p>{error}</p>
        </Card>
      )}

      {/* How to Rank */}
      <Card title="How to Climb the Leaderboard" className="info-card">
        <div className="ranking-tips">
          <div className="tip">
            <span className="icon">🏆</span>
            <div>
              <h4>Complete Challenges</h4>
              <p>Join and finish eco-challenges to earn points and carbon savings</p>
            </div>
          </div>
          <div className="tip">
            <span className="icon">📉</span>
            <div>
              <h4>Reduce Your Footprint</h4>
              <p>Follow AI suggestions to cut emissions and move up the rankings</p>
            </div>
          </div>
          <div className="tip">
            <span className="icon">🌍</span>
            <div>
              <h4>Earn Badges</h4>
              <p>Reach milestones to unlock badges and special achievements</p>
            </div>
          </div>
        </div>
      </Card>
    </div>
  );
}

export default Leaderboard;
