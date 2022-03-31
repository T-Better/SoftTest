import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import alert

driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\注册A.html')

# 回退（忽略跳过）键
driver.find_element(By.CSS_SELECTOR,'.').send_keys(Keys.ESCAPE)

# 判断页面中取消按钮是否可用
e1 = driver.find_element(By.XPATH, '//p/button').is_enabled()

# 获取当前页面url
url = driver.current_url

# 获取弹出框对象
alert = driver.switch_to.alert

# 获取页面上第一个超链接的地址
driver.find_element(By.LINK_TEXT, '新浪').get_attribute('href')

