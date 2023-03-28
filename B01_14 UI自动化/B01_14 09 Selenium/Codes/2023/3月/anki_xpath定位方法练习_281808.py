from selenium import webdriver
from selenium.webdriver.common.by import By
import time


cdp = r'D:\Program Files\pagetest\注册A.html'
driver = webdriver.Chrome()
driver.get(cdp)

"""
# 1).使用绝对路径定位用户名输入框，并输入：admin
driver.find_element(By.XPATH, '//div/fieldset/form/p/input [@id="userA"]').send('admin')
# 2).暂停2秒
time.sleep(2)
# 3).使用相对路径定位用户名输入框，并输入：123
driver.find_element(By.XPATH, '//p/input [@id="userA"]')
# 4）暂停2秒后退出
"""

e2 = driver.find_element(By.ID,'alerta')
# 点击alert
e2.click()
# 获取并打印警告框文本
alert = driver.switch_to.alert
print(alert)
time.sleep(1)

# 接受或忽略警告框
alert.accept()

time.sleep(1)
#忽略警告框
# alert.dismiss()
# time.sleep(1)

driver.close()
