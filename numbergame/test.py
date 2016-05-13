import unittest

from input_factory import InputFactory
from numbergame import Numbergame


class NumbergameTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(Numbergame.work([-1000, -1000, -3, -1000, -1000]), -1000)

    def test2(self):
        self.assertEqual(Numbergame.work([100, -1000, -1000, 100, -1000, -1000]), 1100)

    def test3(self):
        self.assertEqual(Numbergame.work([7, -5, 8, 5, 1, -4, -8, 6, 7, 9]), 7)

    def test4(self):
        r = Numbergame.work(InputFactory.factory("random", int, 50, -1000, 1000))
        print r
