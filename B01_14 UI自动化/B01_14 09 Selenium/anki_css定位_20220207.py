# anki_css定位_20220207.py
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\注册A.html')

# 1).使用CSS定位方式中id选择器定位用户名输入框，并输入：admin
driver.find_element_by_css_selector('[id="userA"]').send_keys('admin')
time.sleep(2)
# 2).使用CSS定位方式中属性选择器定位密码输入框，并输入：123456
driver.find_element_by_css_selector('[name="passwordA"]').send_keys('123456')
time.sleep(2)
# 3).使用CSS定位方式中class选择器定位电话号码输入框，并输入：18600000000
driver.find_element_by_css_selector('.telA').send_keys('18600000000')
time.sleep(2)
# 4).使用CSS定位方式中元素选择器定位注册按钮，并点击 

