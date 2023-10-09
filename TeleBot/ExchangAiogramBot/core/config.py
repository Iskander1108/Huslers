from dotenv import load_dotenv
load_dotenv()

from os import getenv

URL = getenv("URL")
ADMIN_ID = getenv("ADMIN_ID")
PUSH_ADMIN_ID = getenv("PUSH_ADMIN_ID")
TOKEN = getenv("TOKEN")


HEADERS = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36"
}