from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

cdp = r'D:\Program Files\pagetest\注册A.html'
driver = webdriver.Chrome()
driver.get(cdp)

# 获取页面上第一个超链接的文本内容
e1 = driver.find_element(By.LINK_TEXT,'新浪')
print(e1.get_attribute('href'))

# 使用显式等待定位用户名输入框，如果元素存在，就输入admin
WebDriverWait(driver,0,1).until(lambda x:x.find_element(By.ID,'1'))

# time.sleep(1)
driver.close()






