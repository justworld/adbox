# coding: utf-8
"""
外观模式
"""


class ModuleOne:
    def show(self):
        print 'one'


class ModuleTwo:
    def show(self):
        print 'two'


class Facade:
    def __init__(self):
        self.module_one = ModuleOne()
        self.module_two = ModuleTwo()

    def show(self):
        self.module_one.show()
        self.module_two.show()


if __name__ == '__main__':
    Facade().show()
