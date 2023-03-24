# web_鼠标拖动操作_20220127.py  我的代码
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\drag.html')
action = ActionChains(driver)  # 实例化
source_red = driver.find_element_by_xpath('//div[@id="div1"]')  # 源元素
target_blue = driver.find_element_by_xpath('//div[@id="div2"]')  # 目标元素
action.drag_and_drop(source_red,target_blue).perform()  # 调用拖动
time.sleep(2)
driver.close()
