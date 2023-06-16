# test_dog.py
# TODO
from test_dog_log import trace


class test_dog():

    def set_name(self, name):
        self.name = name

    # TODO
    def show_name(self):
        print(self.name)

d = test_dog()
d.set_name('旺财')
d.show_name()
