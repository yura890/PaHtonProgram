import requests
from bs4 import BeautifulSoup

URL = 'https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'


def get_html(url):
    r = requests.get(url).text
    return r


content = BeautifulSoup(get_html(URL), 'html.parser')
title = content.find_all('li')
print(title)