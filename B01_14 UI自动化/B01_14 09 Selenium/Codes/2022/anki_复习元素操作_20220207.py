# anki_复习元素操作_20220207.py
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\注册A.html')
# e1 = driver.find_element_by_css_selector('[id="cancelA"]').is_enabled()

# 获取页面上第一个超链接的文本内容
driver.find_element_by_link_text('新浪').get_attribute('href')
time.sleep(2)
# 获取用户名输入框的大小 
driver.find_element_by_css_selector().size()

# 获取当前页面url 
driver.current_url
# 后退
driver.back()
# 前进
driver.forward()
driver.find_element_by_class_name('telA')


driver.close()