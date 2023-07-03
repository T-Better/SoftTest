# test_dog.py
from loguru import logger


class test_dog():

    def set_name(self, name):
        self.name = name

    @logger.catch
    def show_name(self):
        print(self.name)


d = test_dog()
d.set_name('旺财')
d.show_name()
