from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
time.sleep(3)
driver.implicitly_wait(5)


driver.close()




