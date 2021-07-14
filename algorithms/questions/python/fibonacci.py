"""
斐波那契数列Fibonacci sequence，黄金分割数列。
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233，377，610，987，1597，2584，4181，6765，10946，17711，28657，46368........
实现可以很简单，也可以很巧妙，容易想到的递归算法性能不好且费空间就不写了
"""
import time


def fib_generator(n):
    """
    生成器实现
    :param n:
    :return:
    """
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
        yield a


def fib_matrix(n):
    """
    矩阵实现
    :param n:
    :return:
    """
    import numpy
    res = pow((numpy.matrix([[1, 1], [1, 0]])), n) * numpy.matrix([[1], [0]])
    return res[0][0]


n = 1000

start = time.time()
for i in range(n):
    fib_generator(i)
print(time.time() - start)

start1 = time.time()
for i in range(n):
    fib_matrix(i)
print(time.time() - start1)
