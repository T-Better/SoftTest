from selenium import webdriver
from selenium.webdriver.common.by import By
from config import *
from utils.singledriver import SingleDriver
from time import sleep


class MyDriver():
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(MyDriver, cls).__new__(cls, *args, **kwargs)
            cls.driver = webdriver.Firefox()
        return cls._instance


class BasePage(MyDriver):
    """
    基类 用作初始化 封装常用操作
    """

    def __init__(self):
        """
        初始化driver
        """
        # self.driver = SingleDriver().driver
        self.open_page(CALURL)
        self.digit_btn = (By.ID, 'simple{}')


    def open_page(self,calurl):
        """打开计算页"""
        self.driver.implicitly_wait(10)
        self.driver.get(calurl)
        self.driver.maximize_window()

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


if __name__ == "__main__":
    a = BasePage()
    b = BasePage()
