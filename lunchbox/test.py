import unittest

from input_factory import InputFactory
from lunchbox import Lunchbox


class LunchboxTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(Lunchbox.get_fast_time([2, 2, 2], [2, 2, 2]), 8)

    def test2(self):
        self.assertEqual(Lunchbox.get_fast_time([1, 2, 3], [1, 2, 1]), 7)

    def test3(self):
        a = InputFactory.factory("random", int, 5, 1, 5)
        b = InputFactory.factory("random", int, 5, 1, 5)
        print a, b, Lunchbox.get_fast_time(a, b)
