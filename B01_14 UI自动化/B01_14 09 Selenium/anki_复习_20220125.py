from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\注册A.html')
# 绝对路径法
driver.find_element_by_xpath("/html/body/div[1]/fieldset/form/p[1]/input").send_keys('admin')

# 相对路径法
driver.find_element_by_xpath('//form/p[1]/input').send_keys('admin')
time.sleep(2)

driver.find_element_by_xpath('//form[1]/p[2]/input').send_keys('123456')
time.sleep(2)

driver.quit