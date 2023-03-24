# anki_opench_20220118.py
"""
自动打开谷歌浏览器
然后打开百度网站
等待3秒
退出谷歌浏览器
"""
from selenium import webdriver
import time

# 实例化浏览器驱动对象（创建浏览器驱动对象)
driver = webdriver.Chrome()

# 打开百度网站
driver.get("http://www.baidu.com")

# 等待3秒
time.sleep(3)

# 退出浏览器
driver.quit()
