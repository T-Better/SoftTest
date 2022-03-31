from collections import namedtuple
User = namedtuple('User','name,age,class')
User.__new__.__default__ = (None, None, False)







