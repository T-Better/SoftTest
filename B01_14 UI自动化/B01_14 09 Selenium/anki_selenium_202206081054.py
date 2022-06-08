from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

p1 = r'D:\Program Files\pagetest\{}'.format('注册A.html')
driver.get(p1)
# 获取页面上第一个超链接的文本内容
t1 = driver.find_element_by_link_text('访问 新浪 网站').text
driver.find_element(By.ID,'alerta')
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
alert.dismiss()

"""
1). 填写注册信息
2). 截图保存
"""
driver.find_element(By.ID,'userA').send_keys('user')
driver.get_screenshot_as_file('img01.jpg')

# 根据option属性 value值来定位
select = Select(driver.find_element(By.XPATH))
select.select_by_value('bj')

# 打开‘drag.html’页面，把红色方框拖拽到蓝色方框上
action = ActionChains(driver)
red_box = driver.find_element(By.ID,'')
blue_box = driver.find_element(By.ID, '')
action.drag_and_drop(blue_box)

# selenium指定chrome.exe来发起请求如何实现？
option = webdriver.ChromeOptions()
option.binary_location = r'D:\work\Goole\Chrome\Application\chrome.exe'
driver = webdriver.Chrome()

driver.close()

