import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('D:\Program Files\pagetest\注册A.html')

driver.find_element(By.ID,'')
driver.find_element(By.XPATH, '')
driver.find_element(By.LINK_TEXT,'')
driver.find_element(By.NAME, '')
driver.find_element(By.TAG_NAME, '')
driver.find_element(By.CLASS_NAME, '')
driver.find_element(By.CSS_SELECTOR, '')


driver.find_element(By.ID, '#userA')
# 获取告警框的文字信息



