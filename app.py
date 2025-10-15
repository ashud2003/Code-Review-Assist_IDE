import os
import json
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import google.generativeai as genai
from datetime import datetime
import sqlite3

app = Flask(__name__)
CORS(app)

# Configure Gemini API
API_KEY = "Your-gemini-key-here"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('models/gemini-2.5-flash')

# Initialize database
def init_db():
    conn = sqlite3.connect('reviews.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS reviews
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  filename TEXT,
                  language TEXT,
                  review_text TEXT,
                  timestamp TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/review', methods=['POST'])
def review_code():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        code_content = file.read().decode('utf-8')
        filename = file.filename
        
        extension = filename.split('.')[-1] if '.' in filename else 'unknown'
        language_map = {
            'py': 'Python', 'js': 'JavaScript', 'java': 'Java',
            'cpp': 'C++', 'c': 'C', 'cs': 'C#', 'rb': 'Ruby',
            'go': 'Go', 'php': 'PHP', 'ts': 'TypeScript'
        }
        language = language_map.get(extension, extension.upper())
        
        prompt = f"""Review this {language} code for readability, modularity, and potential bugs, then provide improvement suggestions.

Code:
```{extension}
{code_content}
```

Provide a structured review covering:
1. Code Quality Score (out of 10)
2. Readability Issues
3. Modularity & Structure
4. Potential Bugs or Issues
5. Best Practices Violations
6. Specific Improvement Suggestions

Be concise and actionable."""
        
        response = model.generate_content(prompt)
        review_text = response.text
        
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        conn = sqlite3.connect('reviews.db')
        c = conn.cursor()
        c.execute('INSERT INTO reviews (filename, language, review_text, timestamp) VALUES (?, ?, ?, ?)',
                  (filename, language, review_text, timestamp))
        review_id = c.lastrowid
        conn.commit()
        conn.close()
        
        return jsonify({
            'success': True,
            'review_id': review_id,
            'filename': filename,
            'language': language,
            'review': review_text,
            'timestamp': timestamp
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    try:
        conn = sqlite3.connect('reviews.db')
        c = conn.cursor()
        c.execute('SELECT id, filename, language, review_text, timestamp FROM reviews ORDER BY id DESC LIMIT 20')
        rows = c.fetchall()
        conn.close()
        
        reviews = []
        for row in rows:
            reviews.append({
                'id': row[0],
                'filename': row[1],
                'language': row[2],
                'review': row[3],
                'timestamp': row[4]
            })
        
        return jsonify({'reviews': reviews})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/review/<int:review_id>', methods=['GET'])
def get_review(review_id):
    try:
        conn = sqlite3.connect('reviews.db')
        c = conn.cursor()
        c.execute('SELECT id, filename, language, review_text, timestamp FROM reviews WHERE id = ?', (review_id,))
        row = c.fetchone()
        conn.close()
        
        if row:
            return jsonify({
                'id': row[0],
                'filename': row[1],
                'language': row[2],
                'review': row[3],
                'timestamp': row[4]
            })
        else:
            return jsonify({'error': 'Review not found'}), 404
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
