from flask import Flask, render_template, jsonify, request, session
import google.generativeai as genai
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a real secret key
app.config['JSON_AS_ASCII'] = False  # Allow non-ASCII characters in JSON responses

# Configure Gemini API
genai.configure(api_key=' add your api key / use dotenv to add you key')
model = genai.GenerativeModel('gemini-2.0-flash-thinking-exp')

# Function to replace symbols with <b> tags
def format_response(response_text):
    # Remove * symbols
    response_text = response_text.replace("*", "").strip()
    response_text = response_text.replace("#", " ").strip()
    return response_text

# Route to serve HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Store law query and language in session
@app.route('/set_query', methods=['POST'])
def set_query():
    try:
        law_query = request.form.get('law', '')
        language = request.form.get('language', 'English')

        if not law_query or not language:
            return jsonify({"error": "Both law query and language are required"}), 400

        # Store in session
        session['law_query'] = law_query
        session['language'] = language

        return jsonify({"message": f"Query set: {law_query} in {language}"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Common function to handle Gemini requests
def get_gemini_response(prompt_template):
    try:
        law_query = session.get('law_query', '')
        language = session.get('language', 'English')

        if not law_query or not language:
            return jsonify({"error": "Set law query and language first"}), 400

        # Construct the prompt with user input and selected language
        full_prompt = prompt_template.format(law_query=law_query, language=language)
        
        # Debug with UTF-8 encoding
        debug_prompt = full_prompt.encode('utf-8', 'replace').decode('utf-8')
        print(f"Prompt: {debug_prompt}")

        # Get response from Gemini
        response = model.generate_content(full_prompt)
        
        # Debug response with UTF-8
        debug_response = response.text.encode('utf-8', 'replace').decode('utf-8')
        print(f"Response: {debug_response}")

        # Format the response to remove * symbols
        formatted_response = format_response(response.text)

        return jsonify({"response": formatted_response})
    except Exception as e:
        print(f"Error: {str(e).encode('utf-8', 'replace').decode('utf-8')}")
        return jsonify({"error": str(e)}), 500

# Prompt endpoints
@app.route('/prompt1', methods=['GET'])
def prompt1():
    return get_gemini_response(
        "What is {law_query} in Indian Law System? Explain in {language} in simple terms."
    )

@app.route('/prompt2', methods=['GET'])
def prompt2():
    return get_gemini_response(
        "When is {law_query} applied in Indian Law? Explain in {language} with examples."
    )

@app.route('/prompt3', methods=['GET'])
def prompt3():
    return get_gemini_response(
        "What are legal implications of {law_query} under Indian Law? Explain in {language}."
    )

if __name__ == '__main__':
    app.run(debug=True)