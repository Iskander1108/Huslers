import requests
from bs4 import BeautifulSoup


def get_html(url, HEADERS):
    r = requests.get(url, headers=HEADERS)
    if r.status_code == 200:
        return r.text
    else:
        raise Exception("Error while getting html")

def progressing(html):
    soup = BeautifulSoup(html, "lxml").find("div", {"class":"col-md-12"}).find("div", {"class":"blockquote-classic"}).find("p")

    kz = soup.find_all("span")[0].get_text(strip=True)
    sum = soup.find_all("span")[1].get_text(strip=True)
    data= soup.find("time").get_text(strip=True)

    return [kz, sum, data]

def run(HEADERS, url, currency, summa):
    
    html = get_html(url + currency + "/" + summa, HEADERS)
    src = progressing(html)
    
    return f"{src[0]} kzt = {src[1]} {currency} по курсу на {src[2]}"


