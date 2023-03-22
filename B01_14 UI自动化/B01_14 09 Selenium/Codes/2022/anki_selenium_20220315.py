from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.get()
driver.implicitly_wait(5)

# 截图保存
driver.get_screenshot_as_file('./img/image20220315.png')
WebDriverWait(driver, 4, 1).until(lambda x:x.find_element_by_id()).send_keys('admin')
driver.find_element_by_xpath('').send_keys(Keys.CONTROL, 'v')
# 使用显式等待定位用户名输入框，如果元素存在，就输入admin

