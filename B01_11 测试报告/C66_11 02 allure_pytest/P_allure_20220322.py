import os

import allure
import pytest


@pytest.fixture(scope="session")
def login_fixture():
    print("=== 前置登录 ===")


@allure.step("步骤1")
def step_1():
    print("操作步骤---------------1")


@allure.step("步骤2")
def step_2():
    print("操作步骤---------------2")


@allure.step("步骤3")
def step_3():
    print("操作步骤---------------3")


@allure.epic("epic 相当于总体描述")
@allure.feature("测试模块")
class TestAllureALL:

    @allure.testcase("https://www.cnblogs.com/poloyy/", '测试用例,点我一下')
    @allure.issue("https://www.cnblogs.com/poloyy/p/12219145.html", 'Bug 链接,点我一下')
    @allure.title("用例的标题")
    @allure.story("story one")
    @allure.severity("critical")
    def test_case_1(self, login_fixture):
        """
        小菠萝测试笔记地址：https://www.cnblogs.com/poloyy/
        """
        print("测试用例1")
        step_1()
        step_2()

    @allure.story("story two")
    def test_case_2(self, login_fixture):
        print("测试用例2")
        step_1()
        step_3()


@allure.epic("另一个 epic")
@allure.feature("查找模块")
class TestAllureALL2:
    @allure.story("story three")
    def test_case_3(self, login_fixture):
        print("测试用例3")
        step_1()

    @allure.story("story four")
    def test_case_4(self, login_fixture):
        print("测试用例4")
        step_3()


if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './allure'])
    os.system('allure -c ./allure')
    os.system('allure serve ./allure-report')
