# anki_浏览器操作_20220129.py
from re import template
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

# 前进 
driver.forward()
# 判断页面中'旅游'对应的复选框是否为选中的状态
res = driver.find_element_by_css_selector('[value="旅游"]').is_selected()
# 设置浏览器窗口位置 --> 设置浏览器位置
driver.set_window_position(200,300)

driver.refresh()
driver.maximize_window()

driver.close()
