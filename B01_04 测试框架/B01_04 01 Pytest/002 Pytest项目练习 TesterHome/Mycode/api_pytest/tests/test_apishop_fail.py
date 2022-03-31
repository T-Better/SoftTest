import requests


class TestinTheaters():
    def test_in_theaters(self):
        host = "https://api.apishop.net"

        path = "/common/joke/getJokesByRandom"

        params = {"apikey": "GJXZpTX599fb46a77353776bdf7f3e746405b472379e292", "pageSize": 20}

        headers = {
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
        }

        r = requests.get(url=host + path, headers=headers, params=params)

        response = r.json()
        assert response["statusCode"] == "100001"
        assert response["desc"] == "传递的apiKey非法或格式不正确"  # 将错就错，测反案例
