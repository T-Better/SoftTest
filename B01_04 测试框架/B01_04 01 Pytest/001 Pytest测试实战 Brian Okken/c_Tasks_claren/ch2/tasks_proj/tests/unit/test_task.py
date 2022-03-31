"""Test the Task data type."""
from tasks import Task
# Task是ch1中一个包中定义的：Task=namedtuple('Task','summary,owner,done,id')

def test_asdict():
    """
    _asdict() should return a dictionary.
    判断nametuple的task是否通过._asdict()转换成了字典
    """
    t_task = Task('do something', 'okken', True, 21)
    t_dict = t_task._asdict()
    expected = {'summary': 'do something',
                'owner': 'okken',
                'done': True,
                'id': 21}
    assert t_dict == expected


def test_replace():
    """
    replace() should change passed in fields.
    判断namedtuple的t_before是否由._replace()将其值做修改
    """
    t_before = Task('finish book', 'brian', False)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task('finish book', 'brian', True, 10)
    assert t_after == t_expected


def test_defaults():
    """
    Using no parameters should invoke defaults.
    判断Task默认赋值是否（成功）同预期一致
    """
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2


def test_member_access():
    """
    Check .field functionality of namedtuple.
    测试Task的值是否同预期一致
    """
    t = Task('buy milk', 'brian')
    assert t.summary == 'buy milk'
    assert t.owner == 'brian'
    assert (t.done, t.id) == (False, None)
