# 17. 08. 23


import requests
from os import getenv, system
from dotenv import load_dotenv
from pprint import pprint
import json

load_dotenv()
system("clear")

api = getenv("API")


def get_api(api):
    responce = requests.get(api)

    if responce.status_code == 200:
        return responce.json()
    else:
        raise ValueError("Error connecting to API")
    
        
def run():

    id = input("Введите id персонажа: ")
    try:

        if int(id) > 826:
            return "Нет такого персонажа"
    except ValueError:
        return "Разрешены только цифры"
    
    
    api_character = getenv("API_character") + id

    # with open("info.json", "wt") as file:
    #     json.dump(get_api(api_character),file, indent=4, ensure_ascii=False)

    data = get_api(api_character)

    img_url = data["image"]
    img_responce = requests.get(img_url)

    with open(f"image/{data['name']}.jpg", "wb") as file:
        file.write(img_responce.content)


    # json() = Ключи и значения
    # text = Текст
    # content = фотоб видео ,музыку


    return f"""
Имя персонажа: {data["name"]}
Состояние: {data["status"]}
Расса: {data["species"]}
Пол: {data["gender"]}
Вид: {data["type"]}
Происхождение: {data["origin"]["name"]}
Местоположение: {data["location"]["name"]}
Дата создания: {data["created"]}



"""
        

print(run())