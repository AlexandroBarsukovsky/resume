import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useWebSocket } from '../hooks/useWebSocket';
import { useApi } from '../hooks/useApi';
import { metricsApi, tasksApi, agentsApi } from '../services/api';
import { setMetrics, addHealthHistory } from '../store/slices/metricsSlice';
import { setTasks } from '../store/slices/tasksSlice';
import { setAgents } from '../store/slices/agentsSlice';
import Dashboard from '../components/Dashboard/Dashboard';
import TaskQueue from '../components/TaskQueue/TaskQueue';
import AgentPanel from '../components/AgentPanel/AgentPanel';
import HealthScore from '../components/HealthScore/HealthScore';

export default function DashboardPage() {
  const dispatch = useDispatch();
  const { isConnected, send } = useWebSocket();
  const metrics = useSelector(state => state.metrics);
  const tasks = useSelector(state => state.tasks.list);
  const agents = useSelector(state => state.agents.list);

  const fetchMetrics = useApi(metricsApi.getMetrics);
  const fetchTasks = useApi(tasksApi.getTasks);
  const fetchAgents = useApi(agentsApi.getAgents);

  useEffect(() => {
    fetchMetrics.execute().then(data => dispatch(setMetrics(data)));
    fetchTasks.execute().then(data => dispatch(setTasks(data)));
    fetchAgents.execute().then(data => dispatch(setAgents(data)));
  }, []);

  return (
    <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
      <div className="lg:col-span-2 space-y-6">
        <Dashboard metrics={metrics} />
        <HealthScore healthScore={metrics.healthScore} history={metrics.healthHistory} />
        <TaskQueue tasks={tasks} onApprove={(id) => send({ type: 'approve', taskId: id })} />
      </div>
      <div>
        <AgentPanel agents={agents} onRun={(name, params) => agentsApi.runAgent(name, params)} />
      </div>
    </div>
  );
}