# coding: utf-8
from unittest import TestCase

from libs.sort.quick_sort import *


class TestSort(TestCase):
    def test_quick(self):
        """
        测试快速排序
        :return:
        """
        l = [23, 4, 2, 232, 1, 33, 43, 111, 3456, 3, 2, 3, 4444, 333]
        quick_sort(l)
        self.assertEquals(l, [1, 2, 2, 3, 3, 4, 23, 33, 43, 111, 232, 333, 3456, 4444])
