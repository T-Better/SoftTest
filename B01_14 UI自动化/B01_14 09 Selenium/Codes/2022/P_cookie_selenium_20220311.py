from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.add_cookie({"name":"BDUSS","value":"根据实际填写"})
time.sleep(2)
driver.refresh()
time.sleep(2)
driver.close()

