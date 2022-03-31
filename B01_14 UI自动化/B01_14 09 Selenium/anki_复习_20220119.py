from selenium import webdriver
import time


driver = webdriver.Chrome()

driver.get('D:\Program Files\pagetest\注册A.html')

driver.find_element_by_link_text('访问 新浪 网站').click()
time.sleep(3)

driver.quit()