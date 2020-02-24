#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase

from ImpSort import (ImpSort, ImpSortException)


class TestImpSort(TestCase):
    def test_incorrect_algorithm(self):
        try:
            _ = ImpSort('nonexistent_sort')  # Compiler should never exit, perfect for testing timeouts
        except ImpSortException as e:
            print(e)
        else:
            self.fail('AssertionError was not raised!')

    def test_empty_list(self):
        sorter = ImpSort('rand_swap')
        unsorted = []
        sorter.sort(unsorted)
        sorted_list = unsorted
        sorted_list.sort()
        self.assertTrue(sorted_list == unsorted)
