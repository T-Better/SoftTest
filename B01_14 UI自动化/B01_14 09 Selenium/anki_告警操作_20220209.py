# anki_告警操作_20220209.py
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\注册A.html')

driver.find_element_by_css_selector('[id="alerta"]').click()
alert = driver.switch_to.alert
alert.accept()
alert.dismiss()
driver.close()
