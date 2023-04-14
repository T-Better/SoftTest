from selenium import webdriver
import time
cdp = r'D:\Program Files\pagetest\注册A.html'
jp = r'C:\Users\Lenovo\Pictures\暂时'
driver = webdriver.Chrome() # chrome实例化
driver.get(cdp)  # 发起请求
# 设置浏览器窗口位置 --> 设置浏览器位置:左上角
driver.set_window_position(1000,1000)

time.sleep(2)



driver.close()






