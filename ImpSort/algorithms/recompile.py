#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import SortAlgorithm
from .common import _is_sorted


class RecompileSort(SortAlgorithm):

    @staticmethod
    def sort(unsorted, meta=None, random=None):
        while not _is_sorted(unsorted, meta):
            if meta:
                meta.iterated()
            RecompileSort._step(unsorted)

    @staticmethod
    def generator(unsorted, meta=None, random=None):
        while not _is_sorted(unsorted, meta):
            if meta:
                meta.iterated()
            RecompileSort._step(unsorted)
            yield unsorted[:]

    @staticmethod
    def _step(unsorted):
        for i in range(len(unsorted)):
            unsorted[i] = unsorted[i]
