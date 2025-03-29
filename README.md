# Computer Science Expert Chatbot

This is a specialized chatbot powered by Google's Gemini AI API, focused on computer science topics. The chatbot is designed to answer questions related to programming, algorithms, data structures, and other computer science concepts.

## Features

- Web-based interface with modern design
- Dark/light mode support
- Responsive design for various screen sizes
- Supports markdown formatting and code syntax highlighting
- Topic filtering - only answers computer science related questions
- Animated visual elements and particle effects
- Close the chatbot by typing "bye" or "byee"

## Requirements

- Python 3.8 or higher
- Google Generative AI Python SDK
- Flask
- python-dotenv
- Internet connection for API access

## Installation

1. Clone the repository or download the files
2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your Google API key:

```
GOOGLE_API_KEY=your_api_key_here
```

You can get an API key from [Google AI Studio](https://makersuite.google.com/).

> **IMPORTANT:** Never commit your `.env` file to version control! The `.gitignore` file is set up to exclude it. Use the provided `.env.example` as a template.

## Usage

To start the web interface:

```bash
python web_chatbot_ui.py
```

Then open your browser and navigate to:
```
http://127.0.0.1:5002
```

## Customization

- The web interface theme, colors, and animations can be modified in the `templates/chat.html` file
- To add more computer science keywords for topic filtering, modify the `is_computer_science_related` function in `web_chatbot_ui.py`

## Security Notes

- This project uses environment variables to protect sensitive API keys
- The `.env` file containing your API key is excluded from Git via `.gitignore`
- If forking or cloning this repo, make sure to create your own `.env` file based on the provided `.env.example`
- Never commit credentials or API keys to public repositories

## License

This project is open source and available for personal and educational use.

## Credits

- Built with Flask and Tailwind CSS
- Powered by Google's Gemini 1.5 Flash API 
