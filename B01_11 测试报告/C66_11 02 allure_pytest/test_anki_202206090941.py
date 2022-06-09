import pytest
import allure

@allure.title('成功登录，测试数据是：{test_loginss}')
@pytest.mark.parametrize("test_loginss", [
    {"username": "name1", "pwd": "pwd1"},
    {"username": "name2", "pwd": "pwd2"}], indirect=True)
def test_success_login(test_loginss):
    name, pwd = test_loginss
    allure.attach(f"账号{name},密码{pwd}")

@allure.title("多个参数{name}{phone}{age}")
@pytest.mark.parametrize("name,phone,age", [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
])
def test_test_test(name, phone, age):
    print(name, phone, age)


def attach_file_in_module_scope_fixture_with_finalizer(request):
    allure.attach('','',allure.attachment_type.TEXT)
    pass
@allure.feature("feature_2")
@allure.story("story_2")
def test_with_story_2_and_feature_2():
    pass

TEST_CASE_LINK = 'https://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637'
@allure.link(TEST_CASE_LINK,name='点我')
def test_with_name():
    pass
@allure.description("""这是一个装饰器说明，没有特别的用处""")
def test_description_from_decorator():
    """
    这是一个装饰器说明，没有特别的用处
    """
    assert 42 == int(6 * 7)

@allure.step("第一步")
def passing_step():
    with allure.step("step1:浏览商品"):
        pass
@allure.severity(allure.severity_level.TRIVIAL)
def test_with_trivial_severity():
    pass

@allure.severity("normal")
def test_case_5():
    """ 没标记 severity 的用例默认为 normal"""
    print("test case 5555555555")
