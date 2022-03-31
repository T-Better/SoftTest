from selenium.webdriver.support.select import Select
from selenium import webdriver

driver = webdriver.Chrome()
driver.get()
select = Select(driver.find_element_by_id('selectA'))


