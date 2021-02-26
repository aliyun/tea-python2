# -*- coding: utf-8 -*-
# Compat
import sys

py2 = sys.version_info.major == 2
py27 = sys.version_info[0:2] == (2, 7)

py3 = sys.version_info.major == 3
py34 = sys.version_info[0:2] == (3, 4)
py35 = sys.version_info[0:2] == (3, 5)


if py3:
    class TeaConverter(object):
        unicode = str
        basestring = (str, bytes)
        number = (int, float)

        @staticmethod
        def to_unicode(s, encoding='utf-8'):
            if s is None:
                return s

            if isinstance(s, bytes):
                return s.decode(encoding)
            else:
                return str(s)

        @staticmethod
        def to_str(s, encoding='utf-8'):
            if s is None:
                return s

            if isinstance(s, bytes):
                return s.decode(encoding)
            else:
                return str(s)

        @staticmethod
        def to_bytes(s, encoding='utf-8'):
            if s is None or isinstance(s, bytes):
                return s

            if isinstance(s, str):
                return s.encode(encoding)
            else:
                return str(s).encode(encoding)

        @staticmethod
        def to_string(s, encoding='utf-8'):
            if s is None:
                return s

            if isinstance(s, bytes):
                return s.decode(encoding)
            else:
                return str(s)
else:
    class TeaConverter(object):
        unicode = unicode
        basestring = basestring
        number = (int, float, long)

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

        @staticmethod
        def to_bytes(s, encoding='utf-8'):
            if s is None:
                return s

            if isinstance(s, unicode):
                return s.encode(encoding)
            else:
                return str(s)

        @staticmethod
        def to_string(s, encoding='utf-8'):
            if s is None:
                return s

            if isinstance(s, str):
                return s.decode(encoding)
            else:
                return unicode(s)
