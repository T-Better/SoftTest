from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

path1 = r'D:\Program Files\pagetest\注册A.html'
driver = webdriver.Chrome()
driver.get(path1)
driver.find_element(By.ID,'userA').send_keys('admin')
driver.find_element(By.ID,'passwordA').send_keys('123456')
time.sleep(3)
res = driver.current_url
print(res)
action = ActionChains(driver)

driver.find_element(By.ID,'passwordA').send_keys(Keys.BACK_SPACE)

select = Select(driver.find_element(By.ID, 'selectA'))
select.select_by_visible_text('北京')

driver.close()
