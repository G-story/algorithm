import unittest

from arctic import Arctic


class ArcticTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(Arctic.get_min_elec_dist([[0, 0], [1, 0], [1, 1], [1, 2], [0, 2]]), 1.00)

    def test2(self):
        self.assertEqual(
            Arctic.get_min_elec_dist([[1.0, 1.0], [30.91, 8], [4.0, 7.64], [21.12, 6.0], [11.39, 3.0], [5.31, 11.0]]),
            10.18)
