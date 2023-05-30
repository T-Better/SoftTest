
from selenium import webdriver
import time


class BasePage():
    def open(self):
        self.driver = webdriver.Firefox()

    def get(self,url):
        self.driver.get(url)
        # 将滚动条滑到最底层
        # js1 = "window.scrollTo(1000,1000)"
        # self.driver.execute_script(js1)
        time.sleep(1)

class B2(BasePage):
    def __init__(self):
        u1 = r'https://www.zhihu.com/signin?next=%2F'
        self.driver.get(u1)

class B3(BasePage):
    def __int__(self):
        u2 = r'D:\Program Files\pagetest\注册A.html'
        self.driver.get(u2)

if __name__ == "__main__":
    b2 = B2
    b3 = B3




















