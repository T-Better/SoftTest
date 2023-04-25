
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

cdp = r'D:\Program Files\pagetest\注册A.html'
zh = r'https://www.zhihu.com/signin?next=%2F'
driver = webdriver.Chrome()
driver.get(cdp)

# 获取页面上第一个超链接的地址
l = driver.find_element(By.LINK_TEXT,'新浪').get_attribute('href')


# 设置浏览器窗口位置 --> 设置浏览器位置:左上角
driver.set_window_position(0,100)



driver.close()








