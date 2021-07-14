"""
工厂方法模式
"""


class Operation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_result(self):
        raise Exception('The method is not implemented')


class AddOperation(Operation):
    def get_result(self):
        return self.a + self.b


class SubOperation(Operation):
    def get_result(self):
        return self.a - self.b


def get_operation(a, b, opera_tpe):
    if opera_tpe == 'add':
        return AddOperation(a, b)
    if opera_tpe == 'sub':
        return SubOperation(a, b)
    return Operation(a, b)


if __name__ == '__main__':
    print(get_operation(10, 10, 'add').get_result())
