# coding: utf-8
"""
适配器模式
"""


class Adapter:
    def __init__(self, obj, **kargs):
        self.__dict__.update(**kargs)

    def __getattr__(self, attr):
        return getattr(self.obj, attr)


class Cat:
    def climb_tree(self):
        print 'climb tree'


class Dog:
    def climb_tree(self):
        print 'just bark'


if __name__ == '__main__':
    cat = Dog()
    cat.climb_tree()
    really_cat = Cat()
    cat = Adapter(cat, **{'climb_tree': really_cat.climb_tree})
    cat.climb_tree()
