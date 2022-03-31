import requests


class TestInTheaters(object):
    def test_in_theaters(self):
        host = "http://api.douban.com"
        path = "/v2/movie/in_theaters"
        params = {"apikey": "0df993c66c0c636e29ecbb5344252a4a",
          "start": 0,
          "count": 10
          }
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
                }
        r = requests.request("GET", url=host + path, headers=headers, params=params)
        response = r.json()
        assert response["count"] == params["count"]
        assert response["start"] == params["start"]
        assert response["title"] == "正在上映的电影-上海", "实际的标题是：{}".format(response["title"])
