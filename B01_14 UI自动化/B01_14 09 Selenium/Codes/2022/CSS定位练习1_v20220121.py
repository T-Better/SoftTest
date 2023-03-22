"""
需求：打开注册A.html页面，完成以下操作 
1).使用CSS定位方式中id选择器定位用户名输入框，并输入：admin 
2).使用CSS定位方式中属性选择器定位密码输入框，并输入：123456 
3).使用CSS定位方式中class选择器定位电话号码输入框，并输入：18600000000 
4).使用CSS定位方式中元素选择器定位注册按钮，并点击 
"""
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('D:\Program Files\pagetest\注册A.html')

e1 = driver.find_element_by_css_selector("#userA").send_keys('admin')

e2 = driver.find_element_by_css_selector('passwordA').send_keys('123456')

e3 = driver.find_element_by_css_selector('.telA').send_keys('18600000000')

e3 = driver.find_element_by_css_selector('button').click()

time.sleep(2)

driver.quit()
