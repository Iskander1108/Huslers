from random import choice

import asyncio
import logging


from aiogram import Bot, Dispatcher, Router, types
from aiogram.types import *
from aiogram.enums import parse_mode
from aiogram.filters import CommandStart
from aiogram.utils.markdown import hbold

from core.pars import proccesing
from core.config import TOKEN, DOMAIN, URL, HEADERS


dp = Dispatcher()

@dp.message(CommandStart())
async def start_message(message: Message):
    await message.answer(f"Привет, {hbold(message.from_user.full_name)}!")

@dp.message()
async def echo_message(message: types.Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try")

@dp.message(ContentType.TEXT)
async def get_citaty(message:Message):
    data = proccesing(URL, HEADERS)
    citaty = choice(data)
    await message.answer(citaty["title"])

async def main():
    bot = Bot(TOKEN, parse_mode="HTML") 
    await dp.start_polling(bot)
    

if __name__ == "__main__":
        # logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())





# import asyncio
# from aiogram import Bot, Dispatcher, F
# from aiogram.types import *

# from core.config import TOKEN

# bot = Bot(TOKEN)
# dp = Dispatcher()

# @dp.message_handler(F.text == "/start")
# async def cmd_start(message: Message):
#     await message.reply(f"Привет")

# async def main():
#     await dp.start_polling(bot)

# if __name__ == "__main__":
#     asyncio.run(main())




# import asyncio
# from aiogram import Bot, Dispatcher, types
# from core.config import TOKEN


# bot = Bot(TOKEN)
# dp = Dispatcher()

# # Инициализируем бот в диспетчере
# dp.init_bot(bot)

# @dp.message_handler(commands=['start'])
# async def start(message: types.Message):
#     if message.text == '/start':
#         await message.reply('Привет!')
#     else:
#         await message.reply('Вы ввели команду /start')

# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     loop.create_task(dp.start_polling())
#     loop.run_forever()
