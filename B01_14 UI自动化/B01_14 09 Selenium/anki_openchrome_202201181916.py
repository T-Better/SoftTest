# anki_openchrome_202201181916.py

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('http://www.baidu.com')

time.sleep(3)

driver.quit()


