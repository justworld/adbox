def _quick_sort(sort_list, low, high):
    if low < high:
        # 基准值
        pivot = sort_list[low]
        i, j = low, high
        while i < j:
            while i < j and sort_list[j] >= pivot:
                j -= 1
            sort_list[i] = sort_list[j]
            while i < j and sort_list[i] <= pivot:
                i += 1
            sort_list[j] = sort_list[i]

        sort_list[i] = pivot

        _quick_sort(sort_list, low, i - 1)
        _quick_sort(sort_list, i + 1, high)


def quick_sort(sort_list):
    """
    1960年由C. A. R. Hoare提出
    通过一趟排序将要排序的数据分割成独立的两部分，
    其中一部分的所有数据都比另外一部分的所有数据都要小，
    然后再按此方法对这两部分数据分别进行快速排序
    最好和平均复杂度是O(nlogn),最坏复杂度是O(n2)
    """
    if not sort_list:
        return sort_list

    length = len(sort_list)
    if length == 1:
        return sort_list

    low = 0
    high = length - 1
    _quick_sort(sort_list, low, high)
