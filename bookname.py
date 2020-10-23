import requests
from bs4 import BeautifulSoup as bs
import html5lib
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:

    x = input("WebAdress: ")

    r = requests.get(x)

    source = bs(r.content,"html5lib")
    booknames = source.find_all("span", attrs={"role":"heading"})
    for bookname in booknames:
        print(bookname.text)
