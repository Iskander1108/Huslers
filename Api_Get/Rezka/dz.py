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
    all_kino = soup.find("div", {"class": "b-content__inline_sidebar"}).find_all("div",{"class":"b-seriesupdate__block"})
    

    rez =[]

    for data in all_kino:
        data_title = data.find("div", {"class" : "b-seriesupdate__block_date"}).text


        rez.append(data_title)

    return rez
        

def run():
    html = get_html(URL, HEADERS)
    source = processing(html)

    with open("dz.json", "w", encoding="UTF=8") as file:
        json.dump(source, file, indent=4, ensure_ascii=False)
    return source


print(run())