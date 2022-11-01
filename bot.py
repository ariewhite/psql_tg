import logging

from create_bot import dp, bot
from aiogram import executor


logging.basicConfig(level=logging.INFO)

from handlers import client, admin, general

client.register_handlers_client(dp=dp)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)