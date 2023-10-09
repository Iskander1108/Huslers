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
    cursor.execute("select characters.name, company.role from characters inner join company ON characters.company_id = company.id where role = 'Директор по персоналу'" )
    all_role = cursor.fetchall()
    print(all_role)


for i in all_role:
    print(i[0])