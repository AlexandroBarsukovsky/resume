import React from 'react';
import AgentCard from './AgentCard';

export default function AgentPanel({ agents, onRun }) {
  return (
    <div className="bg-gray-900 rounded-2xl p-4 border border-gray-800">
      <h2 className="text-xl font-bold mb-4">Агенты</h2>
      <div className="space-y-2">
        {agents.map(agent => (
          <AgentCard key={agent.name} agent={agent} onRun={onRun} />
        ))}
      </div>
    </div>
  );
}