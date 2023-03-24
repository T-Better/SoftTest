# web_弹出框处理_20220129.py  我的代码
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\注册A.html')
driver.find_element_by_id('alerta').click()
alert = driver.switch_to.alert  # 获取警告框文本
time.sleep(2)
print(alert.text)  # 打印警告框文本
time.sleep(2)
alert.accept()  # 接受警告框
# alert.dismiss()  # 取消警告框
time.sleep(2)

driver.close()