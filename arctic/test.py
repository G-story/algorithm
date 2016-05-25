import unittest

from arctic import Arctic


class ArcticTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(Arctic.get_min_elec_dist([[0, 0], [1, 0], [1, 1], [1, 2], [0, 2]]), 1.00)
