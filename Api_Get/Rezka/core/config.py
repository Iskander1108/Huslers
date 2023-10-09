from dotenv import load_dotenv
load_dotenv()

from os import getenv

DOMAIN = getenv("DOMAIN")
URL = getenv("URL")
HEADERS = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaBrowser/23.5.1.667 Yowser/2.5 Safari/537.36"}