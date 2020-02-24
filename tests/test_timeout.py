#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase

from ImpSort import (ImpSort, TimeOutException)


class TestTimeout(TestCase):
    def test_timeout_with_sort(self):
        sorter = ImpSort('recompile')  # Compiler should never exit, perfect for testing timeouts
        unsorted = [24, 106, 2, 42]
        try:
            sorter.sort(unsorted, timeout=1)
        except TimeOutException as e:
            print(e)
        else:
            self.fail('TimeoutException was not raised!')

    def test_timeout_with_generator(self):
        sorter = ImpSort('recompile')  # Compiler should never exit, perfect for testing timeouts
        unsorted = [24, 106, 2, 42]
        try:
            for u in sorter.sort_generator(unsorted, timeout=1):
                self.assertTrue(isinstance(u, list))
        except TimeOutException as e:
            print(e)
        else:
            self.fail('TimeoutException was not raised!')

    def test_timeout_without_failure(self):
        sorter = ImpSort('rand_swap')  # Compiler should never exit, perfect for testing timeouts
        unsorted = [24, 106, 2]
        try:
            for u in sorter.sort_generator(unsorted, timeout=1000):
                self.assertTrue(isinstance(u, list))
        except TimeOutException as e:
            self.fail('TimeoutException was raised!')
