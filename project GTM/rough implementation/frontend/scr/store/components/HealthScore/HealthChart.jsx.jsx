import React from 'react';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

export default function HealthChart({ data }) {
  const chartData = {
    labels: data.map(d => d.date),
    datasets: [
      {
        label: 'Health Score',
        data: data.map(d => d.value),
        borderColor: '#4caf7f',
        backgroundColor: 'rgba(76, 175, 127, 0.1)',
        tension: 0.3,
        fill: true,
      },
    ],
  };
  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: { legend: { labels: { color: '#eef2ff' } } },
    scales: { y: { min: 0, max: 1, grid: { color: '#2d3748' } }, x: { ticks: { color: '#a0aec0' } } },
  };
  return <Line data={chartData} options={options} height={200} />;
}