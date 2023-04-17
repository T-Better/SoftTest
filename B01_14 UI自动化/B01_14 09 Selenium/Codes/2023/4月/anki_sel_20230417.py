
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

cdp = r'D:\Program Files\pagetest\注册A.html'
driver = webdriver.Chrome()
driver.get(cdp)

# 获取页面上第一个超链接的文本内容
e1 = driver.find_element(By.LINK_TEXT,'新浪')
print(e1.text)

# 获取页面上第一个超链接的地址
e1.get_attribute('href')

# 判断页面中'旅游'对应的复选框是否为选中的状态
e1.is_selected()

# time.sleep(1)
driver.close()












