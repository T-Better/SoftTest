from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

path1 = r'D:\Program Files\pagetest\注册A.html'
driver = webdriver.Chrome()
driver.get(path1)

select = Select(driver.find_element(By.ID, 'select'))
select.select_by_visible_text('北京')



