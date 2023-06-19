from selenium import webdriver

def singledriver(cls,*args,**kw):
    instances = {}
    def _singledriver():
        if cls not in instances:
            instances[cls] = cls(*args,**kw)
            print(instances)
        return instances[cls]
    return _singledriver

@singledriver
class SingleDriver():
    """driver单例"""
    def __init__(self):
        self.driver = webdriver.Firefox()