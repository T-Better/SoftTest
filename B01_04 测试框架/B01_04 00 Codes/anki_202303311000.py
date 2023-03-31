from collections import namedtuple

User = namedtuple('User','name,age,id')

User.__new__.__defaults__ = (None,None,False)

user = User('zs','18','01')



