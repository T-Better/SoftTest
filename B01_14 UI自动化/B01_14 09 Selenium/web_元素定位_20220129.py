# web_元素定位_20220129.py
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\注册A.html')

e1 = driver.find_element_by_css_selector('[placeholder="请输入用户名"]')
r1 = e1.size

# 获取页面上第一个超链接的文本内容
url1 = driver.find_element_by_link_text('新浪').text

# 判断页面中的span标签是否可见
e1.title
