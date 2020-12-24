# -*- coding: utf-8 -*-
import unittest
from Tea.converter import TeaConverter


class TestConverter(unittest.TestCase):
    def test_to_str(self):
        self.assertEqual('str', TeaConverter.to_str('str'))
        self.assertTrue(isinstance(TeaConverter.to_str('str'), str))
        self.assertTrue('1001', TeaConverter.to_str(1001))

    def test_to_unicode(self):
        self.assertEqual(u'str', TeaConverter.to_unicode('str'))
        self.assertEqual(u'1001', TeaConverter.to_unicode(1001))
