import logging
import time

from create_bot import dp, bot
from aiogram import types, Discpatcher

# @dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name

    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')
    
    await message.reply(f"Hi, {user_full_name}")


def register_handlers_client(dp : Discpatcher):
    dp.register_message_handler(start_handler)