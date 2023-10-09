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
    all_items = soup.find("div", {"class": "tn-main-news-container tn-sub-container"}).find_all("div",{"class": "tn-main-news-item"})
    
    info = []
    for item in all_items:
        try:
            info.append({
                "title": str(item.find("span").text).replace("\u005c",""),
                "data" : str(item.find("ul", {"class": "tn-data-list"}).find("li").text).strip(),
                "image": DOMAIN + str(item.find("img").get("src")),
                "url": DOMAIN + str(item.find("a").get("href")),
            })
        except:
            continue
    return info

def run():
    html = get_html(URL, HEADERS)
    source = processing(html)

    with open("info.json", "w", encoding="UTF-8") as file:
        json.dump(source, file, indent=4, ensure_ascii=False)

    return source

print(run())