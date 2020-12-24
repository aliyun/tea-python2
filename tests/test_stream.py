# -*- coding: utf-8 -*-
import unittest
import os

from Tea.stream import BaseStream, READABLE, WRITABLE

root_path = os.path.dirname(__file__)


class TestTeaRequest(unittest.TestCase):
    def test_base_stream(self):
        stream = BaseStream()
        self.assertRaises(NotImplementedError, stream.read)
        self.assertRaises(NotImplementedError, stream.__len__)
        self.assertRaises(NotImplementedError, stream.next)

        with open(os.path.join(root_path, 'test.txt'), 'rb') as f:
            self.assertIsInstance(f, file)

        with open(os.path.join(root_path, 'test.txt'), 'wb') as f:
            self.assertIsInstance(f, file)

        try:
            for s in stream:
                continue
        except Exception as e:
            self.assertEqual('__next__ method must be overridden', str(e))
