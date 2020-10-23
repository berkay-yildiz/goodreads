import requests
from bs4 import BeautifulSoup
import html5lib

while True:

    x = input('WebAdress: ')
    r = requests.get(x)
    source = BeautifulSoup(r.content,"html5lib")

    links = source.find_all("a", attrs={"class":"bookTitle"})
    for link in links:
        print('https://www.goodreads.com'+link.get("href"))
