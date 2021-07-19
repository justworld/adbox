"""
直接选择排序
第一次从R[0]~R[n-1]中选取最小值，与R[0]交换，
第二次从R[1]~R[n-1]中选取最小值，与R[1]交换，....，
第i次从R[i-1]~R[n-1]中选取最小值，与R[i-1]交换，.....，
第n-1次从R[n-2]~R[n-1]中选取最小值，与R[n-2]交换，
总共通过n-1次，得到一个按排序码从小到大排列的有序序列
不稳定、o(1)空间复杂度、o(n2)时间复杂度
"""


def select_sort(l):
    if not l:
        return []

    length = len(l)
    for i in range(length):
        min = i
        for j in range(i + 1, length):
            if l[j] < l[min]:
                min = j

        l[min], l[i] = l[i], l[min]

    return l
