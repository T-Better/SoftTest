# css_元素属性_20220128.py
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\注册A.html')
driver.find_element_by_xpath('//p/input[@placeholder="请输入用户名"]').send_keys('admin')
driver.find_element_by_xpath('//*[@placeholder="请输入密码"]').send_keys('123456')
time.sleep(2)
driver.close()
