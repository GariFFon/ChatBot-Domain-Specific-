# Computer Science Expert Chatbot - Web UI

This is a web-based interface for the Computer Science Expert Chatbot powered by Google's Gemini AI. The web interface allows you to interact with the chatbot through a modern, responsive UI.

## Features

- Modern, responsive chat interface
- Dark/light mode toggle
- Syntax highlighting for code snippets
- Markdown formatting support
- Typing indicators
- Chat history within the session

## Requirements

- Python 3.8 or higher
- Flask
- Google Generative AI Python SDK
- python-dotenv

## Installation

1. Make sure you have all the required packages installed:

```bash
pip install -r requirements.txt
```

2. Set up your environment variables by creating a `.env` file with your Google API key:

```
GOOGLE_API_KEY=your_google_api_key_here
```

## Running the Web UI

To start the web interface, run:

```bash
python web_chatbot_ui.py
```

Then open your browser and navigate to:

```
http://127.0.0.1:5000
```

## Usage

1. Type your computer science related question in the input field
2. Press Enter or click the Send button
3. The chatbot will process your question and provide a response
4. You can toggle between dark and light mode using the switch in the top right
5. Click "Clear Chat" to start a new conversation

## Limitations

- The chatbot is specifically focused on computer science topics
- Responses are generated using the Gemini 1.5 Flash model
- Internet connection is required

## Integration

This web UI is designed as a standalone component that can be integrated into other projects. The core functionality is separated from any existing desktop UI implementation. 