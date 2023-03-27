import logging
import requests
from bs4 import BeautifulSoup
url = r'http://python123.io/ws/demo.html'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify)

