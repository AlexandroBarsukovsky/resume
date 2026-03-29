import React from 'react';

export default function KpiCard({ title, value, trend }) {
  return (
    <div className="bg-gray-900 rounded-2xl p-4 border border-gray-800">
      <div className="text-gray-400 text-sm uppercase">{title}</div>
      <div className="text-3xl font-bold mt-1">{value}</div>
      {trend && <div className="text-green-400 text-xs mt-1">{trend}</div>}
    </div>
  );
}