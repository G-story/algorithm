import unittest

from quadtree import quadtree


class QuadTreeTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(quadtree("w"), "w")
        self.assertEqual(quadtree("b"), "b")
