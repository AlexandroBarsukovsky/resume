import React from 'react';

export default function AgentCard({ agent, onRun }) {
  return (
    <div className="flex justify-between items-center p-2 border-b border-gray-800">
      <div>
        <div className="font-medium">{agent.name}</div>
        <div className="text-xs text-gray-400">Статус: {agent.status}</div>
      </div>
      <button
        onClick={() => onRun(agent.name, {})}
        className="px-2 py-1 bg-gray-700 rounded text-xs hover:bg-gray-600"
      >
        Запустить
      </button>
    </div>
  );
}