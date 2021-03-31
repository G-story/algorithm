import unittest

from brackets2 import Brackets2


class Brackets2Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(Brackets2.get_is_correct('()()'), 'YES')

    def test2(self):
        self.assertEqual(Brackets2.get_is_correct('({[}])'), 'NO')

    def test3(self):
        self.assertEqual(Brackets2.get_is_correct('({}[(){}])'), 'YES')

    def test4(self):
        self.assertEqual(Brackets2.get_is_correct(']'), 'NO')

    def test5(self):
        self.assertEqual(Brackets2.get_is_correct('['), 'NO')
