# 定义一个工具类
from selenium import webdriver

class DriverUtil:
    """
    浏览器驱动工具类
    """
    _driver = None

    @ classmethod
    def get_driver(cls):
        """
        获取浏览器驱动对象，并完成初始化设置
        return:浏览器驱动对象
        """
        if cls._driver is None:
            cls._driver = webdriver.Chrome()
            cls._driver.maximize_window()
            cls._driver.implicitly_wait(10)
            cls._driver.get("http://cal.apple886.com/")
        return cls._driver

