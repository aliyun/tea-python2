# -*- coding: utf-8 -*-
from _io import BytesIO


class BaseStream(object):
    def __init__(self, size=1024):
        self.size = size

    def read(self, size=1024):
        raise NotImplementedError('read method must be overridden')

    def __len__(self):
        raise NotImplementedError('__len__ method must be overridden')

    def next(self):
        raise NotImplementedError('__next__ method must be overridden')

    def __iter__(self):
        return self


STREAM_CLASS = (file, BaseStream, BytesIO)
READABLE = (BaseStream, file, BytesIO)
WRITABLE = (file, )
