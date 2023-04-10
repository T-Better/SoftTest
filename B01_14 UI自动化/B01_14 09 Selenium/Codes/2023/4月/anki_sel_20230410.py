from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

cdp = r'D:\Program Files\pagetest\注册A.html'
driver = webdriver.Chrome()
driver.get(cdp)

e1 = ''
zce = driver.find_element(By.XPATH,'//p/button')
# 代码实现隐式等待5秒，说明其含义
driver.implicitly_wait(5)

# 模拟鼠标悬停在‘注册’按钮上
action = ActionChains(driver)
action.move_to_element(zce).perform()

# 下拉框选到上海
e3 = driver.find_element(By.ID,'selectA')
select = Select(e3)
select.select_by_visible_text('上海')
# select.select_by_value('sh')

# 使用显式等待定位用户名输入框，如果元素存在，就输入admin
e4 = WebDriverWait(driver,10,1).until(
    lambda x:x.find_element(By.ID, 'userA')
)

# 获取页面上第一个超链接的文本内容
t = driver.find_element(By.LINK_TEXT,'新浪').text

# 获取当前页面url
driver.current_url

# 获取页面上第一个超链接的地址
t.get_attribute('href')

# 层级选择器：后代关系（不止父子）定位test1，然后写入值test1
e5 = driver.find_element(By.CSS_SELECTOR,'p[p1="p1"] input')

driver.close()
