import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  list: [],
  status: {},
};

const agentsSlice = createSlice({
  name: 'agents',
  initialState,
  reducers: {
    setAgents: (state, action) => {
      state.list = action.payload;
    },
    setAgentStatus: (state, action) => {
      const { name, status } = action.payload;
      state.status[name] = status;
    },
  },
});

export const { setAgents, setAgentStatus } = agentsSlice.actions;
export default agentsSlice.reducer;