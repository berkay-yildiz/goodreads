import requests
from bs4 import BeautifulSoup
import html5lib

while True :

    x = input("WebAdress: ")
    r = requests.get(x, "html5lib")
    source = BeautifulSoup(r.content, "html5lib")
    authors = source.find_all("a", attrs={"class":"authorName"})
    for author in authors:
        print(author.text)
