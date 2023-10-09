
def create_table(connection):
    with connection.cursor() as cursor:
        cursor.execute("CREATE TABLE IF NOT EXISTS users(\
        id SERIAL PRIMARY KEY,\
        user_id BIGINT,\
        username VARCHAR(45) DEFAULT NULL,\
        first_name VARCHAR(225) DEFAULT NULL,\
        last_name VARCHAR(225) DEFAULT NULL,\
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")

        cursor.execute("CREATE TABLE IF NOT EXISTS phone(\
        id SERIAL PRIMARY KEY,\
        user_id BIGINT,\
        number VARCHAR(250) DEFAULT NULL,\
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")

    connection.commit()


def CheckStart(connection, user_id):
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT user_id from users WHERE user_id = {user_id}")

        check_user = cursor.fetchone()
        return check_user
    
def RegisterUser(connection, user_id, first_name, last_name, username):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO users(user_id, first_name, last_name, username) VALUES(%s, %s, %s, %s)",
        (user_id, first_name, last_name, username))

    connection.commit()


def RegisterPHONE(connection, user_id, phone):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO phone(\
        user_id, number) VALUES(%s, %s)", (user_id, phone))

    connection.commit()

def CheckUserPHONE(connection, user_id):
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT user_id FROM phone WHERE user_id = {user_id}")

        check_user = cursor.fetchone()

        return check_user


def UserPhoneUpdate(connection, user_id):
    with connection.cursor() as cursor:
        cursor.execute(f"select id from users where user_id = {user_id}")
        id = cursor.fetchone()[0]

        cursor.execute(f"update phone set id_phone = {id} where user_id = {user_id}")

    connection.commit()