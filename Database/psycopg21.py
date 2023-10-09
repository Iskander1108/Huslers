import json 
from os import getenv, system

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
    cursor.execute("select * from characters where id = 1")


    user_id = cursor.fetchone()
    print(user_id)

    cursor.execute(f"select * from company where id = {user_id[9]}")
    company_id = cursor.fetchone()
    print(company_id)



# После завершения работы с курсором его следует закрыть
# cursor.close()

# Если вы работаете с транзакциями 
# (например, если вы изменяете данные в базе данных), 
# после выполнения всех операций следует фиксировать транзакцию
# connection.commit()

# Если что-то пошло не так и вы хотите откатить все 
# изменения с момента последней фиксации, используйте
# connection.rollback()

# В конце работы с курсором необходимо закрыть 
# соединение с базой данных
# connection.close()

# fetchone(): Извлекает следующую строку результата в 
    # виде кортежа.

    # fetchall(): Извлекает все строки результата.

    # fetchmany(size=None): Извлекает список следующих 
    # size строк результата.