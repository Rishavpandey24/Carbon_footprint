import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Card, ProgressBar } from '../components/shared';
import { ChallengeCard } from '../components/Cards';

const API_BASE_URL = 'https://ecovision-backend-vhmp.onrender.com/api';

function Challenges() {
  const [availableChallenges, setAvailableChallenges] = useState([]);
  const [activeChallenges, setActiveChallenges] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [joinedIds, setJoinedIds] = useState(new Set());

  useEffect(() => {
    fetchChallenges();
  }, []);

  const fetchChallenges = async () => {
    setLoading(true);
    try {
      const [availableRes, activeRes] = await Promise.all([
        axios.get(`${API_BASE_URL}/challenges/available`),
        axios.get(`${API_BASE_URL}/challenges/active`)
      ]);

      if (availableRes.data.status === 'success') {
        setAvailableChallenges(availableRes.data.challenges || []);
      }

      if (activeRes.data.status === 'success') {
        setActiveChallenges(activeRes.data.challenges || []);
        const ids = new Set(activeRes.data.challenges.map(c => c.challenge_id));
        setJoinedIds(ids);
      }
    } catch (err) {
      setError('Failed to load challenges');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleJoinChallenge = async (challengeId) => {
    try {
      const response = await axios.post(`${API_BASE_URL}/challenges/join/${challengeId}`);
      if (response.data.status === 'success' || response.data.status === 'already_joined') {
        setJoinedIds(new Set([...joinedIds, challengeId]));
        // Refresh challenges
        fetchChallenges();
      }
    } catch (err) {
      console.error('Failed to join challenge:', err);
    }
  };

  const handleUpdateProgress = async (userChallengeId, newProgress) => {
    try {
      await axios.post(`${API_BASE_URL}/challenges/update-progress/${userChallengeId}`, 
        { progress: newProgress }
      );
      // Refresh active challenges
      const activeRes = await axios.get(`${API_BASE_URL}/challenges/active`);
      if (activeRes.data.status === 'success') {
        setActiveChallenges(activeRes.data.challenges || []);
      }
    } catch (err) {
      console.error('Failed to update progress:', err);
    }
  };

  if (loading) {
    return <div className="loading">Loading challenges...</div>;
  }

  return (
    <div className="challenges">
      {/* Active Challenges */}
      {activeChallenges.length > 0 && (
        <Card title="Your Active Challenges" className="active-challenges-card">
          <div className="active-challenges-list">
            {activeChallenges.map(challenge => (
              <div key={challenge.id} className="active-challenge-item">
                <h4>{challenge.title}</h4>
                <p className="description">{challenge.description}</p>
                <ProgressBar 
                  label="Progress" 
                  value={challenge.progress}
                  max={100}
                  color={challenge.progress >= 100 ? '#10b981' : '#3b82f6'}
                />
                {challenge.status !== 'completed' && (
                  <div className="progress-input">
                    <input 
                      type="range" 
                      min="0" 
                      max="100" 
                      value={challenge.progress}
                      onChange={(e) => handleUpdateProgress(challenge.id, parseFloat(e.target.value))}
                      className="progress-slider"
                    />
                  </div>
                )}
                {challenge.status === 'completed' && (
                  <span className="badge completed">✓ Completed</span>
                )}
              </div>
            ))}
          </div>
        </Card>
      )}

      {/* Available Challenges */}
      <Card title="Available Challenges">
        <p className="subtitle">Join challenges to reduce your carbon footprint and earn rewards</p>
      </Card>

      {availableChallenges.length > 0 ? (
        <div className="challenges-grid">
          {availableChallenges.map(challenge => (
            <ChallengeCard 
              key={challenge.id}
              challenge={challenge}
              onJoin={handleJoinChallenge}
              isJoined={joinedIds.has(challenge.id)}
            />
          ))}
        </div>
      ) : (
        <Card title="No Challenges Available">
          <p>Check back soon for new challenges!</p>
        </Card>
      )}

      {/* Challenge Info */}
      <Card title="How Challenges Work" className="info-card">
        <ul>
          <li>🎯 Choose a challenge that matches your lifestyle</li>
          <li>📊 Track your daily progress using the slider</li>
          <li>🏆 Complete the challenge to earn rewards and green points</li>
          <li>🌍 Watch your carbon savings grow</li>
          <li>🏅 Unlock achievement badges and climb the leaderboard</li>
        </ul>
      </Card>
    </div>
  );
}

export default Challenges;
