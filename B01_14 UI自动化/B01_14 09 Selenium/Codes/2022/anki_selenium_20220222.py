from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('D:\Program Files\pagetest\注册A.html')
select = Select(driver.find_element(By.XPATH, 'A'))
select.select_by_index('a')
driver.forward()

e1 = driver.find_element(By.XPATH, 'a')
e1.clear()
e1.send_keys('1')
