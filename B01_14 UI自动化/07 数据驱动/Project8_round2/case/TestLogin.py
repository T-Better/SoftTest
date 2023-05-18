# 读取case 登录步骤
from selenium import webdriver
from common.ExcelUtil import *
from selenium.webdriver.common.by import By
import unittest
from ddt import ddt, data, unpack
import time


class Case(object):
    def __init__(self):
        pass

    def get_case(self):
        """
        获取数据
        得到有用的数据，并且使数据以邮箱地址、密码、预期结果定位、预期结果的顺序返回
        """
        # 获取Excel中的文件数据
        sheet = "Login"
        file = ExcelUtil(sheet_name=sheet)
        data = file.get_data()

        # 得到所需要的数据的索引，然后根据索引获取相应顺序的数据
        # data:[['用例编号', '标题', '邮箱地址', '密码', '预期结果定位', '预期结果'], ['login-001',...]]
        email_index = data[0].index('邮箱地址')  # 返回字段位置
        password_index = data[0].index("密码")
        expected_element_index = data[0].index("预期结果定位")
        expected_index = data[0].index("预期结果")

        data_length = data.__len__()  # __len__:Return len(self)
        all_case = []
        # 去除header行，和其他无用的数据
        for i in range(1, data_length):
            case = []
            case.append(data[i][email_index])
            case.append(data[i][password_index])
            case.append(data[i][expected_element_index])
            case.append(data[i][expected_index])
            all_case.append(case)
        return all_case


class Login(object):
    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        """ 登录步骤 """
        # 邮箱地址、密码、单机登录按钮操作
        time.sleep(1)
        if email != None:
            email_element = self.driver.find_element(By.ID,'ty-email')
            email_element.send_keys(email)
        time.sleep(1)

        if password != None:
            password_element = self.driver.find_element(By.ID,'ty-pwd')
            password_element.send_keys(password)
        time.sleep(1)

        login_btn = self.driver.find_element(By.CSS_SELECTOR, 'input[value="登  录"]')
        login_btn.click()

    def login_assert(self, assert_type, assert_message):
        """ 登录后的断言 """
        time.sleep(1)
        if assert_type == 'email err':
            email_message = self.driver.find_element(By.ID,'ty-email-error').text
            assert email_message == assert_message
        elif assert_type == "password error":
            password_message = self.driver.find_element(By.ID, 'ty-pwd-error').text
            assert password_message == assert_message
        elif assert_type in ['login success', 'login fail']:
            login_message = self.driver.switch_to.alert.text
            assert login_message == assert_message
        else:
            print("输入的断言类型不正确")


@ddt
class TestLogin(unittest.TestCase):
    """ 测试登录 """
    def setUp(self):
        self.driver = webdriver.Firefox()
        # url = "http://localhost:14842"
        url1 = r"D:\Program Files\projectHtml\chapter8\index.html"
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get(url=url1)

    def tearDown(self):
        self.driver.quit()

    case = Case().get_case()

    @data(*case)
    @unpack
    def test_login(self, email, password, assert_type, assert_message):
        login = Login(driver=self.driver)
        login.login(email=email, password=password)
        login.login_assert(assert_type=assert_type,assert_message = assert_message)

