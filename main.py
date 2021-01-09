# -*- coding: utf-8 -*-

"""
This is a spaced repetition bot.
It echoes any incoming messages.
And after that resends messages some time later.
"""

import logging
import time


from aiogram import Bot, Dispatcher, executor, types

from consts import (
    TIME_INTERVALS
)
from settings import API_TOKEN


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm Spaced repetition bot!\nPowered by aiogram.")


@dp.message_handler(content_types=[types.ContentType.ANY])
async def echo_handler(message: types.Message):
    """
    Handler will forward received message back to the sender
    """
    await bot.forward_message(
        from_chat_id=message.chat.id, chat_id=message.chat.id, message_id=message.message_id
    )
    for time_interval in TIME_INTERVALS:
        time.sleep(time_interval)
        await bot.forward_message(
            from_chat_id=message.chat.id, chat_id=message.chat.id, message_id=message.message_id
        )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)