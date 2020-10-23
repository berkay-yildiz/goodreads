import requests
from bs4 import BeautifulSoup as bs
import html5lib


x = input('WebAdress: ')
r = requests.get(x)
source = bs(r.content,"html5lib")

links = source.find_all("a", attrs={"class":"bookTitle"})

for n, link in enumerate(links, start=1):

    x_2 = 'https://www.goodreads.com'+link.get("href")
    r_2 = requests.get(x_2)

    source_2 = bs(r_2.content, "html5lib")
    genres = source_2.find_all("a", attrs={"class":"actionLinkLite bookPageGenreLink"})

    print("é"+ " " + str(n)+ " é " + " "+ str(x_2)+ " " + "é")

    for genre in genres:
        print(genre.text+ ",", end="")
