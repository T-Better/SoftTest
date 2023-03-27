import requests
from bs4 import BeautifulSoup

url1 = 'http://python123.io/ws/demo.html'

def parse_data(url):
    r = requests.get(url)
    return r.text

demo = parse_data(url1)
soup = BeautifulSoup(demo, 'html.parser')
print(soup.title)  # <title>This is a python demo page</title>
tag = soup.p  # p标签
# <a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>
print(tag)
print(tag.name, tag.attrs, tag.string)
