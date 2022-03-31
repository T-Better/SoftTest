import requests
from bs4 import BeautifulSoup

url1 = 'http://python123.io/ws/demo.html'

def parse_data(url):
    r = requests.get(url)
    return r.text

demo = parse_data(url1)
soup = BeautifulSoup(demo,'html.parser')  # 对demo解析，使用的解释器是html.parser解释器
print(soup.prettify())  # 格式化后输出