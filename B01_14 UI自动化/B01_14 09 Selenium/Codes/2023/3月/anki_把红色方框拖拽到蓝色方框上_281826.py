from selenium import webdriver
from selenium.webdriver.common.by import By
# TODO
from selenium.webdriver.common.action_chains import ActionChains
import time


cdp = r'D:\Program Files\pagetest\drag.html'
driver = webdriver.Chrome()
driver.get(cdp)

"""
rb = driver.find_element(By.ID,'div1')
bb = driver.find_element(By.ID,'div2')

action = ActionChains(driver)
action.drag_and_drop(rb,bb)
action.perform()
"""

# 双击鼠标左键
# action = ActionChains(driver)
# action.double_click().perform()

# 获取页面上第一个超链接的文本内容
e1 = driver.find_element(By.LINK_TEXT,'新浪')
e1.text


time.sleep(2)
driver.close()

