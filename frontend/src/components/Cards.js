import React from 'react';

// Suggestion Card Component
export const SuggestionCard = ({ suggestion, index }) => {
  const getDifficultyColor = (difficulty) => {
    switch (difficulty) {
      case 'easy':
        return '#10b981';
      case 'medium':
        return '#f59e0b';
      case 'hard':
        return '#ef4444';
      default:
        return '#6b7280';
    }
  };

  const getImpactBadge = (impact) => {
    const impacts = {
      low: '↑',
      medium: '↑↑',
      high: '↑↑↑',
      very_high: '↑↑↑↑'
    };
    return impacts[impact] || '↑';
  };

  return (
    <div className="suggestion-card">
      <div className="suggestion-header">
        <h3 className="suggestion-title">{suggestion.title}</h3>
        <div className="suggestion-badges">
          <span 
            className="badge difficulty"
            style={{ backgroundColor: getDifficultyColor(suggestion.difficulty) }}
          >
            {suggestion.difficulty}
          </span>
          <span className="badge impact">
            Impact: {getImpactBadge(suggestion.impact)}
          </span>
        </div>
      </div>
      
      <p className="suggestion-description">{suggestion.description}</p>
      
      <div className="suggestion-benefits">
        <div className="benefit">
          <span className="benefit-label">💨 Monthly CO₂ Savings:</span>
          <span className="benefit-value">
            {typeof suggestion.estimated_savings.co2_kg_monthly === 'number'
              ? `${suggestion.estimated_savings.co2_kg_monthly.toFixed(1)} kg`
              : suggestion.estimated_savings.co2_kg_monthly
            }
          </span>
        </div>
        <div className="benefit">
          <span className="benefit-label">💰 Monthly Savings:</span>
          <span className="benefit-value">
            {typeof suggestion.estimated_savings.money_saved_monthly === 'number'
              ? `$${suggestion.estimated_savings.money_saved_monthly.toFixed(2)}`
              : suggestion.estimated_savings.money_saved_monthly
            }
          </span>
        </div>
      </div>
    </div>
  );
};

// Challenge Card Component
export const ChallengeCard = ({ challenge, onJoin, isJoined = false }) => {
  const getDifficultyColor = (difficulty) => {
    switch (difficulty) {
      case 'easy':
        return '#10b981';
      case 'medium':
        return '#f59e0b';
      case 'hard':
        return '#ef4444';
      default:
        return '#6b7280';
    }
  };

  return (
    <div className="challenge-card">
      <div className="challenge-header">
        <h3 className="challenge-title">{challenge.title}</h3>
        <span 
          className="badge difficulty"
          style={{ backgroundColor: getDifficultyColor(challenge.difficulty) }}
        >
          {challenge.difficulty}
        </span>
      </div>
      
      <p className="challenge-description">{challenge.description}</p>
      
      <div className="challenge-details">
        <div className="detail">
          <span className="label">🎯 Target:</span>
          <span className="value">{challenge.target}</span>
        </div>
        <div className="detail">
          <span className="label">🏆 Reward:</span>
          <span className="value">{challenge.reward_points} points</span>
        </div>
        <div className="detail">
          <span className="label">🌍 CO₂ Saved:</span>
          <span className="value">{challenge.carbon_saved_potential.toFixed(1)} kg</span>
        </div>
      </div>
      
      <button 
        className="btn btn-primary challenge-btn"
        onClick={() => onJoin && onJoin(challenge.id)}
        disabled={isJoined}
      >
        {isJoined ? '✓ Joined' : 'Join Challenge'}
      </button>
    </div>
  );
};

// Leaderboard Entry Component
export const LeaderboardEntry = ({ rank, user, scoreType = 'green_score' }) => {
  const getBadgeEmoji = (badge) => {
    switch (badge) {
      case 'Eco Beginner':
        return '🌱';
      case 'Carbon Saver':
        return '🌿';
      case 'Climate Champion':
        return '🌳';
      default:
        return '🌍';
    }
  };

  const getMedalEmoji = (rank) => {
    switch (rank) {
      case 1:
        return '🥇';
      case 2:
        return '🥈';
      case 3:
        return '🥉';
      default:
        return `#${rank}`;
    }
  };

  return (
    <div className="leaderboard-entry">
      <div className="rank">
        {getMedalEmoji(rank)}
      </div>
      <div className="user-info">
        <p className="username">{user.username || user.full_name || 'Anonymous'}</p>
        <span className="badge">{getBadgeEmoji(user.badge_level)} {user.badge_level}</span>
      </div>
      <div className="score">
        {scoreType === 'green_score' ? (
          <>
            <span className="value">{user.green_score || 0}</span>
            <span className="label">points</span>
          </>
        ) : (
          <>
            <span className="value">{(user.total_carbon_saved || 0).toFixed(1)}</span>
            <span className="label">kg CO₂</span>
          </>
        )}
      </div>
    </div>
  );
};
