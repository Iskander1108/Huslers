from dotenv import load_dotenv
from os import getenv
load_dotenv()

    

# Для подключения к боту (API)
TOKEN = getenv("TOKEN")
ADMIN_ID = getenv("ADMIN_ID")

# Ссылка от куда мы будем парсить 
URL = getenv("URL")

# Имя сайта 
DOMAIN = getenv("DOMAIN")

#Заполнения для подключения к Базе данных (Psql)
HOST = getenv("HOST")
DATABASE = getenv("DATABASE")
USER = getenv("USER")
PASSWORD = getenv("PASSWORD")
PORT = getenv("PORT")

HEADERS = {
    "user-agent": "Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
}