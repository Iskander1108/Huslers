import json
import requests                   # HTML  страница
from bs4 import BeautifulSoup     # Для обработки HTML
    



class Parser:
    def __init__(self, URL, DOMAIN):
        self.URL = URL
        self.DOMAIN = DOMAIN
        self.HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}

    def get_html(self):
        responce = requests.get(self.URL, headers=self.HEADERS)
        if responce.status_code == 200:
            return responce.text
        else:
            raise Exception("Страница не найдена")
        
    def __str__(self):
        return f"Класс Parser"
    
        
class Kaleso(Parser):  
    def __init__(self, URL, DOMAIN):
        super().__init__(URL, DOMAIN)
    
    def proccesing(self):
        html = self.get_html()
        soup = BeautifulSoup(html, "lxml").find("div", {"class": "a-list"}).find_all("div", {"class": "a-card js__a-card"})

        avto_list = []

        for item in soup:

            avto_img = item.find("div", {"class": "a-card__picture"}).find("picture").find("img").get("src")
            
            avto_info = item.find("div", {"class": "a-card__info"})

            avto_title = avto_info.find("div", {"class": "a-card__header"}).find("h5").text

            avto_price = avto_info.find("div", {"class": "a-card__header"}).find("span", {"class": "a-card__price"}).text

            avto_discription = avto_info.find("div", {"class": "a-card__body"}).find("div", {"class": "a-card__main"}).find("p").text

            avto_city = avto_info.find("div", {"class": "a-card__footer"}).find("div", {"class": "a-card__data"}).find("span", {"class": "a-card__param"}).text

            avto_data = avto_info.find("div", {"class": "a-card__footer"}).find("div", {"class": "a-card__data"}).find("span", {"class": "a-card__param a-card__param--date"}).text

            avto_list.append({
                "img": avto_img,
                "title": str(avto_title).strip(),
                "price": str(avto_price).strip(),
                "discription": str(avto_discription).strip(),
                "city": str(avto_city).strip(),
                "data": avto_data,
            })
        return avto_list
        

    def __str__(self):
        return f"Класс Kaleso domain = {self.DOMAIN}"
    
pars = []    
for num in range(2, 51):
    parser = Kaleso(f"https://kolesa.kz/cars/?page={num}", "https://kolesa.kz")
    source = parser.proccesing()
    print(f"Cтраница {num} завершена! ")
    pars.extend(source)

with open("avto.json", "w") as file:
    json.dump(pars, file, indent=4, ensure_ascii=False)
