import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import Calculator from './pages/Calculator';
import Suggestions from './pages/Suggestions';
import Challenges from './pages/Challenges';
import Leaderboard from './pages/Leaderboard';
import './styles/App.css';

function App() {
  const [currentUser, setCurrentUser] = useState({
    username: 'demo_user',
    greenScore: 0,
    badgeLevel: 'Eco Beginner'
  });

  return (
    <Router>
      <div className="app">
        {/* Navigation Bar */}
        <nav className="navbar">
          <div className="navbar-container">
            <Link to="/" className="navbar-logo">
              <span className="logo-icon">🌱</span>
              EcoVision
            </Link>
            <div className="nav-menu">
              <Link to="/" className="nav-link">Dashboard</Link>
              <Link to="/calculator" className="nav-link">Calculator</Link>
              <Link to="/suggestions" className="nav-link">AI Suggestions</Link>
              <Link to="/challenges" className="nav-link">Challenges</Link>
              <Link to="/leaderboard" className="nav-link">Leaderboard</Link>
            </div>
            <div className="nav-user">
              <span className="badge">{currentUser.badgeLevel}</span>
              <span className="green-score">🟢 {currentUser.greenScore}</span>
            </div>
          </div>
        </nav>

        {/* Main Content */}
        <main className="main-content">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/calculator" element={<Calculator />} />
            <Route path="/suggestions" element={<Suggestions />} />
            <Route path="/challenges" element={<Challenges />} />
            <Route path="/leaderboard" element={<Leaderboard />} />
          </Routes>
        </main>

        {/* Footer */}
        <footer className="footer">
          <div className="footer-content">
            <p>&copy; 2026 EcoVision. Building a sustainable future, one carbon footprint at a time. 🌍</p>
          </div>
        </footer>
      </div>
    </Router>
  );
}

export default App;
