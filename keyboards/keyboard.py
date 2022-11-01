from curses import BUTTON1_RELEASED
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button_start = KeyboardButton('/Start')
button1 = KeyboardButton('')

keyb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

keyb_client.add(button_start)
#keyb_client.insert() # рядом с другой кнопкой в одну строку, если есть место
#keyb_client.row(b1, b2, b3) # всё в одну строку

