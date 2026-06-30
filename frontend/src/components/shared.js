import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { BarChart, Bar, LineChart, Line, PieChart, Pie, Cell, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const API_BASE_URL = "https://ecovision-backend.onrender.com/api";

// Reusable Card Component
const Card = ({ title, children, className = '' }) => (
  <div className={`card ${className}`}>
    <h2 className="card-title">{title}</h2>
    <div className="card-content">
      {children}
    </div>
  </div>
);

// Reusable Progress Bar
const ProgressBar = ({ label, value, max = 100, color = '#10b981' }) => (
  <div className="progress-container">
    <div className="progress-label">
      <span>{label}</span>
      <span className="progress-value">{value.toFixed(1)}</span>
    </div>
    <div className="progress-bar">
      <div 
        className="progress-fill" 
        style={{ width: `${(value / max) * 100}%`, backgroundColor: color }}
      ></div>
    </div>
  </div>
);

export { Card, ProgressBar };
