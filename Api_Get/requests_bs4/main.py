from dotenv import load_dotenv
load_dotenv()

import requests
from os import getenv, system
from bs4 import BeautifulSoup

system("clear")
url = getenv("URL")
user_agent = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}

responce = requests.get(url, headers=user_agent)

data = responce.text

src = BeautifulSoup(data, "lxml").find("div", {"id": "dle-content"}).find_all("h2")

for i in src:
    print(i.text)
# print(src)

# print(data)

# with open("index.html", "w", encoding="utf-8") as file:
#     file.write(data)


