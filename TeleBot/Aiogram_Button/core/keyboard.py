from aiogram.types import *

start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton(text="Время"),
    KeyboardButton(text="Число"),
    KeyboardButton(text ="Info"),
    KeyboardButton(text="изображение"),


    )