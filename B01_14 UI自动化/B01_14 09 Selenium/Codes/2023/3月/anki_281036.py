from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

cdp = r'D:\Program Files\pagetest\注册A.html'
driver = webdriver.Chrome()
driver.get(cdp)
e1 = driver.find_element(By.ID,'selectA')
"""
select = Select(e1)
select.select_by_value('sh')
"""

# 将滚动条滑到最顶层
js1 = "window.scrollTo(10000,10000)"
driver.execute_script(js1)

# 判断页面中取消按钮是否可用
e1.is_enabled()

# 代码实现隐式等待5秒，说明其含义
driver.implicitly_wait(5)

# 粘贴
e1.send_keys(Keys.CONTROL, 'V')

# 全选
e1.send_keys(Keys.CONTROL, 'A')

# 获取用户名输入框的大小
e1.size

# 获取当前页面url
e1.current_url

# 添加cookie
cd = {'name':'1'}
e1.add_cookie(cd)

alert = driver.switch_to.alert
alert.accept()
# 调用：取消对话框选项
alert.dismiss()

# 回车键
e1.send_keys(Keys.ENTER)

# 最大化浏览器
driver.maximize_window()

# 刷新
driver.refresh()

# 打开注册页面A，模拟鼠标悬停在‘注册’按钮上
action = ActionChains(driver)
action.move_to_element(e1)
action.perform()

# 根据option属性 value值来定位
select = Select(driver)
select.select_by_value('sh')

# 判断页面中的span标签是否可见
e1.is_displayed()

# 复制
e1.send_keys(Keys.CONTROL, 'C')

# 获取弹出框对象
alert = driver.switch_to.alert

# 删除
e1.send_keys(Keys.BACK_SPACE)

# 获取告警框的文字信息
alert = driver.switch_to.alert
alert.text()

# 2). 截图保存
driver.get_screenshot_as_file('')

# 设置浏览器窗口位置 --> 设置浏览器位置:左上角
driver.set_window_position(0,0)

# selenium定位用户名输入框并输入制表符
e1.send_keys(Keys.TAB)

# 打开注册页面A，在用户名文本框上点击鼠标右键，注意需要两步
action.context_click(e1).perform()

# 获取指定cookie
driver.get_cookie('')

# 判断页面中'旅游'对应的复选框是否为选中的状态
e1.is_selected()

# 设置浏览器大小 设置浏览器宽、高(像素点300,300)
driver.set_window_size(300,300)

time.sleep(2)
driver.close()
