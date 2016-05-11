import unittest

from jlis import get_jlis_len, get_inc_seq_list, get_lis


class JilsTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(get_lis([1, 2, 3]), [1, 2, 3])

    def test2(self):
        self.assertEqual(get_lis([3, 2, 1, 7, 5, 4, 2, 6]), [3, 5, 6])

    def test3(self):
        self.assertEqual(get_inc_seq_list([1, 2, 4]), [[1, 2], [1, 4], [2, 4]])

    def test4(self):
        self.assertEqual(get_jlis_len([1, 2, 4], [3, 4, 7]), 5)
