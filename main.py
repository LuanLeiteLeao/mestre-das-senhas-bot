import telebot
import os 
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id,'oi')



if __name__ == "__main__":
	bot.infinity_polling()