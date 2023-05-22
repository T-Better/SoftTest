# 在封装常用结构时，需要判断某些元素是否存在，所以我们先要封装一个方法来判断元素是否存在，类似于is_displayed()方法
from selenium import webdriver
from selenium.webdriver.common.by import By

class ElementIsExist(object):
    def __init__(self,driver):
        # driver也是传进来的，这样就方面更换浏览器了
        self.driver = driver  # driver初始化

    def is_exist(self,element):
        """
        判断元素是否存在，存在返回True,不存在返回False
        :element:被判断是否存在的那个元素
        因为可能找不到而报错，所以要用捕获异常
        :return: True/False
        """
        flag = True
        try:
            self.driver.find_element(By.CSS_SELECTOR,element)  #
            return flag
        except:
            flag = False
            return flag








