#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase

from ImpSort import ImpSort


class TestStalin(TestCase):
    def test_stalin_sort(self):
        sorter = ImpSort('stalin')
        unsorted = [24, 106, 2, 42]
        sorter.sort(unsorted)
        sorted_list = [24, 106]
        sorted_list.sort()
        self.assertTrue(sorted_list == unsorted)

    def test_stalin_generated(self):
        sorter = ImpSort('stalin')
        unsorted = [24, 106, 2, 42]
        for u in sorter.sort_generator(unsorted):
            self.assertTrue(isinstance(u, list))
        sorted_list = [24, 106]
        sorted_list.sort()
        self.assertTrue(sorted_list == unsorted)
