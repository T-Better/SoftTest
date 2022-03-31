# anki_框文本操作练习_20220130.py
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\注册A.html')
e1 = driver.find_element_by_id('alerta').click()

alert = driver.switch_to.alert  # 获取告警文本
time.sleep(2)

print(alert.text)  # 打印告警文本
time.sleep(2)

# alert.accept()  # 接受告警
alert.dismiss()  # 忽略告警
time.sleep(2)

driver.close()
