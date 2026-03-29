import React from 'react';
import TaskItem from './TaskItem';

export default function TaskQueue({ tasks, onApprove }) {
  if (!tasks.length) {
    return <div className="text-center text-gray-500 py-8">Нет задач</div>;
  }
  return (
    <div className="space-y-3">
      {tasks.map(task => (
        <TaskItem key={task.id} task={task} onApprove={onApprove} />
      ))}
    </div>
  );
}