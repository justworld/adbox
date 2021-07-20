"""
归并排序
申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列;
设定两个指针，最初位置分别为两个已经排序序列的起始位置;
比较两个指针所指向的元素, 选择相对小的元素放入到合并空间, 并移动指针到下一位置;
重复步骤3直到某一指针超出序列尾;
将另一序列剩下的所有元素直接复制到合并序列尾
稳定、o(n)空间复杂度、o(nlogn)时间复杂度
"""


def merge_sort(l):
    if not l or len(l) == 1:
        return l

    mid = len(l) // 2
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])
    return merge(left, right)


def merge(left, right):
    len1, len2 = len(left), len(right)
    i, j = 0, 0
    result = []
    while i < len1 and j < len2:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
