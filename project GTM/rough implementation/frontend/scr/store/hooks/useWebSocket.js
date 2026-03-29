import { useEffect, useState, useRef } from 'react';
import { useDispatch } from 'react-redux';
import { addTask, removeTask } from '../store/slices/tasksSlice';
import { setMetrics, addHealthHistory } from '../store/slices/metricsSlice';
import { setAgentStatus } from '../store/slices/agentsSlice';

const WS_URL = import.meta.env.VITE_WS_URL || 'ws://localhost:8000/ws';

export function useWebSocket() {
  const dispatch = useDispatch();
  const [isConnected, setIsConnected] = useState(false);
  const socketRef = useRef(null);

  useEffect(() => {
    const socket = new WebSocket(WS_URL);
    socketRef.current = socket;

    socket.onopen = () => {
      setIsConnected(true);
      console.log('WebSocket connected');
    };

    socket.onmessage = (event) => {
      try {
        const data = JSON.parse(event.data);
        switch (data.type) {
          case 'new_task':
            dispatch(addTask(data.payload));
            break;
          case 'task_resolved':
            dispatch(removeTask(data.payload.taskId));
            break;
          case 'metrics_update':
            dispatch(setMetrics(data.payload));
            break;
          case 'health_update':
            dispatch(addHealthHistory(data.payload));
            break;
          case 'agent_status':
            dispatch(setAgentStatus(data.payload));
            break;
          default:
            console.warn('Unknown message type', data);
        }
      } catch (e) {
        console.error('Failed to parse WebSocket message', e);
      }
    };

    socket.onclose = () => {
      setIsConnected(false);
      console.log('WebSocket disconnected');
      setTimeout(() => {
        // reconnect logic
      }, 3000);
    };

    return () => {
      socket.close();
    };
  }, [dispatch]);

  const send = (message) => {
    if (socketRef.current && socketRef.current.readyState === WebSocket.OPEN) {
      socketRef.current.send(JSON.stringify(message));
    }
  };

  return { isConnected, send };
}