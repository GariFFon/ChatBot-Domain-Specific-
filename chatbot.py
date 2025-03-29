import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the Gemini API
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

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
        'blockchain', 'database', 'sql', 'nosql', 'frontend', 'backend', 'devops' , 'binary search tree'
    ]
    
    question_lower = question.lower()
    return any(keyword in question_lower for keyword in cs_keywords)

def get_response(prompt):
    """Get response from Gemini AI"""
    try:
        if not is_computer_science_related(prompt):
            return "I apologize, but I can only answer questions related to computer science. Please ask a question about programming, software development, or other computer science topics."

        # Add context to make responses more CS-focused
        enhanced_prompt = f"As a computer science expert, please answer this question: {prompt}"
        response = model.generate_content(enhanced_prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    print("Welcome to the Computer Science Chatbot!")
    print("I can help you with questions about programming, software development, and computer science topics.")
    print("Type 'quit' to exit")
    print("-" * 50)
    
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() == 'quit':
            print("Goodbye!... See you next time!")
            break
            
        response = get_response(user_input)
        print("\nBot:", response)

if __name__ == "__main__":
    main() 