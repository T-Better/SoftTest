import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

pa1 = r'D:\Program Files\pagetest\注册A.html'
driver = webdriver.Chrome()
driver.get(pa1)
"""
e1 = driver.find_element(By.ID, 'alerta')
time.sleep(1)
e1.click()
alert = driver.switch_to.alert
at1 = alert.text
print(at1)
time.sleep(2)
alert.accept()
# alert.dismiss()
time.sleep(1)
"""

# 根据option属性 value值来定位
e2 = driver.find_element(By.ID, 'selectA')
select = Select(e2)
select.select_by_value('bj')

driver.close()

