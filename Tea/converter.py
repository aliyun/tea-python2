# -*- coding: utf-8 -*-


class TeaConverter(object):
    @staticmethod
    def to_unicode(s, encoding='utf-8'):
        if s is None:
            return s

        if isinstance(s, str):
            return s.decode(encoding)
        else:
            return unicode(s)

    @staticmethod
    def to_str(s, encoding='utf-8'):
        if s is None:
            return s

        if isinstance(s, unicode):
            return s.encode(encoding)
        else:
            return str(s)

