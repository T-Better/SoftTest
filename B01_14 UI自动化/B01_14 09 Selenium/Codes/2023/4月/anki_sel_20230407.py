from selenium import webdriver

cdp = r'D:\Program Files\pagetest\注册A.html'
driver = webdriver.Chrome()
driver.get(cdp)







# e1.send_keys(Keys.SPACE)

driver.close()
