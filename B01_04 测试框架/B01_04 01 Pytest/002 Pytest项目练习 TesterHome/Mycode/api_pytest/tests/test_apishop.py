import requests


class TestinTheaters():
    def test_in_theaters(self):
        host = "https://api.apishop.net"
        apikey = "GJXZpTX599fb46a77353776bdf7f3e746405b472379e292"
        pageSize = 20

        # path = "/common/joke/getJokesByRandom"
        path = "/common/joke/getJokesByRandom?apiKey={}&pageSize={}".format(apikey,pageSize)

        params = {"apikey": "GJXZpTX599fb46a77353776bdf7f3e746405b472379e292", "pageSize": 20}

        headers = {
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
        }

        # r = requests.request("GET", url=host + path, headers=headers, params=params)
        r = requests.get(url=host+path, headers=headers, params=params)

        # r = requests.request("GET", url="https://api.apishop.net//common/joke/getJokesByRandom", headers=headers, params=params)
        print(r)
        response = r.json()
        assert response["statusCode"] == "000000"
        assert response["desc"] == "查询成功"


