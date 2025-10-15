# Code Review Assistant

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.0-lightgrey.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**🎥 Introduction Video:** [Watch the Project Introduction](https://github.com/ashud2003/Code-Review-Assist_IDE/blob/main/Project_Introduction_Video.mp4)

![Code Review Assistant Interface](https://github.com/user-attachments/assets/c826dd21-8fde-4b9d-8662-0d075db211bb)

A modern, AI-powered code review tool that leverages Google Gemini API to provide intelligent code analysis, helping developers improve code quality through automated insights on readability, modularity, potential bugs, and best practices.

## ✨ Features

- **AI-Powered Analysis**: Utilizes Google Gemini 2.5 Flash for comprehensive code reviews
- **Multi-Language Support**: Supports 15+ programming languages including Python, JavaScript, Java, C++, and more
- **Interactive Web Dashboard**: Modern UI with Monaco Editor integration and dark/light theme support
- **Review History**: Persistent SQLite database for storing and retrieving past reviews
- **Export Functionality**: Generate PDF reports of code review results
- **Real-time Feedback**: Instant analysis with detailed scoring and improvement suggestions
- **Responsive Design**: Works seamlessly on desktop and mobile devices

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))

### Installation

1. **Clone the repository** (if applicable) or navigate to the project directory

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Key**:
   - Open `app.py`
   - Replace `"Your-gemini-key-here"` with your actual Google Gemini API key
   - **Security Note**: For production deployments, use environment variables instead of hardcoding the API key

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Access the application**:
   - Open your browser and navigate to `http://localhost:5000`

## 📖 Usage

### Web Interface

1. **Upload Code**: Click the "Upload" button or paste code directly into the editor
2. **Analyze**: Click the "Analyze" button to initiate AI review
3. **Review Results**: View detailed analysis including:
   - Overall code quality score (out of 10)
   - Readability assessment
   - Modularity evaluation
   - Potential bug identification
   - Best practice recommendations
   - Specific improvement suggestions
4. **Export**: Generate PDF reports of your review results
5. **History**: Access previous reviews via the API endpoints

### API Usage

The application provides RESTful API endpoints for programmatic access:

#### Review Code
```bash
curl -X POST -F "file=@your_code.py" http://localhost:5000/api/review
```

#### Get Review History
```bash
curl http://localhost:5000/api/reviews
```

#### Get Specific Review
```bash
curl http://localhost:5000/api/review/1
```

## 🛠️ API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/review` | Upload and analyze code file |
| `GET` | `/api/reviews` | Retrieve recent reviews (last 20) |
| `GET` | `/api/review/<id>` | Get specific review by ID |

## 🌐 Supported Languages

- Python
- JavaScript
- TypeScript
- Java
- C++
- C
- C#
- Ruby
- Go
- PHP
- HTML
- CSS
- SQL

## 🏗️ Tech Stack

- **Backend**: Flask 2.3.0 (Python web framework)
- **AI Engine**: Google Gemini 2.5 Flash API
- **Database**: SQLite (auto-created)
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Editor**: Monaco Editor (VS Code's editor)
- **Charts**: Chart.js for data visualization
- **PDF Export**: html2pdf.js for report generation

## 📁 Project Structure

```
Code-Review-Assistant/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── LICENSE               # MIT License
├── .gitignore           # Git ignore rules
├── templates/
│   └── index.html       # Web dashboard template
└── reviews.db           # SQLite database (auto-generated)
```

## 🔧 Configuration

### Environment Variables (Recommended for Production)

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_actual_api_key_here
FLASK_ENV=production
FLASK_DEBUG=False
```

Update `app.py` to use environment variables:

```python
import os
API_KEY = os.getenv('GEMINI_API_KEY', 'your-fallback-key')
```

### Database

The application automatically creates a SQLite database (`reviews.db`) on first run. No additional configuration required.

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest

# Run with debug mode
FLASK_DEBUG=True python app.py
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Security Notice

- The current implementation has the API key hardcoded for demonstration purposes
- **Never commit API keys to version control**
- Use environment variables or secure key management systems in production
- Regularly rotate your API keys

## 🐛 Troubleshooting

### Common Issues

1. **API Key Errors**: Ensure your Google Gemini API key is valid and has sufficient quota
2. **Port Already in Use**: Change the port in `app.py` if 5000 is occupied
3. **Import Errors**: Verify all dependencies are installed correctly
4. **Browser Issues**: Ensure JavaScript is enabled and try a modern browser

### Getting Help

- Check the browser console for JavaScript errors
- Verify API responses in browser developer tools
- Ensure the Flask server is running and accessible

## 📊 Screenshots & Demo

### Main Interface
![Code Review Assistant Main Interface](https://github.com/user-attachments/assets/c826dd21-8fde-4b9d-8662-0d075db211bb)

### Setup Instructions
![Setup Instructions](https://github.com/user-attachments/assets/f1b3e2f7-4324-45cc-a2af-d68c6dfdfcc7)

### Code Analysis in Progress
![Code Analysis](https://github.com/user-attachments/assets/790d5eae-2cf8-46f3-bcc0-11752c9afd43)

### Review Results Dashboard
![Review Results](https://github.com/user-attachments/assets/d1392aa1-31ca-44a6-ba7a-002e88c08df2)

### Detailed Analysis Report
![Detailed Report](https://github.com/user-attachments/assets/de7a56e0-99aa-4692-9bda-71746b2716e7)

**🎥 Introduction Video:** [Watch the Project Introduction](https://github.com/ashud2003/Code-Review-Assist_IDE/blob/main/Project_Introduction_Video.mp4)

## 🙏 Acknowledgments

- Google Gemini API for powering the AI analysis
- Monaco Editor for the code editing experience
- Chart.js for data visualization
- Font Awesome for icons

---

