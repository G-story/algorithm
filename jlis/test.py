import unittest

from jlis import lis, jlis, set_A, set_B


class JilsTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(lis([1, 2, 3]), [1, 2, 3])

    def test2(self):
        self.assertEqual(lis([3, 2, 1, 7, 5, 4, 2, 6]), [3, 5, 6])

    def test3(self):
        set_A([1])
        set_B([3])
        self.assertEqual(jlis(-1, -1), 2)

    def test4(self):
        set_A([1, 2, 4])
        set_B([3, 4, 7])
        self.assertEqual(jlis(-1, -1), 5)

    def test5(self):
        set_A([1, 2, 3])
        set_B([4, 5, 6])
        self.assertEqual(jlis(-1, -1), 6)

    def test6(self):
        set_A([10, 20, 30, 1, 2])
        set_B([10, 20, 30])
        self.assertEqual(jlis(-1, -1), 5)
