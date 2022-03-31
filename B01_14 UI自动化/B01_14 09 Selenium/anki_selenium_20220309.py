import time
from selenium import webdriver

driver = webdriver.Chrome()

js1 = "Window.scrollTo(0,0)"
driver.execute_script(js1)

# 关闭浏览器单个窗口
driver.close()


