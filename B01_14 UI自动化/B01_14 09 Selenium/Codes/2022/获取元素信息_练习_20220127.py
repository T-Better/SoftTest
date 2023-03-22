# 获取元素信息_练习_20220127.py 我写的
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get(r'D:\Program Files\pagetest\注册A.html')

# 1).获取用户名输入框的大小 
size1 = driver.find_element_by_css_selector('[placeholder="请输入用户名"]').size
# 2).获取页面上第一个超链接的文本内容 
text1 = driver.find_element_by_link_text('访问 新浪 网站').text
# 3).获取页面上第一个超链接的地址 
link1 = driver.find_element_by_link_text('访问 新浪 网站').get_attribute('href')
# 4).判断页面中的span标签是否可见 

span_disp = driver.find_element_by_name('sp1').is_displayed()
# 5).判断页面中取消按钮是否可用 
button_canc = driver.find_element_by_css_selector('[value="取消"]').is_enabled()
# 6).判断页面中'旅游'对应的复选框是否为选中的状态 
lvyou_sele = driver.find_element_by_css_selector('[value="旅游"]').is_selected()

print("用户名输入框大小：{},\n第一个超链接文本内容:{},\n第一个超链接地址:{},\
    \nspan标签是否可见:{},\n页面中取消按钮是否可用？{},\n旅游对应复选框是否\
        为选中状态?{}".format(size1,text1,link1,span_disp,button_canc,lvyou_sele))

driver.close()