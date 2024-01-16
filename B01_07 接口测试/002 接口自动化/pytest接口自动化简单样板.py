import pytest
import requests

# 定义fixture，用于设置测试环境
@pytest.fixture
def base_url():
    return "https://api.example.com"

# 测试获取用户信息的接口
def test_get_user_info(base_url):
    endpoint = "/user/123"
    url = base_url + endpoint

    # 发送GET请求
    response = requests.get(url)

    # 断言响应状态码为200
    assert response.status_code == 200

    # 断言返回的JSON数据中包含特定字段
    assert "user_id" in response.json()
    assert "username" in response.json()

# 测试创建用户的接口
def test_post_create_user(base_url):
    endpoint = "/user/create"
    url = base_url + endpoint

    # 准备POST请求的参数
    data = {
        "username": "new_user",
        "email": "new_user@example.com"
    }

    # 发送POST请求
    response = requests.post(url, json=data)

    # 断言响应状态码为201
    assert response.status_code == 201

    # 断言返回的JSON数据中包含特定字段
    assert "user_id" in response.json()
    assert response.json()["username"] == "new_user"