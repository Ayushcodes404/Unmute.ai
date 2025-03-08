# Unmute.ai
 "Bridging the legal knowledge gap between Indian society and the law"
# Legal Knowledge Bridge

## Overview
This Flask-based web application helps bridge the legal knowledge gap between Indian society and the law. It utilizes Google Gemini AI to provide legal insights in simple terms and different languages. Additionally, it features a conversational chatbot that offers legal assistance in multiple Indian languages.

## Features
- **AI-Powered Legal Assistance**: Uses Google Gemini to generate responses related to Indian law.
- **Conversational Chatbot**: Engages users in legal discussions and provides relevant legal insights.
- **Multi-Language Support**: Users can request legal information in English, Hindi, Kannada, Marathi, Tamil, and Telugu.
- **Session-Based Queries**: Stores user queries and selected language preferences.
- **Formatted Responses**: Cleans and formats AI-generated responses for readability.

## Technologies Used
- **Python** (Flask)
- **Google Generative AI (Gemini 2.0 Flash Thinking Exp)**
- **HTML/CSS** (for rendering templates)
- **JSON API** (for structured responses)
- **dotenv** (for environment variable management)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/legal-knowledge-bridge.git
   cd legal-knowledge-bridge
   ```
2. Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   - Create a `.env` file and add your Google API key:
     ```
     GEMINI_API_KEY=your_google_api_key
     ```

## Running the Application
Start the Flask server with:
```sh
python app.py
```

## API Endpoints
- **`/`** - Renders the homepage.
- **`/set_query`** - Stores user law query and preferred language.
- **`/ask`** - Conversational chatbot endpoint for legal queries.
- **`/prompt1`** - Provides a general explanation of a legal term in Indian law.
- **`/prompt2`** - Explains when a law is applied with examples.
- **`/prompt3`** - Provides legal implications of a law.

## Usage
1. Open the application in a web browser.
2. Enter a legal query and choose a language.
3. Click to receive AI-generated legal explanations.
4. Use the chatbot to have a conversation on legal matters in different languages.

## Troubleshooting
- **Missing API Key:** Ensure `.env` contains `GEMINI_API_KEY`.
- **Flask App Not Running:** Ensure all dependencies are installed and Flask is properly set up.
- **Incorrect Responses:** Ensure queries are relevant to Indian law.

## Contributing
Feel free to contribute by reporting issues or submitting pull requests on GitHub.


## Author
Your Name - [Your GitHub](https://github.com/ayushcodes404)

