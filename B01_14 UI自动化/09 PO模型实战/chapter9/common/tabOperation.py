from time import sleep
from common.elementIsExist import ElementIsExist
from selenium.webdriver.common.by import By

class TabOperation(object):
    """
    获取所有tab，先定位到tab的父元素，然后在父元素下找各个tab
    """
    def __init__(self, driver):
        self.driver = driver
    def get_all_tabs(self):
        """获取所有的tabs"""
        sleep(1)

        # 获取所有的tab的父元素
        # 元素定位，我们默认取css定位
        fathers_tabs = ['.tab','.tabs']

        # 使用is_exist()方法判断父节点是否存在，如果不存在，则查找到tab不匹配
        father_exist = ElementIsExist(self.driver).is_exist(fathers_tabs[0])
        print(father_exist)
        # 父节点存在，则继续找子节点
        tabs = []
        if father_exist:
            father = self.driver.find_element(By.CSS_SELECTOR,fathers_tabs[1])
            tab = father.find_element(By.CSS_SELECTOR, fathers_tabs[1])
            tabs.append(tab)
            return tabs

    def switch_tab(self, tab_text):
        """
        切换tab
        tab_text:需要切换到的tab
        return:无返回 切换完即可
        """
        tabs = self.get_all_tabs()
        for tab in tabs:
            if tab.text == tab_text:  #
                tab.click()
                return

if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Firefox()
    f1 = r'D:\Program Files\projectHtml\chapter9\period4-1\index.html'
    driver.get(f1)
    sleep(2)
    tab = TabOperation(driver)
    tab.switch_tab('Tab2')
    driver.quit()






