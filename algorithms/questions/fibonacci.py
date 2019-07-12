# coding: utf-8
"""
斐波那契数列Fibonacci sequence，黄金分割数列。
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233，377，610，987，1597，2584，4181，6765，10946，17711，28657，46368........
实现可以很简单，也可以很巧妙，容易想到的递归算法性能不好且费空间就不写了
"""
import numpy


def fibonacci_generator(n):
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
    res = pow((numpy.matrix([[1, 1], [1, 0]])), n) * numpy.matrix([[1], [0]])
    return res[0][0]


for i in range(10):
    print(int(fib_matrix(i)), end=' ')


### 2
# 使用矩阵计算斐波那契数列
def Fibonacci_Matrix_tool(n):
    Matrix = numpy.matrix("1 1;1 0")
    # 返回是matrix类型
    return pow(Matrix, n)  # pow函数速度快于 使用双星好 **


def Fibonacci_Matrix(n):
    result_list = []
    for i in range(0, n):
        result_list.append(numpy.array(Fibonacci_Matrix_tool(i))[0][0])
    return result_list


for i in fibonacci_generator(20):
    print(i)

Fibonacci_Matrix(10)
