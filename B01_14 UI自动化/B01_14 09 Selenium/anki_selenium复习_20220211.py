import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\注册A.html')

"""
# 打开‘drag.html’页面，把红色方框拖拽到蓝色方框上
driver.get(r'D:\Program Files\pagetest\drag.html')
action = ActionChains(driver)
red_box = driver.find_element_by_id("div1")
blue_box = driver.find_element_by_id('div2')
action.drag_and_drop(red_box,blue_box)
action.perform()
time.sleep(2)
"""
# url = driver.current_url()
# print(url)

# 获取页面上第一个超链接的地址
f_url = driver.find_element_by_link_text('新浪').get_attribute('href')
print(f_url)
driver.close()
