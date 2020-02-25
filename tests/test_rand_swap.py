#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase

from ImpSort import ImpSort


class TestRandSwap(TestCase):
    def test_rand_swap_sort(self):
        sorter = ImpSort('rand_swap')
        unsorted = [24, 106, 2, 42]
        sorter.sort(unsorted)
        sorted_list = unsorted[:]
        sorted_list.sort()
        self.assertTrue(sorted_list == unsorted)

    def test_rand_swap_generated(self):
        sorter = ImpSort('rand_swap')
        unsorted = [24, 106, 2, 42]
        for u in sorter.sort_generator(unsorted):
            self.assertTrue(isinstance(u, list))
        sorted_list = unsorted[:]
        sorted_list.sort()
        self.assertTrue(sorted_list == unsorted)
