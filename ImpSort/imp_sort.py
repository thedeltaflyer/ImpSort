#!/usr/bin/env python
# -*- coding: utf-8 -*-
import signal
from random import SystemRandom

from .meta import MetaData
from .logs import logger
from .exceptions import (TimeOutException, ImpSortException)

from .algorithms.recompile import RecompileSort
from .algorithms.rand_swap import RandomSwapSort
from .algorithms.bogo import BogoSort
from .algorithms.stalin import StalinSort


class ImpSort(object):
    algorithms = {
        'rand_swap': RandomSwapSort,
        'bogo': BogoSort,
        'recompile': RecompileSort,
        'stalin': StalinSort
    }

    def __init__(self, algorithm='rand_swap', random=None):
        try:
            assert (algorithm in self.algorithms)
        except AssertionError:
            raise ImpSortException('Algorithm must be one of: {}. Got: {}'.format(self.algorithms.keys(), algorithm))
        self._algorithm = algorithm or 'rand_swap'
        self._random = random or SystemRandom()
        self._meta = MetaData(algorithm)

    def sort(self, unsorted, timeout=0):
        self._meta = MetaData(self._algorithm)
        if timeout > 0:
            signal.signal(signal.SIGALRM, self._timeout_handler())
            signal.alarm(timeout)
        self._meta.start()
        self.algorithms[self._algorithm].sort(unsorted, self._meta, self._random)
        self._meta.stop()
        if timeout > 0:
            signal.alarm(0)  # Reset the alarm since we reached the end of sorting.

    def sort_generator(self, unsorted, timeout=0):
        self._meta = MetaData(self._algorithm)
        if timeout > 0:
            signal.signal(signal.SIGALRM, self._timeout_handler())
            signal.alarm(timeout)
        self._meta.start()
        for u in self.algorithms[self._algorithm].generator(unsorted, self._meta, self._random):
            yield u
        self._meta.stop()
        if timeout > 0:
            signal.alarm(0)  # Reset the alarm since we reached the end of sorting.

    @property
    def algorithm(self):
        return self._algorithm

    @algorithm.setter
    def algorithm(self, value):
        try:
            assert (value in self.algorithms)
        except AssertionError:
            logger.exception('Algorithm must be one of: {}. Got: {}'.format(self.algorithms.keys(), value))
        self._algorithm = value

    @property
    def meta(self):
        return self._meta

    def _timeout_handler(self):
        def timeout(signum, frame):
            logger.debug('ImpSort TimeOutException occurred')
            signal.alarm(0)  # Reset our signal
            raise TimeOutException(meta=self.meta)

        return timeout
