from bs4 import BeautifulSoup
import requests
# from config import URL, HEADERS
import json


def get_html(get_URL, get_HEADER):
    responce = requests.get(url=get_URL, headers=get_HEADER)
    if responce.status_code == 200:
        return responce.text
    else:
        raise ValueError("Что то не так в (get_html)")
    

def proccesing(html):

    soup = BeautifulSoup(html , "lxml")
    items = soup.find_all("div", {"class": "views-row"})

    data = []
    for i in items:
        d = i.find("div", {"class": "field-item even last"}).text.replace('\xa0', ' ').replace('\n', ' ')
        data.append({"title":d})

    return data

def run(URL, HEADERS):
    citaty = []
    for i in range(1, 50):
        html = get_html(URL + "?page=" + str(i),HEADERS)
        source = proccesing(html)
        citaty.extend(source)

    
        print(f"Страница {i} Готова !")
    with open("citaty_info.json", "a", encoding="UTF-8") as file:
        json.dump(citaty, file, indent=4, ensure_ascii=False)
    return citaty

# print(run())




# items = [
#     'sdjhfjsgdfhjjf j h jh цитата1 jhjhjhjh jhgjhgjh ',
#     'sdjhfjsgdfhjjf j h jh цитата2 jhjhjhjh jhgjhgjh ',
#     'sdjhfjsgdfhjjf j h jh цитата3 jhjhjhjh jhgjhgjh ',
#     'sdjhfjsgdfhjjf j h jh цитата4 jhjhjhjh jhgjhgjh ',
#     'sdjhfjsgdfhjjf j h jh цитата5 jhjhjhjh jhgjhgjh ',
#     'sdjhfjsgdfhjjf j h jh цитата6 jhjhjhjh jhgjhgjh ',
#     'sdjhfjsgdfhjjf j h jh цитата7 jhjhjhjh jhgjhgjh ',
#     'sdjhfjsgdfhjjf j h jh цитата8 jhjhjhjh jhgjhgjh ',
#     'sdjhfjsgdfhjjf j h jh цитата9 jhjhjhjh jhgjhgjh ',
#     'sdjhfjsgdfhjjf j h jh цитата10 jhjhjhjh jhgjhgjh ',
#     'sdjhfjsgdfhjjf j h jh цитата11 jhjhjhjh jhgjhgjh ',
#     'sdjhfjsgdfhjjf j h jh цитата12 jhjhjhjh jhgjhgjh ',
#     'sdjhfjsgdfhjjf j h jh цитата13 jhjhjhjh jhgjhgjh ',
# ]


# for i in items :
#     print (i.split()[-3])
