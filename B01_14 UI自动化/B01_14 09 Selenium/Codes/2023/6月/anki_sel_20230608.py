from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

cdp = r'D:\Program Files\pagetest\注册A.html'
driver = webdriver.Firefox()
driver.get(cdp)
e1 = driver.find_element(By.NAME,'selecta')
select = Select(e1)
select.select_by_visible_text('上海')

time.sleep(2)
driver.close()







