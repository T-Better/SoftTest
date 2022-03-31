import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

path1 = r'D:\Program Files\pagetest\注册A.html'

driver = webdriver.Chrome()
driver.get(path1)
# action = ActionChains(driver)
# e1 = driver.find_element(By.CSS_SELECTOR, '[placeholder="请输入用户名"]')
# e1.send_keys('admin')
# time.sleep(2)
# action.double_click(e1).perform()
# time.sleep(2)
driver.find_element(By.LINK_TEXT, '新浪').click()
time.sleep(3)
driver.close()


