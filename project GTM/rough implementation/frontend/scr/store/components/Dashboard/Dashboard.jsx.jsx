import React from 'react';
import KpiCard from './KpiCard';

export default function Dashboard({ metrics }) {
  return (
    <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
      <KpiCard title="Pipeline Coverage" value={`${metrics.pipelineCoverage.toFixed(1)}x`} trend="+0.3" />
      <KpiCard title="Forecast Accuracy" value={`${metrics.forecastAccuracy.toFixed(1)}%`} trend="+5%" />
      <KpiCard title="Win Rate" value={`${metrics.winRate.toFixed(1)}%`} trend="+2%" />
      <KpiCard title="Health Score" value={metrics.healthScore.toFixed(2)} trend="+0.05" />
    </div>
  );
}