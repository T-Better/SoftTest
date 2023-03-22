# anki_id定位_20220125.py
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\注册A.html')
driver.find_element_by_id('userA').send_keys('admin')
driver.find_element_by_id('passwordA').send_keys('123456')
time.sleep(3)
driver.quit
