import React, { useState } from 'react';
import TodoForm from './components/TodoForm';
import TodoList from './components/TodoList';

function App() {
  const [tasks, setTasks] = useState([]);

  const addTask = async (task) => {
    const response = await fetch('http://65.1.100.46:5000/add-task', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ task }),
    });
    if (response.ok) {
      setTasks([...tasks, task]);
    }
  };

  const deleteTask = (index) => {
    setTasks(tasks.filter((_, i) => i !== index));
  };

  return (
    <div className="App">
      <h1>To-Do App</h1>
      <TodoForm addTask={addTask} />
      <TodoList tasks={tasks} deleteTask={deleteTask} />
    </div>
  );
}

export default App;
