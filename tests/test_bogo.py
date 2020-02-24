#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase

from ImpSort import ImpSort


class TestBogo(TestCase):
    def test_bogo_sort(self):
        sorter = ImpSort('bogo')
        unsorted = [24, 106, 2, 42]
        sorter.sort(unsorted)
        sorted_list = unsorted
        sorted_list.sort()
        self.assertTrue(sorted_list == unsorted)

    def test_bogo_generated(self):
        sorter = ImpSort('bogo')
        unsorted = [24, 106, 2, 42]
        for u in sorter.sort_generator(unsorted):
            self.assertTrue(isinstance(u, list))
        sorted_list = unsorted
        sorted_list.sort()
        self.assertTrue(sorted_list == unsorted)
