# Telegram Image Generator Bot

This Telegram bot generates AI-generated images based on user prompts using the Segmind API.

## Features
- Accepts text prompts via Telegram command `/gen`
- Uses Segmind API to generate images
- Sends generated images back to users
- Supports basic commands like `/start` and `/help`

## Installation & Setup

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- A Telegram bot token from [BotFather](https://t.me/BotFather)
- A Segmind API key from [Segmind](https://segmind.com)

### Clone the Repository
```bash
git clone https://github.com/your-username/telegram-image-generator-bot.git
cd telegram-image-generator-bot
```

### Install Dependencies
```bash
pip install telebot==3.8.0 requests==2.26.0
```

### Configuration
Create a `config.py` file and add your API keys:
```python
TELEGRAM_BOT_TOKEN = "your-telegram-bot-token"
SEGMIND_API_KEY = "your-segmind-api-key"
SEGMIND_ENDPOINT = "https://api.segmind.com/v1/stable-diffusion/text-to-image"
```

### Running the Bot
```bash
python main.py
```

## Usage
- Start the bot by sending `/start`
- Generate an image using `/gen <your prompt>`
  
  Example:
  ```
  /gen A futuristic city at night
  ```

## License
This project is licensed under the MIT License.



