
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import time

cdp = r'D:\Program Files\pagetest\注册A.html'
driver = webdriver.Chrome()
driver.get(cdp)

# 获取页面上第一个超链接的文本内容
e1 = driver.find_element(By.XPATH,'//p[@id="linkto"]/a')
print(e1.text)

# 层级选择器：后代关系（不止父子）定位test1，然后写入值test1

# 最大化浏览器
driver.maximize_window()

# 设置浏览器窗口位置 --> 设置浏览器位置:左上角
driver.set_window_position(0,1000)

# 使用显式等待定位用户名输入框，如果元素存在，就输入admin
e1 = WebDriverWait(driver,1,10).until(lambda x:x.find_element_by_id('userA'))
e1.send_keys('admin')

# 获取当前页面url

# 获取页面上第一个超链接的地址
driver.find_element(By.LINK_TEXT,'新浪').get_attribute('href')

# time.sleep(1)
driver.close()











