from config import token
import random

#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot

bot = telebot.TeleBot(token)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Привет!!                                                       \
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])

@bot.message_handler(commands=['cube'])
def cube_handler(message):
    cube = str(random.choice(['1', '2', '3', '4', '5', '6']))
    bot.reply_to(message, cube)


bot.infinity_polling()