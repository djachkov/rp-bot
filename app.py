# coding: utf8
import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler
from config import token

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text=START_MESSAGE)



logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
START_MESSAGE = "Welcome, stranger! For now I can't help you, but your adventure will start soon, you just have to wait and believe..."
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)



updater.start_polling()
