"""
需求：打开注册A.html页面，完成以下操作
    1).利用元素的属性信息精确定位用户名输入框，并输入：admin
    两种方式以元素属性方式定位id='userA' 的账号 
"""

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\注册A.html')
driver.find_element_by_xpath('//p/input[@placeholder="请输入用户名"]').send_keys('admin')
driver.find_element_by_xpath('//*[@placeholder="请输入密码"]').send_keys('123456')
time.sleep(2)
driver.quit()
