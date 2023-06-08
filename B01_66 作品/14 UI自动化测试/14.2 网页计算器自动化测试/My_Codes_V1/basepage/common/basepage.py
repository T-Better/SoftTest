from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class BasePage():
    """
    基类 用作初始化 封装常用操作
    """

    def __init__(self):
        """
        初始化driver
        """
        self.driver = webdriver.Firefox()
        self.calurl = r'http://cal.apple886.com/'
        self.digit_btn = (By.ID, 'simple{}')
        self.open_page()

    def open_page(self):
        """打开计算页"""
        self.driver.implicitly_wait(10)
        self.driver.get(self.calurl)

    # def find_element(self, by,element):
    #     """重写find_element，加了个sleep"""
    #     sleep(1)
    #     self.find_element(by,element)

    # def locator(self,by,element):
    #     """
    #     元素定位
    #     """
    #     self.find_element(by,element)

    # def get_result(self):
    #     """
    #     获取屏幕输出结果
    #     """
    #     self.locator().text()

    def close_browser(self):
        """关闭浏览器"""
        self.driver.close()




