#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ImpSortException(Exception):
    def __init__(self, *args, meta=None, **kwargs):
        self.meta = meta
        Exception.__init__(self, *args, **kwargs)

    def __str__(self):
        message = Exception.__str__(self)
        if self.meta is not None:
            message += '\n{}'.format(str(self.meta))
        return message


class TimeOutException(ImpSortException):
    pass
