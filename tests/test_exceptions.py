# -*- coding: utf-8 -*-
from unittest import TestCase
from Tea.exceptions import RetryError, UnretryableException, TeaException, RequiredArgumentException
from Tea.request import TeaRequest


class TestTeaException(TestCase):
    def test_retry_error(self):
        try:
            raise RetryError('test_retry_error')
        except RetryError as e:
            self.assertEqual('test_retry_error', e.message)

    def test_unretryable_exception(self):
        request = TeaRequest()
        ex = Exception()
        ex.message = "test exception"
        try:
            raise UnretryableException(request, ex)
        except UnretryableException as e:
            self.assertIsNotNone(e)
            self.assertIsNotNone(e.last_request)
            self.assertEqual("Retry failed: test exception", e.message)

    def test_tea_exception(self):
        dic = {"code": "200", "message": "message", "data": {"test": "test", "statusCode": 200},
               "description": "description",
               "accessDeniedDetail": {
                   'AuthAction': 'ram:ListUsers',
                   'AuthPrincipalType': 'SubUser',
                   'PolicyType': 'ResourceGroupLevelIdentityBassdPolicy',
                   'NoPermissionType': 'ImplicitDeny'
               }}
        try:
            raise TeaException(dic)
        except TeaException as e:
            self.assertIsNotNone(e)
            self.assertEqual("200", e.code)
            self.assertEqual("message", e.message)
            self.assertIsNotNone(e.data)
            self.assertEqual("test", e.data.get("test"))
            self.assertEqual(200, e.statusCode)
            self.assertEqual("description", e.description)
            self.assertDictEqual({
                'AuthAction': 'ram:ListUsers',
                'AuthPrincipalType': 'SubUser',
                'PolicyType': 'ResourceGroupLevelIdentityBassdPolicy',
                'NoPermissionType': 'ImplicitDeny'
            }, e.accessDeniedDetail)

    def test_RequiredArgumentException(self):
        param_name = 'name'
        try:
            raise RequiredArgumentException(param_name)
        except RequiredArgumentException as e:
            self.assertEqual('"name" is required.', str(e))
