import json
import requests
from bs4 import BeautifulSoup

from core.config import DOMAIN, URL, HEADERS


def get_html(URL, HEADERS):
    responce = requests.get(URL, headers=HEADERS)
    if responce.status_code == 200:
        return responce.text
    else:
        raise ValueError("Error connection", responce.status_code)


def processing(html):
    soup = BeautifulSoup(html, "lxml")
    all_kino = soup.find("div", {"class": "b-content__inline_items"}).find_all("div",{"class":"b-content__inline_item"})

    rez =[]

    for kino in all_kino:
        kino_url = kino.get("data-url")
        kino_title = kino.find("div", {"class" : "b-content__inline_item-link"}).find("a").text
        kino_info = str(kino.find("div", {"class" : "b-content__inline_item-link"}).find("div").text).split(",")
        kino_img = kino.find("div", {"class":"b-content__inline_item-cover"}).find("a").find("img").get("src")

        rez.append({
            "title": kino_title,
            "info": kino_info,
            "img": kino_img,
            "url": kino_url,
              })
    
    return rez


def run():
    for i in range(1, 501):
        
        html = get_html(URL + str(i) , HEADERS)
        source = processing(html)

        with open("rezka_open.json", "w", encoding="UTF=8") as file:
            json.dump(source, file, indent=4, ensure_ascii=False)
            
    print(f"Страница {i} готово!")


run()