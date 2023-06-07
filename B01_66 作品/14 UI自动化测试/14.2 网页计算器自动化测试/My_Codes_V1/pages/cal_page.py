from basepage.common.basepage import BasePage
from selenium.webdriver.common.by import By


# 对象库层
class CalElement(BasePage):
    """
    封装各种元素对象：清屏、加、减、乘、除、等于
    """
    def clear_ele(self):
        """计算器清屏"""
        self.driver.find_element(By.ID,'simpleClearAllBtn')

    def add_ele(self):
        """计算 加"""
        self.driver.find_element(By.ID, 'simpleAdd')

    def subtract_ele(self):
        """计算 减"""
        self.driver.find_element(By.ID, 'simpleSubtr')

    def multiply_ele(self):
        """计算 乘"""
        self.driver.find_element(By.ID, 'simpleMulti')

    def devide_ele(self):
        """计算 除"""
        self.driver.find_element(By.ID, 'simpleDivi')

    def equal_ele(self):
        """计算 等于"""
        self.driver.find_element(By.ID, 'simpleEqual')

    def cal_result(self):
        """计算 结果"""
        self.driver.find_element(By.ID,'resultIpt')


if __name__ == "__main__":
    cal = CalElement()
    cal.subtract_ele()
    print("执行成功")









