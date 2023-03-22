from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

path1 = ''
driver = webdriver.Chrome()
driver.get(path1)
driver.find_element(By.XPATH, '')
select = Select(driver.find_element_by_id)
select.select_by_visible_text()



