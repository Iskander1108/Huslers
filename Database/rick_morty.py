import json 
from os import getenv, system

import psycopg2
import requests
from dotenv import load_dotenv

load_dotenv()
system("clear")

connection = psycopg2.connect(
host = getenv("HOST"),
database = getenv("DATABASE"),
user = getenv("USER"),
password = getenv("PASSWORD"),
port = getenv("PORT"),
)



def get_api(api):
    responce = requests.get(api)
    if responce.status_code == 200:
        return responce.json()
    else:
        raise ValueError("Error connecting to API")


# def run(id):

#     data = get_api(getenv("API_character") + id)
#     return data 

def insert_database(id):
    data = get_api(getenv("RICK_AND_MORTY_API_URL") + id)
    with connection.cursor() as cursor:
        cursor.execute("CREATE TABLE IF NOT EXISTS characters(\
            id SERIAL PRIMARY KEY,\
            name VARCHAR(90) DEFAULT NULL,\
            status VARCHAR(50) DEFAULT NULL,\
            species VARCHAR(125) DEFAULT NULL,\
            gender VARCHAR(50) DEFAULT NULL,\
            type VARCHAR(125) DEFAULT NULL,\
            origin_name VARCHAR(125) DEFAULT NULL,\
            location_name VARCHAR(125) DEFAULT NULL,\
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")

        cursor.execute("INSERT INTO characters(\
                       name, status, species, gender, type, origin_name, location_name)\
                       VALUES(%s, %s, %s, %s, %s, %s, %s)",( 
                            data["name"], data["status"], data["species"], data["gender"], data["type"],
                            data["origin"]["name"], data["location"]["name"]))
    connection.commit()    

for id in range(1,801):
    insert_database(str(id))
    print(f"Персонаж {id} записан!")



#     return f"""
# Имя персонажа: {data["name"]}
# Состаяние: {data["status"]}
# Расса: {data["species"]}
# Пол: {data["gender"]}
# Вид: {data["type"]}
# Произхождение: {data["origin"]["name"]}
# Место проживания: {data["location"]["name"]}

# Дата создание: {data["created"]}
# """