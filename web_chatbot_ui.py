import os
import google.generativeai as genai
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify

# Load environment variables
load_dotenv()

# Configure the Gemini API
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
if not GOOGLE_API_KEY:
    print("WARNING: GOOGLE_API_KEY not found in environment variables!")
    print("Make sure you have a .env file with your API key")

genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-2.0-flash')

def is_computer_science_related(question):
    """Check if the question is related to computer science"""
    cs_keywords = [
        'programming', 'code', 'software', 'computer', 'algorithm', 'data structure',
        'database', 'network', 'web', 'app', 'development', 'coding', 'python',
        'java', 'javascript', 'html', 'css', 'api', 'framework', 'debug',
        'function', 'class', 'object', 'variable', 'loop', 'array', 'string',
        'integer', 'boolean', 'server', 'client', 'cloud', 'security', 'testing',
        'git', 'repository', 'operating system', 'compiler', 'interpreter',
        'machine learning', 'artificial intelligence', 'data science', 'cybersecurity',
        'blockchain', 'database', 'sql', 'nosql', 'frontend', 'backend', 'devops', 'binary search tree'
    ]
    
    question_lower = question.lower()
    return any(keyword in question_lower for keyword in cs_keywords)

def get_response(prompt):
    """Get response from Gemini AI"""
    try:
        if not GOOGLE_API_KEY:
            return "API key not configured. Please set up your GOOGLE_API_KEY in the .env file."
            
        if not is_computer_science_related(prompt):
            return "I apologize, but I can only answer questions related to computer science. Please ask a question about programming, software development, or other computer science topics."

        # Add context to make responses more CS-focused
        enhanced_prompt = f"As a computer science expert, please answer this question: {prompt}"
        response = model.generate_content(enhanced_prompt)
        return response.text
    except Exception as e:
        print(f"Error getting response from Gemini: {e}")
        return f"An error occurred: {str(e)}"

# Create Flask app
app = Flask(__name__)

# Enable CORS for all routes
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

# Create templates directory if it doesn't exist
os.makedirs('templates', exist_ok=True)

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    if not request.is_json:
        return jsonify({'error': 'Request must be JSON'}), 400
        
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid JSON'}), 400
        
    user_message = data.get('message', '')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400
    
    print(f"Received message: {user_message}")
    
    # Special handling for exit command
    if user_message.lower() == 'byee':
        print("Exit command received, sending goodbye message")
        return jsonify({'response': 'Goodbye! It was nice talking with you. I\'ll close this session now.', 'exit': True})
    
    # Regular message handling
    response = get_response(user_message)
    print(f"Sending response: {response[:100]}...")
    return jsonify({'response': response})

if __name__ == '__main__':
    print("Starting the CS Expert Chatbot Web Interface...")
    print("Open your browser and navigate to http://127.0.0.1:5000")
    print(f"API Key configured: {'Yes' if GOOGLE_API_KEY else 'No - Please check your .env file'}")
    app.run(debug=True) 