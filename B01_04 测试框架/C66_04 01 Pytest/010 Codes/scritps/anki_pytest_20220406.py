import pytest
import allure

@allure.title("成功登录，测试数据是{test_loginss}")
@pytest.mark.parametrize("test_loginss", [
    {"username": "name1", "pwd": "pwd1"},
    {"username": "name2", "pwd": "pwd2"}], indirect=True)
def test_success_login(test_loginss):
    name, pwd = test_loginss
    allure.attach(f"账号{name},密码{pwd}")

@allure.title("多个参数{name},{phone},{age}")
@pytest.mark.parametrize("name,phone,age", [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
])
def test_test_test(name, phone, age):
    print(name, phone, age)

# allure如何标记一下用例为normal级别缺陷？
@allure.severity('normal')
def test_case_1():
    """ normal 级别测试用例 """
    print("test case 11111111")

"""
类似@pytest.mark.xxx给不同的用例添加标记，如何用命令行方式
（类似pytest -v）只运行feature名为模块的测试用例
"""
# pytest --allure-feature=feature

"""
类似@pytest.mark.xxx给不同的用例添加标记，如何用命令行方式
（类似pytest -v）只运行epic名为test的测试用例
"""
# pytest --allure-epics=test

# pytest --allure-features=feature, --allure-stories = sotry

# pytest --clean-allure

