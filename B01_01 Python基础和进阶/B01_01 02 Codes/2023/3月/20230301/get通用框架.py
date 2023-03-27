import requests

def parse(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        return r.text
    except Exception as res:
        print(res)
        return "请求失败"

if __name__ == "__main__":
    url = ''
    print(parse(url))



