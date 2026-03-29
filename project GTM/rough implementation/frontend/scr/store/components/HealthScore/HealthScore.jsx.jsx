import React from 'react';
import HealthChart from './HealthChart';

export default function HealthScore({ healthScore, history }) {
  return (
    <div className="bg-gray-900 rounded-2xl p-4 border border-gray-800">
      <h2 className="text-xl font-bold mb-2">Health Score</h2>
      <div className="text-3xl font-bold mb-2">{healthScore.toFixed(2)}</div>
      <div className="w-full bg-gray-700 rounded-full h-2 mb-4">
        <div
          className="bg-green-500 h-2 rounded-full"
          style={{ width: `${healthScore * 100}%` }}
        ></div>
      </div>
      <HealthChart data={history} />
    </div>
  );
}