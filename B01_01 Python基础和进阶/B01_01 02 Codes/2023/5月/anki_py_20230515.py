# 定义 cat 类，属性为eat何drink
"""
class cat:
    def eat(self):
        print("汤姆爱吃鱼")


    def drink(self):
        print("汤姆爱喝水")

# 将cat类实例化为lazy_cat 对象
lazy_cat = cat
# 调用对象的 eat 方法
lazy_cat.eat()
# 调用对象的 drink 方法
lazy_cat.drink()
"""
import requests
from bs4 import BeautifulSoup


u1 = r'http://python123.io/ws/demo.html'

r = requests.get(u1)
b1 = BeautifulSoup(r.text, 'html.parser')
print(b1.prettify())




