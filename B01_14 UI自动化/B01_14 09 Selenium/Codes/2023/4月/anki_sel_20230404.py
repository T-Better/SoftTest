# 获取title
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


cdp = r'D:\Program Files\pagetest\注册A.html'
zh = r'https://www.zhihu.com/signin?next=%2F'
driver = webdriver.Chrome()
driver.get(zh)
b1 = driver.find_element(By.XPATH,'//p/button')
e1 = driver.find_element(By.ID, 'selectA')

# 获取页面上第一个超链接的文本内容


# 获取页面上第一个超链接的地址
e3 = driver.find_element(By.LINK_TEXT,'新浪').get_attribute('href')

# 2). 截图保存
driver.get_screenshot_as_file()

# 层级选择器：后代关系（不止父子）定位test1，然后写入值test1
driver.find_element(By.CSS_SELECTOR, 'p input[@name="user"]')

# 获取页面上第一个超链接的地址
driver.find_element(By.LINK_TEXT,'新浪').get_attribute('href')

# 判断页面中'旅游'对应的复选框是否为选中的状态
e1.is_selected()

# 打开注册页面A，在用户名文本框上点击鼠标右键，注意需要两步
action = ActionChains(driver)
action.context_click(e1).perform()

# selenium定位用户名输入框并输入制表符
e1.send_keys(Keys.TAB)

# 使用显式等待定位用户名输入框，如果元素存在，就输入admin
e2 = WebDriverWait(driver,10,1).until(lambda x:x.find_element(By.ID,'userA'))
e2.send_keys('admin')

# 粘贴
e1.send_keys(Keys.CONTROL,'V')

# 刷新
driver.refresh()

# 拉框选到上海
select = Select(e1)
select.select_by_visible_text('上海')


# 获取当前页面url
# driver.current_url()

# 打开注册页面A，模拟鼠标悬停在‘注册’按钮上
# action = ActionChains(driver)
# action.move_to_element(b1).perform()

# 代码实现隐式等待5秒，说明其含义
# driver.implicitly_wait(5)

# 根据元素的父子关系方式定位test1输入框
# p[id="p1"]>label

# 最大化浏览器
# driver.maximize_window()

# 获取title
# t = driver.title
# print(t)

driver.close()


