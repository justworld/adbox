"""
模板方法模式
"""
import abc


class People(object):
    @abc.abstractmethod
    def sex(self):
        print('no sex')

    def speak(self):
        print('i am human')

    __metaclass__ = abc.ABCMeta


class Man(People):
    def sex(self):
        print('man')


class WoMan(People):
    def sex(self):
        print('woman')


if __name__ == '__main__':
    Man().sex()
    WoMan().sex()
