import telebot
from telebot import types

bot = telebot.TeleBot("token")

web_app_url = "https://t.me/Hamstergey_bot/webapp"

text = "Это приложение - копия игры Hamster Sofia!\n\nНажмите на кнопку снизу, что запустить его!"

button = types.InlineKeyboardButton('Запустить', url=web_app_url)
keyboard = types.InlineKeyboardMarkup()
keyboard.add(button)

@bot.message_handler(commands=['start'])
def send_message(message):
    bot.send_message(message.chat.id, text=text, reply_markup=keyboard)

bot.polling()