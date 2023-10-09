from aiogram.types import *

register_user = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Зарегестрироваться", request_contact=True),
    KeyboardButton("Тест Локация", request_location=True),
)

photo_button = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Фотография")
)


