from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import google.generativeai as genai
import os
import re

load_dotenv()

app = Flask(__name__)

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-2.0-flash-thinking-exp')

# Language mapping
LANGUAGES = {
    'en': 'English',
    'hi': 'Hindi',
    'kn': 'Kannada',
    'mr': 'Marathi',
    'ta': 'Tamil',
    'te': 'Telugu'
}

def clean_response(text):
    """
    Cleans up the response by removing unwanted symbols and formatting.
    """
    # Remove asterisks and other unwanted symbols
    text = re.sub(r'[*]', '', text)
    
    # Remove extra newlines and spaces
    text = re.sub(r'\n+', '\n', text).strip()
    
    return text

@app.route('/')
def index():
    return render_template('index.html', languages=LANGUAGES)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    user_message = data['message']
    lang = data['language']
    
    try:
        # Generate a response using Gemini
        response = model.generate_content(
            f"Respond in {LANGUAGES[lang]} language. Act as a legal expert specializing in Indian law. "
            f"Provide accurate, concise legal advice for: {user_message}. "
            "Include relevant IPC sections if applicable. Maintain a professional tone. "
            "Keep the response short (30-40 words) and human-friendly."
        )
        
        # Clean up the response
        cleaned_response = clean_response(response.text)
        
        return jsonify({'response': cleaned_response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=50001, debug=True)