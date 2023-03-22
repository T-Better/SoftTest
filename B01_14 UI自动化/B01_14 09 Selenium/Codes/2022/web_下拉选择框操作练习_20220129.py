# web_下拉选择框操作练习_20220129.py
import time
from selenium import webdriver

drive = webdriver.Chrome()
drive.get(r'D:\Program Files\pagetest\注册A.html')

# 1).选择‘广州’ 
drive.find_element_by_css_selector('[value="gz"]').click()
time.sleep(2)
# 2).暂停2秒，选择‘上海’ 
drive.find_element_by_css_selector('value="sh"').click()
time.sleep(2)
# 3).暂停2秒，选择‘北京’ 
drive.find_element_by_css_selector('value="bj"').click()
time.sleep(2)

drive.close()
