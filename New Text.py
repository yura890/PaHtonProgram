from wsgiref import headers
import requests
from bs4 import BeautifulSoup
 
q = input()
 
HEADERS = {
   "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
   "user-agent": " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
}
 
URL = 'https://www.google.com/search?q=' + q
 
def get_html(url):
   r = requests.get(url, headers=HEADERS).text
 
   return r
 
content = BeautifulSoup(get_html(URL), 'html.parser')
 
items = content.find_all('h3')
 
for item in items:
   print(item.get_text())