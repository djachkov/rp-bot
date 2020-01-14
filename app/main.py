# coding: utf8

import logging
import os

from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler

from app.commands import start

load_dotenv()
TOKEN = os.getenv("TOKEN")
LOGGING_LEVEL = os.getenv(("LOGGING_LEVEL"))


def main():
    logging.basicConfig(level=LOGGING_LEVEL)
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler("start", start)
    dispatcher.add_handler(start_handler)
    updater.start_polling()


if __name__ == "__main__":
    main()
