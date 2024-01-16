import unittest
import requests

class APITestCase(unittest.TestCase):

    def setUp(self):
        # 在每个测试用例执行前的准备工作
        self.base_url = "https://api.example.com"

    def test_get_user_info(self):
        # 测试获取用户信息的接口
        endpoint = "/user/123"
        url = self.base_url + endpoint

        # 发送GET请求
        response = requests.get(url)

        # 断言响应状态码为200
        self.assertEqual(response.status_code, 200)

        # 断言返回的JSON数据中包含特定字段
        self.assertIn("user_id", response.json())
        self.assertIn("username", response.json())

    def test_post_create_user(self):
        # 测试创建用户的接口
        endpoint = "/user/create"
        url = self.base_url + endpoint

        # 准备POST请求的参数
        data = {
            "username": "new_user",
            "email": "new_user@example.com"
        }

        # 发送POST请求
        response = requests.post(url, json=data)

        # 断言响应状态码为201
        self.assertEqual(response.status_code, 201)

        # 断言返回的JSON数据中包含特定字段
        self.assertIn("user_id", response.json())
        self.assertEqual(response.json()["username"], "new_user")

    def tearDown(self):
        # 在每个测试用例执行后的清理工作
        pass

if __name__ == '__main__':
    unittest.main()