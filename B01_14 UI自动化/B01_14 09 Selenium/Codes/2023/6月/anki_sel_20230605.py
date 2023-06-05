from selenium import webdriver
from selenium.webdriver.common.by import By
# TODO
import time

cdp = r'D:\Program Files\pagetest\注册A.html'
driver = webdriver.Chrome()
driver.get(cdp)

# 获取页面上第一个超链接的文本内容
e1 = driver.find_element(By.LINK_TEXT,'新浪')
e1.get_attribute('href')

# time.sleep(1)
driver.close()
