import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  pipelineCoverage: 0,
  forecastAccuracy: 0,
  winRate: 0,
  healthScore: 0,
  healthHistory: [],
};

const metricsSlice = createSlice({
  name: 'metrics',
  initialState,
  reducers: {
    setMetrics: (state, action) => {
      return { ...state, ...action.payload };
    },
    addHealthHistory: (state, action) => {
      state.healthHistory.push(action.payload);
      if (state.healthHistory.length > 30) state.healthHistory.shift();
    },
  },
});

export const { setMetrics, addHealthHistory } = metricsSlice.actions;
export default metricsSlice.reducer;