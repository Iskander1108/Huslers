from os import system
from datetime import datetime
from random import randint

from aiogram import Bot
from aiogram.types import *
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher

from core.config import TOKEN
from core.inline import start_inline_keyboard
from core.keyboard import start_keyboard


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
system('clear')


@dp.message_handler(commands=['start'])
async def start_command(message:Message):
    await message.reply("Hello, World!", reply_markup=start_inline_keyboard)

    await message.answer("Выбери действие", reply_markup=start_keyboard)

    
@dp.message_handler(commands=['music'])
async def music_command(message: Message):
    with open("source/audio/audio.mp3","rb") as music:
        await message.reply_audio(audio=music)

@dp.message_handler(content_types=ContentTypes.TEXT)
async def text_user(message: Message):
    if message.text.lower() == "время":
        await message.reply(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))


    if message.text.lower() == "число":
        await message.reply(str(randint(0, 100)))


    if message.text.lower() == "info":
        try:
            get_photo = await message.from_user.get_profile_photos()
            print(get_photo)
            photo = get_photo["photos"][0][1].file_id

            caption = f"""
Имя: {message.from_user.first_name}
Фамилия: {message.from_user.last_name}
Пользовательское имя: @{message.from_user.username}
Идентификатор: {message.from_user.id}"""

            await message.reply_photo(photo,caption)
        except:
            await message.reply("В профиле нет фотографии")

    if message.text.lower() == "изображение":
        with open("source/image/img.jpg", "rb") as img:
                await message.reply_photo(img)




if __name__ == '__main__':
    try:
        executor.start_polling(dp, skip_updates=True)
    except (KeyboardInterrupt, SystemExit):
        pass
