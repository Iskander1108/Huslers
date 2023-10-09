import json
from os import getenv, system
from random import randint, choice


import psycopg2
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

with connection.cursor() as cursor:
    for i in range(1,701):
        cursor.execute(f"update characters set company_id = {randint(1, 102)}\
                       where id = {i}")

connection.commit()