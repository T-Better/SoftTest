"""
练习
需求：打开注册A.html页面，完成以下操作 
1).使用绝对路径定位用户名输入框，并输入：admin 
2).暂停2秒 
3).使用相对路径定位用户名输入框，并输入：123 
"""
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('D:\Program Files\pagetest\注册A.html')

e_username = driver.find_element_by_xpath('//form/p[1]/input').send_keys('admin')
time.sleep(2)

e_psw = driver.find_element_by_xpath('//form/p[2]/input').send_keys('123')
time.sleep(3)

driver.quit()
