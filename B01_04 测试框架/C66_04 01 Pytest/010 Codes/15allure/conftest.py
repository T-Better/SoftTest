# 对15allure下所有测试案例进行setup和teardown
import pytest


@pytest.fixture(scope="session")
def login():
    print("===登录功能，返回账户，token===")
    name = "testyy"
    token = "npoi213bn4"
    yield name, token
    print("===退出登录！！！===")

