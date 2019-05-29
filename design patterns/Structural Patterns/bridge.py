# coding: utf-8
"""
桥接模式
"""


class Red:
    def take_on(self):
        return 'red'


class Black:
    def take_on(self):
        return 'black'




class Pen:
    def __init__(self, color):
        self.color = color

    def draw(self):
        print self.color.take_on()


if __name__ == '__main__':
    pen1 = Pen(Red())
    pen1.draw()
    pen2 = Pen(Black())
    pen2.draw()
