# Fullstack Python/JavaScript Project

This is a fullstack web application with a Python (Flask) backend and JavaScript frontend.

## Project Structure

```
.
├── app.py                 # Backend server (Flask)
├── requirements.txt       # Python dependencies
├── frontend/
│   ├── index.html        # Main HTML file
│   ├── styles.css        # CSS styles
│   └── app.js            # Frontend JavaScript
└── PROJECT_CHECKLIST.txt  # Development checklist
```

## Getting Started

### Backend Setup
1. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the backend server:
   ```
   python app.py
   ```
   The server will run at `http://localhost:5000`

### Frontend Setup
1. Open `frontend/index.html` in your web browser
2. The frontend will automatically try to connect to the backend at `http://localhost:5000`

## Development
- Backend API is available at `http://localhost:5000/api`
- Frontend runs on `file://` protocol (no web server needed for development)
- Enable CORS is already configured in the backend for development
