# 读取case 登录步骤
from selenium import webdriver
from common.ExcelUtil import *
from selenium.webdriver.common.by import By
import unittest
from ddt import ddt, data, unpack
import time

# 自己写起来难度2/4
class Case(object):
    def __init__(self):
        pass

    def get_case(self):
        """
        获取数据
        得到有用的数据，并且使数据以邮箱地址、密码、预期结果定位、预期结果的顺序返回
        """
        # 获取Excel中的文件数据
        excelname = "\data\casedata2.xlsx"
        sheet = "LoginTest02"
        file = ExcelUtil(excel_name = excelname, sheet_name=sheet)  # TODO  # 调用函数，执行excel读取
        data = file.get_data()# TODO  # 获取列表类型的数据

        # 得到所需要的数据的索引，然后根据索引获取相应顺序的数据 email_index password_index expected_element_index expected_index
        # data:[['用例编号', '标题', '邮箱地址', '密码', '预期结果定位', '预期结果'], ['login-001',...]]
        email_index = data[0].index('邮箱地址')
        password_index = data[0].index('密码')
        expected_element_index = data[0].index('预期结果定位')
        expected_index = data[0].index('预期结果')

        data_length = len(data)# TODO  # 计算data大列表中有几个小列表
        print(data_length)  # 测试代码
        all_case = []
        # 去除header行和其他无用的数据,只以列表返回email、password、expected_element、expected的每行列表
        for i in range(1, data_length):
            case = []
            case.append(data[i][email_index])
            case.append(data[i][password_index])
            case.append(data[i][expected_element_index])
            case.append(data[i][expected_index])
            all_case.append(case)
        return all_case

# i:自己写起来不难 0/4
class Login(object):
    def __init__(self, driver):
        self.driver = driver  # 初始化driver

    def login(self, email, password):
        """登录步骤"""
        # 邮箱地址、密码、单机登录按钮操作
        time.sleep(1)
        # 如果email不为None，则定位email_element并写入对应值 3行
        if email != None:
            email_element = self.driver.find_element(By.ID, 'ty-email')
            email_element.send_keys(email)
        time.sleep(1)

        # 如果password不为None，则定位password_element并写入对应值 3行
        if password != None:
            password_element = self.driver.find_element(By.ID,'ty-pwd')
            password_element.send_keys(password)
        time.sleep(1)

        # 定位登录按钮并且点击 2行
        login_btn = self.driver.find_element(By.CSS_SELECTOR,'[value="登  录"]')
        login_btn.click()

    def login_assert(self, assert_type, assert_message):
        """登录后的断言"""
        time.sleep(1)
        # 先判断网页中的assert_type与excel中预期结果匹配，如果匹配得上，进一步定位报错信息，与excel中预期结果进行匹配断言 11行 4个分支
        if assert_type == "email error":
            email_msg = self.driver.find_element(By.ID, 'ty-email-error').text
            print(email_msg)
            assert email_msg == assert_message
        elif assert_type == "password error":
            password_msg = self.driver.find_element(By.ID,'ty-pwd-error').text
            assert password_msg == assert_message
        elif assert_type in ["login success","login fail"]:
            login_msg = self.driver.switch_to.alert.text
            assert login_msg == assert_message
        else:
            print("输入的断言类型不正确")


@ddt
class TestLogin(unittest.TestCase):
    """测试登录"""
    def setUp(self):
        self.driver = webdriver.Firefox()  # 用哪个浏览器
        # url = "http://localhost:14842"
        url1 = r"D:\Program Files\projectHtml\chapter8\index.html"
        self.driver.implicitly_wait(20)  # 隐式等待20秒（只是找不到元素时才会等待，找到不等待）
        self.driver.maximize_window()  # 最大化浏览器
        self.driver.get(url=url1)  # 发起请求url1

    def tearDown(self):
        self.driver.quit()  # 退出浏览器

    case = Case().get_case()  # 获取list型测试用例[[1,2,3],[2,3,4]...]

    @data(*case)  # 数据驱动，数据是case获取到的list，test_login来读取，记得解包
    @unpack
    def test_login(self, email, password, assert_type, assert_message):
        login = Login(driver=self.driver)
        login.login(email=email, password=password)
        login.login_assert(assert_type=assert_type,assert_message = assert_message)

