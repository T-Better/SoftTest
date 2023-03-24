# from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\注册A.html')
driver.find_element(By.ID,'alerta').click()
alert = driver.switch_to.alert
time.sleep(2)
alert.accept()
# alert.dismiss()
# option = webdriver.ChromeOptions()
# option.binary_location = r''

driver.close()
