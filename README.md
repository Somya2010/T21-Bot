# Telegram Bot

This bot allows users to generate images using OpenAI's DALL-E model directly from Telegram. Users can provide a prompt, select image size and quality, and receive the generated image within the chat.

## Features
- Accepts text prompts for image generation
- Allows users to select image size and quality
- Supports regeneration of images with the same or different parameters
- Interactive Telegram bot with inline buttons

## Installation

Ensure you have Python installed (version 3.8+ recommended). Then, install the required dependencies:

```bash
pip install telepot requests openai
```

## Configuration

Create a `config.py` file and add your API keys:

```python
# config.py
OPENAI_API_KEY = "your-openai-api-key"
TELEGRAM_BOT_TOKEN = "your-telegram-bot-token"
```

## Usage

Run the bot script:

```bash
python main.py
```

## How It Works
1. Users send a prompt to the bot.
2. The bot asks for size and quality preferences.
3. The bot generates an image using OpenAI's API.
4. The bot sends the generated image back to the user.
5. Users can choose to regenerate the image or start a new request.

## Dependencies
- `telepot` for Telegram bot functionality
- `requests` for making API calls
- `openai` for interfacing with DALL-E

## License
This project is licensed under the MIT License.

---

Feel free to contribute or customize as needed!

