# anki_代开注册A页面输入用户密码_20220118.py
from selenium import webdriver
import time

# 实例化驱动
driver = webdriver.Chrome()

# 打开地址
driver.get('D:\Program Files\pagetest\注册A.html')

# 定位用户名并输入账号
driver.find_element_by_id('userA').send_keys('admin')

# 定位密码并输入密码
driver.find_element_by_id('passwordA').send_keys('123456')

time.sleep(3)

driver.quit()
