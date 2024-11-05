// URL of your Django DRF endpoint
const API_URL = 'http://127.0.0.1:8000/todo/api/';

async function fetchTodos() {
    try {
        const response = await fetch(`${API_URL}list_tasks/`);
        const result = await response.json();

        // Access the `data` array from the response
        const todos = result.data;
        console.log(todos);

        const todoList = document.getElementById('todo-list');
        todoList.innerHTML = '';

        todos.forEach(todo => {
            const li = document.createElement('li');
            li.textContent = todo.title;
            li.onclick = () => deleteTodo(todo.id);
            todoList.appendChild(li);
        });
    } catch (error) {
        console.error('Error fetching todos:', error);
    }
}



document.addEventListener('DOMContentLoaded', fetchTodos);
