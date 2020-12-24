# -*- coding: utf-8 -*-
from Tea.converter import TeaConverter


class TeaException(Exception):
    def __init__(self, dic):
        self.code = dic.get("code")
        self.message = dic.get("message")
        self.data = dic.get("data")

    def __str__(self):
        return 'Error: %s %s Response: %s' % (
            TeaConverter.to_str(self.code),
            TeaConverter.to_str(self.message),
            TeaConverter.to_str(self.data)
        )


class RequiredArgumentException(TeaException):
    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return '"%s" is required.' % TeaConverter.to_str(self.arg)


class RetryError(TeaException):
    def __init__(self, message):
        self.message = message
        self.data = None


class UnretryableException(TeaException):
    def __init__(self, request, ex):
        self.last_request = request
        self.inner_exception = ex
        self.message = "Retry failed: %s" % TeaConverter.to_str(ex.message)

    def __str__(self):
        return str(self.inner_exception)
