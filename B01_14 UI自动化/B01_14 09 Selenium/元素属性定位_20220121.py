"""
打开注册A.html页面，完成以下操作 
1).利用元素的属性信息精确定位用户名输入框，并输入：admin 
"""
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('D:\Program Files\pagetest\注册A.html')

s1 = driver.find_element_by_xpath('//p[1]/input[@id="userA"]').send_keys('admin')
# s1 = driver.find_element_by_xpath('//*[@placeholder="请输入用户名"]')

time.sleep(2)

driver.quit()
