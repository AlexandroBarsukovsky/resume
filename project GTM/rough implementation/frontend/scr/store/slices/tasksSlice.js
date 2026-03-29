import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  list: [],
  loading: false,
};

const tasksSlice = createSlice({
  name: 'tasks',
  initialState,
  reducers: {
    setTasks: (state, action) => {
      state.list = action.payload;
    },
    addTask: (state, action) => {
      state.list.unshift(action.payload);
    },
    removeTask: (state, action) => {
      state.list = state.list.filter(t => t.id !== action.payload);
    },
    setLoading: (state, action) => {
      state.loading = action.payload;
    },
  },
});

export const { setTasks, addTask, removeTask, setLoading } = tasksSlice.actions;
export default tasksSlice.reducer;