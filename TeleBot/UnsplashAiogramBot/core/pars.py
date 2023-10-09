from bs4 import BeautifulSoup
import requests

def get_html(get_URL, get_HEADER):
    responce = requests.get(url=get_URL, headers=get_HEADER)
    if responce.status_code == 200:
        return responce.text
    else:
        raise ValueError("Что то не так в (get_html)")
    
def proccesing(proccesing_url, proccesing_header):
    html = get_html(get_URL=proccesing_url, get_HEADER=proccesing_header)

    soup = BeautifulSoup(html , "lxml").find("div", {"class": "mItv1"}).find("div", {"class": "ripi6"}
            ).find_all("div", {"class":"MorZF"})
    
    all_src_image = []

    for item in soup:
        src = item.find("img").get("src")
        all_src_image.append(src)



    return all_src_image



