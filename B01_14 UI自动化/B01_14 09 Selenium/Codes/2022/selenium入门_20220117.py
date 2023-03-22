# selenium入门_20220117.py

import time
from selenium import webdriver

# 实例化浏览器驱动对象（创建浏览器驱动对象） 
driver = webdriver.Chrome()  # 创建的是谷歌浏览器驱动对象，chrome后面右括号，并且第一个字母要大写

# driver = webdriver.Firefox()  # 创建火狐浏览器驱动对象
# 打开百度网站
driver.get(r'https://www.baidu.com/s?cl=3&tn=baidutop10&fr=top1000&wd=%E6%8B%BC%E5%A4%9A%E5%A4%9A%E6%B3%95%E5%BA%AD%E4%B8%8A%E5%9B%9E%E5%A4%8D%E7%A0%8D%E4%BB%B7%E6%B0%B8%E8%BF%9C%E5%B7%AE%E4%B8%80%E5%88%80&rsv_idx=2&rsv_dl=fyb_n_homepage&sa=fyb_n_homepage&hisfilter=1')

# 等待3秒(代表业务操作)
time.sleep(3)  #$ 通过快捷导包方式导入time模块，光标要在time后面再按alt+enter

# 推出浏览器驱动（释放系统资源）
driver.quit()
