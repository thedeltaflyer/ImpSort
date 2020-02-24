#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import SystemRandom

from . import SortAlgorithm
from .common import _is_sorted


class BogoSort(SortAlgorithm):
    @staticmethod
    def sort(unsorted, meta=None, random=None):
        random = random or SystemRandom()
        while not _is_sorted(unsorted, meta):
            if meta:
                meta.iterated()
            BogoSort._step(unsorted, random)

    @staticmethod
    def generator(unsorted, meta=None, random=None):
        random = random or SystemRandom()
        while not _is_sorted(unsorted, meta):
            if meta:
                meta.iterated()
            BogoSort._step(unsorted, random)
            yield unsorted[:]

    @staticmethod
    def _step(unsorted, random):
        # Please note that random.shuffle is not being used in order to further the inefficiency of the sort.
        temp = unsorted[:]
        for i, j in enumerate(random.sample(range(0, len(unsorted)), len(unsorted))):
            unsorted[i] = temp[j]
