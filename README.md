# Code Review Assistant

The Introduction video is attached in the repository named as Project_Introduction_video.mp4
<img width="1919" height="989" alt="image" src="https://github.com/user-attachments/assets/c826dd21-8fde-4b9d-8662-0d075db211bb" />


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
<img width="1919" height="983" alt="image" src="https://github.com/user-attachments/assets/f1b3e2f7-4324-45cc-a2af-d68c6dfdfcc7" />
<img width="1589" height="401" alt="image" src="https://github.com/user-attachments/assets/790d5eae-2cf8-46f3-bcc0-11752c9afd43" />
<img width="1499" height="988" alt="image" src="https://github.com/user-attachments/assets/d1392aa1-31ca-44a6-ba7a-002e88c08df2" />
<img width="1533" height="756" alt="image" src="https://github.com/user-attachments/assets/de7a56e0-99aa-4692-9bda-71746b2716e7" />

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
