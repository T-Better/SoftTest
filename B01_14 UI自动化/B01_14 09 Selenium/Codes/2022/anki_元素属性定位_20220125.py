# anki_元素属性定位_20220125.py
from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\注册A.html')
driver.find_element_by_xpath("//p[1]/input[@id='userA']").send_keys('admin')
driver.find_element_by_xpath('//p[2]/input[@name="passwordA"]').send_keys('123456')
time.sleep(2)
driver.quit()
driver.find_element_by_name(".telA")