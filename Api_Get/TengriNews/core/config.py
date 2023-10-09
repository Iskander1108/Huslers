from os import getenv
from dotenv import load_dotenv
load_dotenv()

URL = getenv("URL")
DOMAIN = getenv("DOMAIN")

HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}