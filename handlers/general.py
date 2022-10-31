import json

from aiogram import types
from create_bot import dp

@dp.message_handler()
async def filter(message: types.message):
    if {i.lower() for i in message.text.split(' ')}.intersection(set(json.load(open('filter.json')))) != set():
        await message.reply('Маты')