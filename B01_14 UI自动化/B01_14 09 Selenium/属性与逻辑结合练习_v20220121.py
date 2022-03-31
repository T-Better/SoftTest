"""
需求：打开注册A.html页面，完成以下操作 
1).使用属性与逻辑结合定位策略，在test1对应的输入框里输入：admin 
"""
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('D:\Program Files\pagetest\注册A.html')

e1 = driver.find_element_by_xpath('//*[@name=\'userA\' and @id=\'userA\' and @placeholder="请输入用户名"]').send_keys('admin')

time.sleep(2)

driver.quit()
