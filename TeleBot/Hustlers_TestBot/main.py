# fish

# virtualenv venv

# source venv/bin/activate.fish

# Для отключения deactivate

# from os import system
# system("clear")

# from aiogram import Bot  # Связь с сервером телеграмма
# from aiogram.utils import executor # Для работы без остановки
# from aiogram.dispatcher import Dispatcher # Анализ чата
# from aiogram.types import * # Все типы данных aiogram

# from core.config import TOKEN
# from core.weather import weather

# bot = Bot(token=TOKEN, parse_mode="HTML")
# dp = Dispatcher(bot)


# @dp.message_handler(commands=["start"])
# async def start(message: Message):
#     await message.answer("Привет ты можешь отправить название города а я тебе погоду")

# @dp.message_handler(content_types=ContentTypes.TEXT)
# async def message_users(message: Message):
#     try:
#         city = message.text
#         info = weather(city)
#         await message.reply(info)
    
#     except Exception:
#         await message.reply("Не смогли найти город с таким названием!")


# if __name__ == "__main__":
#     try:
#         print("Бот был запущен")
#         executor.start_polling(dp, skip_updates=True)
#     except (KeyboardInterrupt, SystemExit):
#         pass











from os import system
system("clear")

from aiogram import Bot  # Связь с сервером телеграмма
from aiogram.utils import executor # Для работы без остановки
from aiogram.dispatcher import Dispatcher # Анализ чата
from aiogram.types import * # Все типы данных aiogram

from core.config import TOKEN
from core.weather import weather

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: Message):
    await message.answer(f"Привет {message.from_user.first_name} ты можешь отправить название города а я тебе погоду")

@dp.message_handler(content_types=ContentTypes.TEXT)
async def message_users(message: Message):
    if message.text.lower() == "hello" or message.text.lower() == "здарова":
            await message.reply("Hello")
    else:
         await message.reply(f"Не понимаю тебя {message.from_user.first_name} ")

@dp.message_handler(content_types=ContentType.CONTACT)
async def contact_users(message: Message):
     await message.reply(message.contact.first_name)
     await message.reply(message.contact.phone_number)


@dp.message_handler(content_types=ContentType.LOCATION)
async def location_users(message: Message):
     await message.reply(message.location.latitude)
     await message.reply(message.location.longitude)


@dp.message_handler(content_types=ContentType.DOCUMENT)
async def document_users(message: Message):
     await message.reply(message.document.file_name)
     await message.reply(message.document.file_id)
     await message.reply(message.document.file_size / 1024) # Выдает размерв байтах . разделили на 1 024 и выдвет в кб

@dp.message_handler(content_types=ContentType.VOICE)
async def voice_users(message: Message):
     await message.reply(message.voice.duration)
     await message.reply(message.voice.file_size / 1024)

@dp.message_handler(content_types=ContentType.PHOTO)
async def photo_users(message: Message):
     photo = message.photo[3].file_id
     await message.answer_photo(photo)
     

@dp.message_handler(content_types=ContentType.STICKER)
async def sticker_users(message: Message):
     await message.reply(message)
     








        # await message.reply(message.text)

    # try:
    #     city = message.text
    #     info = weather(city)
    
    # except Exception:
    #     await message.reply("Не смогли найти город с таким названием!")


if __name__ == "__main__":
    try:
        print("Бот был запущен")
        executor.start_polling(dp, skip_updates=True)
    except (KeyboardInterrupt, SystemExit):
        pass

