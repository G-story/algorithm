import unittest

from quadtree import get_img, img_to_quadtree, quadtree_to_img


class QuadTreeTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(get_img("w"), "w")
        self.assertEqual(get_img("b"), "b")

    def test_2(self):
        self.assertEqual(quadtree_to_img(img_to_quadtree("xbwwb")), "xbwwb")

    def test_3(self):
        self.assertEqual(quadtree_to_img(img_to_quadtree("xbwxwbbwb")), "xbwxwbbwb")

    def test_4(self):
        compressed_img = "xxwwwbxwxwbbbwwxxxwwbbbwwwwbb"
        self.assertEqual(quadtree_to_img(img_to_quadtree(compressed_img)), compressed_img)

    def test_5(self):
        self.assertEqual(get_img("xbwwb"), "xwbbw")

    def test_6(self):
        self.assertEqual(get_img("xbwxwbbwb"), "xxbwwbbbw")

    def test_7(self):
        self.assertEqual(get_img("xxwwwbxwxwbbbwwxxxwwbbbwwwwbb"), "xxwbxwwxbbwwbwbxwbwwxwwwxbbwb")
