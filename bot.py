import telebot
import requests

bot = telebot.TeleBot('749857527:AAGMZgPom3lE7t_wHcxDC9YmTgRju_6Ll40')

@bot.message_handler(commands=['open'])
def handlle_text (message):
         bot.send_message(message.from_user.id, 'Opening')
         r = requests.get("https://google.com")
         print(r.status_code)

@bot.message_handler(commands=['link'])
def handlle_text(message):
         bot.send_message(message.from_user.id, 'Heres your link')


bot.polling(none_stop=True, interval=0)