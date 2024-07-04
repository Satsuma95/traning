import requests
from bs4 import BeautifulSoup
url = "https://wallpaperscraft.ru/catalog/cars"
urlnew = "https://wallpaperscraft.ru"
responce = requests.get(url)
if responce.status_code != 200:
    print("усё хорошо",responce)
    exit(1488)
Soup = BeautifulSoup(responce.text,"html.parser")
mainblock = Soup.find("div",class_="content-main")
cars = Soup.find_all("li",class_="wallpapers__item")
for x in cars:
    url = urlnew+x.find("a",class_="wallpapers__link")["href"]
    responce2 = requests.get(url)
    if responce.status_code != 200:
        print("усё хорошо", responce)
        exit(1488)
    Soup = BeautifulSoup(responce2.text, "html.parser")
    reslution = Soup.find_all("div",class_="resolutions__table")
    print(reslution)
    break