





from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

cdp = r'D:\Program Files\pagetest\注册A.html'
driver = webdriver.Chrome()
driver.get(cdp)
e1 = driver.find_element(By.ID,'selectA')
select = Select(e1)
select.select_by_value('sh').click()
select.select_by_visible_text('上海').click()

time.sleep(2)
driver.close()


















