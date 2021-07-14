"""
简单插入排序
将一个记录插入到已经排好序的有序表中，从而一个新的、记录数增1的有序表
稳定、o(1)空间复杂度、o(n2)时间复杂度
"""


def insert_sort(l):
    if not l:
        return []

    length = len(l)
    for i in range(1, length):
        for j in range(i, 0, -1):
            if l[j] < l[j - 1]:
                l[j], l[j - 1] = l[j - 1], l[j]
            else:
                break

    return l
