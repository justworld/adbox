"""
单例模式
"""


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kargs):
        if not cls._instance:
            org = super(Singleton, cls)
            cls._instance = org.__new__(cls, *args, **kargs)

        return cls._instance


class Reader(Singleton):

    def enter(self):
        if not hasattr(self, 'num'):
            self.num = 0

        self.num = self.num + 1

    def leave(self):
        if not hasattr(self, 'num'):
            self.num = 0

        if self.num > 0:
            self.num = self.num - 1


if __name__ == '__main__':
    Reader().enter()
    Reader().enter()
    print(Reader().num)
    Reader().leave()
    print(Reader().num)
