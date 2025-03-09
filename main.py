import os
import requests
import telebot
from io import BytesIO
from config import TELEGRAM_BOT_TOKEN, SEGMIND_API_KEY, SEGMIND_ENDPOINT

# Initialize bot
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

def generate_image(prompt):
    headers = {
        "Authorization": f"Bearer {SEGMIND_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "width": 512,
        "height": 512
    }
    
    response = requests.post(SEGMIND_ENDPOINT, json=data, headers=headers)
    
    print("Response Status Code:", response.status_code)  # Debugging
    print("Response Text:", response.text)  # Debugging

    if response.status_code == 200:
        try:
            response_json = response.json()
            if "image_url" in response_json:
                image_url = response_json["image_url"]
                image_response = requests.get(image_url)
                return image_response.content
            elif "image_base64" in response_json:
                import base64
                return base64.b64decode(response_json["image_base64"])
        except Exception as e:
            print("Error parsing response:", e)
    
    return None  # If request fails

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Send a text prompt using /gen command to generate an image!\n\nExample:\n/gen A futuristic city at night")

@bot.message_handler(commands=['gen'])
def handle_generate(message):
    prompt = message.text.replace('/gen', '').strip()
    
    if not prompt:
        bot.reply_to(message, "Please provide a prompt after the /gen command.\n\nExample:\n/gen A futuristic city at night")
        return
    
    bot.reply_to(message, "Generating image, please wait...")
    image_bytes = generate_image(prompt)
    
    if image_bytes:
        bot.send_photo(message.chat.id, BytesIO(image_bytes), caption="Here is your generated image!")
    else:
        bot.reply_to(message, "Failed to generate image. Please try again later.")

# Run bot
if __name__ == "__main__":
    print("Bot is running...")
    bot.polling()
