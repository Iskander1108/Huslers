from aiogram.types import *

exchange_buttons = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("euro"),
    KeyboardButton("dollar"),
    KeyboardButton("ruble"),
    KeyboardButton("pound"),
    KeyboardButton("yen"),
    KeyboardButton("som"),
    KeyboardButton("india"),
    KeyboardButton("Меню"),
)

register_user = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Зарегестрироваться", request_contact=True),
    )


menu = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Крипта"),
    KeyboardButton("Валюта"),


)


crypto_buttons = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Bitcoin"),
    KeyboardButton("DOGE"),
    KeyboardButton("Ethereum"),
    KeyboardButton("Primecoin"),
    KeyboardButton("Peercoin"),
    KeyboardButton("Меню"),

)