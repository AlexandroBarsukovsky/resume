import React from 'react';

export default function TaskItem({ task, onApprove }) {
  return (
    <div className="bg-gray-800/50 rounded-xl p-4 border-l-4 border-yellow-500">
      <div className="font-semibold">{task.title}</div>
      <div className="text-sm text-gray-300 mt-1">{task.description}</div>
      <div className="flex gap-3 mt-3">
        <button
          onClick={() => onApprove(task.id)}
          className="px-3 py-1 bg-green-700 hover:bg-green-600 rounded-full text-sm"
        >
          Принять
        </button>
        <button
          onClick={() => onApprove(task.id)} // reject
          className="px-3 py-1 bg-red-800 hover:bg-red-700 rounded-full text-sm"
        >
          Отклонить
        </button>
      </div>
    </div>
  );
}