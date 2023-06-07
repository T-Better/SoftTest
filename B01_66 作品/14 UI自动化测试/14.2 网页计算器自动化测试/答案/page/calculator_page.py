from ..utils import DriverUtil
from selenium.webdriver.common.by import By

class CalculatorPage:
    """
    计算器页面-对象库层
    """
    def __init__(self):
        self.driver = DriverUtil.get_driver()
        # 数字按钮
        self.digit_btn = (By.ID, "simple{}")
        # 加法按钮
        self.add_btn = (By.ID, "simpleAdd")
        # 等号按钮
        self.eq_btn = (By.ID, "simpleEqual")
        # 计算结果
        self.result = (By.ID, "resultIpt")

    def find_digit_btn(self,digit):
        """
        定位数字按钮
        """
        location = (self.digit_btn[0],self.digit_btn[1].format(digit))
        return self.driver.find_element(*location)

    def find_add_btn(self):
        """
        定位加法按钮
        """
        return self.driver.find_element(*self.add_btn)

    def find_eq_btn(self):
        return self.driver.find_element(*self.eq_btn)

    def find_result(self):
        return self.driver.find_element(*self.result)


class CalculatorHandler:
    """
    计算器页面-操作层
    """
    def __int__(self):
        self.calculator_pamge = CalculatorPage()
    def click_digit_btn(self,digit):
        self.calculator_page.find_digit_btn(digit).click()
    def click_add_btn(self):
        self.calculator_page.find_add_btn().click()
    def click_eq_btn(self):
        self.calculator_page.find_eq_btn().click()
    def get_result(self):
        return self.calculator_page.find_result_btn().get_attribute('value')

    def input_numbers(self, numbers):
        for num in numbers:
            self.click_digit_btn(num)

class CalculatorProxy:
    """
    计算器页面-业务层
    """
    def __init__(self):
        self.calculator_handler = CalculatorHandler()

    def add(self, num1, num2):
        self.calculator_handler.input_numbers(str(num1))
        self.calculator_handler.click_add_btn()
        self.calculator_handler.input_number(str(num2))
        self.calculator_handler.click_eq_btn()
    def get_result(self):
        return self.calculator_handler.get_result()






