"""
需求：打开注册A.html页面，完成以下操作
1).使用link_text定位(访问 新浪 网站)超链接，并点击
2).3秒后关闭浏览器窗口
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('D:\Program Files\pagetest\注册A.html')

driver.find_element(By.ID,'fw').click()
time.sleep(2)

driver.close()
