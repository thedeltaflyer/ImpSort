#!/usr/bin/env python
# -*- coding: utf-8 -*-


class SortAlgorithm(object):
    @staticmethod
    def sort(unsorted, meta=None, random=None):
        raise NotImplementedError('The sort method must be implemented')

    @staticmethod
    def generator(unsorted, meta=None, random=None):
        raise NotImplementedError('The generator method must be implemented')
