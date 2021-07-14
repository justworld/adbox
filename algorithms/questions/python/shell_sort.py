"""
希尔排序
先取一个小于n的整数d1作为第一个增量，把文件的全部记录分成d1个组。
所有距离为d1的倍数的记录放在同一个组中。先在各组内进行直接插入排序；
然后，取第二个增量d2<d1重复上述的分组和排序，直至所取的增量dt=1(dt<dt-l<；…<d2<d1），即所有记录放在同一组中进行直接插入排序为止
不稳定、o(1)空间复杂度、o(n2)最坏时间复杂度、o(n)最好时间复杂度、o(n1.3)平均时间复杂度
"""


def shell_sort(l):
    if not l:
        return []

    length = len(l)
    i = length // 2
    while i:
        for j in range(i, length):
            for m in range(j, i - 1, -i):
                if l[m] < l[m - i]:
                    l[m], l[m - i] = l[m - i], l[m]
                else:
                    break

        i = i // 2

    return l
