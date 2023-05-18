from selenium import webdriver
from selenium.webdriver.common.by import By


cdp = r'D:\Program Files\pagetest\注册A.html'
driver = webdriver.Chrome()
driver.get(cdp)
e1 = '' # 定位复选框
# 判断页面中'旅游'对应的复选框是否为选中的状态
e1.is_selected()

driver.close()
