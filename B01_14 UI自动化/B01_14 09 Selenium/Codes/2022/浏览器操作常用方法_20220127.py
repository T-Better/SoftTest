# 浏览器操作常用方法_20220127.py 我的代码
"""
功能：打开浏览器，缩放到指定大小，移动位置，最大化，搜索，刷新，获取标题和
当前url，后退，前进，关闭当前窗口
"""
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

driver.set_window_size(500,500)  # 设置浏览器窗口大小 --> 设置浏览器宽、高(像素点) 
time.sleep(1)
driver.set_window_position(200,200)  # 设置浏览器窗口位置 --> 设置浏览器位置
time.sleep(1)
driver.maximize_window()  # 最大化浏览器窗口 --> 模拟浏览器最大化按钮 
time.sleep(1)

driver.get('http://www.baidu.com/s?wd=张三')
driver.refresh()  # 刷新 --> 模拟浏览器F5刷新
time.sleep(1)
title = driver.title
url1 = driver.current_url
print('###### 标题：{} 地址 {}'.format(title,url1))
time.sleep(1)
driver.back()  # 后退 --> 模拟浏览器后退按钮
time.sleep(1)
driver.forward()  # 前进 --> 模拟浏览器前进按钮
time.sleep(1)
driver.close()  # 关闭当前窗口 --> 模拟点击浏览器关闭按钮
