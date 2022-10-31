import time
import logging
import string

from aiogram import executor
from create_bot import dp, bot


logging.basicConfig(level=logging.INFO)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)