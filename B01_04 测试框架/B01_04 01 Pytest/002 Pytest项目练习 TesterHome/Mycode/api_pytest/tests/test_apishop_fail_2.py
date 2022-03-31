import requests
import yaml


def get_test_data(test_data_path):
    """
    用于读取test_apishop_fail.yaml内的数据（将测试代码和测试数据分离）
    """
    case = []  # 存储测试用例名称
    http = []  # 存储请求对象
    expected = []  # 存储预期结果
    with open(test_data_path) as f:
        dat = yaml.load(f.read(), Loader=yaml.SafeLoader)
        test = dat['tests']
        for td in test:
            case.append(td.get('case', ''))
            http.append(td.get('http', {}))
            expected.append(td.get('expected', {}))
    parameters = zip(case, http, expected)
    return case, parameters


cases, parameters = get_test_data("/Users/chunming.liu/learn/api_pytest/data/test_in_theaters.yaml")
list_params = list(parameters)


class TestInTheaters(object):
    def test_in_theaters(self):
        host = "http://api.douban.com"
        r = requests.request(list_params[0][1]["method"],
                             url=host + list_params[0][1]["path"],
                             headers=list_params[0][1]["headers"],
                             params=list_params[0][1]["params"])
        response = r.json()
        assert response["count"] == list_params[0][2]['response']["count"]
        assert response["start"] == list_params[0][2]['response']["start"]
        assert response["total"] == len(response["subjects"])


assert response["title"] == list_params[0][2]['response']["title"], "实际的标题是：{}".format(response["title"])
