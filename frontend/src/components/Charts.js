import React from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, Cell } from 'recharts';

// Emission breakdown pie chart
export const EmissionBreakdownChart = ({ data }) => {
  if (!data || Object.keys(data).length === 0) {
    return <p>No data to display</p>;
  }

  const chartData = Object.entries(data).map(([key, value]) => ({
    name: key.charAt(0).toUpperCase() + key.slice(1),
    value: parseFloat(value),
    fill: getCategoryColor(key)
  }));

  const total = chartData.reduce((sum, item) => sum + item.value, 0);

  return (
    <div className="chart-container">
      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={chartData}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="name" />
          <YAxis label={{ value: 'Percentage (%)', angle: -90, position: 'insideLeft' }} />
          <Tooltip formatter={(value) => `${value.toFixed(1)}%`} />
          <Bar dataKey="value" radius={[8, 8, 0, 0]}>
            {chartData.map((entry, index) => (
              <Cell key={`cell-${index}`} fill={entry.fill} />
            ))}
          </Bar>
        </BarChart>
      </ResponsiveContainer>
      <div className="chart-legend">
        {chartData.map((item, idx) => (
          <div key={idx} className="legend-item">
            <div className="legend-color" style={{ backgroundColor: item.fill }}></div>
            <span>{item.name}: {item.value.toFixed(1)}%</span>
          </div>
        ))}
      </div>
    </div>
  );
};

// Emission trend chart
export const EmissionTrendChart = ({ data }) => {
  if (!data || data.length === 0) {
    return <p>No data to display</p>;
  }

  return (
    <ResponsiveContainer width="100%" height={300}>
      <BarChart data={data}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="month" />
        <YAxis label={{ value: 'kg CO₂', angle: -90, position: 'insideLeft' }} />
        <Tooltip 
          formatter={(value) => [`${value.toFixed(1)} kg CO₂`, '']}
          labelFormatter={(label) => `Month: ${label}`}
        />
        <Bar dataKey="predicted_emissions_kg_co2" fill="#ef4444" radius={[8, 8, 0, 0]} />
      </BarChart>
    </ResponsiveContainer>
  );
};

function getCategoryColor(category) {
  const colors = {
    travel: '#3b82f6',
    electricity: '#f59e0b',
    food: '#ec4899',
    lifestyle: '#8b5cf6'
  };
  return colors[category] || '#6b7280';
}
