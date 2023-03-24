# 如何用两种方法定义namedtuple对象User并赋值,如何对User赋默认值；
from collections import namedtuple

User = namedtuple('User','name,age,id')

User.__new__.__defaults__ = (None,None,False)

user = User('张三','18','09')

print(user)






