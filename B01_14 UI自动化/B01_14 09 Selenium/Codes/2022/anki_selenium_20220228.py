from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver



driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\注册.html')
select = Select(driver.find_element(By.ID, 'selectA'))
select.select_by_value('bj')
action = ActionChains(driver)
e1 = driver.find_element(By.XPATH, '//p/button')
action.move_to_element(e1).perform()

e1.send_keys(Keys.ESCAPE)

driver.find_element(By.LINK_TEXT, '新浪').get_attribute('href')

js1 = "window.scrollTo(10000,10000)"
driver.execute_script(js1)


