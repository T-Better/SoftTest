import os
from time import sleep
from selenium import webdriver


class BasePage(object):
    """基础页面"""

    def __init__(self, driver=None, base_url = None):
        """
        基础的参数，driver、默认访问的url
        base_url:默认打开的url，一般都是登录页面
        """
        if driver is None:
            current_path = os.path.abspath(os.path.dirname(__file__))
            # driver_path = current_path + '/../../drivers/chromedriver.exe'
            # self.driver = webdriver.Chrome(driver_path)
            self.driver = webdriver.Firefox()
        else:
            self.driver = driver

        if base_url is None:
            self.base_url = 'http://localhost:18908/#/'
        else:
            self.base_url = base_url

        # 设置默认打开的页面
        self.open_page()

    def open_page(self):
        """打开默认页面"""
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.base_url)
        sleep(1)

    def close_page(self):
        """关闭页面"""
        return self.driver.close()

    def quit_driver(self):
        """关闭页面且退出程序"""
        return self.driver.quit()

    def find_element(self, by, element):
        """
        返回单个定位元素
        by:定位方法
        element：定位元素
        """
        sleep(1)
        return self.driver.find_element(by,element)

    def find_elements(self,by,element):
        """返回一组定位元素"""
        sleep(1)
        return self.driver.find_element(by, element)

    def switch_alert(self):
        """返回弹窗页面"""
        sleep(1)
        return self.driver.switch_to.alert

