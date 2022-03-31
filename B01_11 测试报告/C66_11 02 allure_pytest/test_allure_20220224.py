import pytest
import allure


# 作者：上海-悠悠 qq交流群：874033608@pytest.fixture(scope="session")
def login_fixture():
    print("前置条件：登录")


@allure.step("步骤1")
def step_1():
    print("操作步骤---------------1")


@allure.step("步骤2")
def step_2():
    print("操作步骤---------------2")


@allure.step("步骤3")
def step_3():
    print("操作步骤---------------3")


@allure.epic("epic对大Story的一个描述性标签")
@allure.feature("测试模块")
class TestDemoAllure():
    @allure.testcase("http://49.235.x.x:8080/zentao/testcase-view-6-1.html")
    @allure.issue("http://49.235.x.x:8080/zentao/bug-view-1.html")
    @allure.title("用例的标题")
    @allure.story("用户故事：1")
    @allure.severity("critical")
    def test_case_1(self, login_fixture):
        '''case description:作者：上海-悠悠 qq交流群：874033608
        1.点文章分类导航标签 -跳转编辑页面
        2.编辑页面输入，分类名称，如:上海-悠悠-可以输入
        3.点保存按钮保存成功
        '''
        step_1()
        step_2()

    @allure.story("用户故事：2")
    def test_case_2(self, login_fixture):
        print("测试用例1")
        step_1()
        step_3()


@allure.epic("epic对大Story的一个描述性标签")
@allure.feature("模块2")
class TestDemo2():
    @allure.story("用户故事：3")
    def test_case_3(self, login_fixture):
        print("测试用例1")
        step_1()

    @allure.story("用户故事：4")
    def test_case_4(self, login_fixture):
        print("测试用例1")
        step_3()
