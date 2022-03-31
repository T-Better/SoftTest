# test_three.py

from collections import namedtuple  # nametuple
Task = namedtuple('Task',['summary','owner','done','id'])
Task.__new__.__defaults__ = (None,None,False,None)

def test_defaults():
    """Using no parameters should invoke defaults.""" # invoke:调用
    t1 = Task() # 对Task具名元组实例化
    t2 = Task(None, None, False, None)
    assert t1 == t2

def test_member_access():
    """Check .field functionality of namedtuple"""
    t = Task('buy milk','brian') # 给Task各名字写值：
    assert t.summary == 'buy milk' # 成功
    assert t.owner == 'brian'  # 成功
    assert (t.done, t.id) == (False,None)  




    

