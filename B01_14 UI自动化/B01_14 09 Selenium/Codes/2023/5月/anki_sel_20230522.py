"""
打开‘注册A.html’页面，完成以下操作
1). 填写注册用户名
2). 截图保存
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


cdp = r'D:\Program Files\pagetest\注册A.html'
jp = r'C:\Users\Lenovo\Pictures\暂时'
driver = webdriver.Chrome() # chrome实例化
driver.get(cdp)  # 发起请求

# 1). 填写注册用户名
e1 = ''
e1.send_keys('username')

# 2). 截图保存
driver.get_screenshot_as_file('./1.jpg')

# 删除一个字符，不是全部内容
e1.send_keys(Keys.BACK_SPACE)

# 模拟鼠标悬停在‘注册’按钮上
reg_btn = ""
action = ActionChains(driver)
action.move_to_element(reg_btn).perform()

# 根据option显示文本来定位
e2 = driver.find_element(By.ID,'selectA')
select = Select(e2)
select.select_by_value('sh')

# 打开注册页面A，在用户名文本框上点击鼠标右键，注意需要两步
action.context_click(e2).perform()

driver.close()
