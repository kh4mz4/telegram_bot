from email import message
import telebot

bot = telebot.TeleBot("5130187833:AAEc3WpzIhjnR2bV1d5CNC_mXyIZmVa39Xw")


@bot.message_handler(commands="start")
def start(data):
    bot.send_message(data.chat.id, "salom")



bot.polling()
