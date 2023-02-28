import requests
from bs4 import BeautifulSoup

def parse_sc(url):
    """
    请求 返回源码
    """
    try:
        r = requests.get(url)
        r.raise_for_status()
        return r.text
    except:
        return "请求失败"

def format_data(d):
    """
    将response格式化
    """
    soup = BeautifulSoup(d,'html.parser')
    sc = soup.prettify()
    return sc

if __name__ == "__main__":
    url = r'http://python123.io/ws/demo.html'
    data = parse_sc(url)
    sco = format_data(data)
    print(sco)