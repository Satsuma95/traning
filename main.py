import requests
from bs4 import BeautifulSoup
url = "https://www.worldometers.info/world-population/world-population-by-year/"
responce = requests.get(url)
if responce.status_code != 200:
    print("усё хорошо",responce)
    exit(1488)
Soup = BeautifulSoup(responce.text,"html.parser")
mainblock = Soup.find("div",class_="col-md-8")
tableblock = Soup.find("table",class_="table table-hover table-condensed")
tri = tableblock.find_all("tr")
print(tri)