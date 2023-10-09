
#Все запросы называются CRUD

# CREATE   |  POST    |  INSERT
# READ     |  GET     |  SELECT
# UPDATE   |  PUT     |  UPDATE
# DELETE   |  DELETE  |  DELETE

    
# QUERY request
# requests.txt
# requests.json()  (DICT ключи и значения)
# requests.content (img, mp4, mp3, и т.д)


# INNER join  показывает все связанные таблицы
# FULL join  показывает все связанные таблицы и не связанные таблицы
# LEFT join показывает все связки с приоритетом левой стороны
# RIGTH join показывает с приоритетом правой стороны




from random import choice

import psycopg2
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.types import *
from aiogram.utils import executor

from core.config import DOMAIN, HEADERS, TOKEN, URL, DATABASE, HOST, PASSWORD, PORT, USER
from core.pars import proccesing
from core.database import CheckStart, create_table, RegisterUser, RegisterPHONE, CheckUserPHONE, UserPhoneUpdate
from core.keyboard import register_user, photo_button

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)


connection = psycopg2.connect(
    host = HOST,
    database = DATABASE,
    user = USER,
    password = PASSWORD,
    port = PORT
)


@dp.message_handler(commands=['start'])
async def start(message: Message):
    create_table(connection)
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username

    if CheckStart(connection, message.from_user.id) is not None:
        pass
    else:
        RegisterUser(connection, user_id, first_name, last_name, username)
    photo = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQYzakBVBJbbfd7o8lktLcY973lDeF86TV52UxLFIH3_aDjaurilc3eUxftVWVllMsjoUM&usqp=CAU"

    text = f"""<a href='{photo}'> Привет я бот который отправляет фотографии </a>"""

    await message.reply(text, reply_markup=register_user)


@dp.message_handler(content_types=ContentTypes.CONTACT)
async def message_user_phone(message: Message):
    user_id = message.from_user.id
    phone = message.contact.phone_number

    if CheckUserPHONE(connection, user_id) is not None:
        await message.answer("Вы уже зарегистрированы", 
            reply_markup=photo_button)

    else:
        RegisterPHONE(connection, user_id, phone)
        UserPhoneUpdate(connection, user_id)
        await message.answer("вы успешно зарегистрированы",
            reply_markup=photo_button)

@dp.message_handler(content_types=ContentTypes.TEXT)
async def message_user(message: Message):
    user_id = message.from_user.id

    if CheckUserPHONE(connection, user_id) is None:
        await message.answer("Пройдите регистрацию")

    else:
        if message.text.lower() == "фотография":
            photo = choice(proccesing(URL,HEADERS))

            text = f"<a href='{photo}'> Фотография </a>"
            await message.reply(text)
            

if __name__ == "__main__":
    try:
        executor.start_polling(dp, skip_updates=True)
    except (KeyboardInterrupt, SystemExit):
        pass


