import { configureStore } from '@reduxjs/toolkit';
import tasksReducer from './slices/tasksSlice';
import agentsReducer from './slices/agentsSlice';
import metricsReducer from './slices/metricsSlice';

export const store = configureStore({
  reducer: {
    tasks: tasksReducer,
    agents: agentsReducer,
    metrics: metricsReducer,
  },
});