// Fetch data from the backend API
document.addEventListener('DOMContentLoaded', () => {
    fetch('http://localhost:5000/api/hello')
        .then(response => response.json())
        .then(data => {
            document.getElementById('message').textContent = data.message;
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('message').textContent = 'Failed to connect to the backend server.';
        });
});
