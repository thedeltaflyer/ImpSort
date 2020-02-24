#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import SystemRandom

from . import SortAlgorithm
from .common import _is_sorted


class RandomSwapSort(SortAlgorithm):
    @staticmethod
    def sort(unsorted, meta=None, random=None):
        random = random or SystemRandom()
        while not _is_sorted(unsorted, meta):
            if meta:
                meta.iterated()
            RandomSwapSort._step(unsorted, random)

    @staticmethod
    def generator(unsorted, meta=None, random=None):
        random = random or SystemRandom()
        while not _is_sorted(unsorted, meta):
            if meta:
                meta.iterated()
            RandomSwapSort._step(unsorted, random)
            yield unsorted[:]

    @staticmethod
    def _step(unsorted, random):
        i = random.randint(0, len(unsorted) - 1)
        j = random.randint(0, len(unsorted) - 1)
        temp = unsorted[i]
        unsorted[i] = unsorted[j]
        unsorted[j] = temp
