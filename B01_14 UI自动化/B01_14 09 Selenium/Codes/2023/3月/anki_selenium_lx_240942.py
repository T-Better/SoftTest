from selenium import webdriver
import time

cdp = r'D:\Program Files\pagetest\注册A.html'
zh = r'https://www.zhihu.com/signin?next=%2F'
driver = webdriver.Chrome()
driver.get(cdp)

# 设置浏览器大小 设置浏览器宽、高(像素点300,300)
driver.set_window_size(1000,1000)
time.sleep(2)


driver.close()









