import imp
from telnetlib import AUTHENTICATION
from create_bot import dp, bot

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types

class ConnectToDateBase():
    connection_to_sql = State()
    authentifaction = State()
    connected = State()

# other fucntion