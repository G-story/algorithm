import unittest

from josephus import Josephus


class JosephusTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(Josephus.get_two_person(6, 3), (3, 5))

    def test2(self):
        self.assertEqual(Josephus.get_two_person(40, 3), (11, 26))
