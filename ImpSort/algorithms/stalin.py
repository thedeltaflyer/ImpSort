#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import SortAlgorithm
from .common import _is_sorted


class StalinSort(SortAlgorithm):
    @staticmethod
    def sort(unsorted, meta=None, random=None):
        while not _is_sorted(unsorted, meta):
            if meta:
                meta.iterated()
            StalinSort._step(unsorted)

    @staticmethod
    def generator(unsorted, meta=None, random=None):
        while not _is_sorted(unsorted, meta):
            if meta:
                meta.iterated()
            StalinSort._step(unsorted)
            yield unsorted[:]

    @staticmethod
    def _step(unsorted):
        temp = unsorted[:]
        offset = 0
        last = unsorted[0]
        for i in range(len(unsorted)):
            if temp[i] < last:
                del unsorted[i - offset]
                offset += 1
            else:
                last = temp[i]
