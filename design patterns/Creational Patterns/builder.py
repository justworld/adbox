"""
建造者模式
"""


class Benz:
    def __init__(self):
        self._current = None

    @property
    def current(self):
        if self._current:
            return self._current
        return self._build()

    def _build(self):
        instance = Car()
        instance.color = 'black'
        instance.size = 'big'
        instance.seat = 6
        instance.price = 100
        return instance


class Car:
    def __init__(self):
        self.color = None
        self.size = None
        self.seat = 0
        self.price = 0

    def claim(self):
        print('this car is {} color and {} size, also has {} seats, only for sale {} yuan'.format(
            self.color, self.size, self.seat, self.price))


if __name__ == '__main__':
    Benz().current.claim()
