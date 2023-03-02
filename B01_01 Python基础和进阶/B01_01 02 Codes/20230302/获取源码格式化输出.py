import requests
from bs4 import BeautifulSoup

def parse(url):
    r = requests.get(url)
    r.raise_for_status()
    return r.text

def fc(c):
    """
    格式化源码
    """
    soupc = BeautifulSoup(c, 'html.parser')
    sc = soupc.prettify()
    return sc

if __name__ == "__main__":
    url = r'http://python123.io/ws/demo.html'
    c = parse(url)
    sc = fc(c)
    # with open('demo.txt', mode = 'w') as f：
    #     pass





