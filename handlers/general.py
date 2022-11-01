import json

from aiogram import Dispatcher ,types
from create_bot import dp

# @dp.message_handler()
async def filter(message: types.message):
    if {i.lower() for i in message.text.split(' ')}.intersection(set(json.load(open('filter.json')))) != set():
        await message.reply('Маты')

def register_message_general(dp : Dispatcher):
    dp.register_message_handler(filter)
