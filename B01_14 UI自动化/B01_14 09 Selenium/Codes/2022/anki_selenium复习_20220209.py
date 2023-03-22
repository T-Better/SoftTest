# anki_selenium复习_20220209.py
import time
from selenium.webdriver.support.select import Select
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('')

# 将滚动条滑到最顶层
js1 = "window.scrollTo(10000,10000)"
driver.execute_script(js1)
