# anki_复习python_20220210.py
import requests


def parse(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        return r.text
    except:
        return "请求错误"


if __name__ == "__main__":
    url1 = "http://www.baidu.com"
    print(parse(url1))

