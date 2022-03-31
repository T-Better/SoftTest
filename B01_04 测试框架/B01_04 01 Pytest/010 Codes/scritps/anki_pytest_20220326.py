import pytest
import allure

@allure.title('成功登录，测试数据是：{test_loginss}')
@pytest.mark.parametrize("test_loginss", [
    {"username": "name1", "pwd": "pwd1"},
    {"username": "name2", "pwd": "pwd2"}], indirect=True)
def test_success_login(test_loginss):
    name, pwd = test_loginss
    allure.attach(f"账号{name},密码{pwd}")

@allure.title('多个参数{name},{phone},{age}')
@pytest.mark.parametrize("name,phone,age", [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
])
def test_test_test(name, phone, age):
    print(name, phone, age)

@allure.severity(allure.severity_level.TRIVIAL)
def test_with_trivial_severity():
    pass

@allure.severity('TRIVIAL')
def test_case_5():
    """ 没标记 severity 的用例默认为 normal"""
    print("test case 5555555555")

@allure.link('https://www.baidu.com',name='惦记我看一看百度吧')
def test_with_name():
    pass




