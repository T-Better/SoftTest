from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
driver.get()
e1 = driver.find_element_by_id('userA')
select = Select(driver.find_element_by_id())
# select.find_element_by_index('')

# 显式等待
e1 = WebDriverWait(driver,10,1,).until()
e1.send_keys('admin')



