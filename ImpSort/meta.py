#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime


class MetaData(object):
    def __init__(self, sort_algorithm=None):
        self._sort_algorithm = sort_algorithm or 'random_swap'
        self._iterations = 0
        self._comparisons = 0
        self._start_time = None
        self._end_time = None

    def iterated(self):
        self._iterations += 1

    def compared(self):
        self._comparisons += 1

    def reset(self):
        self._iterations = 0
        self._comparisons = 0
        self._start_time = None
        self._end_time = None

    def start(self):
        self._start_time = datetime.now()

    def stop(self):
        self._end_time = datetime.now()

    @property
    def algorithm(self):
        return self._sort_algorithm

    @algorithm.setter
    def algorithm(self, value):
        self._sort_algorithm = value
        self.reset()

    @property
    def iterations(self):
        return self._iterations

    @property
    def comparisons(self):
        return self._comparisons

    @property
    def start_time(self):
        return self._start_time

    @property
    def end_time(self):
        return self._end_time

    @property
    def total_time(self):
        return None if self._end_time is None or self._start_time is None else self._end_time - self._start_time

    def __repr__(self):
        return '<ImpSort.MetaData ({}) Iterations: {} Comparisons: {}>'.format(
            self._sort_algorithm, self._iterations, self._comparisons)

    def __str__(self):
        return 'Stats:\n\tAlgorithm: {}\n\tIterations: {}\n\tComparisons: {}\n\tTotal Time: {}'.format(
            self._sort_algorithm, self._iterations, self._comparisons, str(self.total_time))
