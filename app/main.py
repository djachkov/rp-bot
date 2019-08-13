import logging
import os
import asyncio
from dotenv import load_dotenv
import telegram
from app.commands import start

# TODO: rewrite this
load_dotenv()
TOKEN = os.getenv("TOKEN")
LOGGING_LEVEL = os.getenv(("LOGGING_LEVEL"))

# TODO: replace
async def main():
    bot = telegram.Bot(TOKEN)
    async with bot:
        print((await bot.get_me()))


if __name__ == "__main__":
    asyncio.run(main())
