#!/usr/bin/env python
# -*- coding: utf-8 -*-


def _is_sorted(unsorted, meta=None, compare_all=True):
    if len(unsorted) < 1:
        return True
    last = unsorted[0]
    if compare_all:
        is_sorted = True
        for item in unsorted[1:]:
            if meta:
                meta.compared()
            if item < last:
                is_sorted = False
            last = item
        return is_sorted
    else:
        for item in unsorted[1:]:
            if meta:
                meta.compared()
            if item < last:
                return False
            last = item
        return True
