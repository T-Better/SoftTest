import time
from selenium import webdriver
from selenium.webdriver.common.by import By

path1 = r'D:\Program Files\pagetest\注册A.html'
driver = webdriver.Chrome()
driver.get(path1)

driver.find_element(By.CSS_SELECTOR, '[id="alerta"]').click()
# driver.find_element_by_id('alerta').click()
driver.find_element(By.NAME, '')
alert = driver.switch_to.alert
t = alert.text
print(t)

alert.accept()
# alert.dismiss()
time.sleep(2)
driver.close()


