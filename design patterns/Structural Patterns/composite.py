"""
和桥接模式很像，区别在于组合对象的性质
"""


class File:
    def preview(self, deep=1):
        print('-' * deep)


class Folder:
    def __init__(self):
        self.childs = list()

    def add(self, f):
        self.childs.append(f)

    def preview(self, deep=1):
        print('-' * deep)
        for i in self.childs:
            i.preview(deep + 2)


if __name__ == '__main__':
    folder = Folder()
    folder.add(File())
    folder.preview()
