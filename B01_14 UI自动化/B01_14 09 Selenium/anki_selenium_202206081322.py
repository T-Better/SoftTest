from selenium import webdriver
from selenium.webdriver.common.by import By
import time

p1 = r'D:\Program Files\pagetest\{}'.format('注册A.html')
driver = webdriver.Chrome()
driver.get(p1)
driver.find_element(By.XPATH,"//p[@id='pa']/input[@name='userA']").send_keys('admin')
time.sleep(2)

driver.find_element(By.XPATH,"//*[@name='passwordA']").send_keys('123')
time.sleep(2)

driver.quit()
