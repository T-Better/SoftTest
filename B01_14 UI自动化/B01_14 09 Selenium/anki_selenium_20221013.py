from selenium import webdriver
from selenium.webdriver.common.by import By
import time

p1 = r'D:\Program Files\pagetest\注册A.html'

driver = webdriver.Chrome()
driver.get(p1)
e1 = driver.find_element(By.LINK_TEXT,'新浪')
e1.click()
time.sleep(2)
driver.close()










