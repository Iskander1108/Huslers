from random import choice

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.types import *
from aiogram.utils import executor


from core.config import TOKEN, URL, HEADERS, ADMIN_ID
from core.Exchange import run
from core.keyboard import exchange_buttons, register_user, menu, crypto_buttons
from core.bin_sticker import S002
from core.Database import (
    create_table, RegistrPHONE, 
     RegistrLOCATION, RegistrMESSAGE,
     InsertUserSTART, ChekUserSTART,
     ChekUserPHONE, UserMesaageUpdate,
     UserPhoneUpdate)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# users = {
#     123123123: {
#         "first": "Ivan",
#         "last_name": "Ivanov",
#         "username": "ivanivaniv",
#         "phone_nuber": "+71234567890"
#     }
# }


@dp.message_handler(commands=["start"])
async def start(message: Message):
    create_table()
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username

    if ChekUserSTART(user_id) is None:
        InsertUserSTART(user_id, first_name, last_name, username)
    else:
        pass
    
    await message.answer("Привет я курс валют",reply_markup=register_user)


@dp.message_handler(content_types=ContentTypes.CONTACT)
async def contact(message: Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    phone_number = message.contact.phone_number
    UserPhoneUpdate(message.from_user.id)
    
    if ChekUserPHONE(user_id) is None:
        RegistrPHONE(user_id, phone_number) 
        
        info = f"""ID: {user_id}
Username: @{username}
First_name: {first_name}
Last_name: {last_name}
Phone_namber: {phone_number}"""


        await bot.send_message(ADMIN_ID, info)

        await message.answer("Вы успешно зарегистрированы!", reply_markup=menu)
    else:
        await message.answer("Вы уже у нас были зарегистрированы!", reply_markup=menu)



@dp.message_handler(content_types=ContentTypes.STICKER)
async def sticker (message: Message):
    if ChekUserPHONE(message.from_user.id) is not None:
        # await message.answer(message.from_user.id)

        await message.answer(message.sticker.file_id)

    else:
        await message.answer("Вы не Зарегестрированы! ")
        



key = None

@dp.message_handler(content_types=ContentTypes.TEXT)
async def exchange(message: Message):
    await message.answer_sticker(choice(S002))

    RegistrMESSAGE(message.from_user.id, message.text)
    UserMesaageUpdate(message.from_user.id)

    if ChekUserPHONE(message.from_user.id) is not None :
        global key

        currency = {
            "euro":"eur",
            "dollar":"usd",
            "ruble":"rub",
            "pound":"gbp",
            "yen":"cny",
            "som":"kgs",
            "india":"inr",
            "Bitcoin": "btc",
            "DOGE": "doge",
            "Ethereum": "eth",
            "Primecoin": "xpm",
            "Peercoin": "ppc",


        }
        if message.text.isdigit():
            if key is not None:
                src = run(HEADERS,URL, key, message.text)
                await message.answer(src)
            else:
                await message.answer("Выберите валюту") 

        elif message.text.upper() == "МЕНЮ":
            await message.answer("Вы в меню", reply_markup=menu)

        elif message.text.upper() == "КРИПТА":
            await message.answer("Вы в крипте", reply_markup=crypto_buttons)

        elif message.text.upper() == "ВАЛЮТА":
            await message.answer("Вы в валюте", reply_markup=exchange_buttons)


        elif message.text.upper() == "EURO":
            key = currency["euro"]
            await message.answer(f"Вы выбрали валюту {currency['euro']} \n Теперь введите сумму")

        elif message.text.upper() == "DOLLAR":
            key = currency["dollar"]
            await message.answer(f"Вы выбрали валюту {currency['dollar']} \n Теперь введите сумму")

        elif message.text.upper() == "RUBLE":
            key = currency["ruble"]
            await message.answer(f"Вы выбрали валюту {currency['ruble']} \n Теперь введите сумму")

        elif message.text.upper() == "POUND":
            key = currency["pound"]
            await message.answer(f"Вы выбрали валюту {currency['pound']} \n Теперь введите сумму")

        elif message.text.upper() == "YEN":
            key = currency["yen"]
            await message.answer(f"Вы выбрали валюту {currency['yen']} \n Теперь введите сумму")

        elif message.text.upper() == "SOM":
            key = currency["som"]
            await message.answer(f"Вы выбрали валюту {currency['som']}\n Теперь введите сумму")
            
        elif message.text.upper() == "INDIA":
            key = currency["india"]
            await message.answer(f"Вы выбрали валюту {currency['india']}\n Теперь введите сумму")

        elif message.text.upper() == "BITCOIN":
            key = currency["Bitcoin"]
            await message.answer(f"Вы выбрали криптовалюту {currency['Bitcoin']}\n Теперь введите сумму")

        elif message.text.upper() == "DOGE":
            key = currency["DOGE"]
            await message.answer(f"Вы выбрали криптовалюту {currency['DOGE']}\n Теперь введите сумму")

        elif message.text.upper() == "ETHEREUM":
            key = currency["Ethereum"]
            await message.answer(f"Вы выбрали криптовалюту {currency['Ethereum']}\n Теперь введите сумму")

        elif message.text.upper() == "PRIMECOIN":
            key = currency["Primecoin"]
            await message.answer(f"Вы выбрали криптовалюту {currency['Primecoin']}\n Теперь введите сумму")

        elif message.text.upper() == "PEERCOIN":
            key = currency["Peercoin"]
            await message.answer(f"Вы выбрали криптовалюту {currency['Peercoin']}\n Теперь введите сумму")
            
        else:
            await message.answer("Убедитесь что ввели целые числа!")
    else:
        await message.answer("Вы не зарегестрированы!")


if __name__ == "__main__":
    try:
        executor.start_polling(dp, skip_updates=True)  
    except (KeyboardInterrupt, SystemExit):
       pass
 