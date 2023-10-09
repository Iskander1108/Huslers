from os import getenv
from dotenv import load_dotenv
import psycopg2

load_dotenv()


connection = psycopg2.connect(
    host = getenv("HOST"),
    database = getenv("DATABASE"),
    user = getenv("USER"),
    password = getenv("PASSWORD"),
    port = getenv("PORT"),
)

def create_table(): 
    with connection.cursor() as cursor:
        cursor.execute("CREATE TABLE IF NOT EXISTS users(\
        id SERIAL PRIMARY KEY,\
        user_id BIGINT,\
        username VARCHAR(45) DEFAULT NULL,\
        first_name VARCHAR(225) DEFAULT NULL,\
        last_name VARCHAR(225) DEFAULT NULL,\
        phone_id BIGINT DEFAULT NULL,\
        message_id BIGINT DEFAULT NULL,\
        location_id BIGINT DEFAULT NULL,\
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")


        cursor.execute("CREATE TABLE IF NOT EXISTS phone(\
        id SERIAL PRIMARY KEY,\
        user_id BIGINT,\
        number VARCHAR(250) DEFAULT NULL,\
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")


        cursor.execute("CREATE TABLE IF NOT EXISTS msg(\
        id SERIAL PRIMARY KEY,\
        user_id BIGINT,\
        message TEXT DEFAULT NULL,\
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")


        cursor.execute("CREATE TABLE IF NOT EXISTS user_location(\
        id SERIAL PRIMARY KEY,\
        user_id BIGINT,\
        location VARCHAR(255) DEFAULT NULL,\
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")


    connection.commit()


def InsertUserSTART(user_id, first_name, last_name, username):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO users(\
        user_id, first_name, last_name, username)\
        VALUES (%s, %s, %s, %s)",(user_id, first_name, last_name, username))


def RegistrPHONE(user_id, phone):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO phone(\
            user_id, number) VALUES(%s, %s)", (user_id, phone))
    connection.commit()
        
       
def RegistrLOCATION(user_id, location):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO user_location(\
            user_id, location) VALUES(%s, %s)", (user_id, location))
    connection.commit()
        

def RegistrMESSAGE(user_id, message_user):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO msg(\
            user_id, message) VALUES(%s, %s)", (user_id, message_user))
    connection.commit()

def ChekUserSTART(user_id):
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT user_id FROM\
            users WHERE user_id = {user_id}")
        
        check_user = cursor.fetchone()
        return check_user
        

def ChekUserPHONE(user_id):
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT user_id FROM\
            phone WHERE user_id = {user_id}")
        
        check_user = cursor.fetchone()
        return check_user
    

def ChekUserLOCATION(user_id):
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT user_id FROM\
            location WHERE user_id = {user_id}")
        
        check_user = cursor.fetchone()
        return check_user
        

def UserMesaageUpdate(user_id):
    with connection.cursor() as cursor:
        cursor.execute(f"select id from users where user_id = {user_id}")

        id = cursor.fetchone()[0]
        cursor.execute(f"update msg set id_msg = {id}\
            where user_id = {user_id}")


    connection.commit()


def UserPhoneUpdate(user_id):
    with connection.cursor() as cursor:
        cursor.execute(f"select id from users where user_id = {user_id}")

        id = cursor.fetchone()[0]
        cursor.execute(f"update phone set id_phone = {id}\
            where user_id = {user_id}")
        
    connection.commit()

        



        











