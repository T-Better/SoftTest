from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

p1 = r'D:\Program Files\pagetest\{}'.format('注册A.html')

# 打开注册页面A，在用户名文本框上点击鼠标右键
driver = webdriver.Chrome()
driver.get(p1)

e1 = driver.find_element()
action = ActionChains(driver)
action.context_click(e1)
action.perform()

# 设置浏览器大小 设置浏览器宽、高(像素点)
driver.set_window_size(300,300)

# 使用显式等待定位用户名输入框，如果元素存在，就输入admin
WebDriverWait(driver,2,1).until(lambda x:x.find_element(By.ID,'userA'))

# 设置浏览器窗口位置 --> 设置浏览器位置
driver.set_window_position(100,100)

# 获取页面上第一个超链接的地址
link1 = driver.find_element(By.LINK_TEXT,'访问 新浪 网站').get_attribute('href')

# 获取弹出框对象
alert = driver.switch_to.alert

# 代码实现隐式等待5秒，说明其含义
driver.implicitly_wait(5)

driver.close()
