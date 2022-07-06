from selenium import webdriver

driver = webdriver.Chrome()
driver.get()
# 获取页面上第一个超链接的地址
# e1 = driver.find_element(By.LINK_TEXT,'').get_attribute('href')

# 打开‘注册A.html’页面，完成以下操作
# 1). 填写注册信息
# 2). 截图保存
e2 = driver.find_element(By.ID,'name')
e2.send_keys()
driver.get_screenshot_as_file('')


driver.close()
