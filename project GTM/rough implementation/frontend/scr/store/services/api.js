const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1';

async function request(endpoint, options = {}) {
  const response = await fetch(`${API_BASE}${endpoint}`, {
    headers: {
      'Content-Type': 'application/json',
      ...options.headers,
    },
    ...options,
  });
  if (!response.ok) {
    const error = await response.text();
    throw new Error(error);
  }
  return response.json();
}

export const tasksApi = {
  getTasks: () => request('/tasks'),
  createTask: (data) => request('/tasks', { method: 'POST', body: JSON.stringify(data) }),
  approveTask: (taskId) => request(`/tasks/${taskId}/approve`, { method: 'POST' }),
  rejectTask: (taskId) => request(`/tasks/${taskId}/reject`, { method: 'POST' }),
};

export const agentsApi = {
  getAgents: () => request('/agents/status'),
  runAgent: (agentName, params) => request(`/agents/run/${agentName}`, { method: 'POST', body: JSON.stringify({ params }) }),
};

export const metricsApi = {
  getMetrics: () => request('/metrics'),
  getHealthHistory: () => request('/health/history'),
};