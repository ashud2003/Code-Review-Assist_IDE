# Code Review Assistant

A simple AI-powered code review tool using Google Gemini API.

## Features
- Upload code files for automated review
- AI analysis for readability, modularity, and bugs
- Review history with SQLite database
- Simple web dashboard

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open browser:
```
http://localhost:5000
```

## API Endpoints

- `POST /api/review` - Upload code file for review
- `GET /api/reviews` - Get recent reviews
- `GET /api/review/<id>` - Get specific review

## Supported Languages
Python, JavaScript, Java, C++, C, C#, Ruby, Go, PHP, TypeScript, HTML, CSS, SQL

## Tech Stack
- Backend: Flask (Python)
- LLM: Google Gemini API
- Database: SQLite
- Frontend: HTML/CSS/JavaScript

## Demo
1. Upload a code file
2. Wait for AI analysis
3. View detailed review report
4. Access review history

## Project Structure
```
Additional/
├── app.py              # Flask backend
├── requirements.txt    # Dependencies
├── README.md          # Documentation
├── templates/
│   └── index.html     # Web dashboard
└── reviews.db         # SQLite database (auto-created)
```

## API Key
The Google Gemini API key is included in the code. For production use, move it to environment variables.
